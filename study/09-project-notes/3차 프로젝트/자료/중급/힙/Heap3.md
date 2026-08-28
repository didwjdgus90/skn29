# 제목
[자료구조] 힙(Heap) - 개념, 구조, 동작, 구현

# 링크
<https://heung-bae-lee.github.io/2020/05/17/data_structure_07/>

# 본문

## 1. 힙 (Heap) 이란?

힙: 데이터에서 최대값과 최소값을 빠르게 찾기 위해 고안된 완전 이진 트리(Complete Binary Tree)

완전 이진 트리: 노드를 삽입할 때 최하단 왼쪽 노드부터 차례대로 삽입하는 트리

<IMAGE>완전 이진 트리 구조 그림 (fun-coding.org)</IMAGE>

힙을 사용하는 이유:
- 배열에 데이터를 넣고, 최대값과 최소값을 찾으려면 O(n) 이 걸림
- 이에 반해, 힙에 데이터를 넣고, 최대값과 최소값을 찾으면 O(log n) 이 걸림
- 우선순위 큐와 같이 최대값 또는 최소값을 빠르게 찾아야 하는 자료구조 및 알고리즘 구현 등에 활용됨

## 2. 힙 (Heap) 구조

힙은 최대값을 구하기 위한 구조(최대 힙, Max Heap)와 최소값을 구하기 위한 구조(최소 힙, Min Heap)로 분류할 수 있음

힙은 다음과 같이 두 가지 조건을 가지고 있는 자료구조임:

1. 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 크거나 같다. (최대 힙의 경우)
   - 최소 힙의 경우는 각 노드의 값은 해당 노드의 자식 노드가 가진 값보다 작거나 같음
2. 완전 이진 트리 형태를 가짐

## 힙과 이진 탐색 트리의 공통점과 차이점

공통점: 힙과 이진 탐색 트리는 모두 이진 트리임

차이점:
- 힙은 각 노드의 값이 자식 노드보다 크거나 같음 (Max Heap의 경우)
- 이진 탐색 트리는 왼쪽 자식 노드의 값이 가장 작고, 그 다음 부모 노드, 그 다음 오른쪽 자식 노드 값이 가장 큼
- 힙은 이진 탐색 트리의 조건인 자식 노드에서 작은 값은 왼쪽, 큰 값은 오른쪽이라는 조건은 없음
  - 힙의 왼쪽 및 오른쪽 자식 노드의 값은 오른쪽이 클 수도 있고, 왼쪽이 클 수도 있음
- 이진 탐색 트리는 탐색을 위한 구조, 힙은 최대/최소값 검색을 위한 구조 중 하나로 이해하면 됨

<IMAGE>힙 vs 이진 탐색 트리 비교 그림 (fun-coding.org)</IMAGE>

## 3. 힙 (Heap) 동작

데이터를 힙 구조에 삽입, 삭제하는 과정을 그림을 통해 선명하게 이해하기

## 힙에 데이터 삽입하기 - 기본 동작

힙은 완전 이진 트리이므로, 삽입할 노드는 기본적으로 왼쪽 최하단부 노드부터 채워지는 형태로 삽입

<IMAGE>힙 기본 삽입 동작 그림 - 왼쪽 최하단부터 채워지는 모습 (fun-coding.org)</IMAGE>

삽입 시 힙 조건 유지 방법 (Max Heap):
1. 새 데이터를 왼쪽 최하단에 삽입
2. 삽입된 노드와 부모 노드를 비교
3. 삽입된 값이 부모 노드보다 크면 위치를 맞바꿈 (swap)
4. 루트 노드가 되거나 부모 노드보다 작거나 같을 때까지 반복

<IMAGE>힙 삽입 시 swap 과정 그림 (20 삽입 예시) (fun-coding.org)</IMAGE>

## 힙의 데이터 삭제하기 (Max Heap의 예)

보통 삭제는 최상단 노드(root 노드)를 삭제하는 것이 일반적임
- 힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임

