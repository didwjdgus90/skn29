# 제목
[자료구조] Heap 자료구조

# 링크
<https://velog.io/@heejeong2993/Heap-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0>

# 본문

## Heap(힙)

힙의 자료구조는 완전이진트리의 일종으로, 특정 규칙을 만족하는 트리 구조이다. 주로 우선순위큐로 사용된다.

## 힙의 특징

1. 완전 이진 트리
   - 완전 이진 트리는 트리의 마지막 레벨을 제외하고, 모든 레벨에 노드가 꽉 차 있는 트리이다.

2. 힙의 성질
   - 힙은 각 노드가 부모 노드와 자식 노드 간의 크기 관계에 따라 구분됨
   - 최소 힙(Min heap) : 부모 노드의 값이 자식 노드의 값보다 작거나 같은 힙이다. 루트 노드가 가장 작은 값을 가지고 있다.
   - 최대 힙(Max heap) : 부모 노드의 값이 자식 노드의 값보다 크거나 같은 힙이다. 루트 노드가 가장 큰 값을 가지고 있다.

## 힙의 기본 연산

1. 삽입(insert)
   - 힙에 원소를 삽입할 때, 힙의 마지막에 추가되고, 이후 부모 노드와 비교하여 힙의 성질을 만족할 때까지 "상향 조정" 한다.
   - 시간 복잡도 O(log n)

2. 삭제(remove)
   - 힙에서 루트 노드를 제거한다 → 최소값 or 최대값
   - 루트 노드를 제거한 뒤, 마지막 노드를 루트 자리에 두고 하향 조정을 통해 힙의 성질을 유지한다.
   - 시간 복잡도 O(log n)

## 최소힙 (Python)

파이썬 heapq은 최소힙 모듈을 제공한다.

```python
import heapq

# 힙 생성
heap = []

# 값 삽입
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)

# 최소값 추출
min_value = heapq.heappop(heap)
print(min_value)  # 3이 출력됨
```

## 최대힙 (Python)

음수를 이용하여 최대힙을 구현한다.

```python
import heapq

# 최대 힙을 구현하려면 음수로 삽입
max_heap = []

heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)

# 최대값 추출
max_value = -heapq.heappop(max_heap)
print(max_value)  # 8이 출력됨
```

## 힙의 시간 복잡도

| 연산 | 시간 복잡도 |
|------|-----------|
| 삽입 | O(log n) |
| 삭제 | O(log n) |
| 최소값/최대값 확인 | O(1) |

## 힙의 삽입과 삭제 예제 (최대힙)

### 시작 상태

```
    20
   /  \
  10   15
 /  \
8    5
```

### 25 삽입

트리의 맨 끝에 삽입됨

```
    20
   /  \
  10   15
 /  \   /
8    5 25
```

부모 노드 15와 비교하여 자리 바꿈

```
    20
   /  \
  10   25
 /  \   /
8    5 15
```

부모 노드 20과 비교하여 자리 바꿈

```
    25
   /  \
  10   20
 /  \   /
8    5 15
```

### 루트(25) 삭제

25가 삭제되고, 마지막 노드 15가 루트로 옴

```
    15
   /  \
  10   20
 /  \
8    5
```

자식 노드인 10과 20 비교 후, 20과 자리 바꿈

```
    20
   /  \
  10   15
 /  \
8    5
```

이후, 더 이상 비교할 자식 노드가 없어서 멈추게 됨.

# 메타데이터
```json
{
  "category": "자료구조",
  "algorithm": "힙",
  "source_type": "blog",
  "style": [
    "easy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "python",
  "source": "velog.io/@heejeong2993"
}
```
