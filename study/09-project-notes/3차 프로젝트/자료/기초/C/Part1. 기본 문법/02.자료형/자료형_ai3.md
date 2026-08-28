# 제목
[C/Cpp 기초] 자료형

# 본문

## 1. 한 줄 요약

자료형은 메모리 레이아웃과 비트 해석 방식을 결정하는 타입 시스템의 기본 단위이며, 연산 결과의 범위와 정밀도를 규정한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

컴퓨터는 모든 데이터를 비트 패턴으로 저장한다. 동일한 비트 패턴도 해석 방식에 따라 전혀 다른 값이 된다.

```c
unsigned char bits = 0x41;
/* 정수로 해석: 65 */
/* 문자로 해석: 'A' */
/* IEEE 754 float의 일부분으로 해석: 완전히 다른 실수값 */
```

자료형은 컴파일러에게 다음을 알려준다.
1. 해당 변수에 몇 바이트를 할당할지
2. 비트 패턴을 어떤 방식으로 해석할지
3. 어떤 연산이 적법한지

---

## 3. 핵심 아이디어

### 정수 표현

C의 정수형은 크기와 부호 여부로 구분된다.

**부호 있는 정수 (2의 보수 표현)**

```text
short (2바이트, 16비트):
MSB = 부호 비트
  0111 1111 1111 1111 = +32767
  1000 0000 0000 0000 = -32768
```

**정수 승격 (integer promotion)**

연산 중 `char`, `short` 등 int보다 작은 타입은 자동으로 `int`로 승격된다.

```c
char a = 100, b = 200;
int result = a + b;  /* a, b가 int로 승격 후 덧셈 */
```

### 부동소수점 표현 (IEEE 754)

`float`(32비트)의 구조:

```text
1비트   8비트        23비트
[부호] [지수부] [가수부(mantissa)]

부호: 0=양수, 1=음수
지수: 실제 지수 + 127 (bias)
가수: 1.xxx...xxx 형태의 분수 부분
```

이 구조로 인해 부동소수점 연산에는 본질적인 정밀도 한계가 있다.

```c
double x = 0.1 + 0.2;
printf("%.17f\n", x);  /* 0.30000000000000004 */
```

---

## 4. 동작 과정 살펴보기

### 타입 크기와 정렬

```c
#include <stdio.h>
#include <stdint.h>

int main() {
    printf("char:      크기=%zu, 정렬=%zu\n",
           sizeof(char), _Alignof(char));
    printf("short:     크기=%zu, 정렬=%zu\n",
           sizeof(short), _Alignof(short));
    printf("int:       크기=%zu, 정렬=%zu\n",
           sizeof(int), _Alignof(int));
    printf("long long: 크기=%zu, 정렬=%zu\n",
           sizeof(long long), _Alignof(long long));
    printf("float:     크기=%zu, 정렬=%zu\n",
           sizeof(float), _Alignof(float));
    printf("double:    크기=%zu, 정렬=%zu\n",
           sizeof(double), _Alignof(double));
    return 0;
}
```

### 정수 오버플로우의 정의된 동작과 미정의 동작

- **부호 없는 정수 오버플로우**: 잘 정의됨 (모듈러 산술)
- **부호 있는 정수 오버플로우**: 정의되지 않은 동작 (undefined behavior)

```c
unsigned int u = UINT_MAX;
u = u + 1;  /* 0이 됨 - 정의된 동작 */

int s = INT_MAX;
s = s + 1;  /* undefined behavior - 컴파일러 최적화에 의해 예측 불가 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <limits.h>   /* 정수 범위 상수 */
#include <float.h>    /* 실수 범위 상수 */
#include <stdint.h>   /* 고정 크기 정수형 */

int main() {
    /* 각 타입의 범위 출력 */
    printf("int 최솟값: %d\n", INT_MIN);
    printf("int 최댓값: %d\n", INT_MAX);
    printf("unsigned int 최댓값: %u\n", UINT_MAX);
    printf("float 최대 정밀도: %d자리\n", FLT_DIG);
    printf("double 최대 정밀도: %d자리\n", DBL_DIG);

    /* 고정 크기 정수형 (이식성) */
    int8_t  a = 127;
    int16_t b = 32767;
    int32_t c = 2147483647;
    int64_t d = 9223372036854775807LL;

    printf("int8_t:  %d\n", a);
    printf("int16_t: %d\n", b);
    printf("int32_t: %d\n", c);
    printf("int64_t: %lld\n", d);

    return 0;
}
```

### 부동소수점 비교 시 주의사항

```c
#include <math.h>

double a = 0.1 + 0.2;
double b = 0.3;

/* 직접 비교는 위험 */
if (a == b) { ... }  /* 거짓일 수 있음 */

/* 엡실론을 이용한 근사 비교 */
#define EPSILON 1e-9
if (fabs(a - b) < EPSILON) { ... }  /* 올바른 방법 */
```

---

## 6. 마지막 정리

C의 자료형은 메모리 할당 크기, 비트 해석 방식, 연산 행동을 결정한다.

정수형은 2의 보수로 표현되며, 부호 있는 오버플로우는 undefined behavior이다.

부동소수점은 IEEE 754 표준을 따르며 본질적인 정밀도 한계가 있다.

이식성을 위해 `<stdint.h>`의 고정 크기 정수형(`int32_t` 등) 사용을 권장한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 자료형",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
