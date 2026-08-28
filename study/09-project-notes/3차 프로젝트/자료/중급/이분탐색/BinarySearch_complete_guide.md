# 제목
[알고리즘] 이분탐색(Binary Search) 완전 정복 — 기본 탐색, Parametric Search, 실전 문제 3선

# 본문

## 한줄 요약

이분탐색은 "정렬된 데이터에서 탐색 범위를 절반씩 줄여가며 원하는 값을 O(log N)에 찾는 기법"이다.

---

## 왜 필요한가

사전에서 "Python"이라는 단어를 찾는다고 하자. 첫 페이지부터 한 장씩 넘기면 수만 페이지를 봐야 한다. 하지만 사전 중간을 펼쳐 "M"이 보이면 뒷쪽으로, "R"이 보이면 앞쪽으로 범위를 좁혀간다. 이것이 이분탐색이다.

- 순차 탐색: O(N) — 데이터 100만 개면 100만 번 비교
- 이분 탐색: O(log N) — 데이터 100만 개면 **20번**이면 충분

단, 전제 조건이 있다: **데이터가 정렬되어 있어야 한다.**

---

## 핵심 개념

### 1. 기본 이분탐색

정렬된 배열에서 특정 값의 위치를 찾는다.

동작:
1. `lo = 0`, `hi = N - 1`로 범위 설정
2. `mid = (lo + hi) // 2` 계산
3. `arr[mid] == target` → 찾음!
4. `arr[mid] < target` → 왼쪽 절반 버림 → `lo = mid + 1`
5. `arr[mid] > target` → 오른쪽 절반 버림 → `hi = mid - 1`
6. `lo > hi`가 되면 → 값 없음

### 2. Lower Bound / Upper Bound

정확히 일치하는 값이 아니라 **경계를 찾는** 변형이다.

| 개념 | 의미 | 조건 |
|------|------|------|
| Lower Bound | target **이상**인 첫 위치 | `arr[mid] >= target` → hi = mid |
| Upper Bound | target **초과**인 첫 위치 | `arr[mid] > target` → hi = mid |

활용: 특정 값의 개수 = `upper_bound - lower_bound`

### 3. Parametric Search (매개변수 탐색)

**"최적값을 구하라"** 문제를 **"이 값이 가능한가?"** 라는 결정 문제로 변환한 뒤, 가능/불가능의 경계를 이분탐색으로 찾는 기법.

패턴:
```
정답이 될 수 있는 범위: [lo, hi]
while lo <= hi:
    mid를 "정답 후보"로 시도
    if 가능하다면:
        결과 갱신, 더 좋은 답 탐색
    else:
        반대쪽 탐색
```

"최솟값의 최대" 또는 "최댓값의 최소"라는 표현이 나오면 Parametric Search를 떠올리자.

### 4. 시간 복잡도

| 연산 | 복잡도 |
|------|--------|
| 기본 이분탐색 | O(log N) |
| Lower/Upper Bound | O(log N) |
| Parametric Search | O(log(범위) × 판별 비용) |

---

## 동작 흐름

### 기본 이분탐색 예시

```
배열: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target: 23

step 1: lo=0, hi=9, mid=4 → arr[4]=16 < 23 → lo=5
step 2: lo=5, hi=9, mid=7 → arr[7]=56 > 23 → hi=6
step 3: lo=5, hi=6, mid=5 → arr[5]=23 == 23 → 찾음! (인덱스 5)

총 비교 횟수: 3회 (순차탐색이면 6회)
```

### Lower Bound 예시

```
배열: [1, 3, 3, 3, 5, 7]
target: 3 → "3 이상인 첫 위치" = 인덱스 1

step 1: lo=0, hi=6, mid=3 → arr[3]=3 >= 3 → hi=3
step 2: lo=0, hi=3, mid=1 → arr[1]=3 >= 3 → hi=1
step 3: lo=0, hi=1, mid=0 → arr[0]=1 < 3 → lo=1
lo==hi → 결과: 인덱스 1
```

---

## Text Flow Chart

### 기본 이분탐색

