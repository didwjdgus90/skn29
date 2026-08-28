# 제목
[C/Cpp 기초] 전역 변수와 지역 변수

# 본문

## 1. 한 줄 요약

전역 변수는 모두가 볼 수 있는 공용 게시판이고, 지역 변수는 본인만 쓰는 개인 수첩이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

회사 사무실을 상상해보자.

**공용 게시판 (전역 변수)**: 모든 직원이 읽고 수정할 수 있다. 회사 전체 공지, 점수판 같은 것.

**개인 수첩 (지역 변수)**: 각 직원이 자기 업무에 쓰는 메모. 다른 직원은 볼 수 없다.

```text
공용 게시판: "총 매출: 5000만원" (전역)
직원A 수첩: "내 할인율 계산: 15%" (지역)
직원B 수첩: "내 상품 재고: 30개" (지역)
```

---

## 3. 핵심 아이디어

### 공용 게시판 (전역 변수)

모든 함수에서 읽고 쓸 수 있다.

```text
int total = 0;  ← 복도에 걸린 공용 게시판

function_A: total을 읽고 씀
function_B: total을 읽고 씀
main: total을 읽고 씀

게시판은 프로그램이 켜질 때부터 꺼질 때까지 존재
```

### 개인 수첩 (지역 변수)

해당 함수 안에서만 유효하다.

```text
void function_A() {
    int memo = 10;  ← 내 수첩
    /* memo 사용 */
}  ← 함수 끝나면 수첩 버림

void function_B() {
    /* function_A의 memo를 볼 수 없음 */
}
```

### 수첩 VS 게시판 비교

| | 전역 변수 | 지역 변수 |
|---|---|---|
| 위치 | 함수 바깥 | 함수/블록 안 |
| 접근 | 모든 함수 | 해당 범위만 |
| 수명 | 프로그램 전체 | 블록 실행 중 |
| 초기화 | 자동 0 | 직접 해야 함 |

---

## 4. 동작 과정 살펴보기

### 같은 이름 충돌 - 가까운 것이 우선

```text
int x = 100;  ← 복도 게시판의 x

void func() {
    int x = 200;  ← 내 수첩의 x (게시판 x를 가림)
    printf(x);   → 200 (내 수첩)
}

main:
    printf(x);   → 100 (복도 게시판)
```

가까운 곳의 변수가 우선이다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 공용 게시판 (전역 변수) */
int score = 0;       /* 점수판 */
int level = 1;       /* 레벨 */

void level_up() {
    int bonus = level * 10;  /* 내 수첩 (지역) */
    score += bonus;
    level++;
    printf("레벨업! 보너스: %d점, 현재 점수: %d\n", bonus, score);
}

void show_status() {
    /* 공용 게시판을 읽음 */
    printf("=== 현황 ===\n");
    printf("레벨: %d\n", level);
    printf("점수: %d\n", score);
}

/* static - 오래 살아남는 개인 수첩 */
void visit_counter() {
    static int visits = 0;  /* 함수가 끝나도 안 버림 */
    int today = 1;           /* 일반 수첩: 함수 끝나면 버림 */
    visits += today;
    printf("총 방문: %d\n", visits);
}

int main() {
    show_status();

    level_up();
    level_up();

    show_status();

    printf("\n방문 카운터:\n");
    visit_counter();  /* visits=1 */
    visit_counter();  /* visits=2 */
    visit_counter();  /* visits=3 */

    return 0;
}
```

### 전역 변수의 위험성

```text
공용 게시판은 누구나 수정할 수 있어서 관리가 어렵다.

직원A가 "점수=100"으로 수정
직원B가 "점수=50"으로 다시 수정
나중에 점수가 왜 50인지 추적하기 어려움
```

가능하면 지역 변수를 사용하고, 전역 변수는 꼭 필요한 경우에만 쓴다.

---

## 6. 마지막 정리

전역 변수는 공용 게시판처럼 모든 함수에서 접근 가능하고, 프로그램 내내 유지된다.

지역 변수는 개인 수첩처럼 해당 함수에서만 사용하고, 함수가 끝나면 사라진다.

같은 이름이 겹치면 가까운(안쪽) 변수가 우선이다.

`static` 지역 변수는 개인 수첩이지만 오래 살아남는 특수한 수첩이다.

전역 변수는 많을수록 코드 관리가 어려워진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 전역 변수와 지역 변수",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
