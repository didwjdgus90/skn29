# 제목
[알고리즘] 동적계획법(DP) 완전 정복 — 메모이제이션, LIS, 배낭 문제, 실전 문제 3선

# 본문

## 한줄 요약

동적계획법(DP)은 "큰 문제를 작은 문제로 쪼개고, 이미 풀었던 작은 문제의 답을 저장해서 반복 계산을 없애는 기법"이다.

---

## 왜 필요한가

계단을 올라가는 방법의 수를 구한다고 하자. 한 번에 1계단 또는 2계단을 오를 수 있을 때, 10번째 계단까지 가는 방법은?

재귀로 풀면 `f(10) = f(9) + f(8)`, `f(9) = f(8) + f(7)` ... 이렇게 같은 하위 문제를 수십 번 반복 계산하게 된다. 계단이 50개면 계산량이 폭발한다.

DP는 `f(1)=1, f(2)=2`부터 시작해 각 결과를 배열에 저장하고, 이전 결과를 재활용하여 `f(10)`까지 **딱 10번의 계산**으로 끝낸다.

핵심 아이디어: **한 번 계산한 건 다시 계산하지 않는다.**

---

## 핵심 개념

### 1. DP가 성립하는 두 조건

| 조건 | 의미 |
|------|------|
| 최적 부분 구조 (Optimal Substructure) | 큰 문제의 최적해가 작은 문제의 최적해로 구성된다 |
| 중복 부분 문제 (Overlapping Subproblems) | 같은 작은 문제가 여러 번 반복 등장한다 |

두 조건 모두 만족해야 DP를 적용할 수 있다.

### 2. Top-Down vs Bottom-Up

| 방식 | 구현 | 특징 |
|------|------|------|
| Top-Down (메모이제이션) | 재귀 + 캐시 | 큰 문제부터 출발, 필요한 것만 계산 |
| Bottom-Up (타뷸레이션) | 반복문 + 배열 | 작은 문제부터 쌓아올림, 모든 항 계산 |

실전에서는 **Bottom-Up이 더 빠르고 안정적**이다 (재귀 깊이 제한 없음).

### 3. 점화식 (Recurrence Relation)

DP의 핵심은 점화식이다. 코드는 단순하지만 **점화식을 찾는 것이 가장 어렵다**.

점화식을 찾는 방법:
1. 작은 예시를 손으로 풀어본다
2. "이 칸의 값은 이전 어떤 칸들로부터 구해지는가?" 를 관찰한다
3. 패턴을 수식으로 표현한다
4. 코드로 옮긴다 (보통 for문 2~3줄)

### 4. 시간 복잡도

| DP 유형 | 시간 복잡도 |
|---------|-----------|
| 1차원 DP (피보나치, 계단) | O(N) |
| 1차원 DP (LIS) | O(N²) |
| 2차원 DP (배낭, 격자) | O(N × M) |
| LIS (이분탐색 최적화) | O(N log N) |

---

## 동작 흐름

### Bottom-Up 예시: 피보나치

```
f(0)=0, f(1)=1
점화식: f(n) = f(n-1) + f(n-2)

n:    0  1  2  3  4  5  6  7
dp:   0  1  1  2  3  5  8  13
           ↑  ↑
           이전 두 값을 더해서 현재 값 생성

f(7) = f(6) + f(5) = 8 + 5 = 13
```

### Top-Down 예시: 피보나치

```
fib(5) 호출
  → fib(4) 호출
    → fib(3) 호출
      → fib(2) 호출
        → fib(1) = 1 (기저)
        → fib(0) = 0 (기저)
        → 캐시에 fib(2)=1 저장
      → fib(1) = 1 (기저)
      → 캐시에 fib(3)=2 저장
    → fib(2) = 1 ← 캐시에서 즉시 반환 (재계산 X)
    → 캐시에 fib(4)=3 저장
  → fib(3) = 2 ← 캐시에서 즉시 반환
  → 캐시에 fib(5)=5 저장
```

---

## Text Flow Chart

### Bottom-Up DP 일반 패턴

