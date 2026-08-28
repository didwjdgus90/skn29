# 제목
[C/Cpp 기초] 배열과 포인터

# 본문

## 1. 한 줄 요약

C에서 배열 이름은 첫 번째 원소의 주소와 같으며, 포인터 산술을 이용해 배열의 원소에 접근할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

배열과 포인터는 C에서 밀접하게 연결되어 있다.

함수에 배열을 전달할 때 실제로는 포인터가 전달되며, 배열을 효율적으로 조작하기 위해 포인터 산술을 사용한다.

```c
void sum_array(int *arr, int n) {  /* 포인터로 배열 받음 */
    int sum = 0;
    for (int *p = arr; p < arr + n; p++) {  /* 포인터 이동 */
        sum += *p;
    }
}
```

---

## 3. 핵심 아이디어

### 배열 이름 = 첫 원소의 주소

```c
int arr[5] = {10, 20, 30, 40, 50};

arr    == &arr[0]  /* 첫 번째 원소의 주소 */
*arr   == arr[0]   /* 10 */
```

### 포인터 산술

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;

p + 0 → arr[0]의 주소
p + 1 → arr[1]의 주소 (p + 1 * sizeof(int))
p + 2 → arr[2]의 주소
```

### arr[i]와 *(arr+i)는 같다

```c
int arr[] = {10, 20, 30};

arr[2]    == *(arr + 2)  /* 30 */
*(arr + 1) == arr[1]     /* 20 */
```

---

## 4. 동작 과정 살펴보기

### 포인터로 배열 순회

```text
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;  /* p → arr[0] (주소 1000) */

*p     → 10 (주소 1000)
*(p+1) → 20 (주소 1004)
*(p+2) → 30 (주소 1008)

p++: p가 arr[1]을 가리킴 (주소 1004)
```

### 함수에 배열 전달

```c
/* 배열을 함수에 전달하면 포인터로 decay */
void print_arr(int arr[], int n)  /* 실제로는 int *arr */
void print_arr(int *arr, int n)   /* 동일한 의미 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 배열을 포인터로 받아서 처리 */
void print_array(int *arr, int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);  /* arr[i] == *(arr + i) */
    }
    printf("\n");
}

/* 포인터로 순회 */
int sum_by_pointer(int *arr, int n) {
    int sum = 0;
    int *end = arr + n;  /* 마지막 원소 다음 주소 */
    for (int *p = arr; p < end; p++) {
        sum += *p;
    }
    return sum;
}

/* 포인터로 배열 역순 출력 */
void print_reverse(int *arr, int n) {
    int *p = arr + n - 1;  /* 마지막 원소 */
    while (p >= arr) {
        printf("%d ", *p);
        p--;
    }
    printf("\n");
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int n = sizeof(arr) / sizeof(arr[0]);

    /* 배열 이름 = 포인터 */
    printf("arr = %p\n", (void *)arr);
    printf("&arr[0] = %p\n", (void *)&arr[0]);
    printf("같은가: %s\n", arr == &arr[0] ? "예" : "아니오");

    /* 인덱스 vs 포인터 산술 */
    printf("\narr[2] = %d\n", arr[2]);
    printf("*(arr+2) = %d\n", *(arr + 2));
    printf("*(2+arr) = %d\n", *(2 + arr));  /* C에서 허용 */
    printf("2[arr] = %d\n", 2[arr]);         /* 이것도 허용! (신기하지만 arr[2]와 같음) */

    /* 함수에 전달 */
    printf("\n배열: ");
    print_array(arr, n);
    printf("합계: %d\n", sum_by_pointer(arr, n));
    printf("역순: ");
    print_reverse(arr, n);

    return 0;
}
```

### sizeof 차이 주의

```c
int arr[5] = {1, 2, 3, 4, 5};
int *p = arr;

sizeof(arr)  /* 20: 배열 전체 크기 */
sizeof(p)    /* 8: 포인터 크기 (64비트) */
```

함수 안에서 배열 매개변수의 sizeof는 포인터 크기를 반환한다!

```c
void func(int arr[]) {
    printf("%zu\n", sizeof(arr));  /* 8: 포인터 크기 (배열 크기 아님!) */
}
```

---

## 6. 마지막 정리

배열 이름은 첫 번째 원소의 주소이다.

`arr[i]`와 `*(arr + i)`는 완전히 동일하다.

함수에 배열을 전달하면 포인터로 변환(decay)된다.

함수 안에서 배열 매개변수의 `sizeof`는 배열 크기가 아닌 포인터 크기를 반환한다.

포인터 산술로 배열을 효율적으로 순회할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 배열과 포인터",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
