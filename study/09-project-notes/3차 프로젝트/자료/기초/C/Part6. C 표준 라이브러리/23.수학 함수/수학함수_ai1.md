# 제목
[C/Cpp 기초] 수학 함수

# 본문

## 1. 한 줄 요약

`<math.h>`는 제곱근, 거듭제곱, 삼각함수, 로그 등 수학 함수를 제공한다. 컴파일 시 `-lm` 링킹이 필요하다(Linux).

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

수학적 계산을 직접 구현하지 않고 검증된 라이브러리 함수를 사용한다.

```c
/* 직접 구현 (복잡, 오차 가능) */
double sqrt_manual(double n) { /* ... */ }

/* math.h 사용 */
#include <math.h>
double result = sqrt(25.0);  /* 5.0 */
```

---

## 3. 핵심 아이디어

### 주요 함수들

```c
#include <math.h>

/* 거듭제곱과 제곱근 */
pow(2.0, 10.0);   /* 2^10 = 1024.0 */
sqrt(16.0);       /* 4.0 */
cbrt(27.0);       /* 세제곱근: 3.0 */

/* 절댓값 */
fabs(-3.14);      /* 3.14 (float용: fabsf) */
abs(-5);          /* 5 (정수: stdlib.h) */

/* 올림/내림/반올림 */
ceil(3.2);        /* 4.0 */
floor(3.9);       /* 3.0 */
round(3.5);       /* 4.0 */

/* 삼각함수 (라디안 단위) */
sin(M_PI / 2);    /* 1.0 */
cos(0.0);         /* 1.0 */
tan(M_PI / 4);    /* 1.0 */

/* 로그 */
log(M_E);         /* 1.0 (자연로그) */
log10(100.0);     /* 2.0 (상용로그) */
log2(8.0);        /* 3.0 */

/* 최솟값/최댓값 */
fmin(3.0, 5.0);   /* 3.0 */
fmax(3.0, 5.0);   /* 5.0 */
```

### 상수

```c
M_PI    /* 3.14159... */
M_E     /* 2.71828... */
```

---

## 4. 동작 과정 살펴보기

### 도(degree)와 라디안(radian) 변환

```text
삼각함수는 라디안 단위를 사용한다.

도 → 라디안: rad = deg * M_PI / 180
라디안 → 도: deg = rad * 180 / M_PI

sin(90°) = sin(M_PI / 2) = 1.0
cos(180°) = cos(M_PI) = -1.0
```

### pow vs 직접 곱셈

```c
pow(2.0, 3.0)  /* 부동소수 연산, 약간의 오차 가능 */
2 * 2 * 2      /* 정수 연산, 정확 */
/* 정수 거듭제곱이면 직접 곱셈이 빠르고 정확 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <math.h>

/* 도 → 라디안 */
double deg_to_rad(double deg) {
    return deg * M_PI / 180.0;
}

/* 두 점 사이의 거리 */
double distance(double x1, double y1, double x2, double y2) {
    double dx = x2 - x1;
    double dy = y2 - y1;
    return sqrt(dx * dx + dy * dy);
}

int main() {
    /* 기본 수학 함수 */
    printf("sqrt(2) = %.6f\n", sqrt(2.0));
    printf("pow(2, 10) = %.0f\n", pow(2.0, 10.0));
    printf("fabs(-3.7) = %.1f\n", fabs(-3.7));

    /* 올림/내림/반올림 */
    double val = 3.5;
    printf("\nceil(%.1f)  = %.1f\n", val, ceil(val));
    printf("floor(%.1f) = %.1f\n", val, floor(val));
    printf("round(%.1f) = %.1f\n", val, round(val));

    /* 삼각함수 */
    printf("\n삼각함수:\n");
    double angles[] = {0, 30, 45, 60, 90};
    for (int i = 0; i < 5; i++) {
        double rad = deg_to_rad(angles[i]);
        printf("sin(%3.0f°) = %6.3f, cos(%3.0f°) = %6.3f\n",
               angles[i], sin(rad), angles[i], cos(rad));
    }

    /* 두 점 거리 */
    printf("\n두 점 거리:\n");
    printf("(0,0)~(3,4) = %.2f\n", distance(0, 0, 3, 4));
    printf("(1,2)~(4,6) = %.2f\n", distance(1, 2, 4, 6));

    /* 로그 */
    printf("\n로그:\n");
    printf("log(%.4f) = %.1f\n", M_E, log(M_E));
    printf("log10(1000) = %.1f\n", log10(1000.0));
    printf("log2(32) = %.1f\n", log2(32.0));

    return 0;
}
```

> 컴파일: `gcc -o prog prog.c -lm` (Linux에서 -lm 필요)

---

## 6. 마지막 정리

`<math.h>`는 제곱근, 삼각함수, 로그, 올림/내림 등 다양한 수학 함수를 제공한다.

삼각함수는 라디안 단위를 사용한다. 도(degree)를 라디안으로 변환 후 사용한다.

Linux에서는 컴파일 시 `-lm` 옵션으로 수학 라이브러리를 링킹해야 한다.

정수의 거듭제곱은 `pow` 대신 직접 곱셈이 더 정확하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 수학 함수",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