```
lo = 0, hi = N-1
        ↓
   ┌─ lo > hi? ──→ YES → 값 없음 (-1)
   │       ↓ NO
   │  mid = (lo + hi) // 2
   │       ↓
   │  arr[mid] == target? → YES → mid 반환
   │       ↓ NO
   │  arr[mid] < target?
   │    → YES → lo = mid + 1
   │    → NO  → hi = mid - 1
   └───────┘ (반복)
```

### Parametric Search

```
lo = 최솟값, hi = 최댓값
answer = 0
        ↓
   ┌─ lo > hi? ──→ YES → answer 반환
   │       ↓ NO
   │  mid = (lo + hi) // 2
   │       ↓
   │  is_feasible(mid)?
   │    → YES → answer = mid, lo = mid + 1 (더 큰 값 탐색)
   │    → NO  → hi = mid - 1
   └───────┘ (반복)
```

---

## 기본 코드 템플릿

### Python

```python
def binary_find(sorted_arr, target):
    """정렬된 배열에서 target의 인덱스를 반환, 없으면 -1"""
    lo, hi = 0, len(sorted_arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if sorted_arr[mid] == target:
            return mid
        elif sorted_arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1


def lower_bound(sorted_arr, target):
    """target 이상인 첫 인덱스를 반환"""
    lo, hi = 0, len(sorted_arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] >= target:
            hi = mid
        else:
            lo = mid + 1

    return lo


def upper_bound(sorted_arr, target):
    """target 초과인 첫 인덱스를 반환"""
    lo, hi = 0, len(sorted_arr)

    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_arr[mid] > target:
            hi = mid
        else:
            lo = mid + 1

    return lo


# --- 실행 ---
nums = [1, 3, 3, 3, 5, 7, 9]
print(binary_find(nums, 5))       # 4
print(lower_bound(nums, 3))       # 1
print(upper_bound(nums, 3))       # 4
print(upper_bound(nums, 3) - lower_bound(nums, 3))  # 3 (3의 개수)
```

**코드 흐름 설명**

1. 기본 탐색: `lo <= hi` 동안 반복. mid 값과 target을 비교해 범위를 절반씩 좁힌다.
2. Lower Bound: `hi = len(arr)`로 시작하고 `lo < hi` 동안 반복. `>=`이면 hi를 당긴다.
3. Upper Bound: `>`이면 hi를 당긴다. Lower와의 차이는 등호 포함 여부 뿐이다.
4. 값의 개수 = `upper_bound - lower_bound`.

### Java

```java
public class BinarySearchTemplate {
    public static int binaryFind(int[] arr, int target) {
        int lo = 0, hi = arr.length - 1;
        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] == target) return mid;
            else if (arr[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    public static int lowerBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] >= target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    public static int upperBound(int[] arr, int target) {
        int lo = 0, hi = arr.length;
        while (lo < hi) {
            int mid = (lo + hi) / 2;
            if (arr[mid] > target) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }
}
```

---

## 실전 문제 풀이

---

### 문제 1: 나무 자르기 (Parametric Search — "나무 자르기" 유형)

#### 핵심 개념

**"N개의 나무를 높이 H로 잘랐을 때, 잘린 부분의 합이 M 이상이 되는 H의 최댓값을 구하라"**

왜 Parametric Search인가?
- H를 0부터 최대 높이까지 하나씩 시도하면 O(최대높이 × N)이 된다.
- H가 커질수록 잘리는 양은 줄어든다 → **단조 감소** → 이분탐색 가능
- "가능한 H 중 최댓값" = **결정 문제로 변환**: "H일 때 M미터 이상 얻을 수 있는가?"

핵심 판별 함수:
```
is_enough(H) = 모든 나무에서 (나무높이 - H) 중 양수만 합산 >= M
```

lo=0, hi=가장 높은 나무. 가능하면 lo를 올리고(더 큰 H 시도), 불가능하면 hi를 내린다.

#### 풀이 전략

```
[전체 흐름]

lo = 0, hi = max(나무 높이), answer = 0
           ↓
      ┌─ lo > hi? ──→ YES → answer 반환
      │       ↓ NO
      │  mid = (lo + hi) // 2
      │       ↓
      │  잘린 총량 >= M?
      │    → YES → answer = mid, lo = mid + 1
      │    → NO  → hi = mid - 1
      └───────┘ (반복)
```

