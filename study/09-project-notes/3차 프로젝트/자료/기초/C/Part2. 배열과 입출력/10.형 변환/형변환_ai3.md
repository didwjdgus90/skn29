# 제목
[C/Cpp 기초] 형 변환

# 본문

## 1. 한 줄 요약

C의 형 변환은 묵시적 변환(implicit conversion, 컴파일러 주도)과 명시적 캐스팅(explicit cast, 프로그래머 주도)으로 분류되며, 정수 승격 규칙과 일반 산술 변환 규칙에 따라 결정된다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

C의 타입 시스템은 표현 범위와 정밀도가 다른 여러 자료형을 정의한다.

이기종 타입 간 연산이나 대입에서 비트 패턴의 재해석 또는 변환이 필요하다.

이 과정이 잘못 이해되면 정밀도 손실, 부호 오류, 정의되지 않은 동작 등의 버그가 발생한다.

---

## 3. 핵심 아이디어

### 정수 승격 (Integer Promotion)

`char`, `short`, `int`보다 작은 타입은 이항 연산에서 `int`로 자동 승격된다.

```c
char a = 250;   /* unsigned: 250, signed: -6 */
char b = 10;
int result = a + b;
/* a, b 모두 int로 승격 후 덧셈 */
/* signed char: (-6) + 10 = 4 */
/* unsigned char: 250 + 10 = 260 */
```

### 일반 산술 변환 (Usual Arithmetic Conversions)

이항 연산자에서 두 피연산자의 타입을 동일하게 맞추는 규칙.

```text
우선순위 (낮음 → 높음 방향으로 변환):
int → unsigned int → long → unsigned long → long long → unsigned long long → float → double → long double
```

하나가 `double`이면 다른 하나도 `double`로 변환된다.

### 명시적 캐스팅

```c
(type) expression
```

컴파일러 경고를 억제하고 프로그래머의 의도를 명시한다. 그러나 UB를 일으킬 수도 있다.

---

## 4. 동작 과정 살펴보기

### 부호 있는/없는 혼용 주의

```c
int i = -1;
unsigned int u = 1;
if (i < u) {
    /* 이 블록은 실행되지 않을 수 있다! */
    /* i가 unsigned로 변환: -1 → 4294967295 (UINT_MAX) */
    /* 4294967295 < 1은 거짓 */
}
```

부호 있는 정수와 부호 없는 정수의 혼용은 예상치 못한 비교 결과를 낳는다.

### 실수 → 정수: 절단(Truncation)

```c
double d = 3.9;
int i = (int)d;   /* 3: 0 방향으로 절단 */
int j = (int)-3.9; /* -3: 0 방향으로 절단 */
```

`floor(-3.9) = -4`이지만 `(int)(-3.9) = -3`이다. 둘은 다르다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdint.h>

int main() {
    /* 부호 있는/없는 혼용 위험성 */
    int si = -1;
    unsigned int ui = 0;
    printf("si > ui: %d\n", si > ui);  /* 1 (예상과 반대!) */
    /* -1이 unsigned로 변환되어 UINT_MAX가 됨 */

    /* 정수 나눗셈과 형 변환 */
    int a = 7, b = 2;
    printf("7/2     = %d\n", a / b);              /* 3 */
    printf("7.0/2   = %.1f\n", (double)a / b);    /* 3.5 */
    printf("(d)(7/2)= %.1f\n", (double)(a / b));  /* 3.0 (너무 늦음) */

    /* 고정 크기 타입으로 안전한 변환 */
    int32_t x = 200;
    int8_t  y = (int8_t)x;  /* 200은 int8_t 범위(-128~127) 초과: 구현 정의 동작 */
    printf("int32 %d → int8 %d\n", x, y);

    uint8_t u = 255;
    uint16_t v = u;  /* 안전: 묵시적 확장 */
    printf("uint8 %u → uint16 %u\n", u, v);

    /* 실수 정밀도 손실 */
    double d = 1234567.89;
    float  f = (float)d;   /* float는 7자리 정밀도 */
    printf("double: %.2f\n", d);  /* 1234567.89 */
    printf("float:  %.2f\n", f);  /* 1234567.88 (정밀도 손실) */

    return 0;
}
```

### `void *` 캐스팅

```c
void *ptr = malloc(10 * sizeof(int));
int *arr = (int *)ptr;  /* C에서는 불필요하나 관례적으로 사용 */
/* C++에서는 필수 */
```

---

## 6. 마지막 정리

정수 승격으로 `char`/`short`는 이항 연산 시 `int`로 자동 변환된다.

일반 산술 변환에서 부호 있는/없는 혼용은 직관에 반하는 결과를 낳으므로 주의한다.

실수 → 정수 캐스팅은 `floor`가 아닌 0 방향 절단(truncation)이다.

큰 타입 → 작은 타입 캐스팅에서 범위 초과는 구현 정의 또는 UB이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 형 변환",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
