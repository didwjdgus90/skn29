# 제목
[C/Cpp 기초] 변수와 상수

# 본문

## 1. 한 줄 요약

변수는 값을 저장해두는 이름 있는 메모리 공간이고, 상수는 한 번 정하면 바꿀 수 없는 값이다.

C에서 변수와 상수를 이해하면 숫자, 문자, 실수 등 다양한 데이터를 이름으로 관리하고 더 안전한 코드를 작성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램에서 같은 값을 여러 번 사용해야 하는 경우가 많다.

예를 들어 원의 넓이를 구하는 계산을 한다고 해보자.

```c
printf("%f\n", 3.14159 * 5 * 5);
printf("%f\n", 3.14159 * 10 * 10);
```

이 코드에서 `3.14159`가 무엇인지 바로 알기 어렵고, 값을 바꿔야 할 때 모든 곳을 찾아서 수정해야 한다.

변수와 상수를 사용하면 의미 있는 이름을 붙일 수 있다.

```c
const double PI = 3.14159;
double radius = 5.0;
printf("%f\n", PI * radius * radius);
```

---

## 3. 핵심 아이디어

변수는 값에 붙이는 이름표이다.

```text
값: 10
↓
int age = 10;

int    → 자료형 (정수)
age    → 변수 이름
10     → 저장할 값
```

C에서는 변수를 만들 때 반드시 자료형을 함께 적는다.

상수는 두 가지 방법으로 만든다.

**방법 1: const 키워드**
```c
const int MAX_SIZE = 100;
```
- 타입 정보가 있어 컴파일러가 타입 검사를 할 수 있다.
- 값 변경 시 컴파일 오류 발생.

**방법 2: #define 전처리기 지시문**
```c
#define MAX_SIZE 100
```
- 컴파일 전에 단순 텍스트 치환이 일어난다.
- 타입 정보가 없다.

---

## 4. 동작 과정 살펴보기

아래 코드를 단계별로 보자.

```c
int score = 80;
score = score + 10;
printf("%d\n", score);
```

### Step 1. 변수 선언과 초기화

```text
score
  │
  ▼
 80    (메모리 어딘가에 int 크기(4바이트)의 공간 확보)
```

`int score = 80;`은 정수 값을 담을 수 있는 `score`라는 변수를 만들고 80을 저장한다.

### Step 2. 오른쪽 계산 먼저 수행

```text
score = score + 10

오른쪽 score의 현재 값: 80
80 + 10 = 90
```

대입문에서는 오른쪽이 먼저 계산된다.

### Step 3. 결과를 다시 저장

```text
변경 전: score → 80
변경 후: score → 90
```

계산 결과 90이 다시 `score`에 저장된다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 변수 선언 및 초기화 */
    int price = 15000;
    int count = 3;

    /* const를 이용한 상수 선언 */
    const int DELIVERY_FEE = 2500;

    /* 계산 */
    int total_price = price * count;
    int final_price = total_price + DELIVERY_FEE;

    /* 출력 */
    printf("상품 가격: %d원\n", price);
    printf("구매 개수: %d개\n", count);
    printf("총 상품 금액: %d원\n", total_price);
    printf("배송비: %d원\n", DELIVERY_FEE);
    printf("최종 결제 금액: %d원\n", final_price);

    return 0;
}
```

### 코드 설명

```c
int price = 15000;
```

정수형 변수 `price`를 선언하고 상품 가격 15000을 저장한다. C에서는 반드시 자료형(`int`)을 앞에 적어야 한다.

```c
const int DELIVERY_FEE = 2500;
```

`const`가 붙었으므로 이 값은 이후 변경할 수 없다. 상수 이름은 관례적으로 대문자와 밑줄로 작성한다.

만약 아래처럼 값을 바꾸려 하면 컴파일 오류가 발생한다.

```c
DELIVERY_FEE = 3000;  /* 오류! const 변수는 변경 불가 */
```

### #define을 이용한 상수 선언

```c
#include <stdio.h>

#define MAX_STUDENTS 30
#define PI 3.14159

int main() {
    printf("최대 학생 수: %d\n", MAX_STUDENTS);
    printf("원주율: %f\n", PI);
    return 0;
}
```

`#define`은 컴파일 전 단순 텍스트 치환으로 처리된다. `MAX_STUDENTS`라고 쓴 곳이 모두 `30`으로 바뀐다.

### 변수 선언 위치 (C89/C90 규칙)

C89/C90 표준에서는 변수를 블록의 맨 앞에서 선언해야 한다.

```c
int main() {
    int a;      /* 선언은 블록 시작 부분에 */
    int b;

    a = 10;     /* 이후에 값 대입 */
    b = 20;
    printf("%d\n", a + b);
    return 0;
}
```

C99 이후부터는 코드 중간에 변수를 선언할 수 있다.

---

## 6. 마지막 정리

변수는 값을 저장하고 다시 사용하기 위한 이름 있는 공간이다.

C에서는 변수를 만들 때 자료형을 반드시 앞에 적는다.

상수는 `const` 키워드 또는 `#define`을 사용해 만든다.

- `const`는 타입 정보가 있어 더 안전하다.
- `#define`은 단순 텍스트 치환이며 타입 검사가 없다.

상수 이름은 보통 대문자와 밑줄로 작성하는 것이 관례이다.

의미 있는 변수 이름을 사용하면 코드가 훨씬 읽기 쉬워진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 변수와 상수",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
