# 제목
[알고리즘] 동적계획법(DP) - 메모이제이션, LIS, 배낭채우기 (SW검정 알고리즘 강의)

# 링크
<https://wikidocs.net/170477>
<https://wikidocs.net/170946>
<https://wikidocs.net/170954>

# 본문

## 동적계획법(Dynamic Programming)이란?

주어진 공식은 없다. 일반화를 통해 점화식을 찾고, 메모이제이션을 이용해서 연산을 반복해서 수행하는 과정이 바로 동적계획법이다.

- DP란: 적절한 점화식을 세운 후, 연산결과를 자료구조에 담아 다음 항 연산에 사용하는 것
- 핵심: 코드는 단순하다. 어려운 건 점화식을 구하는 것이다.

## 3.1.1 메모이제이션(Memoization)

### 메모이제이션이란?

> 컴퓨터 프로그램이 동일한 계산을 반복해야 할 때, 이전에 계산한 값을 메모리에 저장함으로써 동일한 계산의 반복 수행을 제거하여 프로그램 실행 속도를 빠르게 하는 기술이다. 동적 계획법의 핵심이 되는 기술이다.

각 시점에서 계산한 결과를 적당한 자료구조에 저장하여 다음 계산을 할 때 사용한다는 뜻이다.

### 피보나치 수열 메모하기

피보나치 수열: 앞의 두 항을 더한 것을 현재 값으로 갖는 수열

점화식: `f(n) = f(n-1) + f(n-2)` (단, f(0)=1, f(1)=1)

<IMAGE>피보나치 수열 점화식 수식 이미지</IMAGE>

```java
public static void main(String[] args) {
    int arr[] = new int[10];
    arr[0] = 1;
    arr[1] = 1;

    for (int i = 2; i < 10; i++) {
        arr[i] = arr[i-2] + arr[i-1];  // 점화식 그대로 구현
    }

    System.out.println(Arrays.toString(arr));
    // [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
}
```

이름만 거창하지 실제로는 점화식의 각 항을 자료구조에 저장한 후, 관계를 이용해서 다음 항을 도출하는 과정이다.
점화식만 완벽하게 세운다면 구현은 어렵지 않다.

---

## 3.1.2 동적계획법 구현하기(1) - LIS (최장증가수열)

### 문제

> 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.
> 예) A = {10, 20, 10, 30, 20, 50} → LIS = {10, 20, 30, 50} → 길이 4

### 백트래킹으로 먼저 풀어보기

```java
static int[] arr = {10, 20, 10, 30, 20, 50};

public static void main(String[] args) {
    ArrayList<Integer> list = new ArrayList<Integer>();

    for (int i = 0; i < 6; i++) {
        int location = i;
        int value = arr[i];
        list.add(value);
        btr(location, value, list);
        list.remove(list.size() - 1);
    }
}

private static void btr(int location, int value, ArrayList<Integer> list) {
    if (location == 5) {
        System.out.println(list.toString());
        return;
    }
    for (int i = location + 1; i < 6; i++) {
        if (arr[i] > value) {
            list.add(arr[i]);
            btr(i, arr[i], list);
            list.remove(list.size() - 1);
        }
    }
}
```

문제점: 항 6개에 최대 63번 메서드 호출. 항이 늘어날수록 기하급수적으로 증가 → DP 필요

### DP로 풀기

핵심 점화식:
> N번 위치에서의 LIS는,
> ① 나보다 앞에 위치한
> ② 나보다 작은 값을 가진 항 중에
> ③ 가장 큰 LIS값 + 1이다.

```java
static int[] arr = {10, 20, 10, 30, 20, 50};

public static void main(String[] args) {
    int[] dp = new int[6];

    for (int i = 0; i < 6; i++) {
        dp[i] = 1;  // 자기 자신은 무조건 포함 → 초기값 1
        for (int j = 0; j < 6; j++) {
            if (j < i) {                    // ① 나보다 앞에 위치한
                if (arr[j] < arr[i]) {      // ② 나보다 작은 값을 가진 항 중에
                    dp[i] = Math.max(dp[i], dp[j] + 1);  // ③ 가장 큰 LIS값 + 1
                }
            }
        }
    }

    System.out.println(Arrays.toString(dp));
    // [1, 2, 1, 3, 2, 4]
    // 정답: dp 배열의 최댓값 = 4
}
```

dp 배열 해석:
| 인덱스 | 값 | dp 의미 |
|--------|-----|---------|
| 0 | 10 | 1 (자기 자신) |
| 1 | 20 | 2 (10→20) |
| 2 | 10 | 1 (자기 자신) |
| 3 | 30 | 3 (10→20→30) |
| 4 | 20 | 2 (10→20) |
| 5 | 50 | 4 (10→20→30→50) |

DP 코드는 정말 단순하다. 특별한 자료구조도, 복잡한 메서드도 필요 없다. DP가 어려운 이유는 오직 점화식을 구하는 것이 어렵기 때문이다.

---

## 3.1.3 동적계획법 구현하기(2) - 배낭채우기(Knapsack)

