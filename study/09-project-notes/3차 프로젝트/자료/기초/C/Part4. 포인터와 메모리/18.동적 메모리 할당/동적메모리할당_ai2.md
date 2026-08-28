# 제목
[C/Cpp 기초] 동적 메모리 할당

# 본문

## 1. 한 줄 요약

동적 메모리 할당은 필요할 때 공유 창고에서 빌리고, 다 쓰면 반납하는 것이다. 반납 안 하면 창고가 꽉 찬다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

식당에서 손님이 몇 명 올지 미리 알 수 없다.

미리 100명분 자리를 만들어두면 낭비이고, 10명분만 만들면 부족할 수 있다.

동적 메모리 할당은 손님이 오는 만큼 그때그때 자리를 만드는 것이다.

```text
일반 배열: "10명 자리 준비해!"  ← 코드 작성 시 결정
동적 할당: "몇 명이요? 그만큼 바로 준비할게요!"  ← 실행 중 결정
```

---

## 3. 핵심 아이디어

### 창고(힙) 빌리기: malloc

```text
malloc(크기)
  → "힙 창고에서 이만큼의 공간 빌려줘!"
  → 빌린 공간의 주소 반환

int *arr = malloc(5 * sizeof(int));
         = malloc(20)  ← 20바이트 빌림
         = 빌린 공간의 주소
```

### 0으로 깨끗하게 빌리기: calloc

```text
calloc(개수, 크기)
  → malloc과 같지만 내용물을 모두 0으로 깨끗하게 만들어줌

int *arr = calloc(5, sizeof(int));
         = 5개의 int, 모두 0으로 초기화
```

### 창고 반납: free

```text
free(arr)
  → "이 주소의 공간을 창고에 돌려줄게요"
  → 반납 후 arr은 여전히 그 주소를 가리킴 (위험!)

arr = NULL  ← 반납 후 NULL로 정리 (안전)
```

---

## 4. 동작 과정 살펴보기

### 빌리고 쓰고 반납하기

```text
1단계: 빌리기
  int *space = malloc(5 * 4);  → 힙에 20바이트 빌림
  
2단계: 사용하기
  space[0] = 10;
  space[1] = 20;
  ...
  
3단계: 반납하기
  free(space);  → 힙에 20바이트 돌려줌
  space = NULL;  → 안전하게 정리
```

### 반납 안 하면? (메모리 누수)

```text
void 함수_반복_호출() {
    int *p = malloc(1000);
    /* free(p) 안 함 */
}

이 함수를 1000번 호출 = 1,000,000바이트 (1MB) 창고에 남겨둠
프로그램이 길어질수록 창고가 꽉 참 → 메모리 부족!
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    /* 손님 수에 따라 자리 만들기 */
    int guests;
    printf("손님 수를 입력하세요: ");
    scanf("%d", &guests);

    /* 창고에서 손님 수만큼 빌리기 */
    int *seats = malloc(guests * sizeof(int));

    /* 빌리기 실패하면? */
    if (seats == NULL) {
        printf("자리를 만들 수 없어요!\n");
        return 1;
    }

    /* 좌석 번호 부여 */
    for (int i = 0; i < guests; i++) {
        seats[i] = i + 1;
    }

    /* 확인 */
    printf("좌석 번호: ");
    for (int i = 0; i < guests; i++) {
        printf("%d ", seats[i]);
    }
    printf("\n");

    /* 손님이 더 왔어요! (realloc) */
    int more = guests + 3;
    int *bigger_seats = realloc(seats, more * sizeof(int));
    if (bigger_seats == NULL) {
        printf("확장 실패!\n");
        free(seats);
        return 1;
    }
    seats = bigger_seats;

    for (int i = guests; i < more; i++) {
        seats[i] = i + 1;
    }

    printf("추가 후 좌석: ");
    for (int i = 0; i < more; i++) {
        printf("%d ", seats[i]);
    }
    printf("\n");

    /* 반납! */
    free(seats);
    seats = NULL;

    printf("창고 반납 완료!\n");
    return 0;
}
```

### 빌리기(malloc) vs 청결하게 빌리기(calloc)

```c
/* malloc: 이전 쓰레기값이 있을 수 있음 */
int *dirty = malloc(5 * sizeof(int));
printf("%d\n", dirty[0]);  /* 예측 불가능한 값! */

/* calloc: 모두 0으로 깨끗함 */
int *clean = calloc(5, sizeof(int));
printf("%d\n", clean[0]);  /* 0 */

free(dirty);
free(clean);
```

---

## 6. 마지막 정리

동적 메모리 할당은 실행 중에 필요한 만큼 힙에서 메모리를 빌리는 것이다.

`malloc`은 빌리기, `calloc`은 깨끗하게 빌리기, `realloc`은 크기 조절, `free`는 반납.

빌린 메모리를 반납(free)하지 않으면 메모리 누수가 발생한다.

반납 후에는 포인터를 NULL로 설정해서 실수로 사용하는 것을 막는다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 동적 메모리 할당",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
