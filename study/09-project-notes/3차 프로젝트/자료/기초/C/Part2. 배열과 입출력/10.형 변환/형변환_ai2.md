# 제목
[C/Cpp 기초] 형 변환

# 본문

## 1. 한 줄 요약

형 변환은 단위 변환과 같다. 킬로그램을 그램으로, 킬로미터를 미터로 바꾸듯 데이터의 형식을 바꾼다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

요리 레시피에서 "밀가루 2컵"을 그램으로 바꾸려면 단위 변환이 필요하다.

프로그래밍에서도 `int`(정수)와 `double`(실수)처럼 서로 다른 형식의 데이터를 함께 사용할 때 변환이 필요하다.

```text
5 / 2 = 2        (정수 ÷ 정수 = 정수, 소수점 버림)
5.0 / 2 = 2.5    (실수 ÷ 정수 = 실수)
```

5를 5.0으로 바꾸는 것이 형 변환이다.

---

## 3. 핵심 아이디어

### 자동 변환 = 자동 단위 업그레이드

작은 그릇의 내용물을 큰 그릇으로 옮길 때는 자연스럽게 맞춰진다.

```text
int(작은 그릇) + double(큰 그릇)
  → int가 자동으로 double로 업그레이드
  → 두 개 다 double이 되어서 계산
```

```c
int i = 5;
double d = 2.5;
double result = i + d;  /* i가 자동으로 5.0으로 변환 */
/* result = 7.5 */
```

### 명시적 변환 = 직접 변환 명령

큰 그릇에서 작은 그릇으로 옮길 때는 "넘칠 수 있지만 넣어라"고 직접 명령해야 한다.

```c
double d = 3.9;
int i = (int)d;  /* "강제로 정수로 바꿔!" */
/* i = 3 (소수점 이하 버림) */
```

`(int)`처럼 괄호에 타입을 쓰는 것이 명령이다.

---

## 4. 동작 과정 살펴보기

### 변환 방향에 따른 결과

```text
작은 그릇 → 큰 그릇 (안전):
  int 5 → double 5.0    (정보 손실 없음)
  char 'A' → int 65     (ASCII 코드로 자연스럽게)

큰 그릇 → 작은 그릇 (주의!):
  double 3.9 → int 3    (소수점 버림)
  int 300 → char ?      (char는 -128~127 → 넘침!)
```

### 반올림이 아닌 버림!

```text
double 3.1 → int 3    (버림)
double 3.9 → int 3    (버림, 반올림 아님!)
double -3.7 → int -3  (0 방향으로 버림)
```

수학에서의 내림/올림과 다르다. 소수점 이하가 그냥 잘린다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <math.h>

int main() {
    /* 정수 나눗셈 문제 */
    int total_score = 433;
    int count = 5;

    /* 잘못된 방법: 정수 나눗셈 */
    double wrong_avg = total_score / count;
    printf("잘못된 평균: %.1f\n", wrong_avg);  /* 86.0 */

    /* 올바른 방법: 형 변환 후 나눗셈 */
    double right_avg = (double)total_score / count;
    printf("올바른 평균: %.1f\n", right_avg);  /* 86.6 */

    /* 문자 ↔ 숫자 변환 */
    char letter = 'A';
    printf("'A'는 숫자로 %d\n", (int)letter);  /* 65 */
    printf("65는 문자로 %c\n", (char)65);       /* A */

    /* 알파벳 순서 활용 */
    char grade = 'B';
    printf("B는 A에서 %d번째\n", grade - 'A' + 1);  /* 2 */

    /* 반올림 방법 */
    double d = 3.7;
    printf("버림: %d\n", (int)d);          /* 3 */
    printf("반올림: %d\n", (int)round(d)); /* 4 */

    return 0;
}
```

### 형 변환 실수 예시

```text
함정 1: 나누기 전에 변환해야 함
  (double)(7 / 2) = (double)3 = 3.0   ← 잘못!
  (double)7 / 2   = 7.0 / 2 = 3.5    ← 올바름

함정 2: 넘치는 변환
  int 300을 char로 변환하면?
  char 범위는 -128~127
  300 - 256 = 44 → char는 44 (예상치 못한 값!)
```

---

## 6. 마지막 정리

형 변환은 데이터의 단위를 바꾸는 것이다.

자동 변환은 작은 타입 → 큰 타입으로 자연스럽게 일어난다.

명시적 변환(캐스팅)은 `(타입)값`으로 직접 지정한다.

실수 → 정수 변환은 반올림이 아닌 버림이다.

나눗셈에서 실수 결과를 원하면 나누기 전에 변환해야 한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 형 변환",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
