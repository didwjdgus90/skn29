# 제목
[C/Cpp 기초] 정렬 함수 qsort

# 본문

## 1. 한 줄 요약

`qsort`는 비교 함수 포인터를 매개변수로 받는 제네릭 정렬 함수로, 내부적으로 퀵소트(혹은 하이브리드 알고리즘)를 사용하며 평균 O(n log n)이나 최악 O(n²)을 보장하지 않는 구현도 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

타입 독립적인 제네릭 정렬 인터페이스를 제공한다. `void *` 포인터와 함수 포인터를 통해 C에서 제네릭 프로그래밍을 구현한 고전적 사례이다.

---

## 3. 핵심 아이디어

### 오버플로우 없는 비교 함수

```c
/* 위험: 오버플로우 가능 */
int cmp_wrong(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
    /* INT_MIN - 1 = overflow! */
}

/* 안전: 3-방향 비교 */
int cmp_safe(const void *a, const void *b) {
    int ia = *(const int *)a;
    int ib = *(const int *)b;
    return (ia > ib) - (ia < ib);
}
```

### 다중 키 정렬

```c
int cmp_multi(const void *a, const void *b) {
    const Student *sa = a;
    const Student *sb = b;
    /* 1차: 학년 오름차순 */
    if (sa->grade != sb->grade)
        return (sa->grade > sb->grade) - (sa->grade < sb->grade);
    /* 2차: 점수 내림차순 */
    return (sb->score > sa->score) - (sb->score < sa->score);
}
```

### `bsearch` (이진 탐색)

qsort로 정렬 후 `bsearch`로 O(log n) 탐색.

```c
void *bsearch(const void *key, const void *base,
              size_t nmemb, size_t size,
              int (*compar)(const void *, const void *));
```

---

## 4. 동작 과정 살펴보기

### qsort 내부 구현 (glibc)

glibc의 qsort는 퀵소트와 삽입 정렬을 결합한 인트로소트(introsort) 변형이다. 재귀 깊이가 임계값을 초과하면 힙소트로 전환하여 최악 케이스를 완화한다.

```text
배열 크기 ≤ 임계값: 삽입 정렬 (캐시 친화적)
재귀 깊이 초과: 힙소트 (O(n log n) 보장)
일반 케이스: 퀵소트 (평균 O(n log n))
```

### 안정 정렬(stable sort)

qsort는 안정 정렬을 보장하지 않는다. 같은 키를 가진 원소의 원래 순서가 보존되지 않을 수 있다. 안정 정렬이 필요하면 인덱스를 보조 키로 추가한다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[20];
    int grade;
    int score;
} Student;

/* 다중 키 정렬: 학년 오름차순, 점수 내림차순 */
int cmp_student(const void *a, const void *b) {
    const Student *sa = a;
    const Student *sb = b;
    if (sa->grade != sb->grade)
        return (sa->grade > sb->grade) - (sa->grade < sb->grade);
    return (sb->score > sa->score) - (sb->score < sa->score);
}

/* 안정 정렬 래퍼: 원래 인덱스를 보조 키로 사용 */
typedef struct { int val; int orig_idx; } Indexed;

int cmp_indexed(const void *a, const void *b) {
    const Indexed *ia = a;
    const Indexed *ib = b;
    if (ia->val != ib->val)
        return (ia->val > ib->val) - (ia->val < ib->val);
    return ia->orig_idx - ib->orig_idx;  /* 안정성 보장 */
}

int main() {
    /* 다중 키 정렬 */
    Student students[] = {
        {"Alice",   2, 90}, {"Bob",     1, 85},
        {"Charlie", 2, 78}, {"Diana",   1, 92},
        {"Eve",     3, 88}, {"Frank",   2, 90}
    };
    int n = sizeof(students) / sizeof(students[0]);
    qsort(students, n, sizeof(Student), cmp_student);
    printf("학년순, 점수 내림차순:\n");
    for (int i = 0; i < n; i++) {
        printf("  %d학년 %s (%d점)\n",
               students[i].grade, students[i].name, students[i].score);
    }

    /* 안정 정렬 */
    int vals[] = {3, 1, 4, 1, 5, 9, 2, 6};
    int m = sizeof(vals) / sizeof(vals[0]);
    Indexed indexed[8];
    for (int i = 0; i < m; i++) { indexed[i].val = vals[i]; indexed[i].orig_idx = i; }
    qsort(indexed, m, sizeof(Indexed), cmp_indexed);
    printf("\n안정 정렬 결과 (같은 값이면 원래 순서 보존):\n");
    for (int i = 0; i < m; i++) {
        printf("  [orig_idx=%d] %d\n", indexed[i].orig_idx, indexed[i].val);
    }

    /* qsort + bsearch */
    int arr[] = {5, 2, 8, 1, 9, 3, 7, 4, 6};
    int an = sizeof(arr) / sizeof(arr[0]);
    qsort(arr, an, sizeof(int), (int(*)(const void*,const void*))((void*)cmp_indexed));

    /* bsearch 사용 (qsort 후 가능) */
    /* (간단한 버전) */
    int key = 7;
    int *found = NULL;
    for (int i = 0; i < an; i++) {
        if (arr[i] == key) { found = &arr[i]; break; }
    }
    printf("\n%d %s\n", key, found ? "발견" : "없음");

    return 0;
}
```

---

## 6. 마지막 정리

비교 함수에서 `a - b` 방식은 정수 오버플로우가 발생할 수 있으므로 `(a > b) - (a < b)` 패턴이 안전하다.

qsort는 안정 정렬을 보장하지 않는다. 원래 인덱스를 보조 키로 추가하면 안정 정렬을 구현할 수 있다.

glibc의 qsort는 인트로소트 변형으로 최악 케이스 성능을 완화한다.

qsort로 정렬 후 `bsearch`를 사용하면 O(log n) 이진 탐색이 가능하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 정렬 함수 qsort",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 5,
  "target_level": "high",
  "language": "c"
}
```
