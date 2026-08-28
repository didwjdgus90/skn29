# 제목
[C/Cpp 기초] 반복문

# 본문

## 1. 한 줄 요약

반복문은 같은 코드를 여러 번 실행하는 제어 구조이다. `for`, `while`, `do-while` 세 가지가 있다.

C에서 반복문을 이해하면 반복적인 작업을 간결하게 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

1부터 100까지 더하는 코드를 조건문 없이 작성하면 100줄이 필요하다.

```c
int sum = 1 + 2 + 3 + 4 + ... /* 이렇게는 불가능 */
```

반복문을 쓰면 단 몇 줄로 해결된다.

```c
int sum = 0;
for (int i = 1; i <= 100; i++) {
    sum += i;
}
```

---

## 3. 핵심 아이디어

### for 반복문

횟수가 정해진 반복에 적합하다.

```c
for (초기화; 조건; 증감) {
    /* 반복할 코드 */
}
```

```c
for (int i = 0; i < 5; i++) {
    printf("%d\n", i);  /* 0, 1, 2, 3, 4 출력 */
}
```

### while 반복문

조건이 참인 동안 반복한다. 횟수를 미리 모를 때 사용한다.

```c
while (조건) {
    /* 반복할 코드 */
}
```

```c
int n = 1;
while (n <= 5) {
    printf("%d\n", n);
    n++;
}
```

### do-while 반복문

코드를 최소 한 번 실행한 후 조건을 확인한다.

```c
do {
    /* 반복할 코드 (최소 1회 실행) */
} while (조건);
```

---

## 4. 동작 과정 살펴보기

### for 반복문 단계별 동작

```text
for (int i = 0; i < 3; i++) {

Step 1: i = 0           (초기화, 한 번만 실행)
Step 2: 0 < 3 → 참     (조건 검사)
Step 3: 코드 실행
Step 4: i++  → i = 1   (증감)

Step 5: 1 < 3 → 참     (조건 검사)
Step 6: 코드 실행
Step 7: i++  → i = 2

Step 8: 2 < 3 → 참
Step 9: 코드 실행
Step 10: i++ → i = 3

Step 11: 3 < 3 → 거짓  (반복 종료)
```

### break와 continue

```c
for (int i = 0; i < 10; i++) {
    if (i == 5) break;     /* 5에서 반복 완전 종료 */
    if (i % 2 == 0) continue;  /* 짝수는 건너뜀 */
    printf("%d\n", i);     /* 1, 3 출력 */
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* for: 1~10 합계 */
    int sum = 0;
    for (int i = 1; i <= 10; i++) {
        sum += i;
    }
    printf("1~10 합: %d\n", sum);  /* 55 */

    /* while: 입력받아서 합산 */
    int total = 0, num;
    printf("숫자를 입력하세요 (0 입력 시 종료):\n");
    scanf("%d", &num);
    while (num != 0) {
        total += num;
        scanf("%d", &num);
    }
    printf("합계: %d\n", total);

    /* do-while: 메뉴 한 번은 보여주기 */
    int choice;
    do {
        printf("1. 시작  2. 종료\n");
        printf("선택: ");
        scanf("%d", &choice);
    } while (choice != 1 && choice != 2);

    /* 중첩 for: 구구단 */
    for (int i = 2; i <= 3; i++) {
        for (int j = 1; j <= 9; j++) {
            printf("%d x %d = %d\n", i, j, i * j);
        }
    }

    return 0;
}
```

### 무한 반복문

```c
/* 의도적인 무한 루프 */
while (1) {
    /* 서버 프로그램, 게임 루프 등 */
    if (should_exit) break;
}

/* for로도 무한 루프 가능 */
for (;;) {
    /* 조건 없이 무한 반복 */
}
```

---

## 6. 마지막 정리

`for`는 횟수가 정해진 반복에, `while`은 조건 기반 반복에, `do-while`은 최소 1회 실행이 필요할 때 사용한다.

`break`는 반복문을 즉시 탈출하고, `continue`는 현재 반복을 건너뛰고 다음 반복을 실행한다.

무한 루프는 `while(1)` 또는 `for(;;)`로 만든다.

중첩 반복문에서 `break`는 가장 안쪽 반복문만 탈출한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 반복문",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
