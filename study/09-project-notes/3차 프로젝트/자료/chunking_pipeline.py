import os, re, json, sys
import numpy as np


# ============================================================
# 1. 문서 로드 — 구조 자동 감지
# ============================================================

def detect_format(content):
    """md 파일 구조를 자동 감지"""
    if "# 본문" in content and "# 메타데이터" in content:
        return "A"  # 중급 complete 구조
    if re.search(r"^## \d+\.", content, re.MULTILINE) and "## 메타데이터" in content:
        return "B"  # 초급 generated 구조
    return "C"      # 일반 md
    

def load_document(filepath):
    """구조에 맞게 제목/본문/메타데이터 분리"""
    with open(filepath, encoding="utf-8") as f:
        raw = f.read()

    fmt = detect_format(raw)

    if fmt == "A":
        # 중급: # 제목 / # 본문 / # 메타데이터
        title_m = re.search(r"# 제목\n(.+)", raw)
        title = title_m.group(1).strip() if title_m else os.path.basename(filepath)
        body_m = re.search(r"# 본문\s*\n(.*?)(?=\n# 메타데이터)", raw, re.DOTALL)
        body = body_m.group(1).strip() if body_m else raw
        meta_m = re.search(r"# 메타데이터\s*```json\s*(\{.*?\})\s*```", raw, re.DOTALL)

    elif fmt == "B":
        # 초급: # [알고리즘] 제목 / ## 1~15 섹션 / ## 메타데이터
        title_m = re.search(r"^# (.+)", raw, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else os.path.basename(filepath)
        # 본문 = 첫 번째 ## 부터 ## 메타데이터 직전까지
        body_m = re.search(r"(## 1\..+?)(?=\n## 메타데이터)", raw, re.DOTALL)
        if not body_m:
            body_m = re.search(r"(## .+)", raw, re.DOTALL)
        body = body_m.group(1).strip() if body_m else raw
        meta_m = re.search(r"## 메타데이터\s*```json\s*(\{.*?\})\s*```", raw, re.DOTALL)

    else:
        # 일반 md
        title_m = re.search(r"^# (.+)", raw, re.MULTILINE)
        title = title_m.group(1).strip() if title_m else os.path.basename(filepath)
        body = raw
        meta_m = re.search(r"```json\s*(\{.*?\})\s*```", raw, re.DOTALL)

    metadata = json.loads(meta_m.group(1)) if meta_m else {}
    return {"title": title, "body": body, "metadata": metadata, "format": fmt}


# ============================================================
# 2. 전처리
# ============================================================

def clean_text(text):
    blocks = []
    def _save(m):
        blocks.append(m.group(0)); return f"__CODE_{len(blocks)-1}__"
    text = re.sub(r"```[\s\S]*?```", _save, text)
    text = re.sub(r"<IMAGE>(.*?)</IMAGE>", r"[그림: \1]", text)
    text = re.sub(r"https?://\S+", "", text)
    text = re.sub(r"\*\*(.*?)\*\*", r"\1", text)
    text = re.sub(r"\*(.*?)\*", r"\1", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    for i, b in enumerate(blocks):
        text = text.replace(f"__CODE_{i}__", b)
    return text.strip()


# ============================================================
# 3. 청킹 전략 3가지
# ============================================================

def chunk_fixed(text, size=1000, overlap=200):
    chunks, start = [], 0
    while start < len(text):
        t = text[start:start+size].strip()
        if t:
            chunks.append({"text": t, "title": f"fixed_{len(chunks)}", "type": "concept"})
        start += size - overlap
    return chunks


def chunk_recursive(text, max_size=2000, seps=None):
    if seps is None:
        seps = ["\n## ", "\n### ", "\n\n", "\n", ". ", " "]
    def _split(t, si):
        if len(t) <= max_size or si >= len(seps):
            return [t] if t.strip() else []
        parts = t.split(seps[si])
        res, cur = [], ""
        for p in parts:
            cand = cur + seps[si] + p if cur else p
            if len(cand) <= max_size: cur = cand
            else:
                if cur: res.extend(_split(cur, si+1))
                cur = p
        if cur: res.extend(_split(cur, si+1))
        return res
    raw = _split(text, 0)
    return [{"text": c.strip(), "title": f"recursive_{i}", "type": "concept"}
            for i, c in enumerate(raw) if c.strip()]


def chunk_semantic(text, doc_format="A"):
    """
    구조에 따라 분할 기준이 달라짐:
      A(중급): ## 섹션 + ### 문제 통째 보존
      B(초급): ## N. 섹션 단위 분할
      C(일반): ## 헤더 기준 분할
    """
    chunks, cur = [], {"title": "", "lines": [], "type": "concept"}

    for line in text.split("\n"):
        #  구조 A: 문제 섹션 감지 
        if doc_format == "A" and re.match(r"^### 문제 \d+", line):
            if cur["lines"]: chunks.append(cur)
            cur = {"title": line.lstrip("#").strip(), "lines": [line], "type": "problem"}
            continue

        #  공통: ## 헤더 감지 
        if re.match(r"^## ", line):
            # 스킵 대상
            skip_headers = ["실전 문제 풀이", "메타데이터"]
            if any(s in line for s in skip_headers):
                if cur["lines"]: chunks.append(cur)
                cur = {"title": "", "lines": [], "type": "concept"}
                continue

            if cur["lines"]: chunks.append(cur)

            section_title = line.lstrip("#").strip()
            # 구조 B: "1. 한 줄 요약" → 번호 제거
            section_title = re.sub(r"^\d+\.\s*", "", section_title)

            cur = {"title": section_title, "lines": [line], "type": "concept"}
            continue

        cur["lines"].append(line)

    if cur["lines"]: chunks.append(cur)

    return [{"text": "\n".join(c["lines"]).strip(), "title": c["title"], "type": c["type"]}
            for c in chunks if len("\n".join(c["lines"]).strip()) > 30]


# ============================================================
# 4. 평가
# ============================================================

def evaluate(chunks, original):
    texts = [c["text"] for c in chunks]
    sizes = [len(t) for t in texts]
    broken = sum(1 for t in texts if t.count("```") % 2 != 0)
    code_pct = round((1 - broken / max(len(chunks), 1)) * 100, 1)
    markers = ["#### 핵심 개념", "#### 풀이 전략", "#### 소스코드"]
    ctx_ok, ctx_total = 0, 0
    for t in texts:
        found = [m for m in markers if m in t]
        if found:
            ctx_total += 1
            if len(found) == len(markers): ctx_ok += 1
    ctx_pct = round((ctx_ok / max(ctx_total, 1)) * 100, 1)
    return {
        "count": len(chunks), "avg_size": int(np.mean(sizes)),
        "std_size": int(np.std(sizes)), "min_size": min(sizes),
        "max_size": max(sizes), "code_integrity": code_pct,
        "context_completeness": ctx_pct,
    }


def retrieval_test(chunks):
    tests = [
        {"query_kw": ["삽입"], "answer_kw": ["sift", "부모", "Push", "위로", "넣"], "label": "삽입"},
        {"query_kw": ["시간 복잡도", "O("], "answer_kw": ["O(1)", "O(n)", "O(log"], "label": "시간복잡도"},
        {"query_kw": ["코드", "구현"], "answer_kw": ["def ", "public ", "void ", "print", "return"], "label": "코드"},
        {"query_kw": ["실수", "주의"], "answer_kw": ["실수", "주의", "헷갈", "틀리"], "label": "실수"},
        {"query_kw": ["언제", "사용"], "answer_kw": ["신호", "경우", "패턴", "문제"], "label": "사용시점"},
    ]
    texts = [c["text"] for c in chunks]
    hits, details = 0, []
    for tc in tests:
        best_idx, best_score = 0, 0
        for i, t in enumerate(texts):
            score = sum(1 for kw in tc["query_kw"] if kw.lower() in t.lower())
            if score > best_score: best_score, best_idx = score, i
        hit = any(kw.lower() in texts[best_idx].lower() for kw in tc["answer_kw"])
        if hit: hits += 1
        details.append({"label": tc["label"], "chunk": chunks[best_idx].get("title",""), "hit": hit})
    return round(hits / len(tests) * 100, 1), details


# ============================================================
# 5. DB-ready 변환
# ============================================================

def to_db_ready(filepath, chunks, doc_meta, strategy_name):
    # 파일명에서 prefix 생성
    basename = os.path.splitext(os.path.basename(filepath))[0]
    # 긴 이름 줄이기: 알고리즘초급_01_완전탐색_개념_generated → beginner_01
    num_m = re.search(r"_(\d+)_", basename)
    if num_m:
        prefix = f"beginner_{num_m.group(1)}"
    elif "complete" in basename.lower():
        prefix = basename.split("_")[0].lower()
    else:
        prefix = basename[:20].lower().replace(" ", "_")

    ids, docs, metas = [], [], []
    for i, c in enumerate(chunks):
        ids.append(f"{prefix}_{i:03d}")
        docs.append(c["text"])
        metas.append({
            "algorithm": doc_meta.get("algorithm", ""),
            "category": doc_meta.get("category", ""),
            "source_type": doc_meta.get("source_type", "generated"),
            "chunk_type": c.get("type", "concept"),
            "section_title": c.get("title", ""),
            "char_count": len(c["text"]),
            "strategy": strategy_name,
        })
    return ids, docs, metas


# ============================================================
# 메인
# ============================================================

if __name__ == "__main__":
    INPUT_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    if not os.path.isdir(INPUT_DIR):
        print(f" 폴더 없음: {INPUT_DIR}"); exit(1)

    # md 파일 재귀 수집 (하위 폴더 포함, 중복 (1) 파일 제외)
    ALL_FILES = []
    for root, dirs, files in os.walk(INPUT_DIR):
        for f in sorted(files):
            if f.endswith(".md") and "(1)" not in f:
                ALL_FILES.append(os.path.join(root, f))
    if not ALL_FILES:
        print(f"md 파일 없음: {INPUT_DIR}")
        print(f'사용법: python chunking_pipeline.py "C:\\skn29\\3차 프로젝트\\자료"'); exit(1)
    ALL_FILES.sort()
    # 표시용 상대 경로
    ALL_MD = [os.path.relpath(f, INPUT_DIR) for f in ALL_FILES]

    # complete/generated 파일 우선, 없으면 전체
    COMPLETE = [f for f in ALL_MD if "complete" in f.lower() or "generated" in f.lower()]
    TARGETS = COMPLETE if COMPLETE else ALL_MD

    print(f" 폴더: {INPUT_DIR}")
    print(f" 전체 md: {len(ALL_MD)}개 | 청킹 대상: {len(TARGETS)}개\n")

    #  첫 번째 파일로 전략 비교 
    first_path = os.path.join(INPUT_DIR, TARGETS[0]) if not os.path.isabs(TARGETS[0]) else TARGETS[0]
    doc = load_document(first_path)
    body = clean_text(doc["body"])

    print(f" 비교 대상: {TARGETS[0]} (구조: {doc['format']})\n")

    strats = {
        "fixed_size": chunk_fixed(body),
        "recursive": chunk_recursive(body),
        "semantic": chunk_semantic(body, doc["format"]),
    }

    # 1단계: 기본 평가
    print("=" * 75)
    print("1단계: 기본 평가")
    print("=" * 75)
    print(f"\n{'전략':<14} {'청크수':>5} {'평균':>6} {'표준편차':>6} {'최소':>5} {'최대':>5} {'코드보존':>7} {'문맥완결':>7}")
    print("" * 70)
    evals = {}
    for name, ch in strats.items():
        ev = evaluate(ch, body); evals[name] = ev
        print(f"{name:<14} {ev['count']:>4}개 {ev['avg_size']:>5}자 {ev['std_size']:>5}자 "
              f"{ev['min_size']:>4}자 {ev['max_size']:>4}자 {ev['code_integrity']:>6}% {ev['context_completeness']:>6}%")

    # 2단계: 검색 정확도
    print(f"\n{'='*75}\n2단계: 검색 정확도\n{'='*75}\n")
    for name, ch in strats.items():
        acc, details = retrieval_test(ch); evals[name]["retrieval"] = acc
        hits = " ".join(f"{'' if d['hit'] else ''}" for d in details)
        print(f"{name:<14} 정확도: {acc:>5}%  {hits}")

    # 3단계: 종합
    print(f"\n{'='*75}\n3단계: 종합 (코드보존 25% + 문맥완결 35% + 검색정확 40%)\n{'='*75}")
    print(f"\n{'전략':<14} {'코드':>7} {'문맥':>7} {'검색':>7} {'종합':>7}")
    print("" * 45)
    best_name, best_score = "", 0
    for name, ev in evals.items():
        total = ev["code_integrity"]*0.25 + ev["context_completeness"]*0.35 + ev["retrieval"]*0.40
        if total > best_score: best_score, best_name = total, name
        print(f"{name:<14} {ev['code_integrity']:>6.1f}% {ev['context_completeness']:>6.1f}% {ev['retrieval']:>6.1f}% {total:>6.1f}")
    print(f"\n 최적 전략: {best_name} (종합 {best_score:.1f}점)")

    # 4단계: 전체 파일에 적용
    print(f"\n{'='*75}\n4단계: '{best_name}' 전략으로 전체 청킹\n{'='*75}\n")
    all_ids, all_docs, all_metas = [], [], []
    for fname in TARGETS:
        fp = os.path.join(INPUT_DIR, fname) if not os.path.isabs(fname) else fname
        d = load_document(fp)
        b = clean_text(d["body"])
        if best_name == "fixed_size": ch = chunk_fixed(b)
        elif best_name == "recursive": ch = chunk_recursive(b)
        else: ch = chunk_semantic(b, d["format"])
        ids, docs, metas = to_db_ready(fp, ch, d["metadata"], best_name)
        all_ids.extend(ids); all_docs.extend(docs); all_metas.extend(metas)
        c = sum(1 for m in metas if m["chunk_type"]=="concept")
        p = sum(1 for m in metas if m["chunk_type"]=="problem")
        print(f"   {fname[:45]:<47} 구조{d['format']} → {len(ids):>2}개 ({c} {p})")

    # 청크 상세
    print(f"\n{''*75}")
    print(f"{'ID':<18} {'타입':<4} {'크기':>6} {'제목'}")
    print(f"{''*75}")
    for id_, meta in zip(all_ids, all_metas):
        icon = "" if meta["chunk_type"] == "problem" else ""
        print(f"{id_:<18} {icon}  {meta['char_count']:>5}자  {meta['section_title'][:40]}")

    # 저장
    out = {"ids": all_ids, "documents": all_docs, "metadatas": all_metas}
    out_path = os.path.join(INPUT_DIR, "all_chunks_db_ready.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    report = {"strategy_comparison": evals, "best_strategy": best_name,
              "best_score": round(best_score, 1), "total_chunks": len(all_ids),
              "total_chars": sum(m["char_count"] for m in all_metas)}
    rpt_path = os.path.join(INPUT_DIR, "chunking_eval_report.json")
    with open(rpt_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*75}")
    print(f"총 {len(all_ids)}개 청크 | {sum(m['char_count'] for m in all_metas):,}자")
    print(f" {out_path}")
    print(f" {rpt_path}")
    print(f"\n다음 단계: collection.add(**json.load(open('all_chunks_db_ready.json')))")
