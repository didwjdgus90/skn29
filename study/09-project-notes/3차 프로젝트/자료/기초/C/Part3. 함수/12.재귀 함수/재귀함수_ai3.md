# 제목
[C/Cpp 기초] 재귀 함수

# 본문

## 1. 한 줄 요약

재귀 함수는 기저 조건(base case)으로 종료되는 자기 참조 호출 구조로, 호출 스택에 O(n) 공간을 사용하며 분할 정복 알고리즘의 구조적 기반이 된다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

어떤 문제들은 동일한 구조의 더 작은 부분 문제로 귀납적으로 분해된다.

```text
문제 P(n) = f(P(n-1), P(n-2), ...)와 같이 정의될 때 재귀가 자연스럽다.
```

예: 트리 순회, 퀵정렬, 병합정렬, 그래프 DFS, Hanoi 탑 등.

반복문으로 모든 재귀를 구현할 수 있지만, 명시적 스택을 관리해야 하므로 코드 복잡도가 증가한다.

---

## 3. 핵심 아이디어

### 재귀의 구조적 정의

유효한 재귀 함수는 두 성질을 만족해야 한다.

1. **기저 조건(Base Case)**: 재귀 없이 직접 답을 반환
2. **재귀 감소(Progress)**: 각 재귀 호출에서 문제가 기저 조건을 향해 엄격히 감소

```c
int factorial(int n) {
    if (n <= 1) return 1;          /* 기저 조건 */
    return n * factorial(n - 1);   /* n → n-1: 단조 감소 보장 */
}
```

### 재귀 트리와 시간 복잡도

피보나치의 나이브 재귀는 O(2^n) 시간을 사용한다.

```text
fib(5)
├── fib(4)
│   ├── fib(3)
│   │   ├── fib(2), fib(1)
│   └── fib(2)
└── fib(3)
    ├── fib(2), fib(1)
```

중복 계산이 지수적으로 발생 → 메모이제이션(memoization)으로 O(n)으로 개선 가능.

### 꼬리 재귀 (Tail Recursion)

재귀 호출이 함수의 마지막 연산이면 꼬리 재귀이다.

```c
/* 일반 재귀 */
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  /* 반환 후 곱셈 필요 → 비꼬리 재귀 */
}

/* 꼬리 재귀 */
int factorial_tail(int n, int acc) {
    if (n <= 1) return acc;
    return factorial_tail(n - 1, n * acc);  /* 마지막 연산이 재귀 호출 */
}
```

꼬리 재귀 최적화(TCO)가 지원되는 컴파일러(GCC `-O2`)에서는 반복문과 동일한 코드로 변환된다.

---

## 4. 동작 과정 살펴보기

### 메모이제이션으로 피보나치 최적화

```c
#include <string.h>

#define MAX 100
long long memo[MAX];

long long fib_memo(int n) {
    if (n <= 1) return n;
    if (memo[n] != -1) return memo[n];  /* 캐시 히트 */
    memo[n] = fib_memo(n-1) + fib_memo(n-2);
    return memo[n];
}
```

시간 복잡도: O(n), 공간 복잡도: O(n).

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

/* 병합 정렬: 재귀적 분할 정복 */
void merge(int arr[], int l, int m, int r) {
    int n1 = m - l + 1, n2 = r - m;
    int left[n1], right[n2];

    for (int i = 0; i < n1; i++) left[i] = arr[l + i];
    for (int j = 0; j < n2; j++) right[j] = arr[m + 1 + j];

    int i = 0, j = 0, k = l;
    while (i < n1 && j < n2)
        arr[k++] = (left[i] <= right[j]) ? left[i++] : right[j++];
    while (i < n1) arr[k++] = left[i++];
    while (j < n2) arr[k++] = right[j++];
}

void merge_sort(int arr[], int l, int r) {
    if (l >= r) return;  /* 기저 조건: 원소 1개 이하 */
    int m = l + (r - l) / 2;
    merge_sort(arr, l, m);      /* 왼쪽 정렬 */
    merge_sort(arr, m + 1, r);  /* 오른쪽 정렬 */
    merge(arr, l, m, r);        /* 병합 */
}

/* 하노이 탑 */
void hanoi(int n, char from, char to, char aux) {
    if (n == 1) {
        printf("원판 1: %c → %c\n", from, to);
        return;
    }
    hanoi(n - 1, from, aux, to);
    printf("원판 %d: %c → %c\n", n, from, to);
    hanoi(n - 1, aux, to, from);
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = 7;

    merge_sort(arr, 0, n - 1);
    printf("병합 정렬 결과: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    printf("\n하노이 탑 (3개):\n");
    hanoi(3, 'A', 'C', 'B');

    return 0;
}
```

---

## 6. 마지막 정리

재귀는 기저 조건과 단조 감소하는 재귀 조건으로 구성되며, 정확성은 귀납적으로 증명된다.

각 호출마다 O(1) 스택 프레임을 사용하므로 깊이 n의 재귀는 O(n) 스택 공간이 필요하다.

중복 부분 문제가 있는 재귀는 메모이제이션으로 지수 시간을 다항 시간으로 개선할 수 있다.

꼬리 재귀는 컴파일러 최적화로 O(1) 스택 공간의 반복문과 동치가 된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 재귀 함수",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
