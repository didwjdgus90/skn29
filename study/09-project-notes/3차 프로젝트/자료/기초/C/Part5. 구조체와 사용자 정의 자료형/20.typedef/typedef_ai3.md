# 제목
[C/Cpp 기초] typedef

# 본문

## 1. 한 줄 요약

`typedef`는 타입 시스템 내에서 기존 타입의 동의어(synonym)를 생성하는 선언이다. `#define`의 텍스트 치환과 달리 타입 시스템에 실제로 등록되어 포인터·함수 포인터 선언 시 의미론적 일관성을 보장한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

`typedef`는 세 가지 목적에서 사용된다.

1. **추상화**: 구현 타입과 인터페이스 타입을 분리 (`size_t`, `ptrdiff_t`)
2. **가독성**: 복잡한 선언 단순화 (함수 포인터)
3. **이식성**: 플랫폼 의존적 타입을 의미 있는 이름으로 감추기 (`int32_t`)

---

## 3. 핵심 아이디어

### 타입 선언의 파싱 규칙

C의 선언 문법에서 `typedef`는 저장 클래스 지정자(storage-class specifier)처럼 동작한다.

```c
typedef int MyInt;
/* int MyInt; 와 문법적으로 동일하나
   MyInt는 변수가 아닌 타입 이름으로 등록됨 */
```

### 복잡한 타입 선언 단순화

함수 포인터 없이:

```c
int (*signal(int sig, int (*func)(int)))(int);
/* POSIX signal() 함수 시그니처 */
```

`typedef`로 분해:

```c
typedef void (*SigHandler)(int);
SigHandler signal(int sig, SigHandler func);
/* 훨씬 읽기 쉬움 */
```

### `typedef`와 `const`의 상호작용

```c
typedef char* CharPtr;
const CharPtr p;        /* char * const p: p 자체가 상수 */
const char *q;          /* const char *q: 가리키는 값이 상수 */
/* CharPtr은 진짜 타입이므로 const가 상위 레벨에 붙음 */
```

---

## 4. 동작 과정 살펴보기

### 불투명 포인터(Opaque Pointer) 패턴

```c
/* 헤더 파일 (공개 인터페이스) */
typedef struct Buffer Buffer;  /* 선언만, 내부 숨김 */
Buffer *buffer_create(size_t size);
void buffer_free(Buffer *buf);

/* 소스 파일 (구현 숨김) */
struct Buffer {
    char *data;
    size_t size;
    size_t pos;
};
```

이 패턴으로 C에서도 캡슐화가 가능하다.

### 함수 테이블 (vtable 패턴)

```c
typedef struct {
    void (*init)(void *self);
    void (*destroy)(void *self);
    int  (*read)(void *self, void *buf, size_t n);
} IOOps;
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

/* 고정 너비 정수 (이미 stdint.h에 정의됨) */
typedef uint8_t  u8;
typedef uint16_t u16;
typedef uint32_t u32;
typedef uint64_t u64;

/* 함수 포인터 테이블 */
typedef int (*BinaryOp)(int, int);

int op_add(int a, int b) { return a + b; }
int op_sub(int a, int b) { return a - b; }
int op_mul(int a, int b) { return a * b; }

typedef struct {
    const char *name;
    BinaryOp   op;
} Operation;

/* 불투명 포인터 패턴 */
typedef struct Stack Stack;

struct Stack {
    int *data;
    int  top;
    int  capacity;
};

Stack *stack_create(int capacity) {
    Stack *s = malloc(sizeof(Stack));
    if (!s) return NULL;
    s->data = malloc(capacity * sizeof(int));
    if (!s->data) { free(s); return NULL; }
    s->top = -1;
    s->capacity = capacity;
    return s;
}

int stack_push(Stack *s, int val) {
    if (s->top + 1 >= s->capacity) return -1;
    s->data[++(s->top)] = val;
    return 0;
}

int stack_pop(Stack *s, int *val) {
    if (s->top < 0) return -1;
    *val = s->data[(s->top)--];
    return 0;
}

void stack_free(Stack *s) {
    if (s) { free(s->data); free(s); }
}

int main() {
    /* 고정 너비 타입 */
    u32 x = 0xDEADBEEF;
    printf("0x%08X (%u)\n", x, x);

    /* 함수 테이블 */
    Operation ops[] = {
        {"add", op_add},
        {"sub", op_sub},
        {"mul", op_mul}
    };
    int a = 10, b = 3;
    for (size_t i = 0; i < sizeof(ops)/sizeof(ops[0]); i++) {
        printf("%s(%d, %d) = %d\n", ops[i].name, a, b, ops[i].op(a, b));
    }

    /* 스택 */
    Stack *stk = stack_create(5);
    for (int i = 1; i <= 5; i++) stack_push(stk, i * 10);
    int val;
    while (stack_pop(stk, &val) == 0) printf("%d ", val);
    printf("\n");
    stack_free(stk);

    return 0;
}
```

---

## 6. 마지막 정리

`typedef`는 텍스트 치환이 아닌 타입 시스템 등록이므로 `const` 한정자와의 상호작용 등에서 `#define`과 다르게 동작한다.

불투명 포인터 패턴과 함수 포인터 테이블에서 `typedef`는 캡슐화와 다형성을 구현하는 핵심 도구이다.

`stdint.h`의 `int32_t` 계열 타입은 `typedef`를 통한 이식성 추상화의 표준 사례이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp typedef",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 2,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
