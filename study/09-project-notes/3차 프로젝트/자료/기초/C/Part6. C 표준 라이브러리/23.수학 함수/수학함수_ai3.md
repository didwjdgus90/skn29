# 제목
[C/Cpp 기초] 수학 함수

# 본문

## 1. 한 줄 요약

`<math.h>`의 부동소수점 수학 함수들은 IEEE 754 표준을 기반으로 구현되며, 특수 값(`NaN`, `Inf`)과 도메인 오류를 `errno` 및 반환값으로 전달한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

과학/공학 계산의 정밀도 요구사항을 충족하면서도 부동소수점 오차와 도메인 예외를 올바르게 처리하는 코드 작성이 목적이다.

---

## 3. 핵심 아이디어

### IEEE 754와 특수 값

```c
#include <math.h>

sqrt(-1.0);         /* NaN (Not a Number): 도메인 오류 */
log(0.0);           /* -INFINITY */
1.0 / 0.0;          /* INFINITY */

isinf(INFINITY);    /* 1 */
isnan(sqrt(-1.0));  /* 1 */
isfinite(1.0);      /* 1 */
```

### 오차 처리

```c
#include <errno.h>

errno = 0;
double result = sqrt(-1.0);
if (errno == EDOM) printf("도메인 오류\n");

errno = 0;
result = pow(10.0, 309.0);  /* double overflow */
if (errno == ERANGE) printf("범위 오류\n");
```

### 부동소수점 비교의 함정

```c
double a = 0.1 + 0.2;
a == 0.3;         /* FALSE: 부동소수점 오차 */

fabs(a - 0.3) < 1e-9;  /* TRUE: epsilon 비교 */
```

---

## 4. 동작 과정 살펴보기

### `pow` vs 정수 거듭제곱

```c
pow(2.0, 3.0)  /* 내부: exp(3.0 * log(2.0)) — 부동소수 연산 */
/* 결과: 7.9999... 또는 8.0000... — 오차 가능 */

/* 정수 거듭제곱: 빠르고 정확 */
int ipow(int base, int exp) {
    int result = 1;
    for (int i = 0; i < exp; i++) result *= base;
    return result;
}
/* 큰 지수에는 반복 제곱(fast power) */
```

### 수치 안정성

```c
/* 수치 불안정: 큰 수 빼기 큰 수 → 유효 자릿수 소실 */
double a = 1e15 + 1;
double b = 1e15;
double c = a - b;  /* 이상적으로 1, 실제 1 또는 0 */

/* 보상 합산(Kahan summation)으로 누적 오차 줄이기 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <math.h>
#include <errno.h>
#include <float.h>

/* 안전한 제곱근 */
int safe_sqrt(double x, double *result) {
    if (x < 0) return -1;
    *result = sqrt(x);
    return 0;
}

/* 카한(Kahan) 합산으로 부동소수 오차 최소화 */
double kahan_sum(const double *arr, int n) {
    double sum = 0.0, c = 0.0;
    for (int i = 0; i < n; i++) {
        double y = arr[i] - c;
        double t = sum + y;
        c = (t - sum) - y;
        sum = t;
    }
    return sum;
}

/* 반복 제곱(Fast Power): O(log n) */
long long fast_pow(long long base, int exp) {
    long long result = 1;
    while (exp > 0) {
        if (exp & 1) result *= base;
        base *= base;
        exp >>= 1;
    }
    return result;
}

int main() {
    /* 오차 처리 */
    double r;
    printf("sqrt(25) = %s\n", safe_sqrt(25, &r) == 0 ?
           (printf("%.1f\n", r), "OK") : "도메인 오류");
    if (safe_sqrt(-1, &r) != 0) printf("sqrt(-1): 도메인 오류\n");

    /* 부동소수 비교 */
    double a = 0.1 + 0.2;
    printf("\n0.1+0.2 == 0.3: %s\n", a == 0.3 ? "참" : "거짓");
    printf("epsilon 비교: %s\n", fabs(a - 0.3) < DBL_EPSILON * 10 ? "참" : "거짓");

    /* 카한 합산 */
    double vals[5] = {1e15, 1.0, -1e15, 1.0, 1.0};
    printf("\n단순 합: %.1f\n", vals[0]+vals[1]+vals[2]+vals[3]+vals[4]);
    printf("카한 합: %.1f\n", kahan_sum(vals, 5));

    /* 빠른 거듭제곱 */
    printf("\n2^10 = %lld (fast_pow)\n", fast_pow(2, 10));
    printf("2^32 = %lld\n", fast_pow(2, 32));

    /* 특수 값 */
    printf("\nINFINITY: %f, isinf=%d\n", INFINITY, isinf(INFINITY));
    printf("NaN: %f, isnan=%d\n", NAN, isnan(NAN));

    return 0;
}
```

---

## 6. 마지막 정리

`<math.h>` 함수는 `errno`와 특수 값(`NaN`, `Inf`)으로 예외를 보고한다. 중요한 계산에서는 이를 확인해야 한다.

부동소수점 동등 비교(`==`)는 피하고, `fabs(a - b) < epsilon` 방식을 사용한다.

`pow(2, n)` 대신 `fast_pow`를 사용하면 O(log n)으로 정확한 정수 거듭제곱이 가능하다.

Kahan summation으로 부동소수점 누적 오차를 줄일 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 수학 함수",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 2,
  "example_score": 5,
  "target_level": "high",
  "language": "c"
}
```
