# 제목
[C/Cpp 기초] 정렬 함수 qsort

# 본문

## 1. 한 줄 요약

`qsort`는 만능 정렬 직원이다. 어떤 물건이든 "이 기준으로 정렬해줘"라는 규칙(비교 함수)만 주면 알아서 정렬해준다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

도서관 사서에게 책을 정렬해달라고 할 때, 책을 모두 설명하지 않아도 된다. 단지 "어느 책이 앞에 오는지" 판단 기준만 알려주면 된다.

```text
qsort = 만능 사서
비교 함수 = 정렬 기준 ("제목순", "출판일순", "가격순" 등)

사서(qsort)는 기준(비교 함수)만 알면 어떤 책(어떤 타입)이든 정렬 가능!
```

---

## 3. 핵심 아이디어

### qsort에게 전달하는 4가지 정보

```text
qsort(
    배열 시작,        ← "여기 있는 물건들을"
    물건 개수,        ← "이 개수만큼"
    물건 하나의 크기,  ← "한 칸이 이만큼이니까"
    비교 함수         ← "이 기준으로 정렬해줘"
);
```

### 비교 함수: 판사 역할

```text
비교 함수(a, b):
  → 음수 반환: "a가 b보다 앞에 와야 해요" (오름차순이면 a < b)
  → 0 반환:    "둘이 같아요"
  → 양수 반환: "b가 a보다 앞에 와야 해요" (오름차순이면 a > b)
```

---

## 4. 동작 과정 살펴보기

### 오름차순 vs 내림차순

```text
오름차순 (작은 게 앞): "더 작은 게 앞이면 음수 반환"
  → return a - b;
  → 5, 2 비교: 5 - 2 = 3 (양수) → 2가 앞으로

내림차순 (큰 게 앞): "더 큰 게 앞이면 음수 반환"
  → return b - a;
  → 5, 2 비교: 2 - 5 = -3 (음수) → 5가 앞에 유지
```

### 성적표 정렬 비유

```text
선생님(qsort): "학생들 줄 세워!"
규칙(비교 함수): "점수 높은 순"

선생님은 학생 두 명씩 비교해가며 줄을 세운다.
선생님은 비교 규칙만 알면 어떤 기준으로든 줄 세우기 가능.
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 오름차순 판사 */
int judge_ascending(const void *a, const void *b) {
    int x = *(int *)a;
    int y = *(int *)b;
    if (x < y) return -1;  /* x가 앞 */
    if (x > y) return  1;  /* y가 앞 */
    return 0;              /* 같음 */
}

/* 내림차순 판사 */
int judge_descending(const void *a, const void *b) {
    return judge_ascending(b, a);  /* a, b 뒤집기 */
}

/* 학생 성적 판사 */
typedef struct { char name[20]; int score; } Student;

int judge_score(const void *a, const void *b) {
    int sa = ((Student *)a)->score;
    int sb = ((Student *)b)->score;
    return sb - sa;  /* 점수 높은 순 (내림차순) */
}

int main() {
    /* 숫자 줄 세우기 */
    int nums[] = {5, 2, 8, 1, 9, 3};
    int n = 6;

    printf("원본: ");
    for (int i = 0; i < n; i++) printf("%d ", nums[i]);
    printf("\n");

    qsort(nums, n, sizeof(int), judge_ascending);
    printf("오름차순: ");
    for (int i = 0; i < n; i++) printf("%d ", nums[i]);
    printf("\n");

    qsort(nums, n, sizeof(int), judge_descending);
    printf("내림차순: ");
    for (int i = 0; i < n; i++) printf("%d ", nums[i]);
    printf("\n");

    /* 성적 줄 세우기 */
    Student class[] = {
        {"철수", 75},
        {"영희", 92},
        {"민수", 88},
        {"지현", 65}
    };
    int cn = 4;

    qsort(class, cn, sizeof(Student), judge_score);

    printf("\n성적 순위:\n");
    for (int i = 0; i < cn; i++) {
        printf("  %d위: %s (%d점)\n", i+1, class[i].name, class[i].score);
    }

    return 0;
}
```

---

## 6. 마지막 정리

`qsort`는 비교 함수만 주면 어떤 타입의 배열도 정렬하는 만능 사서다.

비교 함수는 두 원소를 받아 "앞에 오면 음수, 같으면 0, 뒤에 오면 양수"를 반환한다.

오름차순은 `a - b`, 내림차순은 `b - a` 패턴이 기본이다.

구조체 정렬 시 원하는 멤버만 선택해서 비교하면 된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 정렬 함수 qsort",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
