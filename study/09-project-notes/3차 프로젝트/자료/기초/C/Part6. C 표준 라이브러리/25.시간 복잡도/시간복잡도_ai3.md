# 제목
[C/Cpp 기초] 시간 복잡도

# 본문

## 1. 한 줄 요약

시간 복잡도는 알고리즘의 연산 횟수를 입력 크기 n의 함수로 표현하며, Big-O 표기법은 최악 케이스의 점근적 상한(asymptotic upper bound)을 나타낸다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

알고리즘의 절대적 실행 시간은 하드웨어에 의존하지만, 시간 복잡도는 하드웨어 독립적으로 알고리즘의 확장성(scalability)을 평가한다. O(n²) 알고리즘과 O(n log n) 알고리즘의 차이는 n=10^6에서 약 5만 배다.

---

## 3. 핵심 아이디어

### Big-O 정의

```text
f(n) = O(g(n))이면:
  n > n₀ 인 모든 n에 대해
  f(n) ≤ c * g(n) 을 만족하는 양수 c, n₀가 존재

즉, n이 충분히 클 때 g(n)의 상수 배가 f(n)의 상한이 됨
```

### 점근 표기법 구분

```text
O(g)  — 상한(upper bound): 최악 케이스 보장
Ω(g)  — 하한(lower bound): 최선 케이스 한계
Θ(g)  — 정확한 한계 (상한 = 하한)

예: 선형 탐색
  최선 O(1): 첫 원소가 답
  최악 O(n): 마지막 원소가 답
  평균 Θ(n): n/2 = Θ(n)
```

### 공간 복잡도 (Space Complexity)

```c
/* O(1) 공간: 추가 메모리 고정 */
void reverse_in_place(int *arr, int n) {
    for (int i = 0, j = n-1; i < j; i++, j--) {
        int tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
}

/* O(n) 공간: n에 비례한 추가 메모리 */
void reverse_copy(int *src, int *dst, int n) {
    for (int i = 0; i < n; i++) dst[i] = src[n-1-i];
}
```

---

## 4. 동작 과정 살펴보기

### 재귀 알고리즘의 복잡도 분석

```c
/* 피보나치 재귀: O(2ⁿ) */
int fib_naive(int n) {
    if (n <= 1) return n;
    return fib_naive(n-1) + fib_naive(n-2);
}
/* 재귀 트리: 깊이 n, 각 노드에서 2개 분기 → 2ⁿ */

/* 메모이제이션: O(n) */
int memo[100] = {0};
int fib_memo(int n) {
    if (n <= 1) return n;
    if (memo[n]) return memo[n];
    return memo[n] = fib_memo(n-1) + fib_memo(n-2);
}
```

### 마스터 정리 (분할 정복)

```text
T(n) = a*T(n/b) + f(n) 형태의 점화식:

퀵소트: T(n) = 2*T(n/2) + O(n) → O(n log n)
이진 탐색: T(n) = T(n/2) + O(1) → O(log n)
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define N 100000

/* 시간 측정 헬퍼 */
double measure_ms(clock_t start, clock_t end) {
    return 1000.0 * (end - start) / CLOCKS_PER_SEC;
}

/* O(n): 선형 합산 */
long long sum_linear(int *arr, int n) {
    long long s = 0;
    for (int i = 0; i < n; i++) s += arr[i];
    return s;
}

/* O(n²): 이중 반복 카운트 */
long long count_pairs(int *arr, int n, int target) {
    long long cnt = 0;
    for (int i = 0; i < n; i++)
        for (int j = i+1; j < n; j++)
            if (arr[i] + arr[j] == target) cnt++;
    return cnt;
}

/* O(n log n): 합산 + qsort */
int cmp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

/* 메모이제이션 피보나치 */
static long long fib_cache[100] = {0};
long long fib(int n) {
    if (n <= 1) return n;
    if (fib_cache[n]) return fib_cache[n];
    return fib_cache[n] = fib(n-1) + fib(n-2);
}

int main() {
    /* 성능 측정 */
    int *arr = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) arr[i] = i + 1;

    clock_t s, e;

    s = clock();
    long long sum = sum_linear(arr, N);
    e = clock();
    printf("O(n) sum: %lld, 시간: %.3fms\n", sum, measure_ms(s, e));

    s = clock();
    int *copy = malloc(N * sizeof(int));
    for (int i = 0; i < N; i++) copy[i] = arr[i];
    qsort(copy, N, sizeof(int), cmp);
    e = clock();
    printf("O(n log n) qsort: 시간: %.3fms\n", measure_ms(s, e));
    free(copy);

    /* n²은 작은 n으로만 */
    int small = 1000;
    s = clock();
    long long pairs = count_pairs(arr, small, small + 1);
    e = clock();
    printf("O(n²) pairs(n=%d): %lld, 시간: %.3fms\n", small, pairs, measure_ms(s, e));

    free(arr);

    /* 피보나치 메모이제이션 */
    printf("\n피보나치:\n");
    for (int i = 0; i <= 40; i += 5) {
        printf("fib(%d) = %lld\n", i, fib(i));
    }

    return 0;
}
```

---

## 6. 마지막 정리

Big-O는 최악 케이스의 점근적 상한으로, 상수 배수와 하위 항을 무시한다.

`Θ`는 정확한 성장률, `Ω`는 하한을 나타낸다. 면접이나 분석에서는 세 가지를 구분해야 한다.

재귀의 시간 복잡도는 재귀 트리의 크기로 분석하며, 메모이제이션으로 지수를 다항 시간으로 줄일 수 있다.

분할 정복의 복잡도는 마스터 정리로 빠르게 도출된다.

공간 복잡도도 항상 함께 고려해야 한다. 시간과 공간은 트레이드오프 관계인 경우가 많다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 시간 복잡도",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 5,
  "target_level": "high",
  "language": "c"
}
```
