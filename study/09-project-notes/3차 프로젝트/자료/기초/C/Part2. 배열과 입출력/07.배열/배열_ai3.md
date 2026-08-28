# 제목
[C/Cpp 기초] 배열

# 본문

## 1. 한 줄 요약

배열은 동일한 자료형의 원소가 연속적인 메모리 주소에 배치된 집합체로, 원소 접근이 O(1)인 임의 접근(random access)을 지원한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

개별 변수 선언으로는 컴파일 타임에 크기를 모르거나 대량의 동종 데이터를 다룰 수 없다.

배열은 연속 메모리 블록을 제공하여 CPU 캐시 지역성(cache locality)을 최대화하고, 포인터 산술을 통한 효율적인 순회를 가능케 한다.

```text
원소 접근: arr[i] → *(arr + i) → base_addr + i * sizeof(T)
시간 복잡도: O(1) (임의 접근)
```

---

## 3. 핵심 아이디어

### 메모리 레이아웃

```c
int arr[5] = {10, 20, 30, 40, 50};
```

```text
base_addr (예: 0x1000):
주소  │ 0x1000│ 0x1004│ 0x1008│ 0x100C│ 0x1010│
값    │  10   │  20   │  30   │  40   │  50   │
인덱스│  [0]  │  [1]  │  [2]  │  [3]  │  [4]  │
```

`arr[i]`는 컴파일러가 `*(arr + i)`로 변환한다. `arr + i`는 `arr`의 주소에 `i * sizeof(int)`를 더한 주소이다.

### 배열 이름의 decay

배열 이름은 대부분의 표현식에서 첫 번째 원소의 포인터로 decay된다.

```c
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;           /* arr → &arr[0]으로 decay */
printf("%d\n", *p);     /* 1 */
printf("%d\n", *(p+2)); /* 3 */
```

예외: `sizeof(arr)`, `&arr` (배열 전체 주소)

### 캐시 지역성

배열 원소가 연속 메모리에 있으므로, 순차 접근 시 CPU 캐시 라인을 효율적으로 활용한다.

```c
/* 캐시 친화적: 순차 접근 */
for (int i = 0; i < N; i++) sum += arr[i];

/* 캐시 비친화적: 큰 보폭 접근 */
for (int i = 0; i < N; i += 64) sum += arr[i];
```

---

## 4. 동작 과정 살펴보기

### 범위 초과 접근 (Out-of-Bounds Access)

C는 배열 경계를 런타임에 검사하지 않는다.

```c
int arr[5] = {1, 2, 3, 4, 5};
printf("%d\n", arr[10]);  /* Undefined Behavior: 임의의 메모리 읽기 */
arr[10] = 99;             /* UB: 다른 변수, 스택 데이터, 리턴 주소 덮어쓸 수 있음 */
```

이는 스택 기반 버퍼 오버플로우 취약점의 근본 원인이다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 버블 정렬 */
void bubble_sort(int *arr, int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j+1]) {
                int tmp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = tmp;
            }
        }
    }
}

int main() {
    int arr[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("정렬 전: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    bubble_sort(arr, n);

    printf("정렬 후: ");
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");

    /* 포인터 산술로 배열 순회 */
    int *p = arr;
    int *end = arr + n;
    printf("포인터 순회: ");
    while (p < end) {
        printf("%d ", *p++);
    }
    printf("\n");

    return 0;
}
```

### VLA (Variable Length Array) - C99

```c
int n;
scanf("%d", &n);
int arr[n];  /* 런타임에 크기 결정: 스택 할당 */
/* C11에서 선택적 기능이 됨. 큰 크기면 스택 오버플로우 위험 */
```

대형 동적 배열은 `malloc`/`free`를 사용하는 것이 안전하다.

---

## 6. 마지막 정리

배열은 연속 메모리의 동종 원소 집합으로 O(1) 임의 접근을 제공한다.

`arr[i]`는 `*(arr + i)`와 동치이며, 배열 이름은 첫 원소 포인터로 decay된다.

C는 경계 검사를 하지 않으므로 범위 초과는 UB이고 심각한 보안 취약점이 된다.

연속 메모리 덕분에 캐시 지역성이 뛰어나 순차 접근 성능이 우수하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 배열",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