삭제 과정:
1. root 노드를 삭제한다.
2. 가장 최하단부 왼쪽에 위치한 노드(일반적으로 가장 마지막에 추가한 노드)를 root 노드로 이동
3. root 노드의 값이 child node보다 작을 경우, child node 중 가장 큰 값을 가진 노드와 root 노드 위치를 바꿔주는 작업을 반복 (swap)

<IMAGE>힙 삭제 동작 그림 - root 삭제 후 재정렬 과정 (fun-coding.org)</IMAGE>

## 4. 힙 구현

### 힙과 배열

일반적으로 힙 구현시 배열 자료구조를 활용함
배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해 root 노드 인덱스 번호를 1로 지정하면 구현이 좀더 수월함

인덱스 관계 규칙:
- 부모 노드 인덱스 = 자식 노드 인덱스 // 2
- 왼쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2
- 오른쪽 자식 노드 인덱스 = 부모 노드 인덱스 * 2 + 1

<IMAGE>힙 배열 표현 그림 - 인덱스 번호와 노드 대응 (fun-coding.org)</IMAGE>

예시:
- 10 노드(인덱스 2)의 부모 노드 인덱스: 2 // 2 = 1 → 인덱스 1 (루트)
- 15 노드(인덱스 1)의 왼쪽 자식 노드 인덱스: 1 * 2 = 2
- 15 노드(인덱스 1)의 오른쪽 자식 노드 인덱스: 1 * 2 + 1 = 3 (실제로는 없으므로 인덱스 5로 바뀜)

### 힙에 데이터 삽입 구현 (Max Heap 예)

```python
class Heap:
    def __init__(self, data):
        # 배열 구조로 주로 하기 때문에
        self.heap_array = list()
        # 완전 이진 트리의 성질을 이용하여 부모, 자식노드를 쉽게 찾기 위해
        # 인덱싱을 활용하기 위해 인덱스를 1부터 가져간다.
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        # 배열에 데이터가 존재하지 않는다면 reset시켜줌.
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)

        # None이 0번째 index에 존재하므로
        # index를 통해 부모,자식노드를 분별하기 쉽게 -1을 해줌
        inserted_idx = len(self.heap_array) - 1

        # index를 통해 heap 구조를 띄도록 추가한 노드의 값이
        # Max heap인 경우 부모노드보다 작은지를 확인한 후에 계속해서
        # 바꿔주게끔 함수 하나를 만들어 바꿔줘야하는 노드이면 True를 반환하여
        # while문을 반복할 수 있게끔 한다.
        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = \
                self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True
```

삽입 테스트:
```python
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
# 결과: [None, 20, 10, 15, 5, 4, 8]
```

### 힙에 데이터 삭제 구현 (Max Heap 예)

삭제 시 move_down 함수로 3가지 케이스를 처리한다:
- case1: 왼쪽 자식 노드도 없을 때 → swap 불필요
- case2: 오른쪽 자식 노드만 없을 때 → 왼쪽 자식과 비교
- case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때 → 자식끼리 먼저 비교 후 큰 쪽과 swap

```python
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
        # 자식노드가 둘다있다면, 먼저 자식노드끼리 비교한다.
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

삭제 테스트:
```python
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)

print(heap.pop())        # 20 (최댓값 반환)
print(heap.heap_array)   # [None, 15, 10, 8, 5, 4]
```

## 5. 힙 (Heap) 시간 복잡도

depth(트리의 높이)를 h라고 표기한다면:
- n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제 시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h = log₂n에 가까움
- 따라서 시간 복잡도: O(log n)
- 한번 실행 시마다 50%의 실행할 수도 있는 명령을 제거한다는 의미 → 50%의 실행시간 단축

| 연산 | 시간 복잡도 |
|------|-----------|
| 최대/최소값 조회 (peek) | O(1) |
| 삽입 (insert) | O(log n) |
| 삭제 (pop) | O(log n) |

# 메타데이터
```json
{
  "category": "자료구조",
  "algorithm": "힙",
  "source_type": "blog",
  "style": [
    "easy",
    "code",
    "theory"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python",
  "source": "heung-bae-lee.github.io"
}
```
