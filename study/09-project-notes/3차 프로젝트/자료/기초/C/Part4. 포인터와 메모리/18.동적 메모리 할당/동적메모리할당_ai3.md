# 제목
[C/Cpp 기초] 동적 메모리 할당

# 본문

## 1. 한 줄 요약

동적 메모리 할당은 런타임에 힙 allocator를 통해 요청 크기의 연속 메모리 블록을 획득하고, 명시적 해제로 수명을 관리하는 메커니즘이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

스택 기반 자동 저장 기간 변수는 컴파일 타임에 크기가 결정되어야 하고, 함수 리턴 시 소멸한다.

동적 할당은 런타임 크기 결정과 함수 경계를 초월하는 객체 수명을 가능케 한다.

- 크기가 런타임에 결정되는 자료구조 (동적 배열, 링크드 리스트, 트리)
- 대용량 데이터 (스택 크기는 수 MB로 제한됨)
- 함수 리턴 후에도 유효한 객체

---

## 3. 핵심 아이디어

### 힙 Allocator 동작 원리

glibc의 `malloc`은 `ptmalloc2` 알고리즘을 사용한다. free list(해제된 블록들의 연결 리스트)를 관리하며, 요청 크기에 맞는 블록을 반환한다.

```text
malloc(n) 내부:
1. free list에서 n 이상 크기 블록 탐색
2. 없으면 sbrk()/mmap()으로 OS에서 메모리 요청
3. 블록 헤더(크기, 사용 여부)와 함께 반환

free(p) 내부:
1. p의 헤더에서 블록 크기 확인
2. 블록을 free list에 반환
3. 인접 블록과 병합(coalescing)
```

### 메모리 문제 유형

| 문제 | 설명 | 결과 |
|---|---|---|
| 메모리 누수 | free 누락 | 메모리 고갈 |
| 댕글링 포인터 | free 후 접근 | UB, 크래시 |
| 이중 해제 | 같은 포인터 free 2회 | 힙 손상 |
| 버퍼 오버플로우 | 할당 크기 초과 쓰기 | 인접 블록 손상 |
| 미초기화 읽기 | malloc 후 초기화 없이 읽기 | UB |

---

## 4. 동작 과정 살펴보기

### 단편화 (Fragmentation)

```text
할당/해제 반복 후:
[FREE:10][USED:5][FREE:10][USED:5][FREE:10]

총 free 공간: 30바이트
but malloc(25) → 실패! (연속 공간 없음)
→ 외부 단편화(external fragmentation)
```

### realloc의 동작

```c
arr = realloc(arr, new_size);
```

1. 현재 블록 뒤에 연속 공간이 있으면 그 자리에서 확장
2. 없으면 새 위치에 할당 + 기존 내용 복사 + 기존 블록 해제

`realloc` 실패 시 원본은 그대로이므로, 반환값을 별도 포인터에 받아야 한다.

```c
/* 위험: 실패 시 원본 포인터 유실 */
arr = realloc(arr, new_size);  /* 실패 시 arr = NULL, 원본 주소 유실 */

/* 안전 */
void *tmp = realloc(arr, new_size);
if (tmp) arr = tmp;
else { free(arr); arr = NULL; }
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 동적 배열 구조체 (벡터) */
typedef struct {
    int *data;
    size_t size;
    size_t capacity;
} DynArray;

DynArray *dynarray_create(size_t initial_capacity) {
    DynArray *da = malloc(sizeof(DynArray));
    if (!da) return NULL;
    da->data = malloc(initial_capacity * sizeof(int));
    if (!da->data) { free(da); return NULL; }
    da->size = 0;
    da->capacity = initial_capacity;
    return da;
}

int dynarray_push(DynArray *da, int val) {
    if (da->size == da->capacity) {
        size_t new_cap = da->capacity * 2;
        void *tmp = realloc(da->data, new_cap * sizeof(int));
        if (!tmp) return -1;
        da->data = tmp;
        da->capacity = new_cap;
    }
    da->data[da->size++] = val;
    return 0;
}

void dynarray_free(DynArray *da) {
    if (da) {
        free(da->data);
        free(da);
    }
}

int main() {
    DynArray *arr = dynarray_create(4);
    if (!arr) { perror("생성 실패"); return 1; }

    for (int i = 0; i < 10; i++) {
        if (dynarray_push(arr, i * i) != 0) {
            fprintf(stderr, "push 실패\n");
            dynarray_free(arr);
            return 1;
        }
    }

    printf("크기: %zu, 용량: %zu\n", arr->size, arr->capacity);
    for (size_t i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");

    dynarray_free(arr);

    return 0;
}
```

### Valgrind를 이용한 메모리 검사

```bash
# Linux에서 메모리 누수 검사
valgrind --leak-check=full ./program
```

---

## 6. 마지막 정리

동적 할당은 힙 allocator를 통해 런타임 크기 결정과 함수 수명을 초월하는 객체를 제공한다.

`realloc` 실패 처리 시 원본 포인터를 별도 변수에 받아야 한다.

메모리 누수, 댕글링 포인터, 이중 해제, 버퍼 오버플로우는 모두 심각한 버그이다.

Valgrind, AddressSanitizer(`-fsanitize=address`) 등 도구로 메모리 오류를 탐지한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 동적 메모리 할당",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
