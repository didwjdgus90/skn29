# 제목
[C/Cpp 기초] 조건문

# 본문

## 1. 한 줄 요약

조건문은 제어 흐름 분기 구조로, 런타임에 평가된 조건 표현식의 진리값에 따라 실행 경로를 선택한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

순차 실행만으로는 다양한 입력에 대해 다른 처리를 할 수 없다.

조건문은 제어 흐름 그래프(Control Flow Graph)에서 분기점을 형성하며, 조건의 진리값(C에서는 0이 false, 비-0이 true)에 따라 서로 다른 기본 블록(basic block)으로 흐름을 전달한다.

---

## 3. 핵심 아이디어

### if 문의 의미론

```c
if (expr) statement1 else statement2
```

`expr`이 0으로 평가되면 `statement2`, 0이 아니면 `statement1`을 실행한다.

C에는 별도의 `bool` 타입이 없으며(C99 이후 `_Bool`과 `<stdbool.h>`가 추가됨), 정수 0이 false를 대리한다.

```c
int p = NULL;
if (p) { ... }        /* NULL == 0 → false */

double x = 0.0;
if (x) { ... }        /* 0.0 == 0 → false */

int arr[5];
if (arr) { ... }      /* 배열 이름은 포인터로 decay → 비-0 → true */
```

### switch 문의 구현 메커니즘

컴파일러는 switch 문을 두 가지 방식으로 최적화한다.

1. **Jump table**: case 값이 연속적이면 포인터 배열로 O(1) 분기
2. **Binary search**: case 값이 산발적이면 비교 트리 생성

```text
case 1, 2, 3, 4, 5 → jump table (base + offset)
case 1, 100, 500, 1000 → binary search or if-else chain
```

### 단락 평가와 조건문

```c
if (ptr != NULL && ptr->value > 0) { ... }
```

`&&`의 단락 평가로 `ptr`이 NULL이면 `ptr->value` 역참조가 일어나지 않는다. 이는 관용적 null 체크 패턴이다.

---

## 4. 동작 과정 살펴보기

### 분기 예측 (Branch Prediction)

현대 CPU는 파이프라인에서 조건 분기 전에 결과를 예측한다. 예측이 틀리면 파이프라인 플러시(stall)가 발생한다.

```c
/* 예측하기 어려운 분기 (랜덤 데이터) */
for (int i = 0; i < N; i++) {
    if (data[i] > 128) sum += data[i];
}

/* 정렬 후 처리하면 분기 예측 성공률 향상 */
sort(data, N);
for (int i = 0; i < N; i++) {
    if (data[i] > 128) sum += data[i];
}
```

GCC의 `__builtin_expect`로 힌트를 줄 수 있다.

```c
if (__builtin_expect(error_condition, 0)) {
    handle_error();  /* 드물게 발생 */
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdbool.h>   /* C99: bool, true, false */

int main() {
    /* C99 bool 타입 사용 */
    bool is_valid = true;
    int value = 42;

    if (is_valid && value > 0) {
        printf("유효한 양수: %d\n", value);
    }

    /* switch 최적화 사례: 연속 case → jump table */
    int opcode = 2;
    switch (opcode) {
        case 0: printf("NOP\n");   break;
        case 1: printf("ADD\n");   break;
        case 2: printf("SUB\n");   break;
        case 3: printf("MUL\n");   break;
        case 4: printf("DIV\n");   break;
        default: printf("UNKNOWN\n"); break;
    }

    /* 삼항 연산자: 조건부 표현식 (문이 아닌 식) */
    int x = 10, y = 20;
    int max = (x > y) ? x : y;
    printf("최댓값: %d\n", max);

    /* 포인터와 조건문 */
    int arr[] = {1, 2, 3};
    int *ptr = arr;
    if (ptr && *ptr > 0) {
        printf("첫 원소: %d\n", *ptr);
    }

    return 0;
}
```

### Dangling else 문제

```c
if (a > 0)
    if (b > 0)
        printf("둘 다 양수\n");
else
    printf("어디에 속하는가?\n");  /* b <= 0일 때 실행 (가장 가까운 if에 결합) */
```

C에서 `else`는 가장 가까운 `if`에 결합된다. 명확성을 위해 항상 중괄호를 사용하는 것을 권장한다.

---

## 6. 마지막 정리

C의 조건문은 0/비-0 진리값 기반으로 동작한다.

`switch`는 컴파일러가 jump table 또는 비교 트리로 최적화한다. `break` 누락 시 fall-through가 발생한다.

분기 예측이 중요한 성능 임계 코드에서는 `__builtin_expect` 또는 데이터 정렬로 CPU 최적화를 도울 수 있다.

`dangling else`를 피하려면 중괄호를 명시적으로 사용해야 한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 조건문",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
