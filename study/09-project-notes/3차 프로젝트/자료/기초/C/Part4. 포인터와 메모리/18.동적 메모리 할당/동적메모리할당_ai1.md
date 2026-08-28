# 제목
[C/Cpp 기초] 동적 메모리 할당

# 본문

## 1. 한 줄 요약

동적 메모리 할당은 프로그램 실행 중에 필요한 만큼 메모리를 요청하고, 사용 후 반납하는 방법이다. `malloc`, `calloc`, `realloc`, `free` 함수를 사용한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

배열 크기를 컴파일 타임에 결정해야 하는 제약을 극복한다.

```c
/* 문제: 크기를 미리 모를 때 */
int n;
scanf("%d", &n);
int arr[n];  /* C99 VLA: 스택, 큰 크기면 위험 */

/* 해결: 동적 할당 */
int *arr = malloc(n * sizeof(int));  /* 힙에서 할당 */
```

---

## 3. 핵심 아이디어

### 주요 함수

**malloc** - 메모리 할당 (초기화 없음)

```c
void *malloc(size_t size);

int *arr = malloc(5 * sizeof(int));
if (arr == NULL) {
    /* 할당 실패 처리 */
}
```

**calloc** - 메모리 할당 + 0으로 초기화

```c
void *calloc(size_t count, size_t size);

int *arr = calloc(5, sizeof(int));  /* 0으로 초기화 */
```

**realloc** - 이미 할당된 메모리 크기 변경

```c
void *realloc(void *ptr, size_t new_size);

arr = realloc(arr, 10 * sizeof(int));  /* 크기 확장 */
```

**free** - 메모리 반납

```c
void free(void *ptr);

free(arr);
arr = NULL;  /* 댕글링 포인터 방지 */
```

---

## 4. 동작 과정 살펴보기

### 메모리 관리 흐름

```text
1. malloc(20) 요청
   → 힙에서 20바이트 공간 확보
   → 그 주소 반환

2. 데이터 사용
   arr[0] = 1; arr[1] = 2; ...

3. free(arr) 호출
   → 힙에 20바이트 공간 반납
   → arr은 여전히 이전 주소를 가리키고 있음 (댕글링)

4. arr = NULL
   → 안전하게 NULL로 설정
```

### NULL 체크 필수

```c
int *p = malloc(100 * sizeof(int));
if (p == NULL) {
    printf("메모리 할당 실패!\n");
    return -1;
}
/* 이후 p 사용 */
```

malloc은 실패 시 NULL을 반환한다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int n;
    printf("배열 크기 입력: ");
    scanf("%d", &n);

    /* malloc으로 동적 배열 */
    int *arr = malloc(n * sizeof(int));
    if (arr == NULL) {
        printf("메모리 할당 실패\n");
        return 1;
    }

    /* 값 입력 */
    for (int i = 0; i < n; i++) {
        arr[i] = i * 10;
    }

    /* 출력 */
    printf("배열: ");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    /* realloc으로 크기 확장 */
    int new_n = n * 2;
    int *new_arr = realloc(arr, new_n * sizeof(int));
    if (new_arr == NULL) {
        printf("realloc 실패\n");
        free(arr);
        return 1;
    }
    arr = new_arr;

    /* 추가된 공간에 값 설정 */
    for (int i = n; i < new_n; i++) {
        arr[i] = i * 10;
    }

    printf("확장된 배열: ");
    for (int i = 0; i < new_n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    /* 반드시 free 호출 */
    free(arr);
    arr = NULL;  /* 댕글링 포인터 방지 */

    /* calloc 예제 */
    double *matrix = calloc(3 * 3, sizeof(double));
    if (matrix) {
        /* 0으로 초기화된 3x3 행렬 */
        printf("\n3x3 영행렬 (calloc):\n");
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                printf("%.1f ", matrix[i * 3 + j]);
            }
            printf("\n");
        }
        free(matrix);
    }

    return 0;
}
```

### 2차원 동적 배열

```c
int rows = 3, cols = 4;

/* 방법 1: 포인터 배열 */
int **mat = malloc(rows * sizeof(int *));
for (int i = 0; i < rows; i++) {
    mat[i] = malloc(cols * sizeof(int));
}

/* 사용 */
mat[1][2] = 10;

/* 해제 (역순) */
for (int i = 0; i < rows; i++) {
    free(mat[i]);
}
free(mat);
```

---

## 6. 마지막 정리

`malloc`/`calloc`으로 힙에 메모리를 요청하고, `free`로 반납한다.

`malloc` 실패 시 NULL을 반환하므로 반드시 NULL 체크를 해야 한다.

`calloc`은 할당과 동시에 0으로 초기화한다.

`realloc`으로 이미 할당된 메모리 크기를 변경할 수 있다.

`free` 후 포인터를 NULL로 설정하면 댕글링 포인터를 방지할 수 있다.

메모리 누수(free 안 함)와 이중 해제(double free)를 주의해야 한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 동적 메모리 할당",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
