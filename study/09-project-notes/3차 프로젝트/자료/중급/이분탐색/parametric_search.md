# 제목
[이분탐색] Parametric Search (파라메트릭 서치) - Python

# 링크
<https://marades.tistory.com/7>

# 본문

## 파라메트릭 서치란?

이분탐색은 "배열에서 특정 값의 위치"를 찾습니다.
파라메트릭 서치는 "조건을 만족하는 최적의 값"을 범위에서 찾습니다.

> 📦 비유: 음식의 간을 맞출 때
> "소금을 얼마나 넣어야 딱 맞는가?"를 찾는 문제.
> 너무 적으면 싱겁고, 너무 많으면 짜다.
> 절반씩 줄여가며 최적값을 찾는 것이 파라메트릭 서치입니다.

### 이분탐색과의 차이

| | 이분탐색 | 파라메트릭 서치 |
|---|---|---|
| 탐색 대상 | 배열 내 값 | 정답이 될 수 있는 범위 |
| 찾는 것 | 특정 값의 위치 | 조건을 만족하는 최적값 |
| 핵심 질문 | "이 값이 배열에 있는가?" | "이 값이 조건을 만족하는가?" |
| 대표 문제 | 특정 수 찾기 | 최솟값의 최댓값, 최댓값의 최솟값 |

---

## 핵심 패턴

파라메트릭 서치 문제는 항상 이 구조로 바꿀 수 있습니다.

```
최적화 문제: "조건을 만족하는 최솟값(또는 최댓값)은?"
      ↓
결정 문제:  "값이 X일 때 조건을 만족하는가? (Yes/No)"
```

범위에서 이분탐색하며 조건을 만족하는 가장 경계에 있는 값을 찾습니다.

### 인식 신호

문제에서 아래 패턴이 보이면 파라메트릭 서치를 의심합니다.
- 범위가 매우 크다 (10억 이상)
- "최솟값 중 최댓값", "최댓값 중 최솟값" 형태
- O(N) 이하로는 풀 수 없어 보인다

---

## 기본 구조 (코드 템플릿)

```python
def check(mid):
    """mid 값이 조건을 만족하는지 Yes/No로 반환"""
    # 문제마다 다르게 구현
    pass

left, right = 최솟값, 최댓값
answer = 0

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = mid        # 조건 만족 → 일단 저장
        left = mid + 1      # 더 큰 값도 가능한지 탐색 (최댓값 찾을 때)
        # right = mid - 1   # 더 작은 값도 가능한지 탐색 (최솟값 찾을 때)
    else:
        right = mid - 1     # 조건 불만족 → 범위 줄이기
        # left = mid + 1
```

---

## 예제: 나무 자르기

높이 H로 나무들을 잘랐을 때 잘린 나무의 합이 M 이상이 되는
H의 최댓값을 구하라.

```
나무: [4, 42, 40, 26, 46],  M = 72

H=30으로 자르면: 0 + 12 + 10 + 0 + 16 = 38  (부족)
H=25로 자르면:  0 + 17 + 15 + 1 + 21 = 54  (부족)
H=15로 자르면:  0 + 27 + 25 + 11 + 31 = 94 (충분)
H=36으로 자르면: 0 + 6 + 4 + 0 + 10 = 20  (부족)
```

**핵심 관찰:** H가 작을수록 더 많이 잘린다. → 단조 감소 함수 → 이분탐색 가능

```python
def solution(trees, M):
    def check(h):
        """높이 h로 잘랐을 때 M 이상 얻을 수 있는가?"""
        total = sum(max(0, t - h) for t in trees)
        return total >= M

    left, right = 0, max(trees)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        if check(mid):          # 조건 만족
            answer = mid        # 일단 저장 (최댓값 탐색이므로)
            left = mid + 1      # 더 높게 잘라도 되는지 탐색
        else:                   # 조건 불만족
            right = mid - 1     # 더 낮게 잘라야 함

    return answer

print(solution([4, 42, 40, 26, 46], 72))  # 36
```

### 탐색 과정 추적

```
left=0, right=46

1회: mid=23, check(23)=True  → answer=23, left=24
2회: mid=35, check(35)=True  → answer=35, left=36
3회: mid=41, check(41)=False → right=40
4회: mid=38, check(38)=False → right=37
5회: mid=36, check(36)=True  → answer=36, left=37
6회: left>right → 종료

return 36  ✅
```

---

## 최솟값 탐색 vs 최댓값 탐색

| | 최솟값 찾기 | 최댓값 찾기 |
|---|---|---|
| 조건 만족 시 | `answer=mid`, `right=mid-1` | `answer=mid`, `left=mid+1` |
| 조건 불만족 시 | `left=mid+1` | `right=mid-1` |
| 예시 | 입국심사(최소 시간) | 나무 자르기(최대 높이) |

---

## 시간복잡도

범위가 N이고, 조건 확인이 O(M)이라면 전체 O(M log N)입니다.
범위가 10억이어도 log₂(10억) ≈ 30번이면 탐색 완료합니다.

# 메타데이터
```json
{
  "category": "탐색",
  "algorithm": "이분탐색",
  "source_type": "blog",
  "style": ["easy", "analogy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python",
  "source": "marades.tistory.com"
}
```
