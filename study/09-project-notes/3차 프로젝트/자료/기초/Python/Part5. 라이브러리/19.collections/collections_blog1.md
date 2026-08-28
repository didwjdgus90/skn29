# [Python 기초] collections 모듈 

---

# 링크
<https://vipdeveloper.tistory.com/135>

---

## 1. 한 줄 요약

`collections`는 파이썬 기본 자료구조(리스트, 딕셔너리 등)를 더 편리하게 쓸 수 있도록 확장한 도구 모음이다. 그 중 코딩에서 가장 자주 쓰이는 세 가지 `Counter`, `deque`, `defaultdict`를 알아본다.

---

## 2. collections 모듈이란?

파이썬에는 리스트, 딕셔너리, 집합 같은 기본 자료구조가 있다. 그런데 실제 코딩을 하다 보면 이런 상황이 자주 생긴다.

- 리스트에서 각 값이 **몇 번 등장하는지 세야** 할 때
- 리스트의 **앞과 뒤 양쪽에서** 빠르게 넣고 빼야 할 때
- 딕셔너리에서 **없는 키를 조회해도 에러 없이** 기본값을 쓰고 싶을 때

이런 상황을 위해 파이썬은 `collections` 모듈에 미리 만들어둔 특수 자료구조들을 제공한다. 직접 구현하면 복잡한 코드를 단 몇 줄로 해결할 수 있다.

```python
from collections import Counter, deque, defaultdict
```

사용하기 전에 위처럼 `import` 해줘야 한다.

---

## 3. Counter — 개수를 세는 도구

### 3-1. 왜 필요할까?

리스트에서 각 요소가 몇 번 나왔는지 세려면 보통 이렇게 한다.

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

count = {}
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)   # {'apple': 3, 'banana': 2, 'cherry': 1}
```

꽤 긴 코드다. `Counter`를 쓰면 한 줄로 끝난다.

```python
from collections import Counter

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = Counter(words)
print(count)   # Counter({'apple': 3, 'banana': 2, 'cherry': 1})
```

### 3-2. Counter의 핵심 아이디어

`Counter`는 **"각 요소가 몇 번 등장했는지"를 자동으로 세서 딕셔너리처럼 저장**하는 도구다. 딕셔너리와 사용법이 거의 같으면서, 개수 세기에 특화된 기능이 추가되어 있다.

```
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
Counter 적용:
  "apple"  등장 횟수 → 3
  "banana" 등장 횟수 → 2
  "cherry" 등장 횟수 → 1
결과: {'apple': 3, 'banana': 2, 'cherry': 1}
```

### 3-3. 주요 기능

**기본 사용법 — 리스트, 문자열 모두 가능**

```python
# 리스트에서 각 요소 개수 세기
fruits = ["apple", "banana", "apple", "cherry"]
c = Counter(fruits)
print(c["apple"])    # 3
print(c["grape"])    # 0  ← 없는 요소도 0 반환 (에러 없음)

# 문자열에서 각 글자 개수 세기
c2 = Counter("abracadabra")
print(c2)   # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

**`most_common(n)` — 가장 많이 등장한 n개 반환**

```python
words = ["apple", "banana", "apple", "cherry", "banana", "apple", "cherry"]
c = Counter(words)

print(c.most_common(2))
# [('apple', 3), ('cherry', 2)]  ← 많은 순서대로 2개
```

`most_common()`은 빈도 분석, 순위 집계 등에 매우 유용하다. 어떤 단어가 가장 많이 등장했는지, 어떤 상품이 가장 많이 팔렸는지 한 줄로 구할 수 있다.

**Counter끼리 연산 — 개수 더하기, 빼기**

```python
c1 = Counter(["apple", "banana", "apple"])
c2 = Counter(["apple", "cherry"])

print(c1 + c2)   # Counter({'apple': 3, 'banana': 1, 'cherry': 1})
print(c1 - c2)   # Counter({'banana': 1, 'apple': 1})  ← 0 이하는 제거
```

