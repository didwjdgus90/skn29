# 제목
[C/Cpp 기초] 연산자

# 본문

## 1. 한 줄 요약

연산자는 값을 계산하거나 비교하거나 조작하는 데 사용하는 기호이다.

C에서 연산자를 이해하면 산술 계산, 조건 비교, 비트 조작 등 다양한 연산을 수행할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램에서는 값을 계산하고 조건을 확인해야 하는 상황이 항상 발생한다.

예를 들어 쇼핑몰에서 할인 여부를 판단하고 최종 가격을 계산하려면 다양한 연산이 필요하다.

```c
int price = 10000;
int discount_rate = 20;

int discount = price * discount_rate / 100;  /* 산술 연산자 */
int final_price = price - discount;

if (final_price < 5000) {  /* 비교 연산자 */
    printf("무료 배송 불가\n");
}
```

---

## 3. 핵심 아이디어

### 산술 연산자

```c
int a = 10, b = 3;

printf("%d\n", a + b);   /* 13: 더하기 */
printf("%d\n", a - b);   /* 7:  빼기 */
printf("%d\n", a * b);   /* 30: 곱하기 */
printf("%d\n", a / b);   /* 3:  나누기 (정수 나눗셈, 소수점 버림) */
printf("%d\n", a % b);   /* 1:  나머지 */
```

정수끼리 나누면 소수점이 버려진다. 실수로 나누려면 float/double을 사용한다.

### 비교 연산자

결과는 참(1) 또는 거짓(0)이다.

```c
printf("%d\n", 5 == 5);   /* 1 (같다) */
printf("%d\n", 5 != 3);   /* 1 (다르다) */
printf("%d\n", 5 > 3);    /* 1 (크다) */
printf("%d\n", 5 < 3);    /* 0 (작다) */
printf("%d\n", 5 >= 5);   /* 1 (크거나 같다) */
printf("%d\n", 5 <= 4);   /* 0 (작거나 같다) */
```

### 논리 연산자

```c
int x = 1, y = 0;

printf("%d\n", x && y);   /* 0: AND (둘 다 참이어야 참) */
printf("%d\n", x || y);   /* 1: OR  (하나라도 참이면 참) */
printf("%d\n", !x);        /* 0: NOT (참을 거짓으로) */
```

### 증감 연산자

```c
int n = 5;
n++;   /* n = 6: 1 증가 */
n--;   /* n = 5: 1 감소 */

/* 전위(prefix) vs 후위(postfix) */
int a = 5;
printf("%d\n", ++a);  /* 6: 증가 후 값 사용 */
printf("%d\n", a++);  /* 6: 값 사용 후 증가 (a는 7이 됨) */
```

---

## 4. 동작 과정 살펴보기

### 연산자 우선순위

곱셈과 나눗셈이 덧셈과 뺄셈보다 먼저 계산된다.

```c
int result = 2 + 3 * 4;
/* 3 * 4 = 12, 2 + 12 = 14 */
printf("%d\n", result);  /* 14 */

/* 괄호로 우선순위 변경 */
result = (2 + 3) * 4;
/* 2 + 3 = 5, 5 * 4 = 20 */
printf("%d\n", result);  /* 20 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 산술 연산자 */
    int a = 17, b = 5;
    printf("17 + 5 = %d\n", a + b);
    printf("17 - 5 = %d\n", a - b);
    printf("17 * 5 = %d\n", a * b);
    printf("17 / 5 = %d\n", a / b);    /* 3 (정수 나눗셈) */
    printf("17 %% 5 = %d\n", a % b);   /* 2 (나머지) */

    /* 삼항 연산자 */
    int score = 75;
    char *result = (score >= 60) ? "합격" : "불합격";
    printf("결과: %s\n", result);

    /* 복합 대입 연산자 */
    int x = 10;
    x += 5;   /* x = x + 5 = 15 */
    x -= 3;   /* x = x - 3 = 12 */
    x *= 2;   /* x = x * 2 = 24 */
    x /= 4;   /* x = x / 4 = 6  */
    x %= 4;   /* x = x % 4 = 2  */
    printf("x = %d\n", x);

    /* 비트 연산자 */
    int flags = 0b1010;   /* 2진수 10 */
    int mask  = 0b1100;   /* 2진수 12 */
    printf("AND: %d\n", flags & mask);   /* 1000 = 8 */
    printf("OR:  %d\n", flags | mask);   /* 1110 = 14 */
    printf("XOR: %d\n", flags ^ mask);   /* 0110 = 6 */
    printf("NOT: %d\n", ~flags);          /* 비트 반전 */
    printf("LEFT SHIFT: %d\n", flags << 1);  /* 10100 = 20 */
    printf("RIGHT SHIFT: %d\n", flags >> 1); /* 101 = 5 */

    return 0;
}
```

### 나머지 연산자의 활용

```c
/* 짝수/홀수 판별 */
int n = 7;
if (n % 2 == 0) {
    printf("짝수\n");
} else {
    printf("홀수\n");
}

/* 자릿수 추출 */
int num = 1234;
printf("일의 자리: %d\n", num % 10);    /* 4 */
printf("십의 자리: %d\n", (num / 10) % 10);  /* 3 */
```

---

## 6. 마지막 정리

산술 연산자: `+`, `-`, `*`, `/`, `%`

비교 연산자: `==`, `!=`, `<`, `>`, `<=`, `>=` (결과는 0 또는 1)

논리 연산자: `&&`(AND), `||`(OR), `!`(NOT)

삼항 연산자: `조건 ? 참일때값 : 거짓일때값`

복합 대입: `+=`, `-=`, `*=`, `/=`, `%=`

비트 연산자: `&`, `|`, `^`, `~`, `<<`, `>>`

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 연산자",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
