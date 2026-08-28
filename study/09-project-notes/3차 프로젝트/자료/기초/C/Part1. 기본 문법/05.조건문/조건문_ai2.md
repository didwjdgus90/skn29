# 제목
[C/Cpp 기초] 조건문

# 본문

## 1. 한 줄 요약

조건문은 갈림길이다. 조건에 따라 어느 길로 갈지 결정한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

GPS 내비게이션을 생각해보자.

직진할 때도 있고, 왼쪽으로 꺾을 때도 있고, 오른쪽으로 꺾을 때도 있다.

```text
if (앞이 막혀 있다면) → 우회전
else if (좌회전 가능하다면) → 좌회전
else → 직진
```

프로그램도 마찬가지로 상황에 따라 다른 길을 선택해야 한다. 이것이 조건문이다.

---

## 3. 핵심 아이디어

### if-else: 두 갈래 길

```text
조건이 참? ─── 예 ──→ 이 길로 간다 (if 블록 실행)
    │
    └─── 아니오 ──→ 저 길로 간다 (else 블록 실행)
```

### else if: 여러 갈래 길

신호등을 생각해보자.

```text
빨간불 → 멈춰라
노란불 → 준비해라
초록불 → 가라
```

```c
if (light == RED) {
    printf("멈춰라\n");
} else if (light == YELLOW) {
    printf("준비해라\n");
} else {
    printf("가라\n");
}
```

### switch: 번호판 앞의 여러 방

호텔 복도를 상상해보자. 방 번호에 따라 어느 방으로 들어갈지 결정한다.

```text
복도에 서서 방 번호 확인
  → 101호? → 101호 문 열기
  → 102호? → 102호 문 열기
  → 해당 없음? → 프런트에 문의
```

---

## 4. 동작 과정 살펴보기

### if 갈림길 통과하기

```text
score = 85

if (score >= 90)  → 거짓, 패스
else if (score >= 80)  → 참! ← 여기서 실행
else if (score >= 70)  → 도달 안 함
else  → 도달 안 함
```

첫 번째로 참인 조건에서 실행하고, 나머지는 건너뛴다.

### switch의 fall-through (미끄럼틀 주의!)

`break` 없이 case를 쓰면 미끄럼틀처럼 아래로 쭉 내려간다.

```text
switch (n = 2):
  case 1: 건너뜀
  case 2: 실행! → break 없으면 ↓ 계속
  case 3: 계속 실행!
  break: 여기서 멈춤
```

일부러 fall-through를 쓰는 경우도 있다 (토요일과 일요일을 같이 처리할 때).

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 날씨에 따른 옷 선택 (if-else if-else) */
    int temperature = 15;

    if (temperature >= 30) {
        printf("반팔을 입으세요.\n");
    } else if (temperature >= 20) {
        printf("긴팔을 입으세요.\n");
    } else if (temperature >= 10) {
        printf("자켓을 입으세요.\n");
    } else {
        printf("패딩을 입으세요.\n");
    }

    /* 요일에 따른 계획 (switch-case) */
    int day = 6;  /* 1=월, ..., 7=일 */

    switch (day) {
        case 1:
            printf("월요일: 회의\n");
            break;
        case 2:
            printf("화요일: 운동\n");
            break;
        case 3:
            printf("수요일: 스터디\n");
            break;
        case 4:
            printf("목요일: 운동\n");
            break;
        case 5:
            printf("금요일: 회식\n");
            break;
        case 6:
        case 7:
            /* 토요일, 일요일 둘 다 같은 처리 */
            printf("주말: 휴식!\n");
            break;
        default:
            printf("잘못된 요일\n");
    }

    return 0;
}
```

### 중첩 조건문 - 갈림길 안의 갈림길

```text
나이가 성인인가?
  → 예: 면허가 있는가?
           → 예: 운전 가능
           → 아니오: 면허 취득 필요
  → 아니오: 미성년자 운전 불가
```

```c
if (age >= 18) {
    if (has_license) {
        printf("운전 가능\n");
    } else {
        printf("면허 취득 필요\n");
    }
} else {
    printf("미성년자 운전 불가\n");
}
```

---

## 6. 마지막 정리

조건문은 프로그램의 갈림길이다.

`if`는 두 갈래, `else if`는 여러 갈래, `switch`는 번호판으로 방 찾기와 같다.

`switch`에서 `break`는 방 문을 닫는 것이다. 없으면 다음 방으로 계속 들어간다.

C에서는 0이 거짓, 1이 참이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 조건문",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