```
dp 배열 초기화 (기저 조건 설정)
        ↓
   i = 시작값부터 N까지 반복
        ↓
   dp[i] = 점화식(dp[i-1], dp[i-2], ...)
        ↓
   반복 종료 → dp[N] 또는 max(dp) 반환
```

### Top-Down DP 일반 패턴

```
solve(n) 호출
        ↓
   기저 조건? → YES → 값 반환
        ↓ NO
   캐시에 있나? → YES → 캐시값 반환
        ↓ NO
   result = 점화식(solve(n-1), solve(n-2), ...)
        ↓
   캐시에 저장 → result 반환
```

---

## 기본 코드 템플릿

### Python — Bottom-Up (피보나치)

```python
def fib_bottom_up(n):
    """피보나치 n번째 항 (Bottom-Up)"""
    if n <= 1:
        return n

    table = [0] * (n + 1)
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]

print(fib_bottom_up(10))  # 55
```

### Python — Top-Down (피보나치)

```python
import sys
sys.setrecursionlimit(10000)

def fib_top_down(n, cache={}):
    """피보나치 n번째 항 (Top-Down 메모이제이션)"""
    if n <= 1:
        return n
    if n in cache:
        return cache[n]

    cache[n] = fib_top_down(n - 1) + fib_top_down(n - 2)
    return cache[n]

print(fib_top_down(10))  # 55
```

### Java — Bottom-Up

```java
public class FibDP {
    public static int fibBottomUp(int n) {
        if (n <= 1) return n;
        int[] table = new int[n + 1];
        table[1] = 1;

        for (int i = 2; i <= n; i++) {
            table[i] = table[i - 1] + table[i - 2];
        }
        return table[n];
    }

    public static void main(String[] args) {
        System.out.println(fibBottomUp(10)); // 55
    }
}
```

**코드 흐름 설명**

1. 기저 조건을 배열에 직접 설정한다 (`table[0]=0, table[1]=1`).
2. 작은 인덱스부터 점화식을 적용해 한 칸씩 채워나간다.
3. 최종적으로 `table[n]`이 정답이다.
4. Top-Down은 같은 점화식을 재귀로 구현하되, 딕셔너리(캐시)로 중복 계산을 방지한다.

---

## 실전 문제 풀이

---

### 문제 1: 최장 증가 수열 (LIS — Longest Increasing Subsequence)

#### 핵심 개념

**"수열에서 원래 순서를 유지하면서 값이 계속 증가하는 가장 긴 부분수열의 길이를 구하라"**

예: `[10, 20, 10, 30, 20, 50]` → LIS = `[10, 20, 30, 50]` → 길이 **4**

왜 DP인가?
- 백트래킹으로 풀면 모든 부분수열을 검사해야 해서 O(2^N) 이상.
- DP를 쓰면 **각 위치에서의 LIS 길이를 저장**하여 중복 계산을 제거, O(N²)로 해결.

핵심 점화식:
```
dp[i] = 1 (자기 자신만 포함)
j < i 이고 arr[j] < arr[i] 인 모든 j에 대해:
    dp[i] = max(dp[i], dp[j] + 1)
```

한 줄 해석: **"나(i) 앞에 있고, 나보다 값이 작은 원소들 중 가장 긴 LIS에 나를 이어붙인다"**

#### 풀이 전략

```
[전체 흐름]

dp 배열을 전부 1로 초기화 (최소 자기 자신)
        ↓
i = 0부터 N-1까지:
  j = 0부터 i-1까지:
    arr[j] < arr[i]?
      → YES → dp[i] = max(dp[i], dp[j]+1)
        ↓
max(dp) 반환
```

#### 소스코드

**Python**

```python
def longest_increasing(sequence):
    """최장 증가 수열의 길이를 반환한다"""
    n = len(sequence)
    memo = [1] * n  # 최소 길이 = 자기 자신(1)

    for i in range(1, n):
        for j in range(i):
            # j가 i보다 앞에 있고, 값이 더 작으면
            if sequence[j] < sequence[i]:
                memo[i] = max(memo[i], memo[j] + 1)

    return max(memo)

# --- 실행 ---
print(longest_increasing([10, 20, 10, 30, 20, 50]))  # 4
```

**Java**

