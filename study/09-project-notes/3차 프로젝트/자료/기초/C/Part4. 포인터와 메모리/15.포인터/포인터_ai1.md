# 제목
[C/Cpp 기초] 포인터

# 본문

## 1. 한 줄 요약

포인터는 메모리 주소를 저장하는 변수이다. 포인터를 통해 다른 변수의 메모리 위치를 직접 다룰 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

함수에서 변수의 값을 직접 변경하려면 주소가 필요하다.

```c
void double_it(int x) {
    x *= 2;  /* 복사본만 변경, 원본 변화 없음 */
}

/* 포인터를 사용하면 원본 변경 가능 */
void double_it_ptr(int *x) {
    *x *= 2;  /* 주소를 통해 원본 변경 */
}

int n = 5;
double_it_ptr(&n);  /* n = 10 */
```

---

## 3. 핵심 아이디어

### 포인터 선언

```c
int *p;      /* int 타입 포인터 */
double *dp;  /* double 타입 포인터 */
char *cp;    /* char 타입 포인터 */
```

### & 연산자 (주소 연산자)

변수의 메모리 주소를 얻는다.

```c
int x = 10;
int *p = &x;  /* p에 x의 주소를 저장 */
printf("x의 주소: %p\n", (void *)p);
```

### * 연산자 (역참조 연산자)

포인터가 가리키는 주소의 값에 접근한다.

```c
int x = 10;
int *p = &x;
printf("%d\n", *p);  /* 10: p가 가리키는 값 */
*p = 20;             /* x의 값을 20으로 변경 */
printf("%d\n", x);   /* 20 */
```

### NULL 포인터

아무것도 가리키지 않는 포인터.

```c
int *p = NULL;  /* 안전한 초기화 */
if (p != NULL) {
    *p = 10;    /* NULL 체크 후 사용 */
}
```

---

## 4. 동작 과정 살펴보기

### 포인터 동작 시각화

```text
메모리:
주소     값
0x100   10   ← int x = 10;
0x200   0x100 ← int *p = &x;  (p는 x의 주소 저장)

p → 0x100 → 10

*p 는 0x100 주소의 값 = 10
*p = 20 → 0x100 주소에 20을 저장 → x가 20이 됨
```

### 포인터 크기

포인터 자체는 주소를 저장하므로, 타입과 무관하게 같은 크기이다.

```c
printf("%zu\n", sizeof(int *));    /* 8 (64비트 시스템) */
printf("%zu\n", sizeof(double *)); /* 8 */
printf("%zu\n", sizeof(char *));   /* 8 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 포인터로 두 값 교환 */
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

/* 포인터로 두 값 동시에 반환 */
void min_max(int arr[], int n, int *min, int *max) {
    *min = *max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] < *min) *min = arr[i];
        if (arr[i] > *max) *max = arr[i];
    }
}

int main() {
    int x = 10, y = 20;
    printf("교환 전: x=%d, y=%d\n", x, y);
    swap(&x, &y);
    printf("교환 후: x=%d, y=%d\n", x, y);

    /* 포인터 기본 연산 */
    int n = 42;
    int *p = &n;
    printf("n = %d\n", n);
    printf("&n = %p\n", (void *)&n);
    printf("p = %p\n", (void *)p);
    printf("*p = %d\n", *p);

    /* 포인터로 값 변경 */
    *p = 100;
    printf("변경 후 n = %d\n", n);

    /* min, max 찾기 */
    int arr[] = {5, 3, 8, 1, 9, 2};
    int min_val, max_val;
    min_max(arr, 6, &min_val, &max_val);
    printf("최솟값: %d, 최댓값: %d\n", min_val, max_val);

    return 0;
}
```

### 포인터와 배열 관계

```c
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;  /* arr = &arr[0] */

printf("%d\n", *p);      /* 10 */
printf("%d\n", *(p+1));  /* 20 */
printf("%d\n", *(p+2));  /* 30 */
```

---

## 6. 마지막 정리

포인터는 메모리 주소를 저장하는 변수이다.

`&`는 변수의 주소를 얻고, `*`는 포인터가 가리키는 값에 접근한다.

포인터를 통해 함수에서 원본 변수를 변경할 수 있다.

NULL 포인터는 역참조하면 프로그램이 종료되므로 반드시 NULL 체크를 해야 한다.

포인터 크기는 타입과 무관하게 플랫폼에 따라 결정된다 (64비트 시스템: 8바이트).

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 포인터",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