#### 소스코드

**Python**

```python
def max_cut_height(trees, need):
    """나무들을 높이 H로 잘라 need 이상 얻을 수 있는 H의 최댓값"""
    lo, hi = 0, max(trees)
    best = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        # 판별: mid 높이로 잘랐을 때 총 수확량
        harvest = sum(t - mid for t in trees if t > mid)

        if harvest >= need:
            best = mid          # 가능 → 더 높이 시도
            lo = mid + 1
        else:
            hi = mid - 1        # 불가능 → 더 낮게

    return best

# --- 실행 ---
print(max_cut_height([20, 15, 10, 17], 7))  # 15
```

**Java**

```java
public class TreeCutter {
    public static int maxCutHeight(int[] trees, int need) {
        int lo = 0, hi = 0;
        for (int t : trees) hi = Math.max(hi, t);
        int best = 0;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            long harvest = 0;
            for (int t : trees)
                if (t > mid) harvest += (t - mid);

            if (harvest >= need) {
                best = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return best;
    }

    public static void main(String[] args) {
        int[] trees = {20, 15, 10, 17};
        System.out.println(maxCutHeight(trees, 7)); // 15
    }
}
```

**코드 흐름 설명**

| 단계 | lo | hi | mid | 수확량 | 판정 |
|------|----|----|-----|--------|------|
| 1 | 0 | 20 | 10 | 5+5+0+7=17 ≥ 7 | ✅ best=10, lo=11 |
| 2 | 11 | 20 | 15 | 5+0+0+2=7 ≥ 7 | ✅ best=15, lo=16 |
| 3 | 16 | 20 | 18 | 2+0+0+0=2 < 7 | ❌ hi=17 |
| 4 | 16 | 17 | 16 | 4+0+0+1=5 < 7 | ❌ hi=15 |
| 종료 | 16 > 15 | | | | **답: 15** |

---

### 문제 2: 심사 시간 최소화 (Parametric Search — "입국심사" 유형)

#### 핵심 개념

**"N개의 심사대가 각각 다른 시간이 걸릴 때, M명을 모두 심사하는 데 필요한 최소 시간을 구하라"**

왜 Parametric Search인가?
- 시간 T를 정하면, 각 심사대가 T 동안 처리할 수 있는 인원수는 `T // 심사시간`
- T가 길수록 처리 가능 인원이 늘어난다 → **단조 증가** → 이분탐색 가능
- "M명 이상 처리 가능한 최소 T" = 결정 문제로 변환

핵심 판별 함수:
```
can_finish(T) = sum(T // 각 심사대 시간) >= M
```

lo=1, hi=가장 느린 심사대 × M. 가능하면 hi를 줄이고(더 짧은 시간 시도), 불가능하면 lo를 올린다.

#### 풀이 전략

```
[전체 흐름]

lo = 1, hi = max(심사시간) × M, answer = hi
           ↓
      ┌─ lo > hi? ──→ YES → answer 반환
      │       ↓ NO
      │  mid = (lo + hi) // 2
      │       ↓
      │  mid 시간 내 처리 가능 인원 >= M?
      │    → YES → answer = mid, hi = mid - 1  (더 짧게)
      │    → NO  → lo = mid + 1
      └───────┘ (반복)
```

#### 소스코드

**Python**

```python
def min_total_time(review_times, people):
    """M명을 모두 심사하는 최소 시간"""
    lo = 1
    hi = max(review_times) * people
    answer = hi

    while lo <= hi:
        mid = (lo + hi) // 2

        # 판별: mid 시간 동안 총 몇 명 처리 가능?
        capacity = sum(mid // t for t in review_times)

        if capacity >= people:
            answer = mid        # 가능 → 더 짧은 시간 시도
            hi = mid - 1
        else:
            lo = mid + 1        # 불가능 → 더 긴 시간 필요

    return answer

# --- 실행 ---
print(min_total_time([7, 10], 6))  # 28
```

**Java**

