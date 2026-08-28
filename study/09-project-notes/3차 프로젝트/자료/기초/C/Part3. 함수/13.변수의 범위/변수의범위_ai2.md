# 제목
[C/Cpp 기초] 변수의 범위

# 본문

## 1. 한 줄 요약

변수의 범위는 방(블록)과 같다. 방 안에서 만든 물건은 그 방 안에서만 쓸 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

큰 도서관을 상상해보자.

1층, 2층, 3층 각 층에 "참고 자료실"이 있다.

각 층의 "참고 자료실"은 독립적이다. 1층에서 자료를 빌려도 3층에는 영향을 주지 않는다.

```text
1층 참고 자료실: (int x = 10)
2층 참고 자료실: (int x = 20) ← 1층 x와 별개
3층 참고 자료실: (int x = 30) ← 완전히 독립
```

이처럼 각 블록(방)의 변수들은 독립적으로 존재한다.

---

## 3. 핵심 아이디어

### 블록 = 독립된 방

중괄호 `{}`가 방의 벽이다. 방 안에서 만든 변수는 방 밖에서 볼 수 없다.

```text
방 바깥
┌─────────────────┐
│  방 안            │
│  int x = 10;    │
│  (x는 방 안에만) │
└─────────────────┘
방 밖에서 x 사용 → 없는 변수!
```

### 방 안의 방 (중첩 스코프)

작은 방이 큰 방 안에 있다면, 작은 방에서는 큰 방의 것도 볼 수 있다.

```text
큰 방 (함수)
  int outer = 1;
  ┌──────────────┐
  │ 작은 방(for) │
  │   int i = 0; │
  │ outer 보임   │  ← 바깥 것도 접근 가능
  └──────────────┘
  i 보이지 않음    ← 작은 방 것은 밖에서 못 봄
```

### 이름이 같으면? (변수 숨김)

작은 방에서 큰 방과 같은 이름을 쓰면, 작은 방의 것이 우선이다.

```text
큰 방: x = 1
  ┌────────┐
  │ 작은 방 │
  │ x = 99  │  ← 이 x가 우선 (큰 방 x를 가림)
  └────────┘
큰 방 x = 1 (원래대로)
```

---

## 4. 동작 과정 살펴보기

### 방 단계별 접근

```c
int a = 1;        /* 가장 큰 방 (전역) */

void func() {     /* 함수 방 */
    int b = 2;

    for (int i = 0; i < 3; i++) {  /* for 방 */
        int c = 3;
        /* 여기서 볼 수 있는 것: a, b, i, c */
    }
    /* 여기서 볼 수 있는 것: a, b */
}
/* 여기서 볼 수 있는 것: a */
```

바깥 방으로 갈수록 볼 수 있는 것이 줄어든다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 가장 바깥 방: 전역 */
int building_name = 42;  /* 모든 방에서 접근 가능 */

void room1() {
    int furniture = 10;  /* room1 방 소유물 */
    printf("room1: building=%d, furniture=%d\n",
           building_name, furniture);

    /* 방 안의 방 */
    {
        int item = 99;
        printf("inner: building=%d, furniture=%d, item=%d\n",
               building_name, furniture, item);
    }
    /* item은 여기서 없음 */
}

void room2() {
    int furniture = 20;  /* room1의 furniture와 별개! */
    printf("room2: furniture=%d\n", furniture);
}

int main() {
    room1();
    room2();

    /* for 루프 방 */
    for (int i = 0; i < 3; i++) {
        int temp = i * 10;
        printf("loop: i=%d, temp=%d\n", i, temp);
    }
    /* i, temp는 여기서 없음 */

    printf("building_name: %d\n", building_name);
    return 0;
}
```

### static - 방이 없어져도 살아남는 물건

```c
void counter() {
    static int count = 0;  /* 처음 한 번만 초기화 */
    count++;
    printf("호출 횟수: %d\n", count);
}

counter();  /* 1 */
counter();  /* 2 */
counter();  /* 3 */
```

`static` 변수는 함수 방이 닫혀도 사라지지 않고 계속 유지된다.

---

## 6. 마지막 정리

변수의 범위는 방(블록)과 같다. 방 안 변수는 방 밖에서 볼 수 없다.

안쪽 방에서는 바깥 방의 변수도 접근할 수 있다.

같은 이름이 겹치면 가장 안쪽(가까운) 방의 변수가 우선이다.

`static` 변수는 스코프는 함수 안이지만 프로그램 내내 살아있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 변수의 범위",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
