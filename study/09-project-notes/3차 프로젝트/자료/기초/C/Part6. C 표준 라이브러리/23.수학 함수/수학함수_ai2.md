# 제목
[C/Cpp 기초] 수학 함수

# 본문

## 1. 한 줄 요약

수학 함수는 계산기의 버튼들이다. 직접 계산하는 수식을 짜지 않아도 sqrt 버튼 하나로 제곱근을 구할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

게임에서 두 캐릭터 사이의 거리를 계산해야 한다.

피타고라스 정리: 거리 = √((x2-x1)² + (y2-y1)²)

직접 제곱근을 구하는 코드를 짜는 것은 매우 복잡하다.

```c
/* math.h의 sqrt() 사용 */
double dist = sqrt(pow(x2-x1, 2) + pow(y2-y1, 2));
```

계산기 버튼 누르듯 간단하다.

---

## 3. 핵심 아이디어

### 수학 계산기 버튼 목록

```text
[sqrt] 제곱근   → sqrt(16) = 4
[pow]  거듭제곱  → pow(2, 8) = 256
[abs]  절댓값   → fabs(-5) = 5
[ceil] 올림     → ceil(3.1) = 4
[floor] 내림   → floor(3.9) = 3
[round] 반올림  → round(2.5) = 3
[sin/cos/tan] 삼각함수
[log]  자연로그  → log(e) = 1
[log10] 상용로그 → log10(100) = 2
```

### 라디안 계산기

```text
삼각함수 계산기는 "라디안"으로 계산한다.
우리가 아는 "도(degree)"와 다르다.

90도 → π/2 라디안 (약 1.5708)
180도 → π 라디안 (약 3.1416)
360도 → 2π 라디안 (약 6.2832)

변환 공식: 라디안 = 도 × π / 180
```

---

## 4. 동작 과정 살펴보기

### 게임 캐릭터 거리 계산

```text
캐릭터 A: (3, 0)
캐릭터 B: (0, 4)

가로 거리 = 3 - 0 = 3
세로 거리 = 4 - 0 = 4

대각선(직선) 거리 = sqrt(3² + 4²)
               = sqrt(9 + 16)
               = sqrt(25)
               = 5
```

### 올림과 내림의 실생활

```text
배달비 계산: 3.2km → 올림하면 4km 요금
잔돈 계산: 3,750원 → 내림하면 3,000원
반올림: 시험 점수 87.5 → 반올림 → 88점
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <math.h>

int main() {
    /* 계산기 버튼들 */
    printf("=== 계산기 ===\n");
    printf("sqrt(25)    = %.1f\n", sqrt(25.0));
    printf("pow(2, 10)  = %.0f\n", pow(2.0, 10.0));
    printf("fabs(-7.5)  = %.1f\n", fabs(-7.5));

    printf("\n=== 올림/내림/반올림 ===\n");
    double prices[] = {3.1, 3.5, 3.9};
    for (int i = 0; i < 3; i++) {
        printf("%.1f → 올림: %.0f, 반올림: %.0f, 내림: %.0f\n",
               prices[i], ceil(prices[i]), round(prices[i]), floor(prices[i]));
    }

    /* 게임 거리 계산 */
    printf("\n=== 게임 거리 계산 ===\n");
    typedef struct { double x, y; } Point;
    Point hero   = {0, 0};
    Point monster = {5, 12};

    double dx = monster.x - hero.x;
    double dy = monster.y - hero.y;
    double dist = sqrt(dx*dx + dy*dy);
    printf("영웅(0,0) ~ 몬스터(5,12) 거리: %.2f\n", dist);
    printf("공격 범위 10 이내: %s\n", dist <= 10 ? "공격 가능!" : "너무 멀어요...");

    /* 삼각함수 (90도 방향 계산) */
    printf("\n=== 방향 계산 ===\n");
    double angle_deg = 45.0;
    double angle_rad = angle_deg * M_PI / 180.0;
    double speed = 10.0;
    printf("45도 방향으로 속도 10 이동:\n");
    printf("  x 이동: %.2f\n", speed * cos(angle_rad));
    printf("  y 이동: %.2f\n", speed * sin(angle_rad));

    return 0;
}
```

---

## 6. 마지막 정리

`<math.h>`는 계산기 버튼처럼 다양한 수학 계산 도구를 제공한다.

삼각함수는 라디안 단위를 쓰므로 `도 × π/180` 으로 변환해야 한다.

Linux에서 컴파일할 때 `-lm` 옵션을 붙여야 한다.

게임 물리, 그래픽, 통계 등 다양한 분야에서 math.h를 자주 사용한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 수학 함수",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
