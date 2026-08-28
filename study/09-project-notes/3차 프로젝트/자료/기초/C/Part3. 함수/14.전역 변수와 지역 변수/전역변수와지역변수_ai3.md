# 제목
[C/Cpp 기초] 전역 변수와 지역 변수

# 본문

## 1. 한 줄 요약

전역 변수는 파일 스코프와 정적 저장 기간을 가지며 `.data`/`.bss` 세그먼트에 배치되고, 지역 변수는 블록 스코프와 자동 저장 기간을 가지며 스택에 할당된다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

저장 기간과 가시성의 선택은 데이터의 수명과 공유 범위를 결정한다.

전역 변수는 여러 번역 단위에 걸친 상태 공유를 가능케 하지만, 전역 상태는 예측 불가능한 사이드 이펙트와 테스트 어려움을 초래한다.

지역 변수는 스택에 할당되어 함수 종료 시 자동 해제되며, 가시성이 제한되어 캡슐화와 재진입성(reentrancy)을 보장한다.

---

## 3. 핵심 아이디어

### 메모리 세그먼트와 변수 유형

```text
프로세스 주소 공간:

[ .text   ] 코드 영역 (read-only)
[ .rodata ] 문자열 리터럴, const 전역 (read-only)
[ .data   ] 초기화된 전역/static 변수
[ .bss    ] 미초기화 전역/static 변수 (0으로 초기화됨)
[ heap    ] 동적 할당 (malloc/free)
[ stack   ] 지역(자동) 변수, 함수 인수, 리턴 주소
```

```c
int g1 = 10;      /* .data */
int g2;           /* .bss (자동 0 초기화) */
static int s1 = 5; /* .data */

void f() {
    int local;    /* stack (초기화 안 됨) */
    static int s2; /* .bss */
}
```

### 링크(Linkage)

| 선언 | 스코프 | 저장 기간 | 링크 |
|---|---|---|---|
| 전역 `int x` | 파일 | 정적 | 외부(external) |
| `static int x` (전역) | 파일 | 정적 | 내부(internal) |
| 지역 `int x` | 블록 | 자동 | 없음 |
| `static int x` (지역) | 블록 | 정적 | 없음 |
| `extern int x` | 파일 | 정적 | 외부 |

### 재진입성 (Reentrancy)

지역 변수를 사용하는 함수는 재진입 가능하다(멀티스레드 안전 가능성 있음). 전역 변수를 사용하는 함수는 재진입이 불안전하다.

```c
/* 비재진입: 전역 버퍼 사용 */
char buffer[100];
char *non_reentrant_func(int x) {
    sprintf(buffer, "%d", x);
    return buffer;  /* 스레드 안전하지 않음 */
}

/* 재진입 가능: 호출자 제공 버퍼 */
void reentrant_func(int x, char *buf, size_t size) {
    snprintf(buf, size, "%d", x);
}
```

---

## 4. 동작 과정 살펴보기

### static 지역 변수의 초기화 보장

C11 이후 멀티스레드 환경에서 `static` 지역 변수는 최초 진입 시 단 한 번만 초기화된다.

```c
/* 싱글턴 패턴 (단일 스레드) */
struct Config *get_config() {
    static struct Config config = {0};
    static int initialized = 0;
    if (!initialized) {
        /* 초기화 */
        initialized = 1;
    }
    return &config;
}
```

### 전역 변수의 초기화 순서 문제

같은 번역 단위 내에서는 선언 순서대로 초기화되지만, 다른 번역 단위 간 초기화 순서는 미정의이다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdint.h>

/* 외부 링크: 다른 파일에서 extern으로 접근 가능 */
uint32_t error_code = 0;

/* 내부 링크: 이 파일에서만 접근 가능 */
static uint32_t internal_state = 0;

/* static 지역 변수: 싱글턴 카운터 */
int generate_id() {
    static int next_id = 1;
    return next_id++;
}

/* 순수 함수: 전역 상태 없음, 재진입 가능 */
int pure_add(int a, int b) {
    return a + b;
}

/* 부작용 함수: 전역 상태 수정 */
void set_error(uint32_t code) {
    error_code = code;
}

int main() {
    /* 지역 변수: 스택에 할당 */
    int local1 = 10;
    int local2 = 20;

    printf("local1 주소: %p\n", (void *)&local1);
    printf("local2 주소: %p\n", (void *)&local2);
    /* 두 주소가 가깝고 연속적: 같은 스택 프레임 */

    printf("error_code 주소: %p\n", (void *)&error_code);
    /* 완전히 다른 주소 영역: .data 또는 .bss */

    for (int i = 0; i < 3; i++) {
        printf("ID: %d\n", generate_id());
    }

    set_error(404);
    printf("Error: %u\n", error_code);

    return 0;
}
```

---

## 6. 마지막 정리

전역 변수는 `.data`/`.bss`에 배치되어 프로그램 수명 내내 유지되며, 기본적으로 외부 링크를 가진다.

지역 변수는 스택에 할당되며 블록 종료 시 자동 해제된다.

`static`은 저장 기간을 정적으로, `static` 전역은 링크를 내부로 변경한다.

전역 상태는 재진입성을 깨뜨리므로 멀티스레드 코드에서 뮤텍스나 TLS(Thread-Local Storage)가 필요하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 전역 변수와 지역 변수",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
