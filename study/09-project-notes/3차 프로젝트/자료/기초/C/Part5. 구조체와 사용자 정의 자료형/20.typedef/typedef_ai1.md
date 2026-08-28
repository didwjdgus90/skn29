# 제목
[C/Cpp 기초] typedef

# 본문

## 1. 한 줄 요약

`typedef`는 기존 자료형에 새로운 이름(별명)을 붙여주는 키워드로, 코드 가독성을 높이고 타입 선언을 간결하게 만든다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

구조체를 사용할 때마다 `struct` 키워드를 반복 작성해야 하는 번거로움을 줄인다.

```c
/* typedef 없이 */
struct Student s1;
struct Student s2;

/* typedef 사용 */
typedef struct Student Student;

Student s1;  /* struct 없이 사용 가능 */
Student s2;
```

---

## 3. 핵심 아이디어

### 기본 문법

```c
typedef 기존타입 새이름;

typedef int Int32;         /* int를 Int32로 */
typedef unsigned char Byte; /* unsigned char를 Byte로 */
typedef char* String;       /* char*를 String으로 */
```

### 구조체와 함께 사용

```c
/* 방법 1: 별도 typedef */
struct Point { int x, y; };
typedef struct Point Point;

/* 방법 2: 한번에 정의 (일반적) */
typedef struct {
    int x;
    int y;
} Point;

/* 사용 */
Point p = {3, 5};  /* struct Point p 대신 */
```

### 함수 포인터 typedef

```c
/* 함수 포인터 타입 정의 */
typedef int (*Comparator)(const void *, const void *);

/* 사용 */
Comparator cmp = compare_int;
```

---

## 4. 동작 과정 살펴보기

### typedef vs #define

```c
typedef char* String;
#define STRING char*

String a, b;   /* char *a, *b (둘 다 포인터) */
STRING c, d;   /* char *c, d  (c만 포인터, d는 char!) */
```

typedef는 타입 전체를 별명으로 만들어 위 문제가 없다.

### 플랫폼 독립적 타입

```c
/* stdint.h 방식 */
typedef signed char        int8_t;
typedef short              int16_t;
typedef int                int32_t;
typedef long long          int64_t;
typedef unsigned char      uint8_t;
/* ... */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 기본 타입 별명 */
typedef unsigned char Byte;
typedef int Bool;
#define TRUE  1
#define FALSE 0

/* 구조체에 typedef 적용 */
typedef struct {
    double real;
    double imag;
} Complex;

/* 함수 포인터에 typedef 적용 */
typedef double (*MathFunc)(double);

/* 복소수 출력 */
void print_complex(Complex c) {
    if (c.imag >= 0) printf("%.2f + %.2fi\n", c.real, c.imag);
    else             printf("%.2f - %.2fi\n", c.real, -c.imag);
}

/* 복소수 덧셈 */
Complex complex_add(Complex a, Complex b) {
    return (Complex){a.real + b.real, a.imag + b.imag};
}

double square(double x) { return x * x; }
double cube(double x)   { return x * x * x; }

int main() {
    /* 기본 typedef 사용 */
    Byte flags = 0xFF;
    printf("flags = 0x%X (%d)\n", flags, flags);

    Bool is_valid = TRUE;
    printf("유효: %s\n", is_valid ? "예" : "아니오");

    /* 구조체 typedef */
    Complex c1 = {3.0, 4.0};
    Complex c2 = {1.0, -2.0};

    printf("c1 = "); print_complex(c1);
    printf("c2 = "); print_complex(c2);

    Complex c3 = complex_add(c1, c2);
    printf("c1 + c2 = "); print_complex(c3);

    /* 함수 포인터 typedef */
    MathFunc funcs[] = {square, cube};
    const char *names[] = {"square", "cube"};

    double x = 3.0;
    for (int i = 0; i < 2; i++) {
        printf("%s(%.0f) = %.1f\n", names[i], x, funcs[i](x));
    }

    return 0;
}
```

---

## 6. 마지막 정리

`typedef`는 기존 타입에 새 이름을 붙여 사용을 편리하게 한다.

구조체 정의 시 `typedef struct { ... } 이름;` 형태로 `struct` 키워드를 생략할 수 있다.

`#define`과 달리 `typedef`는 진짜 타입이므로 포인터 등 복합 선언 시 예상대로 동작한다.

함수 포인터에 typedef를 적용하면 가독성이 크게 향상된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp typedef",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
