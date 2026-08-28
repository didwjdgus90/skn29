# 제목
[C/Cpp 기초] 변수의 범위

# 본문

## 1. 한 줄 요약

변수의 범위(scope)는 식별자가 유효한 프로그램 텍스트 영역이며, C는 블록 스코프, 파일 스코프, 함수 프로토타입 스코프, 함수 스코프(레이블)를 정의한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

스코프는 명명 충돌을 방지하고, 캡슐화를 통해 변수의 가시성을 제한함으로써 코드의 모듈성과 안전성을 높인다.

링커 관점에서 external linkage는 다른 번역 단위에서 접근 가능하고, internal linkage(`static`)는 현재 번역 단위에만 제한된다.

---

## 3. 핵심 아이디어

### 스코프 분류

**블록 스코프 (Block Scope)**

`{...}` 내에서 선언된 식별자는 선언 지점부터 블록 끝까지 유효하다.

```c
{
    int x = 1;      /* x의 스코프 시작 */
    printf("%d", x); /* 유효 */
}                   /* x의 스코프 끝 */
```

**파일 스코프 (File Scope)**

모든 블록 밖에서 선언된 식별자. 번역 단위 전체에서 유효하다.

**함수 프로토타입 스코프**

함수 선언의 매개변수 이름은 선언 내에서만 유효하다.

```c
int func(int x, int y);  /* x, y는 이 선언 내에서만 */
```

### 스코프와 링크(Linkage) 구분

스코프(scope)는 **가시성**이고, 링크(linkage)는 **공유 범위**이다.

```c
static int x = 1;  /* 파일 스코프 + 내부 링크 (다른 파일에서 접근 불가) */
       int y = 2;  /* 파일 스코프 + 외부 링크 (다른 파일에서 접근 가능) */
```

### 변수 숨김과 심볼 테이블

컴파일러는 심볼 테이블에서 내부 스코프부터 바깥 스코프 순으로 이름을 탐색한다.

```c
int x = 1;
{
    int x = 2;     /* 새 심볼 테이블 엔트리 */
    printf("%d", x);  /* 내부 x(2) 발견: 외부 x(1) 숨김 */
}
```

---

## 4. 동작 과정 살펴보기

### 저장 기간(Storage Duration)과 스코프의 차이

```c
void f() {
    int a = 1;        /* 자동 저장 기간: 블록 스코프 */
    static int b = 1; /* 정적 저장 기간: 블록 스코프이지만 .data 세그먼트에 상주 */
}
```

`static` 지역 변수는 스코프는 함수 내부지만, 메모리는 전역 변수처럼 프로그램 수명 내내 유지된다.

```text
메모리 세그먼트:
  .text:   코드
  .data:   초기화된 전역/static 변수
  .bss:    초기화되지 않은 전역/static 변수
  stack:   자동(지역) 변수
  heap:    동적 할당
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 파일 스코프 + 외부 링크 */
int global_counter = 0;

/* 파일 스코프 + 내부 링크 (이 파일에서만) */
static int file_private = 0;

/* static 지역 변수: 싱글턴 카운터 패턴 */
int get_id() {
    static int id = 0;  /* 초기화는 최초 1회만 */
    return ++id;
}

/* 스코프 시연 */
void scope_demo() {
    int x = 10;
    printf("외부 x = %d\n", x);

    {
        int x = 20;  /* 외부 x 숨김 (shadowing) */
        printf("내부 x = %d\n", x);

        /* 외부 x에 접근하려면 포인터 필요 */
    }
    printf("외부 x (복원) = %d\n", x);
}

int main() {
    /* get_id: static 변수로 호출마다 증가 */
    printf("ID: %d, %d, %d\n", get_id(), get_id(), get_id());

    scope_demo();

    /* for 루프 변수 스코프 (C99) */
    for (int i = 0; i < 3; i++) {
        /* i는 이 루프 블록에서만 유효 */
    }
    /* printf("%d", i); */  /* 컴파일 오류: i는 스코프 밖 */

    return 0;
}
```

### 함수 스코프의 레이블

`goto` 레이블은 함수 전체에서 유효한 함수 스코프를 가진다.

```c
void f() {
    goto end;  /* 함수 내 어디서든 레이블 참조 가능 */
    /* ... */
end:
    printf("종료\n");
}
```

---

## 6. 마지막 정리

C의 스코프는 블록, 파일, 함수 프로토타입, 함수(레이블) 4종류이다.

스코프는 가시성(visibility), 링크는 공유 범위(sharing), 저장 기간은 수명(lifetime)이다.

`static` 지역 변수는 블록 스코프이지만 정적 저장 기간을 가져 함수 호출 간 상태를 유지한다.

내부 스코프의 선언은 동일 이름의 외부 선언을 숨긴다(shadowing). 의도치 않은 숨김은 버그 원인이 된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 변수의 범위",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
