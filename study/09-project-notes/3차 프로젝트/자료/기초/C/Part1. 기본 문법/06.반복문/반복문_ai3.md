# 제목
[C/Cpp 기초] 반복문

# 본문

## 1. 한 줄 요약

반복문은 제어 흐름 그래프에서 후위 에지(back edge)를 형성하는 루프 구조로, 조건이 만족되는 동안 기본 블록을 반복 실행한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

선형 제어 흐름만으로는 임의 크기의 데이터를 처리하거나, 수렴 조건이 런타임에 결정되는 알고리즘을 구현할 수 없다.

반복문은 동일한 코드 세그먼트를 반복 실행하면서 루프 변수나 외부 상태를 조건으로 종료를 결정한다.

```c
/* O(n) 선형 탐색 — 배열 크기 n이 컴파일 타임에 미결정 */
int linear_search(int *arr, int n, int target) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == target) return i;
    }
    return -1;
}
```

---

## 3. 핵심 아이디어

### 루프의 구조적 분류

**for 루프** - 카운터 기반 루프 (definite iteration)

```c
for (init; condition; update) body;
```

의미론적으로 다음과 동치이다.

```c
{
    init;
    while (condition) {
        body;
        update;
    }
}
```

**while 루프** - 조건 기반 루프 (pre-test loop)

진입 전 조건을 검사하므로 0회 실행이 가능하다.

**do-while 루프** - 후위 조건 루프 (post-test loop)

본문을 먼저 실행하므로 최소 1회 실행을 보장한다.

### 루프 불변 조건 (Loop Invariant)

올바른 루프 작성의 핵심은 불변 조건(loop invariant)을 유지하는 것이다.

```c
/* 최솟값 탐색: 불변 조건 = arr[min_idx]는 arr[0..i-1] 중 최솟값 */
int min_idx = 0;
for (int i = 1; i < n; i++) {
    if (arr[i] < arr[min_idx]) {
        min_idx = i;  /* 불변 조건 갱신 */
    }
}
/* 종료 후: arr[min_idx]는 전체 최솟값 */
```

---

## 4. 동작 과정 살펴보기

### 루프 언롤링 (Loop Unrolling)

컴파일러 최적화 중 루프 언롤링은 반복 횟수를 줄여 분기 오버헤드와 루프 제어 비용을 감소시킨다.

```c
/* 원본 */
for (int i = 0; i < 4; i++) arr[i] *= 2;

/* 언롤링 후 (개념적) */
arr[0] *= 2;
arr[1] *= 2;
arr[2] *= 2;
arr[3] *= 2;
```

GCC `-O2` 이상에서 자동으로 적용된다.

### break와 continue의 의미론

- `break`: 가장 가까운 루프(또는 switch)의 다음 문으로 무조건 분기 (goto와 동치)
- `continue`: 루프의 증감 표현식(for) 또는 조건 검사(while)로 분기

중첩 루프에서 `break`는 한 단계만 탈출한다. 다중 탈출에는 goto 또는 플래그 변수가 필요하다.

```c
/* 다중 루프 탈출: goto 활용 */
for (int i = 0; i < M; i++) {
    for (int j = 0; j < N; j++) {
        if (found) goto done;
    }
}
done:
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <time.h>

int main() {
    /* 이진 탐색: O(log n) — while 루프 */
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int n = 8, target = 7;
    int lo = 0, hi = n - 1, mid, result = -1;

    while (lo <= hi) {
        mid = lo + (hi - lo) / 2;  /* 오버플로우 방지 */
        if (arr[mid] == target) {
            result = mid;
            break;
        } else if (arr[mid] < target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    printf("탐색 결과: 인덱스 %d\n", result);

    /* 루프 성능 측정 */
    clock_t start = clock();
    long long sum = 0;
    for (long long i = 0; i < 1000000LL; i++) {
        sum += i;
    }
    clock_t end = clock();
    printf("합계: %lld\n", sum);
    printf("소요 시간: %f초\n", (double)(end - start) / CLOCKS_PER_SEC);

    return 0;
}
```

### 무한 루프와 서버 패턴

```c
/* 이벤트 루프 패턴 */
while (1) {
    Event e = wait_for_event();
    if (e.type == EXIT) break;
    handle_event(e);
}
```

`for(;;)`와 `while(1)` 모두 무한 루프를 만든다. GCC는 둘 다 동일한 코드를 생성한다.

---

## 6. 마지막 정리

`for`는 카운터 기반 루프, `while`은 조건 선검사(0회 가능), `do-while`은 조건 후검사(최소 1회)이다.

루프 불변 조건을 유지하며 작성하면 정확성을 보장할 수 있다.

컴파일러는 루프 언롤링, SIMD 벡터화 등으로 루프를 최적화한다.

다중 루프 탈출이 필요하면 `goto`(단, 해당 범위 내) 또는 플래그 변수를 사용한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 반복문",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