```java
public class ReviewScheduler {
    public static long minTotalTime(int[] reviewTimes, int people) {
        long lo = 1;
        long hi = 0;
        for (int t : reviewTimes) hi = Math.max(hi, t);
        hi *= people;
        long answer = hi;

        while (lo <= hi) {
            long mid = (lo + hi) / 2;
            long capacity = 0;
            for (int t : reviewTimes) capacity += mid / t;

            if (capacity >= people) {
                answer = mid;
                hi = mid - 1;
            } else {
                lo = mid + 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        int[] times = {7, 10};
        System.out.println(minTotalTime(times, 6)); // 28
    }
}
```

**코드 흐름 설명 (심사대: [7, 10], 인원: 6)**

| 단계 | lo | hi | mid | 7분대 | 10분대 | 합계 | 판정 |
|------|----|----|-----|-------|--------|------|------|
| 1 | 1 | 60 | 30 | 4명 | 3명 | 7 ≥ 6 | ✅ ans=30, hi=29 |
| 2 | 1 | 29 | 15 | 2명 | 1명 | 3 < 6 | ❌ lo=16 |
| 3 | 16 | 29 | 22 | 3명 | 2명 | 5 < 6 | ❌ lo=23 |
| 4 | 23 | 29 | 26 | 3명 | 2명 | 5 < 6 | ❌ lo=27 |
| 5 | 27 | 29 | 28 | 4명 | 2명 | 6 ≥ 6 | ✅ ans=28, hi=27 |
| 6 | 27 | 27 | 27 | 3명 | 2명 | 5 < 6 | ❌ lo=28 |
| 종료 | 28 > 27 | | | | | | **답: 28** |

---

### 문제 3: 공유기 설치 (Parametric Search — "최솟값의 최대" 유형)

#### 핵심 개념

**"N개의 집에 C개의 공유기를 설치할 때, 가장 가까운 두 공유기 사이 거리의 최댓값을 구하라"**

왜 Parametric Search인가?
- "거리 D 이상 간격으로 C개 설치 가능한가?" → 결정 문제
- D가 커지면 설치 가능 개수가 줄어든다 → **단조 감소** → 이분탐색 가능
- "가능한 D 중 최댓값" 탐색

핵심 판별 함수 (그리디):
```
정렬된 집 리스트에서 첫 집에 설치
다음 집부터 순회하며, 마지막 설치 위치에서 D 이상 떨어진 집에 설치
설치 개수 >= C면 가능
```

#### 풀이 전략

```
[전체 흐름]

집 좌표 정렬
lo = 1, hi = max(좌표) - min(좌표), answer = 0
           ↓
      ┌─ lo > hi? ──→ YES → answer 반환
      │       ↓ NO
      │  mid = (lo + hi) // 2  (최소 거리 후보)
      │       ↓
      │  mid 간격으로 C개 설치 가능?
      │    → YES → answer = mid, lo = mid + 1
      │    → NO  → hi = mid - 1
      └───────┘ (반복)
```

#### 소스코드

**Python**

```python
def max_min_gap(houses, routers):
    """공유기 간 최소 거리의 최댓값을 반환"""
    houses.sort()
    lo, hi = 1, houses[-1] - houses[0]
    best = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        # 판별: mid 이상 간격으로 몇 개 설치 가능?
        installed = 1
        last_pos = houses[0]
        for i in range(1, len(houses)):
            if houses[i] - last_pos >= mid:
                installed += 1
                last_pos = houses[i]

        if installed >= routers:
            best = mid
            lo = mid + 1
        else:
            hi = mid - 1

    return best

# --- 실행 ---
print(max_min_gap([1, 2, 8, 4, 9], 3))  # 3
```

**Java**

```java
import java.util.Arrays;

public class RouterPlacer {
    public static int maxMinGap(int[] houses, int routers) {
        Arrays.sort(houses);
        int lo = 1, hi = houses[houses.length - 1] - houses[0];
        int best = 0;

        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            int installed = 1;
            int lastPos = houses[0];

            for (int i = 1; i < houses.length; i++) {
                if (houses[i] - lastPos >= mid) {
                    installed++;
                    lastPos = houses[i];
                }
            }

            if (installed >= routers) {
                best = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return best;
    }

    public static void main(String[] args) {
        int[] houses = {1, 2, 8, 4, 9};
        System.out.println(maxMinGap(houses, 3)); // 3
    }
}
```

