# [Python 기초] collections 모듈

# 본문

## 1. 한 줄 요약

`collections`는 파이썬에서 자주 필요한 특수한 자료구조를 모아둔 표준 라이브러리이다.

`collections`를 이해하면 개수 세기, 큐 구현, 기본값이 있는 딕셔너리 같은 작업을 더 간단하게 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

기본 자료형만으로도 많은 문제를 해결할 수 있다.

하지만 코딩 테스트에서는 특정 작업이 매우 자주 나온다.

```text
문자가 몇 번 나왔는지 세기
앞뒤로 값을 넣고 빼는 큐 만들기
존재하지 않는 키에 기본값 넣기
```

일반 딕셔너리로 문자의 개수를 세려면 다음처럼 작성해야 한다.

```python
count = {}

for char in text:
    if char not in count:
        count[char] = 0
    count[char] += 1
```

이 코드는 맞지만 조금 길다.

`collections.Counter`를 사용하면 훨씬 간단하다.

```python
from collections import Counter

count = Counter(text)
```

`collections`는 자주 쓰는 자료구조 작업을 미리 편하게 만들어둔 도구 상자이다.

---

## 3. 핵심 아이디어

`collections`는 기본 도구보다 조금 더 전문적인 공구 세트라고 생각하면 쉽다.

기본 자료형은 일반 공구다.

```text
list
dict
tuple
set
```

`collections`는 특정 상황에 맞게 준비된 특수 공구다.

```text
Counter      → 개수 세기 전용
deque        → 앞뒤 삽입/삭제가 빠른 큐
defaultdict  → 기본값이 자동으로 생기는 딕셔너리
```

예를 들어 문자의 개수를 세는 상황은 매우 흔하다.

```text
banana

b → 1
a → 3
n → 2
```

`Counter`는 이런 작업을 바로 해준다.

큐가 필요한 상황에서는 `deque`가 유용하다.

```text
Queue

앞쪽 꺼내기  ← [1] [2] [3] ← 뒤쪽 넣기
```

일반 리스트로 앞쪽 값을 빼면 느릴 수 있지만, `deque`는 앞뒤 작업에 적합하다.

---

## 4. 동작 과정 살펴보기

### 4-1. Counter로 개수 세기

```python
from collections import Counter

text = "banana"
counter = Counter(text)
```

문자열을 하나씩 살펴본다.

```text
b a n a n a
```

각 문자의 개수를 센다.

```text
b → 1
a → 3
n → 2
```

결과는 다음과 비슷하다.

```python
Counter({'a': 3, 'n': 2, 'b': 1})
```

### 4-2. deque로 큐 만들기

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
```

처음에는 비어 있다.

```text
queue

[]
```

값을 뒤에 넣는다.

```text
append(1) → [1]
append(2) → [1, 2]
append(3) → [1, 2, 3]
```

앞에서 값을 꺼낸다.

```text
popleft()

[1, 2, 3]
 ↑
꺼냄

결과: 1
남은 큐: [2, 3]
```

### 4-3. defaultdict로 기본값 자동 생성

```python
from collections import defaultdict

scores = defaultdict(list)
scores["민수"].append(80)
```

일반 딕셔너리라면 `"민수"` 키가 없을 때 오류가 날 수 있다.

`defaultdict(list)`는 키가 없으면 빈 리스트를 자동으로 만들어준다.

```text
scores["민수"]가 없음
   │
   ▼
빈 리스트 [] 자동 생성
   │
   ▼
80 추가
```

---

## 5. 구현 코드 및 상세 설명

```python
from collections import Counter, deque, defaultdict

# Counter: 개수 세기
text = "banana"
counter = Counter(text)
print(counter)
print(counter["a"])


# deque: 큐 구현
queue = deque()

queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())
print(queue)


# defaultdict: 기본값이 있는 딕셔너리
group = defaultdict(list)

group["과일"].append("사과")
group["과일"].append("바나나")
group["음료"].append("물")

print(group)
```

### 코드 설명

```python
counter = Counter(text)
```

문자열 안의 각 문자가 몇 번 나오는지 센다.

```text
banana

a: 3
n: 2
b: 1
```

```python
counter["a"]
```

문자 `"a"`의 등장 횟수를 꺼낸다.

```python
queue = deque()
```

앞뒤에서 값을 빠르게 넣고 뺄 수 있는 큐를 만든다.

```python
queue.append("A")
```

오른쪽 끝에 값을 추가한다.

```python
queue.popleft()
```

왼쪽 끝에서 값을 꺼낸다.

BFS 같은 알고리즘에서 자주 사용된다.

```python
group = defaultdict(list)
```

키가 없을 때 빈 리스트를 자동으로 만들어주는 딕셔너리다.

```python
group["과일"].append("사과")
```

`"과일"` 키가 없어도 자동으로 빈 리스트가 생기고, 그 안에 `"사과"`가 추가된다.

---

## 6. 마지막 정리

`collections`는 유용한 자료구조를 제공하는 파이썬 표준 라이브러리이다.

`Counter`는 값의 등장 횟수를 셀 때 사용한다.

`deque`는 큐처럼 앞뒤에서 값을 넣고 뺄 때 사용한다.

`defaultdict`는 키가 없을 때 기본값을 자동으로 만들어준다.

코딩 테스트에서는 `Counter`, `deque`, `defaultdict`가 특히 자주 사용된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 collections",
  "source_type": "generated",
  "style": [
    "easy",
    "analogy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```
