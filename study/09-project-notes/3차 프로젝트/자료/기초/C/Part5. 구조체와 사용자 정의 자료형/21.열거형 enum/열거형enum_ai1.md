# 제목
[C/Cpp 기초] 열거형 enum

# 본문

## 1. 한 줄 요약

`enum`(열거형)은 정수 상수에 의미 있는 이름을 부여하여, 코드에서 숫자 대신 이름으로 표현하는 사용자 정의 자료형이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

방향을 0, 1, 2, 3으로 표현하면 의미를 알기 어렵다.

```c
/* 나쁜 예: 숫자만 보면 의미 불명확 */
if (direction == 0) move_up();
if (direction == 2) move_down();

/* enum 사용 */
enum Direction { UP, DOWN, LEFT, RIGHT };

if (direction == UP)   move_up();
if (direction == DOWN) move_down();
```

---

## 3. 핵심 아이디어

### enum 정의와 사용

```c
enum Color { RED, GREEN, BLUE };
/*           ↑     ↑      ↑
             0     1      2  (자동으로 0부터 증가) */

enum Color c = RED;
printf("%d\n", c);  /* 0 출력 */
```

### 값 직접 지정

```c
enum HttpStatus {
    OK = 200,
    NOT_FOUND = 404,
    SERVER_ERROR = 500
};

enum HttpStatus status = NOT_FOUND;
printf("상태 코드: %d\n", status);  /* 404 */
```

### 일부만 지정

```c
enum Weekday {
    MON = 1,  /* 1 */
    TUE,      /* 2 */
    WED,      /* 3 */
    THU,      /* 4 */
    FRI,      /* 5 */
    SAT,      /* 6 */
    SUN       /* 7 */
};
```

---

## 4. 동작 과정 살펴보기

### switch문과 함께 사용

```c
enum Season { SPRING, SUMMER, FALL, WINTER };

enum Season s = SUMMER;

switch (s) {
    case SPRING: printf("봄\n"); break;
    case SUMMER: printf("여름\n"); break;
    case FALL:   printf("가을\n"); break;
    case WINTER: printf("겨울\n"); break;
}
```

enum은 switch문과 함께 사용하면 가독성이 크게 향상된다.

### typedef와 함께

```c
typedef enum {
    RED, GREEN, BLUE
} Color;

Color c = GREEN;  /* enum 키워드 없이 사용 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* HTTP 상태 코드 */
typedef enum {
    HTTP_OK           = 200,
    HTTP_CREATED      = 201,
    HTTP_BAD_REQUEST  = 400,
    HTTP_UNAUTHORIZED = 401,
    HTTP_NOT_FOUND    = 404,
    HTTP_SERVER_ERROR = 500
} HttpStatus;

/* 트래픽 신호등 */
typedef enum {
    RED,
    YELLOW,
    GREEN
} TrafficLight;

const char *status_message(HttpStatus status) {
    switch (status) {
        case HTTP_OK:           return "OK";
        case HTTP_CREATED:      return "Created";
        case HTTP_BAD_REQUEST:  return "Bad Request";
        case HTTP_UNAUTHORIZED: return "Unauthorized";
        case HTTP_NOT_FOUND:    return "Not Found";
        case HTTP_SERVER_ERROR: return "Internal Server Error";
        default:                return "Unknown";
    }
}

void handle_traffic(TrafficLight light) {
    switch (light) {
        case RED:    printf("정지!\n"); break;
        case YELLOW: printf("준비...\n"); break;
        case GREEN:  printf("출발!\n"); break;
    }
}

/* enum을 배열 인덱스로 활용 */
typedef enum { MON, TUE, WED, THU, FRI, SAT, SUN } Weekday;

int main() {
    /* HTTP 상태 코드 */
    HttpStatus responses[] = {HTTP_OK, HTTP_NOT_FOUND, HTTP_SERVER_ERROR};
    for (int i = 0; i < 3; i++) {
        printf("%d: %s\n", responses[i], status_message(responses[i]));
    }

    printf("\n");

    /* 신호등 */
    for (TrafficLight l = RED; l <= GREEN; l++) {
        handle_traffic(l);
    }

    printf("\n");

    /* 요일 배열 인덱스 */
    const char *day_names[] = {"월", "화", "수", "목", "금", "토", "일"};
    Weekday today = WED;
    printf("오늘은 %s요일입니다.\n", day_names[today]);

    /* enum 값 확인 */
    printf("\n열거값 확인:\n");
    printf("RED=%d, YELLOW=%d, GREEN=%d\n", RED, YELLOW, GREEN);

    return 0;
}
```

---

## 6. 마지막 정리

`enum`은 정수 상수에 의미 있는 이름을 부여한다.

기본값은 0부터 시작하며 1씩 증가한다. 특정 값을 직접 지정하면 이후 값은 지정 값부터 증가한다.

`switch`문과 함께 사용하면 각 케이스의 의미가 명확해진다.

`typedef`와 함께 정의하면 `enum` 키워드 없이 타입 이름만으로 사용할 수 있다.

enum 값 자체는 정수이므로 배열 인덱스 등에도 사용할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 열거형 enum",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
