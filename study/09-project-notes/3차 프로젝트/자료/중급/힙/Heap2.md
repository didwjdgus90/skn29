# 제목
[자료구조] 힙(Heap)이란?

# 링크
<https://gbdai.tistory.com/17>

# 본문

## 힙(Heap)이란?

힙(Heap)은 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 자료구조로, 완전 이진 트리(Complete binary tree)의 형태를 가진다.

이러한 힙은 힙 속성을 만족하는데, 힙 속성이란,

- 최대 힙 속성(max heap property) : 부모 노드의 키 값은 항상 자식 노드의 키 값보다 크거나 같다.
- 최소 힙 속성(min heap property) : 부모 노드의 키 값은 항상 자식 노드의 키 값보다 작거나 같다.

다음과 같으며, 어떤 힙 속성을 만족하는지에 따라 최대 힙(Max heap)과 최소 힙(Min heap)으로 나뉜다.

## 힙(Heap)의 특징

- 루트 노드(root node)는 항상 최댓값 또는 최솟값을 가진다 (만족하는 힙 속성에 따라)
- 부모-자식 사이의 크기 관계만 존재하며, 왼쪽 자식-오른쪽 자식 간의 크기 관계는 존재하지 않는다
- 완전 이진 트리이기 때문에 트리의 높이를 h라고 하면 h = log₂n 이다.
- 힙 정렬, 우선순위 큐, 다익스트라 알고리즘 등에 응용된다.

## 힙(Heap)의 시간 복잡도

- 최댓값/최솟값 참조: O(1)
- 원소 삽입 또는 삭제: O(log N)

## 힙(Heap)과 이진 탐색 트리 비교

|                    | 힙             | 이진 탐색 트리                       |
| ------------------ | ------------- | -------------------------------- |
| 트리 형태              | 완전 이진 트리      | 이진 트리                           |
| 원소의 중복 여부          | 중복 가능         | 중복 불가능                          |
| 원소의 정렬 여부          | 정렬 X          | 정렬 O                            |
| 원소 탐색 시간 복잡도       | O(n) 순차 탐색    | O(log N) 이진 탐색                  |
| 원소의 삽입 및 삭제 시간 복잡도 | O(log N)      | O(log N) / O(n) (skewed tree)   |
| 최댓값/최솟값 참조 시간 복잡도  | O(1)          | O(log N) / O(n) (skewed tree)   |

## 힙(Heap)의 동작

지금부터 다루는 모든 내용은 최대 힙을 기준으로 한다.

<IMAGE>초기 최대 힙 그림 (루트 15, 자식 10, 7, ...)</IMAGE>

## 힙(Heap)의 삽입

힙은 완전 이진 트리이다. 따라서 노드가 삽입될 때마다 왼쪽 최하단부터 채워진다.

삽입 과정:
1. 새 데이터를 왼쪽 최하단에 삽입한다.
2. 삽입된 값과 부모 노드를 비교한다.
3. 삽입된 값이 부모 노드보다 크면 자리를 맞바꾼다.
4. 더 이상 바꿀 필요가 없을 때까지 2~3을 반복한다.

예시: 위의 힙에 20을 삽입하면,
- 왼쪽 최하단에 20 삽입
- 20의 부모 노드 7과 비교 → 20이 더 크므로 위치 교환
- 다음 부모 노드 10과 비교 → 20이 더 크므로 교환
- 다음 부모 노드 15와 비교 → 20이 더 크므로 교환
- 20이 루트 노드가 됨

<IMAGE>20 삽입 후 최대 힙 최종 형태</IMAGE>

## 힙(Heap)의 삭제

힙을 통해 최댓값(혹은 최솟값)을 얻고 싶을 때 최상단 루트 노드의 값을 참조하고 삭제한다.

삭제 과정:
1. 루트 노드를 삭제한다.
2. 최하단부 가장 왼쪽의 노드를 루트 노드로 올린다.
3. 루트 노드의 값이 자식 노드보다 작을 경우, 자식 노드들 중 가장 큰 값과 위치를 바꾼다.
4. 더 이상 바꿀 필요가 없을 때까지 반복한다.

<IMAGE>루트 삭제 후 힙 재정렬 과정</IMAGE>

## 힙(Heap)의 구현 (Python)

힙은 완전 이진 트리이기에 배열로 쉽게 구현할 수 있다.
편의를 위해 root node의 index는 1로 지정한다. index 0에는 None값을 넣는다.

부모-자식 인덱스 관계:
- 인덱스 i의 부모: i // 2
- 인덱스 i의 왼쪽 자식: i * 2
- 인덱스 i의 오른쪽 자식: i * 2 + 1

```python
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        # 리스트 인덱스 1부터 시작하도록
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        # 삽입된 값의 인덱스가 1보다 작으면(root node이면) 바꿀 필요 없음
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        # 삽입된 값이 parent node보다 크면 True 반환
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            # 삽입된 값과 parent node를 교환
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = \
                self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = \
                        self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = \
                            self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = \
                            self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx

        return returned_data
```

## Python heapq 모듈 활용 (실전)

직접 구현 대신 Python 내장 heapq 모듈을 코딩테스트에서 주로 사용한다.
heapq는 기본적으로 Min Heap이다.

```python
import heapq

# Min Heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

print(heapq.heappop(heap))  # 1 (최솟값)
print(heapq.heappop(heap))  # 3

# Max Heap (음수 변환 트릭)
max_heap = []
for val in [5, 3, 7, 1]:
    heapq.heappush(max_heap, -val)

print(-heapq.heappop(max_heap))  # 7 (최댓값)
```

# 메타데이터
```json
{
  "category": "자료구조",
  "algorithm": "힙",
  "source_type": "blog",
  "style": [
    "easy",
    "analogy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python",
  "source": "gbdai.tistory.com"
}
```
