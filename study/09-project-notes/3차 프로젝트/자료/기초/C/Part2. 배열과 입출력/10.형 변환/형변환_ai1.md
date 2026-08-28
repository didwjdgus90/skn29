# 제목
[C/Cpp 기초] 형 변환

# 본문

## 1. 한 줄 요약

형 변환은 한 자료형의 값을 다른 자료형으로 바꾸는 것이다. 자동으로 일어나는 묵시적 변환과 명시적으로 지정하는 캐스팅이 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

정수끼리 나누면 소수점이 버려진다.

```c
int a = 7, b = 2;
printf("%d\n", a / b);  /* 3 (소수점 버림) */
```

실수 결과를 얻으려면 형 변환이 필요하다.

```c
printf("%f\n", (double)a / b);  /* 3.500000 */
```

또한 서로 다른 자료형끼리 연산할 때 형 변환이 자동으로 일어난다.

---

## 3. 핵심 아이디어

### 묵시적 형 변환 (자동 변환)

연산에서 자동으로 더 큰 자료형으로 변환된다.

```c
int i = 10;
double d = 3.14;
double result = i + d;  /* i가 자동으로 double로 변환 → 13.14 */
```

```text
변환 우선순위 (낮음 → 높음):
char → short → int → long → float → double
```

### 명시적 형 변환 (캐스팅)

```c
(변환할자료형) 값
```

```c
int a = 7, b = 2;
double result = (double)a / b;  /* a를 double로 변환 후 나눗셈 */
```

---

## 4. 동작 과정 살펴보기

### 정수 → 실수: 정밀도 향상

```c
int x = 5;
double d = (double)x;  /* 5 → 5.000000 */
```

### 실수 → 정수: 소수점 버림 (반올림이 아님!)

```c
double d = 3.9;
int i = (int)d;    /* 3 (버림, 반올림 아님!) */
int j = (int)-3.9; /* -3 (0 방향으로 버림) */
```

### 큰 타입 → 작은 타입: 데이터 손실 위험

```c
int big = 300;
char small = (char)big;  /* 300은 char 범위 초과 → 데이터 손실! */
printf("%d\n", small);   /* 44 (300 % 256 = 44) */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 정수 나눗셈 vs 실수 나눗셈 */
    int a = 7, b = 3;
    printf("정수 나눗셈: %d\n", a / b);               /* 2 */
    printf("실수 나눗셈: %.4f\n", (double)a / b);     /* 2.3333 */

    /* 평균 계산 (정수들의 평균을 실수로) */
    int scores[] = {85, 92, 78, 90, 88};
    int n = 5;
    int sum = 0;
    for (int i = 0; i < n; i++) sum += scores[i];

    double avg = (double)sum / n;  /* 형 변환 필수! */
    printf("평균: %.2f\n", avg);

    /* 실수 → 정수 변환 */
    double price = 99.99;
    int int_price = (int)price;
    printf("정가: %.2f, 정수 변환: %d\n", price, int_price);

    /* 문자 ↔ 정수 변환 */
    char ch = 'A';
    int code = (int)ch;    /* 문자를 ASCII 코드로 */
    printf("'A'의 ASCII: %d\n", code);  /* 65 */

    char from_code = (char)(code + 1);
    printf("66 → 문자: %c\n", from_code);  /* 'B' */

    /* 묵시적 변환 예시 */
    int i = 5;
    double d = 2.5;
    double result = i * d;  /* i가 자동으로 double로 변환 */
    printf("5 * 2.5 = %.1f\n", result);  /* 12.5 */

    return 0;
}
```

### 형 변환 시 주의사항

```c
/* 주의 1: 캐스팅 위치 */
int a = 7, b = 2;
double wrong = (double)(a / b);  /* 3.000000 (나눗셈 후 변환) */
double right = (double)a / b;    /* 3.500000 (변환 후 나눗셈) */

/* 주의 2: 실수 → 정수는 버림 */
double d = 3.99;
int n = (int)d;  /* 3 (반올림 아님!) */

/* 반올림 방법 */
#include <math.h>
int rounded = (int)round(d);  /* 4 */
```

---

## 6. 마지막 정리

묵시적 변환은 자동으로 일어나며, 작은 타입이 큰 타입으로 변환된다.

명시적 캐스팅은 `(타입)값` 형태로 직접 지정한다.

실수 → 정수 변환은 반올림이 아닌 버림(truncation)이다.

큰 타입 → 작은 타입 변환 시 데이터 손실이 발생할 수 있다.

정수 나눗셈에서 실수 결과를 얻으려면 피연산자 중 하나를 먼저 캐스팅해야 한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 형 변환",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
