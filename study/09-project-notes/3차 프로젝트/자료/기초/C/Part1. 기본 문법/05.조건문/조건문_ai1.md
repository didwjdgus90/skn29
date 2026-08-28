# 제목
[C/Cpp 기초] 조건문

# 본문

## 1. 한 줄 요약

조건문은 조건에 따라 다른 코드를 실행하도록 흐름을 분기하는 제어 구조이다.

C에서 조건문을 이해하면 상황에 따라 다른 동작을 하는 프로그램을 작성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 항상 같은 동작만 하면 쓸모가 없다.

예를 들어 로그인 프로그램은 비밀번호가 맞으면 "환영합니다", 틀리면 "오류"를 출력해야 한다.

```c
if (password == correct) {
    printf("환영합니다!\n");
} else {
    printf("비밀번호 오류\n");
}
```

이처럼 조건에 따라 다른 코드를 실행하는 것이 조건문의 역할이다.

---

## 3. 핵심 아이디어

### if - else if - else

```c
if (조건1) {
    /* 조건1이 참일 때 */
} else if (조건2) {
    /* 조건1이 거짓이고 조건2가 참일 때 */
} else {
    /* 모든 조건이 거짓일 때 */
}
```

### switch - case

여러 값 중 하나와 일치하는 경우를 처리할 때 유용하다.

```c
switch (변수) {
    case 값1:
        /* 값1일 때 */
        break;
    case 값2:
        /* 값2일 때 */
        break;
    default:
        /* 해당되는 case가 없을 때 */
        break;
}
```

`break`가 없으면 다음 case로 실행이 이어진다 (fall-through).

---

## 4. 동작 과정 살펴보기

### if 조건 평가

C에서는 0이 거짓, 0이 아닌 모든 값이 참이다.

```c
int x = 5;
if (x) {       /* 0이 아니므로 참 */
    printf("참\n");
}

int y = 0;
if (y) {       /* 0이므로 거짓 */
    printf("이건 출력 안 됨\n");
}
```

### switch fall-through 주의

```c
int n = 2;
switch (n) {
    case 1:
        printf("one\n");
        /* break 없음! */
    case 2:
        printf("two\n");
        /* break 없음! */
    case 3:
        printf("three\n");
        break;
}
/* 출력: two, three (n=2부터 break 전까지 모두 실행) */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* if - else if - else 예제 */
    int score = 85;

    if (score >= 90) {
        printf("A등급\n");
    } else if (score >= 80) {
        printf("B등급\n");
    } else if (score >= 70) {
        printf("C등급\n");
    } else if (score >= 60) {
        printf("D등급\n");
    } else {
        printf("F등급\n");
    }

    /* switch - case 예제 */
    int day = 3;
    switch (day) {
        case 1:
            printf("월요일\n");
            break;
        case 2:
            printf("화요일\n");
            break;
        case 3:
            printf("수요일\n");
            break;
        case 4:
            printf("목요일\n");
            break;
        case 5:
            printf("금요일\n");
            break;
        case 6:
        case 7:
            printf("주말\n");
            break;
        default:
            printf("잘못된 입력\n");
            break;
    }

    /* 중첩 if */
    int age = 25;
    int has_license = 1;

    if (age >= 18) {
        if (has_license) {
            printf("운전 가능\n");
        } else {
            printf("면허 필요\n");
        }
    } else {
        printf("미성년자는 운전 불가\n");
    }

    return 0;
}
```

### switch에서 문자열을 사용할 수 없다

switch는 정수형 값만 사용 가능하다.

```c
char *color = "red";
/* switch (color)는 불가! 문자열 비교는 if-else 사용 */
if (strcmp(color, "red") == 0) {
    printf("빨간색\n");
} else if (strcmp(color, "blue") == 0) {
    printf("파란색\n");
}
```

---

## 6. 마지막 정리

`if`는 조건이 참일 때 실행, `else`는 조건이 거짓일 때 실행한다.

`else if`로 여러 조건을 순서대로 검사할 수 있다.

`switch`는 정수형 값과 case를 비교할 때 유용하다.

`switch`에서 `break`를 빠뜨리면 다음 case로 실행이 계속된다 (fall-through).

C에서는 0이 거짓, 0이 아닌 값이 참이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 조건문",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
