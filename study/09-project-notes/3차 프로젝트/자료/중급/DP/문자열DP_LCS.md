# 제목
[DP] 문자열 DP - LCS (최장 공통 부분 수열) - Python

# 링크
<https://redjun89.tistory.com/123>
<https://velog.io/@doorbals_512/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EC%9D%B8%EB%8D%B0-DP%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C>

# 본문

## 문자열 DP란?

두 문자열 사이의 관계(공통 부분, 편집 거리 등)를 2차원 DP 테이블로 표현하는 기법입니다.
가장 대표적인 문제가 **LCS(Longest Common Subsequence, 최장 공통 부분 수열)**입니다.

---

## LCS vs LCS (헷갈리는 두 개념)

LCS라는 약자가 두 가지를 가리킵니다.

| 이름 | 의미 | 조건 |
|---|---|---|
| Longest Common **Substring** | 최장 공통 **문자열** | 연속해야 함 |
| Longest Common **Subsequence** | 최장 공통 **부분 수열** | 연속하지 않아도 됨 |

> 📦 예시: ABCD와 ABFC 비교
> 최장 공통 문자열(Substring): AB (연속된 공통 부분)
> 최장 공통 부분 수열(Subsequence): ABC (순서만 맞으면 됨)

코딩테스트에서 LCS는 보통 **Subsequence(부분 수열)** 을 의미합니다.

---

## 점화식

두 문자열 `str1`, `str2`에서 `dp[i][j]` = str1의 i번째까지, str2의 j번째까지 볼 때의 LCS 길이

```
str1[i] == str2[j] 이면:
    dp[i][j] = dp[i-1][j-1] + 1      # 두 문자 모두 LCS에 포함

str1[i] != str2[j] 이면:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])   # 어느 쪽을 제외할지 선택
```

> 📦 비유: 두 사람의 여행 일정을 비교해 겹치는 최장 방문지 목록 찾기.
> 오늘 방문지가 같으면 공통 목록에 추가(+1),
> 다르면 한쪽을 빼고 더 긴 쪽을 선택합니다.

---

## 코드 (길이만 구하기)

```python
def lcs_length(str1, str2):
    m, n = len(str1), len(str2)
    # dp[i][j]: str1[:i]와 str2[:j]의 LCS 길이
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:       # 문자가 같으면
                dp[i][j] = dp[i-1][j-1] + 1  # 대각선 + 1
            else:                              # 다르면
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # 위, 왼쪽 중 최대

    return dp[m][n]

print(lcs_length("ABCDGH", "AEDFHR"))  # 3 (ADH)
print(lcs_length("ABCD", "ABFC"))      # 3 (ABC)
```

---

## DP 테이블 채우기 과정

str1 = "ABCD", str2 = "ABFC"

```
    ""  A  B  F  C
""   0  0  0  0  0
A    0  1  1  1  1
B    0  1  2  2  2
C    0  1  2  2  3  ← dp[4][4]=3 이 LCS 길이
D    0  1  2  2  3
```

채우는 규칙:
- (1,1): A==A → dp[0][0]+1 = 1
- (1,2): A≠B → max(dp[0][2], dp[1][1]) = max(0,1) = 1
- (2,2): B==B → dp[1][1]+1 = 2
- (3,4): C==C → dp[2][3]+1 = 3

---

## 코드 (실제 LCS 문자열 복원)

길이만 구한 뒤 역추적(traceback)으로 실제 문자열도 복원할 수 있습니다.

```python
def lcs_string(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # 역추적: dp 오른쪽 아래에서 시작
    lcs = ""
    i, j = m, n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:     # 문자가 같으면 LCS에 포함
            lcs = str1[i-1] + lcs
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:  # 위쪽이 더 크면 위로
            i -= 1
        else:                            # 왼쪽이 더 크면 왼쪽으로
            j -= 1

    return lcs

print(lcs_string("ABCDGH", "AEDFHR"))  # ADH
print(lcs_string("ABCD", "ABFC"))      # ABC
```

---

## 최소 편집 거리 (Minimum Edit Distance)

LCS와 함께 자주 나오는 문자열 DP입니다.
두 문자열을 서로 변환하기 위한 **최소 편집 횟수**를 구합니다.

편집 연산: 삽입(Insert), 삭제(Delete), 대체(Substitute) — 각 1회

```
dp[i][j]: str1[:i]를 str2[:j]로 만드는 최소 편집 횟수

str1[i] == str2[j] → dp[i][j] = dp[i-1][j-1]          (그대로)
str1[i] != str2[j] → dp[i][j] = min(
    dp[i-1][j] + 1,    # 삭제
    dp[i][j-1] + 1,    # 삽입
    dp[i-1][j-1] + 1   # 대체
)
```

```python
def min_edit_distance(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # 초기화: 빈 문자열과의 편집 거리
    for i in range(m + 1): dp[i][0] = i   # str2가 빈 경우 → i번 삭제
    for j in range(n + 1): dp[0][j] = j   # str1이 빈 경우 → j번 삽입

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    return dp[m][n]

print(min_edit_distance("kitten", "sitting"))  # 3
```

---

## 두 알고리즘 비교

| | LCS | 최소 편집 거리 |
|---|---|---|
| 목적 | 공통 부분 수열의 최대 길이 | 변환에 필요한 최소 연산 수 |
| 점화식 핵심 | 같으면 +1, 다르면 max | 같으면 그대로, 다르면 min+1 |
| 활용 | 유사도 비교, diff 도구 | 철자 교정, 번역 품질 평가 |
| 시간복잡도 | O(M×N) | O(M×N) |

---

## 시간복잡도

두 문자열 길이를 M, N이라 하면 전체 O(M×N)입니다.

# 메타데이터
```json
{
  "category": "동적계획법",
  "algorithm": "DP",
  "source_type": "blog",
  "style": ["easy", "analogy", "code", "theory"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python",
  "source": "redjun89.tistory.com, velog.io/@doorbals_512"
}
```
