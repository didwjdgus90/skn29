# 제목
[C/Cpp 기초] 열거형 enum

# 본문

## 1. 한 줄 요약

C의 `enum`은 명명된 정수 상수의 집합을 정의하는 타입으로, 컴파일러가 값의 의미를 이해하지 못하므로 타입 안전성이 약하다. C++의 `enum class`와 달리 정수 간 암묵적 변환이 허용된다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

매직 넘버(magic number)를 제거하고 코드의 의도를 명시화한다. 컴파일러 경고(`-Wswitch`)를 통해 `switch`문에서 처리되지 않은 enum 값을 탐지할 수 있다.

---

## 3. 핵심 아이디어

### C enum의 타입 특성

```c
enum Color { RED, GREEN, BLUE };

int n = RED;           /* OK: enum → int 암묵적 변환 */
enum Color c = 5;      /* 경고 없음: int → enum 암묵적 변환 */
enum Color d = GREEN + 1; /* BLUE와 같지만 타입이 int */
```

C enum은 사실상 `int`와 동일하게 취급된다. 타입 안전성이 없다.

### 열거자 범위(Enumerator Scope)

```c
enum A { VALUE = 1 };
enum B { VALUE = 2 };  /* 컴파일 오류: VALUE 재정의 */
```

C enum의 열거자는 파일 범위(file scope)에 들어간다. 이름 충돌 주의.

### 내부 표현 타입

```c
/* 컴파일러 구현 의존적이나 일반적으로 int 크기 */
printf("sizeof(enum Color) = %zu\n", sizeof(enum Color));
/* 보통 4 */
```

---

## 4. 동작 과정 살펴보기

### 비트 마스크 플래그 패턴

```c
typedef enum {
    PERM_NONE    = 0,
    PERM_READ    = 1 << 0,  /* 0001 */
    PERM_WRITE   = 1 << 1,  /* 0010 */
    PERM_EXECUTE = 1 << 2,  /* 0100 */
    PERM_ALL     = PERM_READ | PERM_WRITE | PERM_EXECUTE
} Permission;

Permission p = PERM_READ | PERM_WRITE;  /* 0011 */
if (p & PERM_READ) printf("읽기 가능\n");
```

### -Wswitch 경고 활용

```c
enum State { IDLE, RUNNING, PAUSED, STOPPED };

switch (state) {
    case IDLE:    /* ... */ break;
    case RUNNING: /* ... */ break;
    /* PAUSED, STOPPED 누락 → -Wswitch 경고 */
}
/* 새 enum 값 추가 시 switch 누락을 컴파일러가 경고 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 비트 플래그 권한 */
typedef enum {
    PERM_NONE    = 0,
    PERM_READ    = 1 << 0,
    PERM_WRITE   = 1 << 1,
    PERM_EXECUTE = 1 << 2,
    PERM_ALL     = (1 << 3) - 1
} Permission;

/* FSM 상태 */
typedef enum {
    STATE_IDLE,
    STATE_RUNNING,
    STATE_PAUSED,
    STATE_STOPPED,
    STATE_COUNT  /* 개수 파악용: 항상 마지막에 */
} State;

const char *state_names[STATE_COUNT] = {
    "IDLE", "RUNNING", "PAUSED", "STOPPED"
};

/* 권한 문자열 변환 */
void print_perms(Permission p) {
    printf("[%c%c%c]",
           (p & PERM_READ)    ? 'r' : '-',
           (p & PERM_WRITE)   ? 'w' : '-',
           (p & PERM_EXECUTE) ? 'x' : '-');
}

/* FSM 전이 */
State transition(State cur, int input) {
    switch (cur) {
        case STATE_IDLE:
            return input == 1 ? STATE_RUNNING : cur;
        case STATE_RUNNING:
            if (input == 2) return STATE_PAUSED;
            if (input == 3) return STATE_STOPPED;
            return cur;
        case STATE_PAUSED:
            return input == 1 ? STATE_RUNNING : cur;
        case STATE_STOPPED:
            return cur;
        default:
            return cur;
    }
}

int main() {
    /* 권한 비트 마스크 */
    Permission file_perms = PERM_READ | PERM_WRITE;
    printf("파일 권한: ");
    print_perms(file_perms);
    printf(" (0x%X)\n", file_perms);

    Permission exec_perms = PERM_ALL;
    printf("실행 파일 권한: ");
    print_perms(exec_perms);
    printf(" (0x%X)\n", exec_perms);

    /* FSM */
    printf("\n상태 머신 시뮬레이션:\n");
    State s = STATE_IDLE;
    int inputs[] = {1, 2, 1, 3};  /* 시작, 일시정지, 재시작, 종료 */
    printf("초기 상태: %s\n", state_names[s]);
    for (size_t i = 0; i < sizeof(inputs)/sizeof(inputs[0]); i++) {
        s = transition(s, inputs[i]);
        printf("입력 %d → %s\n", inputs[i], state_names[s]);
    }

    /* STATE_COUNT 활용 */
    printf("\n총 상태 수: %d\n", STATE_COUNT);

    return 0;
}
```

---

## 6. 마지막 정리

C enum은 정수 상수의 집합이며 진정한 타입 안전성이 없다. `int`와의 암묵적 변환이 허용된다.

비트 플래그 패턴(`1 << n`)으로 권한 등 플래그 조합을 깔끔하게 표현한다.

마지막 열거자로 `COUNT` 값을 두면 개수를 코드에 하드코딩하지 않아도 된다.

`-Wswitch` 컴파일러 경고로 `switch` 처리 누락을 자동 탐지한다.

FSM(유한 상태 머신) 구현 시 상태를 enum으로 표현하면 상태 전이가 명확해진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 열거형 enum",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 5,
  "target_level": "high",
  "language": "c"
}
```
