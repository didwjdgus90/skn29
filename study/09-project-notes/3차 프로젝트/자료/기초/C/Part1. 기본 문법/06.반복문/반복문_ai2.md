# 제목
[C/Cpp 기초] 반복문

# 본문

## 1. 한 줄 요약

반복문은 공장의 컨베이어 벨트이다. 같은 작업을 지치지 않고 정해진 횟수만큼 반복한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

공장에서 상품 100개에 스티커를 붙이는 작업을 상상해보자.

사람이 직접 하면 같은 동작을 100번 반복해야 한다.

컨베이어 벨트(반복문)가 있다면 한 번 설정해두고 자동으로 100번 처리한다.

```text
컨베이어 벨트 설정:
  시작: 첫 번째 상품
  조건: 100개가 될 때까지
  작업: 스티커 붙이기
  끝나면: 다음 상품으로 이동
```

```c
for (int i = 0; i < 100; i++) {
    attach_sticker();
}
```

---

## 3. 핵심 아이디어

### for - 횟수가 정해진 컨베이어 벨트

처음부터 몇 번 돌릴지 알 때 사용한다.

```text
for (시작, 멈출 조건, 한 번 돌고 나서 할 일) {
    반복할 작업
}

for (i = 0, i < 5, i++) {
  i=0: 작업 → i++
  i=1: 작업 → i++
  i=2: 작업 → i++
  i=3: 작업 → i++
  i=4: 작업 → i++
  i=5: 조건 실패 → 벨트 멈춤
}
```

### while - 신호등 반복

초록불인 동안(조건이 참인 동안) 계속 달린다.

```text
while (초록불) {
    달린다
}
빨간불이 되면 멈춤
```

### do-while - 맛보기 시식

음식을 한 입 먹어보고, 맛있으면 계속 먹는다. 일단 한 번은 무조건 먹어본다.

```text
do {
    한 입 먹어보기
} while (맛있다);
```

---

## 4. 동작 과정 살펴보기

### 컨베이어 벨트 동작 순서

```text
for (i = 1; i <= 3; i++) {
    printf(i);
}

1단계: i = 1          (벨트 시작)
2단계: 1 <= 3? → 참  (계속 진행)
3단계: printf(1)      (작업)
4단계: i++ → i = 2   (벨트 이동)

5단계: 2 <= 3? → 참
6단계: printf(2)
7단계: i++ → i = 3

8단계: 3 <= 3? → 참
9단계: printf(3)
10단계: i++ → i = 4

11단계: 4 <= 3? → 거짓 (벨트 멈춤)

출력: 1, 2, 3
```

### break와 continue - 비상 정지 버튼과 건너뜀 버튼

```text
break:    비상 정지 버튼 (즉시 반복 종료)
continue: 다음 번으로 건너뜀 버튼 (현재 것만 건너뜀)
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 1부터 5까지 출력 (for 컨베이어 벨트) */
    printf("for 반복:\n");
    for (int i = 1; i <= 5; i++) {
        printf("%d ", i);
    }
    printf("\n");

    /* 같은 작업을 while로 */
    printf("while 반복:\n");
    int i = 1;
    while (i <= 5) {
        printf("%d ", i);
        i++;
    }
    printf("\n");

    /* do-while: 최소 한 번 실행 */
    printf("\n메뉴 선택:\n");
    int choice;
    do {
        printf("1. 계속  2. 종료: ");
        scanf("%d", &choice);
        if (choice == 1) printf("계속합니다!\n");
    } while (choice == 1);
    printf("종료합니다.\n");

    /* break: 비상 정지 */
    printf("\nbreak 예시:\n");
    for (int j = 0; j < 10; j++) {
        if (j == 5) break;  /* 5에서 멈춤 */
        printf("%d ", j);
    }
    printf("\n");

    /* continue: 건너뜀 */
    printf("\ncontinue 예시 (홀수만):\n");
    for (int k = 0; k < 10; k++) {
        if (k % 2 == 0) continue;  /* 짝수 건너뜀 */
        printf("%d ", k);
    }
    printf("\n");

    return 0;
}
```

### 구구단 - 중첩 컨베이어 벨트

```text
바깥 벨트: 단(2~9)
안쪽 벨트: 곱할 수(1~9)

바깥 한 번 돌면 → 안쪽이 9번 돌아감
```

```c
for (int i = 2; i <= 9; i++) {      /* 바깥 벨트 */
    for (int j = 1; j <= 9; j++) {  /* 안쪽 벨트 */
        printf("%d×%d=%d\t", i, j, i*j);
    }
    printf("\n");
}
```

---

## 6. 마지막 정리

반복문은 컨베이어 벨트처럼 같은 작업을 자동으로 반복한다.

`for`는 횟수가 정해진 반복, `while`은 조건이 참인 동안, `do-while`은 최소 1번 실행 보장.

`break`는 비상 정지(반복 종료), `continue`는 현재 것만 건너뜀.

반복문 안에 반복문을 넣으면(중첩) 구구단처럼 2차원적 반복이 가능하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 반복문",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