```java
import java.util.Arrays;

public class LISSolver {
    public static int longestIncreasing(int[] sequence) {
        int n = sequence.length;
        int[] memo = new int[n];
        Arrays.fill(memo, 1);

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (sequence[j] < sequence[i]) {
                    memo[i] = Math.max(memo[i], memo[j] + 1);
                }
            }
        }

        int longest = 0;
        for (int val : memo) longest = Math.max(longest, val);
        return longest;
    }

    public static void main(String[] args) {
        int[] seq = {10, 20, 10, 30, 20, 50};
        System.out.println(longestIncreasing(seq)); // 4
    }
}
```

**코드 흐름 설명**

| i | arr[i] | j 탐색 결과 | memo[i] | 설명 |
|---|--------|-----------|---------|------|
| 0 | 10 | (없음) | 1 | 자기 자신 |
| 1 | 20 | arr[0]=10 < 20 → memo[0]+1=2 | 2 | [10,20] |
| 2 | 10 | 앞에 더 작은 것 없음 | 1 | [10] |
| 3 | 30 | arr[0]<30→2, arr[1]<30→3 | 3 | [10,20,30] |
| 4 | 20 | arr[0]<20→2, arr[2]<20→2 | 2 | [10,20] |
| 5 | 50 | arr[3]<50→4 (최대) | 4 | [10,20,30,50] |

**최종: max(memo) = 4**

---

### 문제 2: 배낭 채우기 (0/1 Knapsack)

#### 핵심 개념

**"N개의 물건(각각 무게 W, 가치 V)이 있고, 최대 무게 K인 배낭에 넣을 수 있는 최대 가치를 구하라"**

왜 DP인가?
- 각 물건을 "넣는다/안 넣는다" 2가지 선택 → 전부 탐색하면 O(2^N)
- **2차원 DP 테이블**을 사용하면 O(N × K)로 해결

핵심 점화식:
```
dp[i][j] = i번째 물건까지 고려, 용량 j일 때의 최대 가치

if weight[i] <= j:  (이 물건을 넣을 수 있다면)
    dp[i][j] = max(
        dp[i-1][j],               ← 이 물건 안 넣기
        dp[i-1][j-weight[i]] + value[i]  ← 이 물건 넣기
    )
else:               (이 물건이 너무 무겁다면)
    dp[i][j] = dp[i-1][j]        ← 이전 상태 그대로
```

핵심 통찰: **"넣는 경우"의 최적값은 이 물건 무게만큼 용량을 뺀 이전 행의 값 + 이 물건 가치**

#### 풀이 전략

```
[전체 흐름]

dp[N+1][K+1] 테이블 생성 (0행/0열은 더미)
        ↓
i = 1부터 N까지 (물건 순회):
  j = 1부터 K까지 (용량 순회):
    물건i 무게 <= j?
      → YES → dp[i][j] = max(안넣기, 넣기)
      → NO  → dp[i][j] = dp[i-1][j]
        ↓
dp[N][K] 반환
```

0행/0열 더미를 두는 이유: 첫 번째 물건부터 `dp[i-1]`을 참조할 수 있게 하기 위함.

#### 소스코드

**Python**

```python
def knapsack_max(items, capacity):
    """배낭에 넣을 수 있는 최대 가치를 반환
    items: [(weight, value), ...]
    """
    n = len(items)
    # dp[i][j]: i번째 물건까지 고려, 용량 j일 때 최대 가치
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i - 1]  # 0-indexed items
        for j in range(1, capacity + 1):
            if w <= j:
                dp[i][j] = max(
                    dp[i - 1][j],              # 안 넣기
                    dp[i - 1][j - w] + v       # 넣기
                )
            else:
                dp[i][j] = dp[i - 1][j]       # 무게 초과

    return dp[n][capacity]

# --- 실행 ---
stuff = [(6, 13), (4, 8), (3, 6), (5, 12)]
print(knapsack_max(stuff, 7))  # 14
```

**Java**

