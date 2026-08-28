# 제목
[C/Cpp 기초] 시간 복잡도

# 본문

## 1. 한 줄 요약

시간 복잡도는 입력 크기 n이 증가할 때 알고리즘의 연산 횟수가 얼마나 늘어나는지를 Big-O 표기법으로 나타낸 것이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

같은 결과를 내는 두 코드 중 어느 것이 더 빠른지 판단해야 한다.

```c
/* 방법 1: 배열에서 최댓값 찾기 */
int max1 = arr[0];
for (int i = 1; i < n; i++)     /* n번 반복 */
    if (arr[i] > max1) max1 = arr[i];

/* 방법 2: 매번 전체 탐색 */
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) /* n*n번 반복 */
        /* ... */
```

n=1000일 때 방법1은 1000번, 방법2는 1,000,000번 연산한다.

---

## 3. 핵심 아이디어

### 주요 Big-O 표기

| 표기 | 이름 | 예시 |
|---|---|---|
| O(1) | 상수 | 배열 인덱스 접근 |
| O(log n) | 로그 | 이진 탐색 |
| O(n) | 선형 | 배열 순회 |
| O(n log n) | 선형 로그 | 효율적 정렬 |
| O(n²) | 이차 | 버블 정렬 |
| O(2ⁿ) | 지수 | 피보나치 재귀 |

### 코드에서 복잡도 파악하기

```c
/* O(1): 반복 없음 */
int x = arr[0];

/* O(n): 반복 1개 */
for (int i = 0; i < n; i++) { ... }

/* O(n²): 중첩 반복 */
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++) { ... }

/* O(log n): 반씩 줄어듦 */
while (n > 1) n /= 2;
```

---

## 4. 동작 과정 살펴보기

### n 크기별 연산 횟수

```text
n = 1,000,000 (백만)일 때:

O(1)      :           1
O(log n)  :          20
O(n)      :   1,000,000
O(n log n):  20,000,000
O(n²)     : 10^12 (1조!) ← 불가능
O(2ⁿ)     : 10^300,000   ← 우주 나이보다 긴 시간
```

### 이진 탐색이 O(log n)인 이유

```text
100개 중 탐색:
  1번: 50개로 줄임
  2번: 25개로 줄임
  3번: 12개로 줄임
  ...
  7번: 1개 남음
  → 총 7번 = log₂(100) ≈ 7
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <time.h>

#define N 10000

/* O(1): 상수 시간 */
int get_first(int *arr) {
    return arr[0];
}

/* O(n): 선형 탐색 */
int linear_search(int *arr, int n, int target) {
    for (int i = 0; i < n; i++)
        if (arr[i] == target) return i;
    return -1;
}

/* O(log n): 이진 탐색 (정렬된 배열 필요) */
int binary_search(int *arr, int n, int target) {
    int lo = 0, hi = n - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

/* O(n²): 버블 정렬 */
void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++)
        for (int j = 0; j < n - i - 1; j++)
            if (arr[j] > arr[j+1]) {
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
}

int main() {
    int arr[N];
    for (int i = 0; i < N; i++) arr[i] = i;

    /* O(1) 측정 */
    clock_t start, end;
    start = clock();
    volatile int v = get_first(arr);
    end = clock();
    printf("O(1) get_first: %ld ticks\n", end - start);

    /* O(n) 측정 */
    start = clock();
    for (int r = 0; r < 1000; r++) linear_search(arr, N, N-1);
    end = clock();
    printf("O(n) linear (1000회): %ld ticks\n", end - start);

    /* O(log n) 측정 */
    start = clock();
    for (int r = 0; r < 1000; r++) binary_search(arr, N, N-1);
    end = clock();
    printf("O(log n) binary (1000회): %ld ticks\n", end - start);

    return 0;
}
```

---

## 6. 마지막 정리

Big-O는 입력 크기 n에 따른 연산 횟수의 증가 추세를 나타낸다. 상수 배수는 무시한다.

중첩 반복문은 O(n²), 반이 줄어드는 구조는 O(log n)이다.

알고리즘 선택 시 시간 복잡도를 먼저 확인해야 한다.

O(n²) 이상은 n이 커질수록 빠르게 느려지므로 주의가 필요하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 시간 복잡도",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
