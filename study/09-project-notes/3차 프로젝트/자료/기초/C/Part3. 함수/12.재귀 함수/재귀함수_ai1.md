# 제목
[C/Cpp 기초] 재귀 함수

# 본문

## 1. 한 줄 요약

재귀 함수는 자기 자신을 호출하는 함수이다. 반드시 종료 조건(기저 조건)이 있어야 무한 반복을 막을 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

5의 팩토리얼을 계산한다고 하자.

5! = 5 × 4 × 3 × 2 × 1

이것을 반복문으로도 풀 수 있지만, 팩토리얼의 수학적 정의 자체가 재귀적이다.

```text
5! = 5 × 4!
4! = 4 × 3!
3! = 3 × 2!
2! = 2 × 1!
1! = 1  (여기서 멈춤)
```

재귀 함수로 이 구조를 코드로 그대로 표현할 수 있다.

---

## 3. 핵심 아이디어

### 재귀 함수의 두 가지 요소

1. **기저 조건(Base Case)**: 재귀를 멈추는 조건
2. **재귀 조건(Recursive Case)**: 자기 자신을 다시 호출

```c
int factorial(int n) {
    if (n <= 1) return 1;        /* 기저 조건 */
    return n * factorial(n - 1); /* 재귀 조건 */
}
```

기저 조건 없으면 → 무한 재귀 → 스택 오버플로우 → 프로그램 강제 종료!

### 피보나치 수열

```c
int fibonacci(int n) {
    if (n <= 1) return n;   /* 기저 조건: fib(0)=0, fib(1)=1 */
    return fibonacci(n-1) + fibonacci(n-2);  /* 재귀 */
}
```

---

## 4. 동작 과정 살펴보기

### factorial(4) 호출 추적

```text
factorial(4)
  → 4 * factorial(3)
        → 3 * factorial(2)
              → 2 * factorial(1)
                    → return 1  (기저 조건 도달!)

이제 역방향으로 계산:
  2 * 1 = 2
  3 * 2 = 6
  4 * 6 = 24

factorial(4) = 24
```

### 스택 프레임 쌓이는 모습

```text
[factorial(4)] ← 제일 마지막에 쌓임
[factorial(3)]
[factorial(2)]
[factorial(1)] ← 제일 먼저 실행 완료
[main]         ← 맨 아래
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 팩토리얼 */
long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

/* 피보나치 수열 */
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n - 1) + fibonacci(n - 2);
}

/* 거듭제곱 */
double power(double base, int exp) {
    if (exp == 0) return 1.0;  /* 기저 조건: x^0 = 1 */
    if (exp < 0) return 1.0 / power(base, -exp);
    return base * power(base, exp - 1);
}

/* 배열 합계 (재귀) */
int sum_array(int arr[], int n) {
    if (n == 0) return 0;  /* 기저 조건 */
    return arr[n - 1] + sum_array(arr, n - 1);
}

int main() {
    /* 팩토리얼 */
    for (int i = 0; i <= 10; i++) {
        printf("%d! = %lld\n", i, factorial(i));
    }

    /* 피보나치 */
    printf("\n피보나치 수열:\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", fibonacci(i));
    }
    printf("\n");

    /* 거듭제곱 */
    printf("\n2^10 = %.0f\n", power(2.0, 10));
    printf("3^3  = %.0f\n", power(3.0, 3));

    /* 배열 합계 */
    int arr[] = {1, 2, 3, 4, 5};
    printf("\n배열 합계: %d\n", sum_array(arr, 5));

    return 0;
}
```

### 재귀 vs 반복문

```c
/* 팩토리얼을 반복문으로 */
long long factorial_loop(int n) {
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}
```

재귀가 더 읽기 쉽지만, 큰 n에서는 반복문이 더 효율적이다.

---

## 6. 마지막 정리

재귀 함수는 자기 자신을 호출하는 함수이다.

반드시 기저 조건(종료 조건)이 있어야 한다.

함수 호출마다 스택에 쌓이므로, 너무 깊이 재귀하면 스택 오버플로우가 발생한다.

재귀는 트리, 그래프 탐색 등 분할 정복 문제에 자주 사용된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 재귀 함수",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