LIS와 함께 가장 대표적인 동적계획법 문제. 2차원 DP의 가장 기본형이다.

### 문제

> N개의 물건과 K만큼의 무게를 넣을 수 있는 배낭이 있다.
> N개의 물건은 각각 무게 W와 가치 V를 가진다.
> 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 구하라.

예제:
- N=4, K=7 (물건 4개, 배낭 최대 무게 7)
- 물건: (W=6, V=13), (W=4, V=8), (W=3, V=6), (W=5, V=12)

### 2차원 배열 DP

dp 테이블 구성:
- 행(i): 물건 번호 (0~N)
- 열(j): 배낭 용량 (0~K)
- `dp[i][j]`: i번째 물건까지 고려했을 때, 용량 j인 배낭에 넣을 수 있는 최대 가치

점화식:
```
if (weight <= j):
    dp[i][j] = max(dp[i-1][j],  dp[i-1][j-weight] + value)
    //          이 물건 안 넣기   이 물건 넣기 (남은 공간의 최적 + 이 물건 가치)
else:
    dp[i][j] = dp[i-1][j]       // 무게 초과 → 이 물건 넣기 불가
```

```java
public static void main(String[] args) {
    int N = 4;
    int K = 7;
    // 0번 인덱스는 더미값 (점화식 일반화를 위해)
    int[][] arr = {{0,0}, {6,13}, {4,8}, {3,6}, {5,12}};

    int[][] dp = new int[N+1][K+1];

    for (int i = 1; i <= N; i++) {
        int weight = arr[i][0];
        int value  = arr[i][1];
        for (int j = 1; j <= K; j++) {
            if (weight <= j) {
                // 이 물건을 넣을 수 있을 때: 넣는 경우 vs 안 넣는 경우 중 최대
                dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-weight] + value);
            } else {
                // 이 물건을 넣을 수 없을 때: 이전 물건까지의 최적값 그대로
                dp[i][j] = dp[i-1][j];
            }
        }
    }

    for (int i = 0; i < N+1; i++) {
        System.out.println(Arrays.toString(dp[i]));
    }
    // [0, 0, 0, 0, 0, 0, 0,  0]
    // [0, 0, 0, 0, 0, 0, 13, 13]  ← 물건1(W=6,V=13)
    // [0, 0, 0, 0, 8, 8, 13, 13]  ← 물건2(W=4,V=8)
    // [0, 0, 0, 6, 8, 8, 13, 14]  ← 물건3(W=3,V=6)
    // [0, 0, 0, 6, 8, 12,13, 14]  ← 물건4(W=5,V=12)
    // 정답: dp[4][7] = 14
}
```

### dp 테이블 읽는 법

<IMAGE>Knapsack dp 테이블 step1 - 첫 번째 물건(W=6,V=13) 채우기</IMAGE>

첫 번째 물건(W=6, V=13): 용량 6 이상인 칸부터 13을 채운다.

<IMAGE>Knapsack dp 테이블 step2 - 두 번째 물건(W=4,V=8) 채우기 + 위 행과 비교</IMAGE>

두 번째 물건(W=4, V=8): 용량 4에서 8을 채운다. 용량 6에서 위(13)와 비교 → 13이 더 크므로 유지.

<IMAGE>Knapsack dp 테이블 step3 - 세 번째 물건(W=3,V=6) + 두 물건 동시 고려</IMAGE>

세 번째 물건(W=3, V=6): 용량 7에서 위(13)와 비교할 때,
물건3 무게=3이므로 남은 공간 7-3=4에서의 최적값(dp[i-1][4]=8)과 물건3 가치(6)를 더하면 14.
→ `dp[i][7] = max(13, 8+6) = 14`

### arr와 dp 행/열을 1개씩 더 만드는 이유

첫 번째 물건부터 바로 위 행과 비교할 수 있도록 하기 위한 더미값이다.
더미 행/열이 있어야 점화식을 예외처리 없이 일반적으로 적용할 수 있다.

---

## DP 접근 전략 정리

1. 작은 예시로 손으로 직접 테이블을 채워보면서 패턴을 찾는다.
2. 패턴을 점화식으로 표현한다.
3. 점화식을 코드로 구현한다. (코드 자체는 단순)
4. 극단적인 케이스(경계값, 최솟값/최댓값)를 확인한다.

| 문제 유형 | dp 차원 | 핵심 점화식 |
|----------|---------|-----------|
| 피보나치 | 1차원 | `dp[i] = dp[i-1] + dp[i-2]` |
| LIS | 1차원 | `dp[i] = max(dp[j]+1)` (j<i, arr[j]<arr[i]) |
| Knapsack | 2차원 | `dp[i][j] = max(dp[i-1][j], dp[i-1][j-W]+V)` |

# 메타데이터
```json
{
  "category": "동적계획법",
  "algorithm": "DP",
  "source_type": "blog",
  "style": [
    "easy",
    "code",
    "theory"
  ],
  "intuition_score": 4,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "java",
  "source": "wikidocs.net SW검정 알고리즘 강의"
}
```
