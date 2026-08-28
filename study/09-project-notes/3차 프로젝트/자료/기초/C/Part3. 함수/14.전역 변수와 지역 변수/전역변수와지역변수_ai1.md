# 제목
[C/Cpp 기초] 전역 변수와 지역 변수

# 본문

## 1. 한 줄 요약

전역 변수는 모든 함수에서 접근 가능한 변수이고, 지역 변수는 선언된 함수 또는 블록 안에서만 유효한 변수이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

여러 함수에서 같은 데이터를 공유해야 할 때 전역 변수를 사용한다.

반면, 함수 내부에서만 필요한 임시 데이터는 지역 변수로 선언한다.

```c
int score = 0;  /* 전역: 모든 함수가 공유 */

void add_score(int points) {
    score += points;  /* 전역 변수 수정 */
}

void print_score() {
    printf("점수: %d\n", score);  /* 전역 변수 읽기 */
}
```

---

## 3. 핵심 아이디어

### 전역 변수

함수 바깥에 선언하며, 파일 전체 어디서든 접근 가능하다.

```c
#include <stdio.h>

int count = 0;  /* 전역 변수 */

void increment() { count++; }
void decrement() { count--; }

int main() {
    increment();
    increment();
    decrement();
    printf("%d\n", count);  /* 1 */
    return 0;
}
```

전역 변수는 프로그램 시작 시 자동으로 0으로 초기화된다.

### 지역 변수

함수 또는 블록 안에 선언하며, 해당 범위 안에서만 유효하다.

```c
void my_func() {
    int local = 10;  /* 지역 변수: my_func 안에서만 유효 */
    printf("%d\n", local);
}
/* local은 여기서 없음 */
```

지역 변수는 초기화하지 않으면 쓰레기 값이 들어있다.

### static 지역 변수

함수 안에서 선언하지만 전역처럼 값이 유지된다.

```c
void counter() {
    static int n = 0;  /* 처음 한 번만 초기화 */
    n++;
    printf("%d\n", n);
}
```

---

## 4. 동작 과정 살펴보기

### 전역 vs 지역 이름 충돌

전역 변수와 같은 이름의 지역 변수가 있으면 지역 변수가 우선이다.

```c
int x = 100;  /* 전역 */

void func() {
    int x = 200;  /* 지역: 전역 x를 가림 */
    printf("func: x = %d\n", x);  /* 200 */
}

int main() {
    printf("main: x = %d\n", x);  /* 100 */
    func();
    printf("main: x = %d\n", x);  /* 100 (전역 그대로) */
    return 0;
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 전역 변수 */
int total_score = 0;
int game_lives = 3;
const int MAX_SCORE = 1000;

void earn_points(int points) {
    int bonus;  /* 지역 변수 */
    if (points > 100) {
        bonus = points * 2;  /* 보너스 적용 */
    } else {
        bonus = points;
    }
    total_score += bonus;
    printf("%d점 획득 (보너스: %d)\n", points, bonus);
}

void lose_life() {
    int remaining;  /* 지역 변수 */
    game_lives--;
    remaining = game_lives;
    if (remaining <= 0) {
        printf("게임 오버!\n");
    } else {
        printf("라이프 %d개 남음\n", remaining);
    }
}

void static_demo() {
    static int call_count = 0;  /* static 지역 변수 */
    int temp = 0;               /* 일반 지역 변수 */
    call_count++;
    temp++;
    printf("call_count=%d, temp=%d\n", call_count, temp);
}

int main() {
    earn_points(50);
    earn_points(150);

    printf("총 점수: %d\n", total_score);

    lose_life();
    lose_life();
    lose_life();

    printf("\nstatic 변수 시연:\n");
    static_demo();  /* call_count=1, temp=1 */
    static_demo();  /* call_count=2, temp=1 */
    static_demo();  /* call_count=3, temp=1 */

    return 0;
}
```

### 전역 변수의 단점

```c
/* 전역 변수는 어디서든 변경 가능 → 버그 추적 어려움 */
int shared = 0;

void func_a() { shared = 10; }
void func_b() { shared = 20; }  /* func_a의 효과를 덮어씀 */
void func_c() { printf("%d\n", shared); }  /* 어떤 값이 나올지 예측 어려움 */
```

전역 변수는 꼭 필요한 경우에만 최소한으로 사용하는 것이 좋다.

---

## 6. 마지막 정리

전역 변수는 함수 밖에 선언하며 모든 함수에서 접근 가능하다. 자동으로 0 초기화된다.

지역 변수는 함수/블록 안에 선언하며 해당 범위에서만 유효하다. 반드시 초기화해야 한다.

이름이 겹치면 지역 변수가 전역 변수를 가린다.

`static` 지역 변수는 스코프는 함수 안이지만 값은 함수 호출 사이에도 유지된다.

전역 변수는 남용하면 유지보수가 어려워지므로 최소화하는 것이 좋다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 전역 변수와 지역 변수",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
