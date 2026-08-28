# 제목
[이분탐색] Lower Bound & Upper Bound - Python

# 링크
<https://12bme.tistory.com/120>

# 본문

## 기본 이분탐색의 한계

일반 이분탐색은 "정확히 일치하는 값"을 찾습니다.
값이 없거나 중복된 값이 여러 개면 어떻게 될까요?

```
[1, 3, 5, 7, 7]에서 7을 찾을 때
→ 두 개의 7 중 어느 위치를 반환해야 할까?
→ 6을 찾으면? → 없으므로 탐색 실패!
```

이런 상황을 처리하기 위해 Lower Bound와 Upper Bound가 등장합니다.

---

## Lower Bound — "k 이상인 값이 처음 나타나는 위치"

> 📦 비유: 번호표를 뽑는 줄에서 "7번 이상인 사람 중 가장 앞에 있는 사람의 위치"

```
배열: [1, 3, 5, 7, 7]  (인덱스 0~4)
k = 7 → lower_bound = 3  (첫 번째 7의 위치)
k = 6 → lower_bound = 3  (6 이상인 첫 번째 값인 7의 위치)
k = 8 → lower_bound = 5  (모든 값이 k보다 작으면 n 반환)
```

### 일반 이분탐색 vs Lower Bound 차이

| 조건 | 일반 이분탐색 | Lower Bound |
|---|---|---|
| `arr[mid] == k` | 탐색 종료, mid 반환 | `e = mid` (더 왼쪽에 같은 값이 있을 수 있으므로 계속) |
| `arr[mid] > k` | `e = mid - 1` | `e = mid` |
| `arr[mid] < k` | `s = mid + 1` | `s = mid + 1` |

핵심 차이: **`arr[mid] >= k`이면 `e = mid`** (같아도 왼쪽을 더 탐색)

### 코드

```python
def lower_bound(arr, k):
    s, e = 0, len(arr)  # e를 n으로 잡아야 "없으면 n 반환" 가능
    while s < e:
        mid = (s + e) // 2
        if arr[mid] < k:
            s = mid + 1   # k보다 작으면 오른쪽 탐색
        else:
            e = mid        # k 이상이면 e를 mid로 (같아도 왼쪽 더 탐색)
    return e               # s == e가 되는 지점이 lower bound

# 예시
arr = [1, 3, 5, 7, 7]
print(lower_bound(arr, 7))  # 3 (첫 번째 7의 인덱스)
print(lower_bound(arr, 6))  # 3 (6 이상인 첫 값 7의 인덱스)
print(lower_bound(arr, 8))  # 5 (없으면 배열 길이)
```

### 탐색 과정 추적

```
arr = [1, 3, 5, 7, 7], k = 7
s=0, e=5

1회: mid=2, arr[2]=5 < 7  → s=3
2회: mid=3, arr[3]=7 >= 7 → e=3
s==e → 종료, return 3  ✅
```

---

## Upper Bound — "k를 초과하는 값이 처음 나타나는 위치"

> 📦 비유: "7번보다 큰 번호를 가진 사람 중 가장 앞에 있는 사람의 위치"

```
배열: [1, 3, 5, 7, 7]  (인덱스 0~4)
k = 7 → upper_bound = 5  (7을 초과하는 값이 없으므로 n)
k = 6 → upper_bound = 3  (6을 초과하는 첫 번째 값 7의 위치)
k = 3 → upper_bound = 2  (3을 초과하는 첫 번째 값 5의 위치)
```

### Lower Bound vs Upper Bound 비교

| 조건 | Lower Bound | Upper Bound |
|---|---|---|
| `arr[mid] < k` | `s = mid + 1` | `s = mid + 1` |
| `arr[mid] == k` | `e = mid` ← 같으면 왼쪽 | `s = mid + 1` ← 같으면 오른쪽 |
| `arr[mid] > k` | `e = mid` | `e = mid` |

핵심 차이: **`arr[mid] <= k`이면 `s = mid + 1`** (같아도 오른쪽 탐색)

### 코드

```python
def upper_bound(arr, k):
    s, e = 0, len(arr)
    while s < e:
        mid = (s + e) // 2
        if arr[mid] <= k:
            s = mid + 1   # k 이하면 오른쪽 탐색 (같아도 오른쪽!)
        else:
            e = mid        # k 초과면 e를 mid로
    return e

# 예시
arr = [1, 3, 5, 7, 7]
print(upper_bound(arr, 7))  # 5 (7 초과 값 없음 → 배열 길이)
print(upper_bound(arr, 6))  # 3 (6 초과 첫 값 7의 인덱스)
print(upper_bound(arr, 3))  # 2 (3 초과 첫 값 5의 인덱스)
```

---

## 활용: 중복 원소 개수 세기

```python
# lower_bound ~ upper_bound 사이의 범위 = 해당 값의 개수
arr = [1, 3, 5, 7, 7, 7, 9]
k = 7
count = upper_bound(arr, k) - lower_bound(arr, k)
print(count)  # 6 - 3 = 3 (7이 3개)
```

## Python bisect 모듈

직접 구현 대신 표준 라이브러리를 쓸 수도 있습니다.

```python
from bisect import bisect_left, bisect_right

arr = [1, 3, 5, 7, 7]
print(bisect_left(arr, 7))   # 3  ← lower_bound
print(bisect_right(arr, 7))  # 5  ← upper_bound
```

---

## 세 가지 비교 정리

```
배열: [1, 3, 5, 7, 7],  k = 7

이분탐색:   값이 정확히 있으면 그 인덱스 반환, 없으면 -1
lower_bound: 3  (7 이상인 첫 위치)
upper_bound: 5  (7 초과인 첫 위치)
```

# 메타데이터
```json
{
  "category": "탐색",
  "algorithm": "이분탐색",
  "source_type": "blog",
  "style": ["easy", "analogy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python",
  "source": "12bme.tistory.com"
}
```
