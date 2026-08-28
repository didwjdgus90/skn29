# 제목
[C/Cpp 기초] 배열과 포인터

# 본문

## 1. 한 줄 요약

C에서 배열 이름은 대부분의 컨텍스트에서 첫 번째 원소의 포인터로 decay되며, `arr[i]`는 `*(arr + i)`의 문법적 설탕이다. 단, `sizeof`와 `&` 연산자는 예외이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

배열-포인터 동치관계는 C의 핵심 설계 결정 중 하나이다.

배열을 포인터로 전달하면 복사 오버헤드 없이 대용량 데이터를 함수에 전달할 수 있고, 포인터 산술로 임의 접근 및 순회를 O(1)에 수행할 수 있다.

그러나 이 동치관계는 완전하지 않으며 오해가 버그의 원인이 된다.

---

## 3. 핵심 아이디어

### Array Decay (배열 소멸)

배열 이름이 포인터로 변환되는 암묵적 변환.

```c
int arr[5];
int *p = arr;   /* arr → &arr[0]: array decay */
```

**Decay가 발생하지 않는 경우:**

```c
sizeof(arr)      /* 배열 전체 크기 반환: 20 */
sizeof(p)        /* 포인터 크기: 8 */

&arr             /* int (*)[5] 타입: 배열 전체의 주소 */
&arr + 1         /* sizeof(int[5]) = 20바이트 이동 */
```

### 배열과 포인터의 근본적 차이

| | 배열 `int arr[5]` | 포인터 `int *p` |
|---|---|---|
| 메모리 | 원소 저장 공간 | 주소 저장 공간 |
| sizeof | 전체 크기 (20) | 포인터 크기 (8) |
| `&` | `int (*)[5]` | `int **` |
| 재할당 | 불가 | 가능 |
| 배열 이름 | lvalue이지만 수정 불가 | 수정 가능 |

### 포인터 산술의 정의된 범위

```c
int arr[5];
int *p = arr;

p + 5;  /* 정의됨: arr[5] 바로 뒤 (역참조 불가) */
p + 6;  /* UB: 배열 범위 외 */
```

포인터 산술은 같은 배열 내부 또는 하나 뒤(past-the-end)에서만 정의된다.

---

## 4. 동작 과정 살펴보기

### 함수 파라미터의 배열-포인터 동치

```c
void f(int arr[])    /* 컴파일러가 int *arr로 해석 */
void f(int arr[10])  /* 크기 무시됨, int *arr와 동일 */
void f(int *arr)     /* 위와 동일 */
```

이 세 선언은 모두 동일한 함수 시그니처이다.

결과적으로 함수 내부에서 `sizeof(arr)`는 포인터 크기(8)를 반환한다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 세 선언 모두 동일 */
void func_a(int arr[], int n);
void func_b(int arr[10], int n);
void func_c(int *arr, int n);

void func_c(int *arr, int n) {
    printf("함수 내 sizeof(arr): %zu (포인터 크기)\n", sizeof(arr));
    for (int i = 0; i < n; i++) {
        /* arr[i] == *(arr + i) == *(i + arr) == i[arr] */
        printf("arr[%d] = %d = *(arr+%d) = %d\n",
               i, arr[i], i, *(arr + i));
    }
}

int main() {
    int arr[5] = {10, 20, 30, 40, 50};

    printf("main 내 sizeof(arr): %zu (배열 크기)\n", sizeof(arr));

    /* & 연산자 비교 */
    int *p = arr;   /* &arr[0]: int * */
    /* int (*q)[5] = &arr; */  /* &arr: int (*)[5] */

    printf("arr = %p\n", (void *)arr);
    printf("arr + 1 = %p (차이: %zu)\n",
           (void *)(arr + 1),
           (size_t)((unsigned char *)(arr + 1) - (unsigned char *)arr));

    func_c(arr, 5);

    /* 포인터 차이: 원소 개수 반환 */
    int *first = arr;
    int *last = arr + 4;
    ptrdiff_t count = last - first;
    printf("포인터 차이: %td (원소 수)\n", count);

    return 0;
}

void func_a(int arr[], int n) { (void)arr; (void)n; }
void func_b(int arr[10], int n) { (void)arr; (void)n; }
```

---

## 6. 마지막 정리

배열 이름은 `sizeof`와 `&`를 제외한 모든 컨텍스트에서 첫 번째 원소의 포인터로 decay된다.

`arr[i]` == `*(arr + i)`가 성립하고, `sizeof(arr)` != `sizeof(ptr)`이다.

함수 파라미터의 배열 선언은 모두 포인터로 해석되므로, 배열 크기는 별도 매개변수로 전달해야 한다.

포인터 산술은 같은 배열 범위 내에서만 정의된 동작이며, 범위 외 접근은 UB이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 배열과 포인터",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
