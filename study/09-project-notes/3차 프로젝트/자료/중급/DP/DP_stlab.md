# 제목
[알고리즘] 동적 계획법 (Dynamic Programming)

# 링크
<https://st-lab.tistory.com/128>

# 본문

## DP란?
DP는 큰 문제를 작은 문제로 쪼개서 풀고, 이미 푼 결과를 저장해두었다가 재활용하는 기법이다.

시험 공부할 때 노트 필기와 같다.
어제 공부한 내용을 노트에 적어두면 오늘 다시 처음부터 공부하지 않아도 된다.
DP도 계산한 결과를 저장(메모이제이션)해두고 같은 계산이 필요할 때 재사용한다.

적용 조건:
1. 최적 부분 구조: 큰 문제의 최적해 = 작은 문제의 최적해들의 조합
2. 중복되는 부분 문제: 같은 작은 문제가 여러 번 반복 등장

## Top-Down vs Bottom-Up
Top-Down (메모이제이션): 재귀로 위에서 아래로 풀면서 결과를 저장
Bottom-Up (타뷸레이션): 작은 문제부터 순서대로 풀면서 테이블을 채움

## 예제: 계단 오르기
계단이 N개 있다. 한 번에 1칸 또는 2칸 오를 수 있을 때, N번째 계단에 오르는 방법의 수는?

점화식: dp[n] = dp[n-1] + dp[n-2]
n번째 계단 = (n-1번째에서 1칸) + (n-2번째에서 2칸)

dp[1]=1, dp[2]=2, dp[3]=3, dp[4]=5, dp[5]=8

## 구현 코드 (Python)
Bottom-Up 방식으로 dp 배열을 채워나간다.
이전 두 값만 있으면 되므로 공간 효율적으로 최적화도 가능하다.

```python
def climb_stairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(climb_stairs(5))  # 출력: 8
```

## 예제: 배낭 문제 (0/1 Knapsack)
무게 한도 W인 배낭, N개의 물건 (각각 무게w, 가치v)
배낭에 넣을 수 있는 최대 가치를 구하라.

dp[i][w] = i번째 물건까지 고려했을 때 무게 w 이하로 담을 수 있는 최대 가치
점화식: dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight[i]] + value[i])

```python
def knapsack(W, items):
    n = len(items)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = items[i-1]
        for cap in range(W + 1):
            dp[i][cap] = dp[i-1][cap]  # 안 넣는 경우
            if cap >= w:
                dp[i][cap] = max(dp[i][cap], dp[i-1][cap-w] + v)

    return dp[n][W]

items = [(2,3), (3,4), (4,5), (5,8)]
print(knapsack(5, items))  # 출력: 7
```

# 메타데이터
```json
{
  "category": "동적 계획법",
  "algorithm": "DP",
  "source_type": "blog",
  "style": [
    "easy",
    "analogy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python"
}
```