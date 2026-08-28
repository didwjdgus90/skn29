
import html
import re
from pathlib import Path

import pandas as pd
import streamlit as st

# 🔥 여기가 핵심 (경로 + 파일명 정확히 맞춤)
BASE_DIR = Path(__file__).resolve().parent / "data"

FILES = {
    "삼성화재": BASE_DIR / "삼성화재_FAQ (1).xlsx",
    "현대해상": BASE_DIR / "현대해상_FAQ_209건_정리 (1).xlsx",
    "DB손해보험": BASE_DIR / "db손해보험FAQ.xlsx",
}


def clean_question(text: str) -> str:
    text = str(text or "").strip()
    text = re.sub(r"^\s*\d+\s*[.)]?\s*", "", text)
    return text.strip()


@st.cache_data
def load_samsung():
    df = pd.read_excel(FILES["삼성화재"], sheet_name="카테고리_질문_답변")
    df = df[["구분", "카테고리", "질문", "답변"]]
    return normalize_df(df)


@st.cache_data
def load_db():
    df = pd.read_excel(FILES["DB손해보험"])
    df = df[["구분", "카테고리", "질문", "답변"]]
    return normalize_df(df)


@st.cache_data
def load_hyundai():
    raw = pd.read_excel(FILES["현대해상"], sheet_name="FAQ_원본", header=None)

    header_row_idx = None
    for idx, row in raw.iterrows():
        values = [str(v).strip() for v in row.tolist()]
        if values[:4] == ["번호", "카테고리", "질문", "답변"]:
            header_row_idx = idx
            break

    df = pd.read_excel(FILES["현대해상"], sheet_name="FAQ_원본", header=header_row_idx)
    df = df.iloc[:, :4]
    df.columns = ["구분", "카테고리", "질문", "답변"]

    return normalize_df(df)


def normalize_df(df):
    df = df.dropna(subset=["질문", "답변"])
    df["구분"] = pd.to_numeric(df["구분"], errors="coerce")
    df["카테고리"] = df["카테고리"].astype(str).str.strip()
    df["질문"] = df["질문"].astype(str).str.strip()
    df["답변"] = df["답변"].astype(str).str.strip()
    df["표시질문"] = df["질문"].apply(clean_question)

    df = df.drop_duplicates(subset=["질문", "답변"])

    # 🔥 정렬
    df = df.sort_values(["구분", "카테고리", "질문"]).reset_index(drop=True)

    return df


def render_company_faq(company_name, df):
    st.subheader(f"{company_name} FAQ")

    col1, col2 = st.columns([1, 2])

    category_list = ["전체"] + sorted(df["카테고리"].unique())
    selected_category = col1.selectbox(f"{company_name}_카테고리", category_list)

    keyword = col2.text_input(f"{company_name}_검색", placeholder="검색")

    filtered = df.copy()

    if selected_category != "전체":
        filtered = filtered[filtered["카테고리"] == selected_category]

    if keyword:
        filtered = filtered[
            filtered["질문"].str.contains(keyword, case=False) |
            filtered["답변"].str.contains(keyword, case=False)
        ]

    st.caption(f"{len(filtered)}건")

    # ✅ 페이지 설정
    ITEMS_PER_PAGE = 10
    total_pages = (len(filtered) - 1) // ITEMS_PER_PAGE + 1

    page = st.number_input(
        "페이지 선택",
        min_value=1,
        max_value=total_pages,
        value=1,
        step=1
    )

    start_idx = (page - 1) * ITEMS_PER_PAGE
    end_idx = start_idx + ITEMS_PER_PAGE

    page_df = filtered.iloc[start_idx:end_idx]

    # ✅ 탭 유지 (카테고리별)
    tabs = ["전체"] + sorted(filtered["카테고리"].unique())
    tab_objs = st.tabs(tabs)

    for tab_name, tab in zip(tabs, tab_objs):
        with tab:
            view = page_df if tab_name == "전체" else page_df[page_df["카테고리"] == tab_name]

            for _, row in view.iterrows():
                title = f"{int(row['구분']) if pd.notna(row['구분']) else ''}. {row['표시질문']}"

                with st.expander(title):
                    safe = html.escape(row["답변"]).replace("\n", "<br>")
                    st.markdown(safe, unsafe_allow_html=True)

    st.markdown(f"페이지 {page} / {total_pages}")


def main():
    st.title("보험사 FAQ 통합")

    samsung = load_samsung()
    hyundai = load_hyundai()
    db = load_db()

    tabs = st.tabs(["삼성화재", "현대해상", "DB손해보험"])

    with tabs[0]:
        render_company_faq("삼성화재", samsung)

    with tabs[1]:
        render_company_faq("현대해상", hyundai)

    with tabs[2]:
        render_company_faq("DB손해보험", db)


if __name__ == "__main__":
    main()