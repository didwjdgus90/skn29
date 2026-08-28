# 제목
[자료구조] 힙 (Heap)

# 링크
<https://gmlwjd9405.github.io/2018/05/10/data-structure-heap.html>

# 본문

## 힙이란?
힙은 완전 이진 트리를 기반으로 한 자료구조로,
부모 노드가 항상 자식 노드보다 크거나(Max Heap) 작은(Min Heap) 성질을 가진다.

우선순위 큐를 구현하는 데 주로 사용된다.

<IMAGE>Max Heap과 Min Heap 구조 그림</IMAGE>

Max Heap: 부모 >= 자식 (루트가 최댓값)
Min Heap: 부모 <= 자식 (루트가 최솟값)

## 힙의 시간복잡도
삽입(insert): O(log N)
삭제(delete): O(log N)
최솟값/최댓값 조회: O(1)

이진 탐색 트리(BST)와 다르게 힙은 완전 이진 트리 구조를 유지하므로
항상 O(log N)을 보장한다.

## 활용 예시
- 우선순위 큐
- 힙 정렬 (Heap Sort)
- 다익스트라 알고리즘
- 프림 알고리즘
- 중앙값 유지 문제

## 구현 코드 (Python)
Python의 heapq 모듈은 기본적으로 Min Heap이다.
Max Heap이 필요하면 값에 음수를 취해서 넣는다.

```python
import heapq

# Min Heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

print(heap)                  # [1, 3, 7, 5]
print(heapq.heappop(heap))   # 1 (최솟값)
print(heapq.heappop(heap))   # 3

# Max Heap (음수 변환 트릭)
max_heap = []
for val in [5, 3, 7, 1]:
    heapq.heappush(max_heap, -val)

print(-heapq.heappop(max_heap))  # 7 (최댓값)
```

## 예제: K번째 큰 수
N개의 수 중에서 K번째로 큰 수를 구하라.
Min Heap으로 크기 K를 유지하면 힙의 루트가 K번째로 큰 수가 된다.

```python
import heapq

def kth_largest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # 가장 작은 것 제거
    return heap[0]  # 힙의 루트 = K번째로 큰 수

print(kth_largest([3,2,1,5,6,4], 2))  # 출력: 5
```

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
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "mid",
  "language": "python"
}
```