```java
public class KnapsackSolver {
    public static int knapsackMax(int[][] items, int capacity) {
        int n = items.length;
        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {
            int w = items[i - 1][0];
            int v = items[i - 1][1];
            for (int j = 1; j <= capacity; j++) {
                if (w <= j) {
                    dp[i][j] = Math.max(
                        dp[i - 1][j],
                        dp[i - 1][j - w] + v
                    );
                } else {
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }
        return dp[n][capacity];
    }

    public static void main(String[] args) {
        int[][] stuff = {{6,13},{4,8},{3,6},{5,12}};
        System.out.println(knapsackMax(stuff, 7)); // 14
    }
}
```

**코드 흐름 설명 (물건: (6,13)(4,8)(3,6)(5,12), 배낭 용량 7)**

| i\j | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-----|---|---|---|---|---|---|---|---|
| 0(더미) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1(W6,V13) | 0 | 0 | 0 | 0 | 0 | 0 | 13 | 13 |
| 2(W4,V8) | 0 | 0 | 0 | 0 | 8 | 8 | 13 | 13 |
| 3(W3,V6) | 0 | 0 | 0 | 6 | 8 | 8 | 13 | **14** |
| 4(W5,V12) | 0 | 0 | 0 | 6 | 8 | 12 | 13 | 14 |

dp[3][7] = max(dp[2][7]=13, dp[2][7-3]+6=8+6=14) = **14** (물건2+물건3)

---

### 문제 3: 격자 최대 합 경로

#### 핵심 개념

**"N×M 격자의 왼쪽 위에서 오른쪽 아래까지, 오른쪽 또는 아래로만 이동하며 지나는 칸의 합이 최대인 경로의 합을 구하라"**

왜 DP인가?
- 각 칸에 도달하는 최대 합은 **바로 위 칸** 또는 **바로 왼쪽 칸**에서의 최대 합 + 현재 칸 값
- 이전 칸의 결과를 재활용 → DP

점화식:
```
dp[r][c] = grid[r][c] + max(dp[r-1][c], dp[r][c-1])
```

첫 행/첫 열은 한 방향으로만 올 수 있으므로 누적합으로 초기화한다.

#### 풀이 전략

```
[전체 흐름]

dp[0][0] = grid[0][0]
첫 행: dp[0][c] = dp[0][c-1] + grid[0][c]
첫 열: dp[r][0] = dp[r-1][0] + grid[r][0]
        ↓
나머지 칸:
  dp[r][c] = grid[r][c] + max(위, 왼쪽)
        ↓
dp[N-1][M-1] 반환
```

#### 소스코드

**Python**

```python
def grid_max_path(grid):
    """격자 왼쪽위→오른쪽아래 최대 합 경로"""
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]

    # 첫 행 초기화 (왼쪽에서만 올 수 있음)
    for c in range(1, cols):
        dp[0][c] = dp[0][c - 1] + grid[0][c]

    # 첫 열 초기화 (위에서만 올 수 있음)
    for r in range(1, rows):
        dp[r][0] = dp[r - 1][0] + grid[r][0]

    # 나머지 칸
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = grid[r][c] + max(dp[r - 1][c], dp[r][c - 1])

    return dp[rows - 1][cols - 1]

# --- 실행 ---
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(grid_max_path(board))  # 29 (1→4→7→8→9)
```

**Java**

```java
public class GridPathMax {
    public static int gridMaxPath(int[][] grid) {
        int rows = grid.length, cols = grid[0].length;
        int[][] dp = new int[rows][cols];

        dp[0][0] = grid[0][0];

        for (int c = 1; c < cols; c++)
            dp[0][c] = dp[0][c - 1] + grid[0][c];

        for (int r = 1; r < rows; r++)
            dp[r][0] = dp[r - 1][0] + grid[r][0];

        for (int r = 1; r < rows; r++)
            for (int c = 1; c < cols; c++)
                dp[r][c] = grid[r][c] + Math.max(dp[r - 1][c], dp[r][c - 1]);

        return dp[rows - 1][cols - 1];
    }

    public static void main(String[] args) {
        int[][] board = {{1,2,3},{4,5,6},{7,8,9}};
        System.out.println(gridMaxPath(board)); // 29
    }
}
```

**코드 흐름 설명**

