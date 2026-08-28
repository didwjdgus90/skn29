# 제목
[C/Cpp 기초] 변수의 범위

# 본문

## 1. 한 줄 요약

변수의 범위(스코프)는 변수에 접근할 수 있는 코드 영역이다. C에서 변수는 선언된 블록(`{}`) 안에서만 유효하다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램이 커지면 여러 함수에서 변수 이름이 겹치는 경우가 생긴다.

스코프 덕분에 각 함수의 `i`, `count`, `result` 같은 변수들이 서로 충돌하지 않는다.

```c
void func1() {
    int x = 10;  /* 이 x는 func1 전용 */
}

void func2() {
    int x = 20;  /* 이 x는 func2 전용, 위의 x와 별개 */
}
```

---

## 3. 핵심 아이디어

### 블록 스코프

중괄호 `{}` 안에서 선언된 변수는 그 블록 안에서만 유효하다.

```c
{
    int x = 10;  /* x는 이 블록 안에서만 유효 */
    printf("%d\n", x);  /* OK */
}
printf("%d\n", x);  /* 오류! x가 범위를 벗어남 */
```

### 함수 스코프

매개변수와 지역 변수는 함수 안에서만 유효하다.

```c
void my_function(int param) {
    int local = 5;  /* 이 함수 안에서만 유효 */
}
/* local, param은 여기서 접근 불가 */
```

### 중첩 스코프와 변수 숨김

안쪽 블록에서 바깥쪽과 같은 이름의 변수를 선언하면, 안쪽 변수가 바깥쪽을 가린다.

```c
int x = 1;  /* 바깥쪽 x */
{
    int x = 2;  /* 안쪽 x: 바깥 x를 가림 */
    printf("%d\n", x);  /* 2 */
}
printf("%d\n", x);  /* 1 (바깥 x) */
```

---

## 4. 동작 과정 살펴보기

### 스코프별 접근 가능 범위

```c
int a = 1;  /* 파일 스코프 (전역) */

void outer() {
    int b = 2;  /* outer 함수 스코프 */

    for (int i = 0; i < 3; i++) {  /* for 블록 스코프 */
        int c = 3;  /* for 블록 스코프 */
        printf("a=%d b=%d i=%d c=%d\n", a, b, i, c);
        /* a, b, i, c 모두 접근 가능 */
    }
    /* i, c는 여기서 접근 불가 */
    printf("a=%d b=%d\n", a, b);  /* OK */
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int global = 100;  /* 전역 변수: 모든 함수에서 접근 */

void test_scope() {
    int local = 10;  /* 지역 변수 */
    printf("함수 안: global=%d, local=%d\n", global, local);

    {  /* 내부 블록 */
        int inner = 20;
        int local = 99;  /* 바깥 local 숨김 */
        printf("내부 블록: local=%d (숨김), inner=%d\n", local, inner);
    }
    /* inner는 여기서 없음 */

    printf("블록 후: local=%d\n", local);  /* 10 (원래 local) */
}

void scope_in_loop() {
    for (int i = 0; i < 3; i++) {
        int square = i * i;
        printf("i=%d, square=%d\n", i, square);
    }
    /* i, square는 여기서 없음 */
}

int main() {
    test_scope();
    printf("\n");
    scope_in_loop();

    int local_main = 50;
    printf("\nmain의 local: %d\n", local_main);

    return 0;
}
```

### 변수 수명(Lifetime)

스코프와 수명은 다른 개념이다.

```c
void count() {
    int c = 0;     /* 일반 지역 변수: 함수 호출마다 새로 생성 */
    static int s = 0;  /* 정적 지역 변수: 프로그램 종료까지 유지 */
    c++;
    s++;
    printf("c=%d, s=%d\n", c, s);
}

count();  /* c=1, s=1 */
count();  /* c=1, s=2 */
count();  /* c=1, s=3 */
```

---

## 6. 마지막 정리

변수의 범위는 접근 가능한 코드 영역이다.

`{}` 블록 안에서 선언된 변수는 그 블록 안에서만 존재한다.

안쪽 스코프에서 바깥쪽과 같은 이름을 쓰면 바깥 변수가 가려진다(shadowing).

`static` 지역 변수는 스코프가 함수 내부지만 수명은 프로그램 전체이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 변수의 범위",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