---

## 4. deque — 양쪽에서 넣고 뺄 수 있는 큐

### 4-1. 왜 필요할까?

일반 리스트는 맨 뒤에 요소를 추가하거나 꺼내는 건 빠르다. 하지만 **맨 앞**에서 요소를 꺼내는 `lst.pop(0)` 작업은 느리다. 뒤에 있는 모든 요소를 한 칸씩 앞으로 이동시켜야 하기 때문이다.

```
리스트에서 pop(0) 연산:

[1, 2, 3, 4, 5]
 ↑ 이걸 꺼내면...
[2, 3, 4, 5]   ← 나머지를 전부 한 칸씩 앞으로 이동 (느림!)
```

데이터가 많을수록 이 작업이 점점 느려진다. `deque`는 앞뒤 양쪽 끝에서 O(1), 즉 **데이터 양과 관계없이 일정한 속도**로 빠르게 넣고 뺄 수 있는 자료구조다.

### 4-2. deque의 핵심 아이디어

`deque`(덱, Double-Ended Queue)는 이름 그대로 **양쪽 끝에서 넣고 빼는 게 모두 빠른 큐**다. 양방향 통로가 있는 터널을 생각해보자. 왼쪽에서도 들어오고 나갈 수 있고, 오른쪽에서도 들어오고 나갈 수 있다.

```
왼쪽(앞)                           오른쪽(뒤)
  ↕                                   ↕
appendleft / popleft      append / pop
  │                                   │
  ← [ A ] [ B ] [ C ] [ D ] [ E ] →
```

리스트와 사용법이 거의 같아서 익히기 쉽다. BFS(너비 우선 탐색) 알고리즘이나 슬라이딩 윈도우 문제에서 특히 자주 쓰인다.

### 4-3. 주요 기능

```python
from collections import deque

dq = deque([1, 2, 3])

# 오른쪽(뒤)에 추가/제거 — 리스트와 동일
dq.append(4)       # [1, 2, 3, 4]
dq.pop()           # 4 반환, [1, 2, 3]

# 왼쪽(앞)에 추가/제거 — deque만의 강점
dq.appendleft(0)   # [0, 1, 2, 3]
dq.popleft()       # 0 반환, [1, 2, 3]
```

**`rotate(n)` — 요소들을 n칸 회전**

```python
dq = deque([1, 2, 3, 4, 5])

dq.rotate(2)     # 오른쪽으로 2칸 회전
print(dq)        # deque([4, 5, 1, 2, 3])

dq.rotate(-2)    # 왼쪽으로 2칸 회전
print(dq)        # deque([1, 2, 3, 4, 5])
```

```
rotate(2) 동작:

원본:   [1, 2, 3, 4, 5]
                ↓ 뒤 2개가 앞으로 이동
결과:   [4, 5, 1, 2, 3]
```

**`maxlen` — 최대 크기 제한**

`maxlen`을 지정하면 그 크기를 넘었을 때 반대편 끝에서 자동으로 제거된다. 최근 N개만 유지하고 싶을 때 유용하다.

```python
# 최근 3개만 유지하는 큐
dq = deque(maxlen=3)

for i in range(5):
    dq.append(i)
    print(list(dq))
# [0]
# [0, 1]
# [0, 1, 2]
# [1, 2, 3]  ← 4번째 추가 시 가장 오래된 0이 자동으로 제거됨
# [2, 3, 4]
```

실제로 최근 방문 기록, 로그 버퍼, 슬라이딩 윈도우 등 "최근 N개"를 유지해야 하는 상황에서 자주 쓰인다.

**리스트처럼 사용 가능**

deque는 리스트의 대부분 기능을 그대로 쓸 수 있다. 리스트로 변환도 쉽다.

