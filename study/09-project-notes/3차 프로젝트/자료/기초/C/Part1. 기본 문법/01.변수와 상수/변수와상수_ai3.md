# 제목
[C/Cpp 기초] 변수와 상수

# 본문

## 1. 한 줄 요약

변수는 특정 자료형의 값을 저장하기 위해 스택 메모리에 할당된 식별자이며, 상수는 `const` 한정자 또는 전처리기 매크로를 통해 재할당이 금지된 값이다.

변수와 상수는 C 프로그램에서 데이터의 의미와 변경 가능성을 명확히 표현하는 기본 단위이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 데이터를 저장하고, 변경하고, 연산하는 방식으로 동작한다.

값을 직접 코드에 기술하는 방식(매직 넘버)은 가독성과 유지보수성이 낮다.

```c
printf("%f\n", 3.14159 * 5.0 * 5.0);
```

이 식에서 `3.14159`, `5.0`이 각각 무엇을 의미하는지 코드만으로는 파악하기 어렵다.

변수와 상수를 통해 값의 의미를 코드에 명시적으로 드러낼 수 있다.

```c
const double PI = 3.14159;
double radius = 5.0;
printf("%f\n", PI * radius * radius);
```

---

## 3. 핵심 아이디어

### 메모리 관점에서의 변수

C에서 변수는 자동 저장 기간(automatic storage duration)을 가진 객체로, 함수 호출 시 스택 프레임에 할당된다.

```text
스택 프레임 (main 함수):
┌──────────────────────┐  높은 주소
│  int count  = 3      │  0x7fff...c
│  int price  = 15000  │  0x7fff...8
└──────────────────────┘  낮은 주소
```

변수 선언은 컴파일러에게 특정 크기의 메모리를 해당 이름으로 접근하겠다고 알리는 것이다.

### const 한정자의 의미

```c
const int MAX = 100;
```

`const`는 해당 변수를 통한 쓰기 접근을 금지한다. 그러나 이것은 언어 수준의 제약이며, 포인터를 이용한 우회가 기술적으로 가능하지만 정의되지 않은 동작(undefined behavior)이다.

```c
const int x = 10;
int *p = (int *)&x;
*p = 20;  /* undefined behavior */
```

### #define과 const의 차이

| 구분 | `const` | `#define` |
|---|---|---|
| 처리 단계 | 컴파일 타임 | 전처리 단계 |
| 타입 안전성 | 있음 | 없음 |
| 디버거 가시성 | 있음 | 없음 |
| 메모리 할당 | 할 수 있음 | 없음 (치환) |
| 스코프 | 블록 스코프 | 파일 전체 |

---

## 4. 동작 과정 살펴보기

### 변수 선언과 메모리 할당

```c
int score = 80;
```

1. 컴파일러는 스택에 `sizeof(int)` (통상 4바이트) 크기의 공간을 예약한다.
2. 프로그램 실행 시 해당 위치에 80이라는 값(비트 패턴)이 기록된다.

```text
주소     값(바이트)
0x100    0x50 0x00 0x00 0x00  → int 80 (리틀 엔디언)
```

### lvalue와 rvalue

대입 연산자의 왼쪽과 오른쪽은 역할이 다르다.

```c
score = score + 10;
```

- 왼쪽 `score` (lvalue): 메모리 위치를 가리킨다. 쓰기 대상.
- 오른쪽 `score` (rvalue): 메모리에서 읽은 값(80). 읽기 대상.

`const` 변수는 lvalue로 사용할 수 없다.

```c
const int MAX = 100;
MAX = 200;  /* 오류: const lvalue에 대한 쓰기 시도 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 파일 스코프 상수: 전처리기 매크로 */
#define BUFFER_SIZE 256

int main() {
    /* 자동 저장 기간 변수 */
    int price = 15000;
    int count = 3;

    /* const 한정 변수: 재할당 금지 */
    const int DELIVERY_FEE = 2500;

    int total_price = price * count;
    int final_price = total_price + DELIVERY_FEE;

    printf("최종 결제 금액: %d원\n", final_price);

    /* 변수의 크기와 주소 확인 */
    printf("price의 크기: %zu바이트\n", sizeof(price));
    printf("price의 주소: %p\n", (void *)&price);

    return 0;
}
```

### sizeof를 통한 자료형 크기 확인

```c
#include <stdio.h>

int main() {
    printf("char:   %zu바이트\n", sizeof(char));
    printf("int:    %zu바이트\n", sizeof(int));
    printf("long:   %zu바이트\n", sizeof(long));
    printf("float:  %zu바이트\n", sizeof(float));
    printf("double: %zu바이트\n", sizeof(double));
    return 0;
}
```

자료형의 크기는 플랫폼(32비트/64비트)과 컴파일러에 따라 달라질 수 있다. 이식성 있는 코드를 작성하려면 `<stdint.h>`의 `int32_t`, `uint64_t` 등 고정 크기 정수형을 사용하는 것이 바람직하다.

### const의 전파 (const correctness)

함수 파라미터에도 `const`를 적용하면, 함수 내부에서 입력 데이터를 수정하지 않음을 명시할 수 있다.

```c
void print_value(const int x) {
    printf("%d\n", x);
    /* x = 10; */  /* 컴파일 오류 */
}
```

---

## 6. 마지막 정리

변수는 스택 메모리에 할당된 이름 있는 저장 공간이며, 자료형이 메모리 크기와 해석 방식을 결정한다.

`const`는 컴파일러 수준의 쓰기 금지로 타입 안전성을 제공한다.

`#define`은 전처리기 수준의 텍스트 치환으로 타입 검사가 없으며, 스코프 제한도 없다.

이식성과 안전성을 위해 `const`와 고정 크기 정수형 사용을 권장한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 변수와 상수",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 4,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
