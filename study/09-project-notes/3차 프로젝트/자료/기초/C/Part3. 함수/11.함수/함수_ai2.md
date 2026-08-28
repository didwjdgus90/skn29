# 제목
[C/Cpp 기초] 함수

# 본문

## 1. 한 줄 요약

함수는 레시피이다. 한 번 만들어두면 필요할 때마다 꺼내 쓸 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

김치찌개 레시피를 생각해보자.

레시피 없이 매번 처음부터 만들면 시간도 걸리고, 매번 결과가 달라질 수 있다.

레시피(함수)를 만들어두면 누구든 언제든 같은 결과를 얻을 수 있다.

```text
레시피 이름: 김치찌개
재료 (매개변수): 김치, 돼지고기, 두부
만드는 법 (함수 본문): ...
결과물 (반환값): 완성된 김치찌개
```

---

## 3. 핵심 아이디어

### 함수 = 재사용 가능한 레시피

```c
/* 레시피 만들기 (함수 정의) */
int add(int a, int b) {
    return a + b;
}

/* 레시피 사용하기 (함수 호출) */
int result1 = add(3, 4);   /* 7 */
int result2 = add(10, 20); /* 30 */
```

같은 레시피를 재료(인수)만 바꿔서 여러 번 쓸 수 있다.

### 함수의 4가지 구성 요소

```text
int add (int a, int b) {
 ↑        ↑    ↑
결과물    재료1  재료2
타입      (매개변수)

    return a + b;
    ↑
  완성된 결과물 반환
}
```

### void 함수 - 결과물 없는 작업

```text
출력처럼 "하기만 하고 결과물을 주지 않는" 경우:
void say_hello() {
    printf("안녕하세요!\n");
}
```

---

## 4. 동작 과정 살펴보기

### 레시피 실행 과정

```text
주방(main)에서 요청:
"사각형 넓이 계산해줘! 가로=5, 세로=3"
    ↓
레시피(rectangle_area) 실행:
  width = 5, height = 3
  계산: 5 * 3 = 15
  완성된 넓이 반환: 15
    ↓
주방으로 돌아옴:
area = 15
```

### 재료는 복사본! (값 전달)

레시피에 재료를 줄 때 원본이 아닌 복사본을 준다.

```text
재료통: n = 5 (원본)

함수 호출: double_it(n)
          n의 복사본 → x = 5
          x = x * 2 → x = 10 (복사본 변경)
          함수 종료

원본 n = 5 (그대로!)
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 계산기 함수들 (레시피 모음) */
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }
int multiply(int a, int b) { return a * b; }
double divide(double a, double b) { return a / b; }

/* 출력 전용 함수 (결과물 없음) */
void print_line(int length) {
    for (int i = 0; i < length; i++) printf("-");
    printf("\n");
}

/* 반복 줄이기 */
void print_result(char *op, int a, int b, int result) {
    printf("%d %s %d = %d\n", a, op, b, result);
}

int main() {
    int x = 15, y = 4;

    print_line(20);
    printf("계산기\n");
    print_line(20);

    print_result("+", x, y, add(x, y));
    print_result("-", x, y, subtract(x, y));
    print_result("*", x, y, multiply(x, y));
    printf("%d / %d = %.2f\n", x, y, divide(x, y));

    print_line(20);

    return 0;
}
```

### 함수 선언 - 레시피 목차

```text
요리책 앞부분에 목차가 있듯이,
코드 앞부분에 함수 목록(선언)을 쓸 수 있다.

int add(int a, int b);  ← 목차(선언): 세미콜론으로 끝
```

이렇게 하면 레시피(정의)가 나중에 나와도 먼저 사용할 수 있다.

---

## 6. 마지막 정리

함수는 한 번 만들어두고 여러 번 쓰는 레시피이다.

입력(매개변수)을 받아서 처리하고 결과(반환값)를 돌려준다.

반환값이 없으면 `void` 레시피이다.

재료(인수)는 복사본이 전달되므로 원본 변수는 변하지 않는다.

함수를 잘 나누면 코드가 읽기 쉽고 수정하기 쉬워진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 함수",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