```python
dq = deque([1, 2, 3])
print(len(dq))     # 3
print(dq[0])       # 1
print(list(dq))    # [1, 2, 3]
```

---

## 5. defaultdict — 없는 키도 에러 없이 쓰는 딕셔너리

### 5-1. 왜 필요할까?

일반 딕셔너리에서 없는 키를 조회하면 `KeyError`가 발생한다.

```python
d = {}
d["apple"] += 1   # ❌ KeyError: 'apple'
```

이 에러를 피하기 위해 매번 이런 코드를 써야 한다.

```python
d = {}
if "apple" in d:
    d["apple"] += 1
else:
    d["apple"] = 1
```

또는 `get()` 메서드를 쓸 수도 있지만 여전히 번거롭다.

```python
d["apple"] = d.get("apple", 0) + 1
```

`defaultdict`를 쓰면 없는 키를 처음 사용할 때 **자동으로 기본값을 만들어줘서** 이런 번거로움이 사라진다.

```python
from collections import defaultdict

d = defaultdict(int)   # 기본값: 정수 0
d["apple"] += 1        # ✅ 에러 없음! 자동으로 0 → 1
d["banana"] += 3
print(dict(d))   # {'apple': 1, 'banana': 3}
```

### 5-2. defaultdict의 핵심 아이디어

`defaultdict`는 **처음 보는 키를 만났을 때 지정한 타입의 기본값을 자동으로 만들어주는 딕셔너리**다. 괄호 안에 어떤 타입의 기본값을 쓸지 지정한다.

```
defaultdict(int)   → 없는 키의 기본값: 0     (int()의 결과)
defaultdict(list)  → 없는 키의 기본값: []    (list()의 결과)
defaultdict(str)   → 없는 키의 기본값: ""    (str()의 결과)
defaultdict(set)   → 없는 키의 기본값: set() (set()의 결과)
```

### 5-3. 주요 활용 패턴

**`defaultdict(int)` — 개수 세기**

```python
from collections import defaultdict

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
count = defaultdict(int)

for word in words:
    count[word] += 1   # 처음 등장해도 에러 없이 0에서 시작

print(dict(count))   # {'apple': 3, 'banana': 2, 'cherry': 1}
```

개수 세기에는 `Counter`가 더 간편하지만, 복잡한 조건이 있을 때는 `defaultdict(int)`가 더 유연하다.

**`defaultdict(list)` — 그룹 묶기**

같은 키를 가진 항목들을 리스트로 묶을 때 매우 유용하다.

```python
# 학생들을 학년별로 묶기
students = [("1학년", "철수"), ("2학년", "영희"), ("1학년", "민수"), ("2학년", "지수")]

groups = defaultdict(list)
for grade, name in students:
    groups[grade].append(name)   # 없는 키도 자동으로 [] 생성

print(dict(groups))
# {'1학년': ['철수', '민수'], '2학년': ['영희', '지수']}
```

```
동작 흐름:

("1학년", "철수") → groups["1학년"]이 없으면 [] 자동 생성 → ["철수"]
("2학년", "영희") → groups["2학년"]이 없으면 [] 자동 생성 → ["영희"]
("1학년", "민수") → groups["1학년"]이 이미 있음 → ["철수", "민수"]
("2학년", "지수") → groups["2학년"]이 이미 있음 → ["영희", "지수"]
```

이 패턴은 그래프 문제에서 인접 리스트를 만들 때도 자주 쓰인다.

```python
# 그래프 인접 리스트 구성
edges = [(1, 2), (1, 3), (2, 4), (3, 4)]
graph = defaultdict(list)

for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

print(dict(graph))
# {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3]}
```

**`defaultdict(set)` — 중복 없이 그룹 묶기**

같은 값이 여러 번 추가되어도 하나만 유지하고 싶을 때는 `set`을 기본값으로 쓴다.