```
grid:           dp:
1  2  3         1   3   6
4  5  6         5  10  16
7  8  9        12  20  29

dp[2][2] = 9 + max(dp[1][2]=16, dp[2][1]=20) = 9 + 20 = 29
경로: 1→4→7→8→9 = 29
```

| 칸 | 계산 | dp값 |
|-----|------|------|
| (0,0) | 초기값 | 1 |
| (1,0) | 1+4 | 5 |
| (2,0) | 5+7 | 12 |
| (2,1) | 12+8 | 20 |
| (2,2) | max(16,20)+9 | **29** |

---

## 자주 하는 실수

### 1. 점화식의 방향을 잘못 잡는다

Bottom-Up에서 `dp[i]`가 `dp[i+1]`을 참조하면 아직 채워지지 않은 값을 읽게 된다. 항상 **이전에 계산된 값만 참조**하는지 확인하자.

### 2. 기저 조건을 빼먹는다

피보나치에서 `f(0)=0, f(1)=1`을 설정하지 않으면 배열 범위 에러가 발생한다. LIS에서 `dp[i]=1` 초기화를 빼먹으면 0이 나온다.

### 3. 1차원 DP와 2차원 DP를 혼동한다

LIS는 1차원 배열, 배낭은 2차원 배열이다. 문제에서 **변수가 2개** (물건 번호 + 용량)이면 2차원, **변수가 1개**면 1차원으로 설계한다.

### 4. 배낭 문제에서 더미 행/열을 안 만든다

`dp[i-1][j-w]`를 참조할 때 i=0이면 인덱스 에러. 0번 행/열을 더미로 두면 예외 처리 없이 일관되게 점화식을 적용할 수 있다.

### 5. 정답 위치를 잘못 읽는다

- LIS: `dp[N-1]`이 아니라 **`max(dp)`** 전체 최댓값
- 배낭: `dp[N][K]` — 마지막 행 마지막 열
- 격자: `dp[rows-1][cols-1]` — 오른쪽 아래 꼭짓점

---

## 언제 사용하면 좋은가

| 신호 | 예시 |
|------|------|
| "최대/최소 ~를 구하라" + 작은 문제 반복 | 배낭, 동전 교환, 격자 경로 |
| "~하는 방법의 수" | 계단 오르기, 타일 채우기 |
| "가장 긴/짧은 부분수열" | LIS, 최장 공통 부분수열(LCS) |
| "~의 최적 분할" | 행렬 곱셈 순서, 팰린드롬 분할 |
| "선택/비선택 구조" | 도둑 문제(인접 집 불가), 0/1 배낭 |
| 재귀로 풀면 같은 인자가 반복 호출됨 | → 메모이제이션 적용 신호 |

한 줄 판별: **"최대/최소/방법의 수" + "이전 결과를 재활용 가능"하면 → DP**

---

## 요약 정리

| 항목 | 내용 |
|------|------|
| 핵심 | 중복 계산 제거 (메모이제이션) |
| 두 조건 | 최적 부분 구조 + 중복 부분 문제 |
| Top-Down | 재귀 + 캐시 (필요한 것만 계산) |
| Bottom-Up | 반복문 + 배열 (작은 것부터 전부 계산) |
| 가장 어려운 것 | 점화식 도출 |
| 1차원 DP | 피보나치, LIS, 계단 |
| 2차원 DP | 배낭, 격자 경로, LCS |
| 시간복잡도 | 보통 O(N²) 또는 O(N×M) |

---

# 메타데이터
```json
{
  "category": "[고급 알고리즘] 동적계획법",
  "algorithm": "DP",
  "source_type": "generated",
  "style": ["easy", "code", "analogy", "theory"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "high",
  "language": "java"
}
```

---

```
변환 검수
- 원문 문장을 그대로 사용하지 않았는가: 예
- 원문 목차 구조를 그대로 따르지 않았는가: 예
- 원문 비유를 그대로 사용하지 않았는가: 예
- 원문 코드의 변수명과 주석을 그대로 사용하지 않았는가: 예
- 원문 이미지를 재사용하지 않았는가: 예
- 개념 설명의 정확성을 유지했는가: 예
- 초급자가 이해할 수 있는 흐름으로 재작성했는가: 예
```
