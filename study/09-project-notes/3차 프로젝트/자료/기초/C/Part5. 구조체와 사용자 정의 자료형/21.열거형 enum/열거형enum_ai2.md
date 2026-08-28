# 제목
[C/Cpp 기초] 열거형 enum

# 본문

## 1. 한 줄 요약

열거형은 선택지에 번호 대신 이름표를 붙이는 것이다. 메뉴판처럼 각 선택지에 의미 있는 이름을 달아준다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

카드 게임에서 카드 무늬를 0=스페이드, 1=하트, 2=다이아, 3=클럽으로 나타낸다고 하자.

```c
/* 숫자만 보면 뭔지 모름 */
if (suit == 1) printf("하트!");
if (suit == 3) printf("클럽!");

/* enum: 이름표 부착 */
enum Suit { SPADE, HEART, DIAMOND, CLUB };
if (suit == HEART)  printf("하트!");
if (suit == CLUB)   printf("클럽!");
```

코드를 보는 사람이 바로 이해할 수 있다.

---

## 3. 핵심 아이디어

### 이름표 목록 만들기

```text
enum 목록이름 {
    이름표1,   ← 자동으로 0
    이름표2,   ← 자동으로 1
    이름표3,   ← 자동으로 2
    ...
};
```

```c
enum Season { SPRING, SUMMER, FALL, WINTER };
/*              0       1      2      3     */
```

### 이름표에 숫자 직접 붙이기

```c
enum Planet {
    MERCURY = 1,   /* 태양에서 1번째 */
    VENUS   = 2,
    EARTH   = 3,
    MARS    = 4,
};
```

---

## 4. 동작 과정 살펴보기

### 계절 분류기 비유

```text
enum 없이:
  switch (season) {
      case 0: ...  ← 0이 뭔 계절?
      case 1: ...  ← 1이 뭔 계절?
  }

enum 사용:
  switch (season) {
      case SPRING: ...  ← 봄! 바로 이해
      case SUMMER: ...  ← 여름! 명확
  }
```

### 신호등 예시

```text
이름표:  RED → YELLOW → GREEN
숫자:     0  →    1   →   2

신호등은 왼쪽에서 오른쪽으로 순서가 있다.
enum은 이 순서를 이름으로 표현한다.
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 계절 열거형 */
typedef enum {
    SPRING, SUMMER, FALL, WINTER
} Season;

/* 방향 열거형 */
typedef enum {
    NORTH, EAST, SOUTH, WEST
} Direction;

/* 상태 코드 (의미 있는 숫자) */
typedef enum {
    SUCCESS  = 0,
    ERROR    = -1,
    PENDING  = 1
} Status;

/* 계절 이름 반환 */
const char *season_name(Season s) {
    switch (s) {
        case SPRING: return "봄 🌸";
        case SUMMER: return "여름 ☀️";
        case FALL:   return "가을 🍂";
        case WINTER: return "겨울 ❄️";
        default:     return "알 수 없음";
    }
}

/* 방향 이동 */
void move(Direction d) {
    switch (d) {
        case NORTH: printf("북쪽으로 이동!\n"); break;
        case EAST:  printf("동쪽으로 이동!\n"); break;
        case SOUTH: printf("남쪽으로 이동!\n"); break;
        case WEST:  printf("서쪽으로 이동!\n"); break;
    }
}

int main() {
    /* 계절 순환 */
    printf("사계절:\n");
    for (Season s = SPRING; s <= WINTER; s++) {
        printf("  %s\n", season_name(s));
    }

    printf("\n나침반 이동:\n");
    Direction path[] = {NORTH, NORTH, EAST, SOUTH};
    for (int i = 0; i < 4; i++) {
        move(path[i]);
    }

    printf("\n상태 코드 확인:\n");
    Status result = SUCCESS;
    if (result == SUCCESS) printf("작업 성공!\n");
    else if (result == ERROR) printf("오류 발생!\n");
    else printf("대기 중...\n");

    return 0;
}
```

---

## 6. 마지막 정리

열거형은 이름표 목록이다. 숫자 대신 의미 있는 이름으로 선택지를 표현한다.

기본값은 0부터 시작하고 1씩 늘어난다. 원하면 직접 숫자를 지정할 수 있다.

`switch`문과 함께 쓰면 코드의 의미가 훨씬 명확해진다.

`typedef`로 별명을 붙이면 `enum` 키워드 없이 간결하게 사용할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 열거형 enum",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