```python
pairs = [("A", 1), ("B", 2), ("A", 3), ("A", 1)]   # ("A", 1)이 중복

groups = defaultdict(set)
for key, val in pairs:
    groups[key].add(val)

print(dict(groups))   # {'A': {1, 3}, 'B': {2}}  ← 중복 1이 하나만 남음
```

---

## 6. Counter vs defaultdict(int) — 언제 뭘 쓸까?

둘 다 개수를 세는 데 쓸 수 있다. 차이를 알면 상황에 맞게 선택할 수 있다.

```
Counter:
  - 리스트나 문자열을 바로 넣으면 자동으로 세어줌
  - most_common(), 산술 연산 등 개수 특화 기능 제공
  - "전체 데이터에서 빈도를 집계할 때" 적합

defaultdict(int):
  - 하나씩 처리하며 복잡한 조건으로 카운트할 때 유연함
  - "조건부 집계"나 "그룹별 카운트" 등 커스텀 로직에 적합
```

```python
# Counter — 전체 데이터 한꺼번에 집계할 때
c = Counter(["apple", "banana", "apple"])

# defaultdict(int) — 하나씩 처리하면서 조건에 따라 셀 때
d = defaultdict(int)
for item in data:
    if 조건:
        d[item] += 1
```

---

## 7. 종합 예제 — 세 가지 함께 쓰기

실제 문제처럼 세 가지를 조합해서 쓰는 예제다. 텍스트에서 단어 빈도를 분석하고, 최근 3개의 최고 빈도 단어를 추적한다.

```python
from collections import Counter, deque, defaultdict

# 텍스트 데이터
texts = [
    "apple banana apple cherry",
    "banana cherry cherry apple",
    "apple apple banana",
]

# 1. Counter로 전체 단어 빈도 집계
total_count = Counter()
for text in texts:
    total_count.update(text.split())

print("전체 빈도:", dict(total_count))
# {'apple': 5, 'banana': 3, 'cherry': 3}

# 2. most_common으로 상위 2개 추출
print("상위 2개:", total_count.most_common(2))
# [('apple', 5), ('banana', 3)]

# 3. defaultdict로 텍스트별 단어 그룹화
text_words = defaultdict(list)
for i, text in enumerate(texts):
    text_words[f"텍스트{i+1}"] = text.split()

print("텍스트별 단어:", dict(text_words))
# {'텍스트1': ['apple', 'banana', 'apple', 'cherry'], ...}

# 4. deque로 최근 2개 텍스트의 첫 단어만 유지
recent = deque(maxlen=2)
for text in texts:
    recent.append(text.split()[0])

print("최근 2개 텍스트 첫 단어:", list(recent))
# ['banana', 'apple']  ← 마지막 2개만 유지
```

---

## 8. 마지막 정리

**Counter**
- 리스트나 문자열에서 **각 요소의 등장 횟수를 자동으로 세는** 딕셔너리다.
- `most_common(n)`으로 **가장 많이 등장한 n개**를 바로 꺼낼 수 있다.
- Counter끼리 `+`, `-` 연산도 가능하다.

**deque**
- 리스트와 달리 **앞(왼쪽)과 뒤(오른쪽) 양쪽에서 빠르게 넣고 뺄 수 있다.**
- `appendleft()`, `popleft()`로 앞쪽을 다룬다.
- `maxlen`을 지정하면 크기 초과 시 반대편이 자동 제거된다 — "최근 N개 유지"에 유용.
- BFS, 슬라이딩 윈도우 문제에서 자주 쓰인다.

**defaultdict**
- 일반 딕셔너리와 달리 **없는 키를 처음 사용할 때 자동으로 기본값을 생성**한다.
- `defaultdict(int)` → 기본값 0 (개수 세기), `defaultdict(list)` → 기본값 [] (그룹 묶기)
- 그래프 인접 리스트, 그룹별 분류 등 에서 매우 자주 쓰인다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "collections",
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
  "language": "python"
}
```