**코드 흐름 설명 (집: [1,2,4,8,9] 정렬 후, 공유기 3개)**

| 단계 | lo | hi | mid | 설치 위치 | 개수 | 판정 |
|------|----|----|-----|----------|------|------|
| 1 | 1 | 8 | 4 | 1, 8, (9는 8과 1차이<4) | 2 < 3 | ❌ hi=3 |
| 2 | 1 | 3 | 2 | 1, 4, 8 | 3 ≥ 3 | ✅ best=2, lo=3 |
| 3 | 3 | 3 | 3 | 1, 4, 8 | 3 ≥ 3 | ✅ best=3, lo=4 |
| 종료 | 4 > 3 | | | | | **답: 3** |

---

## 자주 하는 실수

### 1. lo ≤ hi vs lo < hi 혼동

- 값 찾기 (기본 탐색): `while lo <= hi` + `hi = mid - 1`
- 경계 찾기 (Lower/Upper Bound): `while lo < hi` + `hi = mid`

이 두 패턴을 섞으면 무한 루프나 오프바이원(off-by-one) 에러가 발생한다.

### 2. 오버플로우 (mid 계산)

lo와 hi가 매우 클 때 `(lo + hi)`가 int 범위를 초과할 수 있다. Java에서는 `long`을 사용하거나 `lo + (hi - lo) / 2`로 계산한다.

### 3. Parametric Search에서 판별 함수 방향을 잘못 잡는다

- "가능할 때 lo를 올릴지, hi를 내릴지"가 문제마다 다르다.
- **최댓값을 구하면** → 가능할 때 `lo = mid + 1`
- **최솟값을 구하면** → 가능할 때 `hi = mid - 1`

### 4. 탐색 범위 초기값을 잘못 잡는다

입국심사 문제에서 `hi = max(시간) * M`이 아니라 `max(시간)`만 넣으면 답을 놓친다. 범위를 충분히 크게 잡아야 한다.

### 5. 정렬을 안 한다

이분탐색의 전제는 **정렬**이다. 공유기 문제에서 집 좌표를 정렬하지 않으면 그리디 판별이 틀린다.

---

## 언제 사용하면 좋은가

| 신호 | 유형 |
|------|------|
| "정렬된 배열에서 ~를 찾아라" | 기본 이분탐색 |
| "~의 개수를 구하라" (정렬됨) | Lower/Upper Bound |
| "최솟값의 최대" / "최댓값의 최소" | Parametric Search |
| "M개 이상 가능한 최소 시간" | Parametric Search |
| "N개를 잘라서 M개 이상 만들기" | Parametric Search |
| 범위가 10억 이상으로 거대함 | O(log N)이 필요 → 이분탐색 |

---

## 요약 정리

| 항목 | 내용 |
|------|------|
| 전제 조건 | 정렬됨 또는 단조성(monotonic) |
| 기본 탐색 | O(log N), 값의 위치 |
| Lower Bound | target 이상인 첫 위치 |
| Upper Bound | target 초과인 첫 위치 |
| Parametric Search | 결정 문제로 변환 + 이분탐색 |
| lo ≤ hi | 값 찾기용 |
| lo < hi | 경계 찾기용 |
| 판별 함수 | "가능한가?"를 O(N)에 판별 |

---

# 메타데이터
```json
{
  "category": "[기초 알고리즘] 탐색",
  "algorithm": "이분탐색",
  "source_type": "generated",
  "style": ["easy", "code", "analogy", "theory"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "java"
}
```

---

```
변환 검수
- 원문 문장을 그대로 사용하지 않았는가: 예
- 원문 목차 구조를 그대로 따르지 않았는가: 예
- 원문 비유를 그대로 사용하지 않았는가: 예
- 원문 코드의 변수명과 주석을 그대로 사용하지 않았는가: 예
- 원문 이미지를 재사용하지 않았는가: 예
- 개념 설명의 정확성을 유지했는가: 예
- 초급자가 이해할 수 있는 흐름으로 재작성했는가: 예
```
