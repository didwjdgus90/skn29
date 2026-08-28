# 제목
[C/Cpp 기초] 정렬 함수 qsort

# 본문

## 1. 한 줄 요약

`qsort`는 `<stdlib.h>`가 제공하는 범용 정렬 함수로, 사용자가 제공한 비교 함수를 통해 어떤 타입의 배열도 정렬할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

정렬 알고리즘을 직접 구현하지 않고 표준 라이브러리를 활용한다. 정수 배열뿐만 아니라 문자열, 구조체 등 어떤 타입도 정렬 가능하다.

```c
/* 직접 구현 (버블정렬) */
for (int i = 0; i < n-1; i++)
    for (int j = 0; j < n-i-1; j++)
        if (arr[j] > arr[j+1]) swap(&arr[j], &arr[j+1]);

/* qsort 사용 */
qsort(arr, n, sizeof(int), compare_int);
```

---

## 3. 핵심 아이디어

### qsort 시그니처

```c
void qsort(void *base,          /* 배열 시작 주소 */
           size_t nmemb,        /* 원소 개수 */
           size_t size,         /* 원소 하나의 크기 */
           int (*compar)(const void *, const void *));
                              /* 비교 함수 포인터 */
```

### 비교 함수 작성 규칙

```c
int compare(const void *a, const void *b) {
    /* 반환값: */
    /* 음수: a가 b보다 앞 */
    /* 0:    같음 */
    /* 양수: a가 b보다 뒤 */
}
```

### 정수 비교 함수

```c
int compare_int(const void *a, const void *b) {
    int ia = *(int *)a;
    int ib = *(int *)b;
    return (ia > ib) - (ia < ib);  /* 안전한 뺄셈 대체 */
    /* 또는: return ia - ib; (오버플로우 주의) */
}
```

---

## 4. 동작 과정 살펴보기

### 내림차순 정렬

```c
int compare_desc(const void *a, const void *b) {
    int ia = *(int *)a;
    int ib = *(int *)b;
    return ib - ia;  /* a와 b 반대로 */
}
```

### 문자열 정렬

```c
int compare_str(const void *a, const void *b) {
    return strcmp(*(char **)a, *(char **)b);
}

char *words[] = {"banana", "apple", "cherry"};
qsort(words, 3, sizeof(char *), compare_str);
/* 결과: apple, banana, cherry */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 정수 오름차순 비교 */
int cmp_int_asc(const void *a, const void *b) {
    int ia = *(int *)a;
    int ib = *(int *)b;
    return (ia > ib) - (ia < ib);
}

/* 정수 내림차순 비교 */
int cmp_int_desc(const void *a, const void *b) {
    return cmp_int_asc(b, a);  /* 인자 반전 */
}

/* 문자열 비교 */
int cmp_str(const void *a, const void *b) {
    return strcmp(*(const char **)a, *(const char **)b);
}

/* 구조체 정렬 */
typedef struct {
    char name[20];
    int score;
} Student;

int cmp_student_by_score(const void *a, const void *b) {
    const Student *sa = (const Student *)a;
    const Student *sb = (const Student *)b;
    return sb->score - sa->score;  /* 점수 내림차순 */
}

void print_int_arr(int *arr, int n) {
    for (int i = 0; i < n; i++) printf("%d ", arr[i]);
    printf("\n");
}

int main() {
    /* 정수 정렬 */
    int nums[] = {5, 2, 8, 1, 9, 3};
    int n = sizeof(nums) / sizeof(nums[0]);

    qsort(nums, n, sizeof(int), cmp_int_asc);
    printf("오름차순: "); print_int_arr(nums, n);

    qsort(nums, n, sizeof(int), cmp_int_desc);
    printf("내림차순: "); print_int_arr(nums, n);

    /* 문자열 정렬 */
    const char *words[] = {"banana", "apple", "cherry", "date"};
    int wn = sizeof(words) / sizeof(words[0]);
    qsort(words, wn, sizeof(char *), cmp_str);
    printf("\n문자열 정렬: ");
    for (int i = 0; i < wn; i++) printf("%s ", words[i]);
    printf("\n");

    /* 구조체 정렬 */
    Student students[] = {
        {"홍길동", 85},
        {"이순신", 92},
        {"유관순", 78},
        {"안중근", 96}
    };
    int sn = sizeof(students) / sizeof(students[0]);
    qsort(students, sn, sizeof(Student), cmp_student_by_score);

    printf("\n점수 내림차순:\n");
    for (int i = 0; i < sn; i++) {
        printf("%d등. %s (%d점)\n", i+1, students[i].name, students[i].score);
    }

    return 0;
}
```

---

## 6. 마지막 정리

`qsort`는 4개의 인자를 받는다: 배열 주소, 원소 개수, 원소 크기, 비교 함수.

비교 함수는 `const void *` 두 인자를 받아 정수를 반환하며, 음수/0/양수로 순서를 결정한다.

정수 비교 시 오버플로우를 피하려면 `a - b` 대신 `(a > b) - (a < b)` 패턴을 사용한다.

문자열 배열은 `char *` 배열이므로 비교 함수에서 `*(char **)` 로 캐스팅한다.

구조체 정렬은 구조체 포인터로 캐스팅해서 원하는 멤버로 비교한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 정렬 함수 qsort",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
