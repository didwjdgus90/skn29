# [Python 기초] heapq (힙 / 우선순위 큐)

# 본문

## 1. 한 줄 요약

`heapq`는 파이썬 리스트를 최소 힙 구조로 유지하면서, 최솟값 삽입과 삭제를 효율적으로 수행하게 해주는 표준 라이브러리이다.

`heapq`를 이해하면 우선순위가 있는 데이터를 매번 전체 정렬하지 않고도 효율적으로 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

어떤 문제에서는 여러 값 중 가장 작은 값을 반복해서 꺼내야 한다.

예를 들어 다음과 같은 작업 시간이 있다고 하자.

```text
작업 시간: 7, 2, 5, 1, 9
```

가장 짧은 작업부터 처리하려면 매번 최솟값을 찾아야 한다.

리스트를 사용할 경우 가장 단순한 방법은 매번 정렬하는 것이다.

```python
tasks.sort()
current = tasks.pop(0)
```

하지만 데이터가 계속 추가되고 삭제된다면 매번 전체를 정렬하는 방식은 비효율적이다.

```text
값 추가
전체 정렬
최솟값 꺼내기
값 추가
전체 정렬
최솟값 꺼내기
```

`heapq`는 이런 문제를 해결한다.

힙은 전체 데이터를 완전히 정렬하지 않는다.

대신 **가장 작은 값이 항상 먼저 나올 수 있도록 필요한 규칙만 유지**한다.

---

## 3. 핵심 아이디어

힙은 “전체 정렬”보다 “최솟값 접근”에 집중한 자료구조이다.

정렬된 리스트는 모든 값의 순서가 정확히 정리되어 있다.

```text
정렬 리스트

[1, 2, 5, 7, 9]
```

반면 힙은 전체 순서가 완전히 정렬되어 있지 않을 수 있다.

```text
힙 리스트 예시

[1, 2, 5, 7, 9]
[1, 5, 2, 9, 7]
```

두 번째 형태도 힙일 수 있다.

중요한 것은 가장 작은 값이 맨 앞에 있다는 점이다.

힙을 트리처럼 보면 부모 노드는 자식 노드보다 작거나 같다.

```text
        1
      /   \
     5     2
    / \
   9   7
```

파이썬은 이 트리 구조를 실제 노드 객체로 만들지 않고 리스트로 표현한다.

```text
인덱스:  0  1  2  3  4
값:     [1, 5, 2, 9, 7]
```

`heapq`의 핵심 연산은 두 가지이다.

```text
heappush → 값을 넣고 힙 규칙 유지
heappop  → 가장 작은 값을 꺼내고 힙 규칙 재정렬
```

---

## 4. 동작 과정 살펴보기

아래 과정을 따라가 보자.

```python
import heapq

heap = []

heapq.heappush(heap, 7)
heapq.heappush(heap, 2)
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
```

### Step 1. 빈 힙 준비

```text
heap

[]
```

힙은 일반 리스트로 시작한다.

`heapq` 함수가 이 리스트를 힙 규칙에 맞게 관리한다.

### Step 2. 7 삽입

```text
heappush(heap, 7)

[7]
```

값이 하나뿐이므로 별도 조정이 필요 없다.

### Step 3. 2 삽입

```text
삽입 전
[7]

2 삽입 후
[2, 7]
```

2가 7보다 작으므로 앞쪽으로 이동한다.

최솟값 2가 0번 인덱스에 위치한다.

### Step 4. 5 삽입

```text
삽입 전
[2, 7]

5 삽입 후
[2, 7, 5]
```

5는 2보다 크므로 루트는 그대로 2이다.

### Step 5. 1 삽입

```text
삽입 전
[2, 7, 5]

1 삽입 후
[1, 2, 5, 7]
```

1이 가장 작은 값이므로 맨 앞까지 올라온다.

### Step 6. 최솟값 삭제

```python
smallest = heapq.heappop(heap)
```

```text
꺼낸 값: 1

남은 힙
[2, 7, 5]
```

`heappop()`은 0번 인덱스의 최솟값을 꺼낸 뒤, 남은 값들이 다시 힙 규칙을 만족하도록 조정한다.

---

## 5. 구현 코드 및 상세 설명

```python
import heapq

# 처리해야 할 숫자 목록
numbers = [7, 2, 5, 1, 9]

# 빈 힙 생성
heap = []

# 숫자를 하나씩 힙에 삽입
for number in numbers:
    heapq.heappush(heap, number)

print("힙 상태:", heap)

# 최솟값을 하나씩 꺼내기
while heap:
    smallest = heapq.heappop(heap)
    print("꺼낸 값:", smallest)
```

### 코드 설명

```python
import heapq
```

파이썬에서 힙 기능을 사용하기 위해 `heapq` 모듈을 불러온다.

```python
heap = []
```

힙으로 사용할 빈 리스트를 만든다.

파이썬의 `heapq`는 별도의 힙 클래스를 제공하지 않고, 리스트를 힙처럼 다룬다.

```python
heapq.heappush(heap, number)
```

값을 힙에 삽입한다.

삽입 후에도 힙 규칙이 유지되도록 내부 위치가 조정된다.

```python
heapq.heappop(heap)
```

힙에서 가장 작은 값을 꺼낸다.

전체 리스트가 완전 정렬되어 있지 않아도 최솟값은 정확히 나온다.

```text
꺼내는 순서

1 → 2 → 5 → 7 → 9
```

### 최대 힙처럼 사용하기

파이썬 `heapq`는 기본적으로 최소 힙만 제공한다.

최댓값을 먼저 꺼내고 싶다면 값을 음수로 바꿔 넣는 방법을 사용한다.

```python
import heapq

numbers = [7, 2, 5, 1, 9]
heap = []

for number in numbers:
    heapq.heappush(heap, -number)

while heap:
    largest = -heapq.heappop(heap)
    print(largest)
```

```text
실제 저장: -7, -2, -5, -1, -9
가장 작은 음수 -9가 먼저 나옴
다시 부호를 바꾸면 9
```

---

## 6. 마지막 정리

`heapq`는 파이썬 리스트를 최소 힙으로 관리하는 라이브러리이다.

힙은 전체 정렬이 아니라 최솟값을 빠르게 꺼내는 데 집중한다.

`heappush()`는 값을 삽입하고 힙 규칙을 유지한다.

`heappop()`은 최솟값을 꺼내고 남은 값들을 다시 힙 규칙에 맞춘다.

최댓값을 먼저 꺼내려면 값을 음수로 바꿔 저장하는 방식을 사용할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 heapq",
  "source_type": "generated",
  "style": [
    "theory",
    "code"
  ],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "mid",
  "language": "python"
}
```
