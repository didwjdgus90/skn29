# 제목
[Python 기초] 리스트 컴프리헨션 (List Comprehensions)

# 링크
https://docs.python.org/ko/3.11/tutorial/datastructures.html#list-comprehensions

# 본문

## 1. 한 줄 요약

리스트 컴프리헨션은 **리스트를 만드는 간결한 방법**을 제공하는 파이썬 문법이다. 공식 문서의 정의에 따르면, 리스트 컴프리헨션은 표현식과 그 뒤를 따르는 `for` 절, 그리고 없거나 여러 개의 `for`나 `if` 절들을 감싸는 **대괄호**로 구성된다.

---

## 2. 등장 배경 — 기존 방식의 한계

공식 문서는 리스트 컴프리헨션의 도입 배경을 다음 두 가지 문제를 통해 제시한다.

**문제 1: 변수 오염(variable leakage)**

`for` 루프로 리스트를 생성하면 루프 변수가 루프 종료 후에도 스코프에 남아 있다.

```python
>>> squares = []
>>> for x in range(10):      # x가 루프 종료 후에도 남음
...     squares.append(x**2)
...
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> x                        # 루프 변수 x = 9 가 남아 있음
9
```

**문제 2: `map()` + `lambda` 방식의 가독성 저하**

```python
squares = list(map(lambda x: x**2, range(10)))
```

위 방식은 부작용은 없지만 `lambda`와 `map`의 중첩으로 가독성이 떨어진다.

**리스트 컴프리헨션은 두 문제를 동시에 해결한다.** 루프 변수가 컴프리헨션 스코프 내에 한정되며, 표현식이 단일 구문으로 직관적으로 읽힌다.

```python
squares = [x**2 for x in range(10)]   # 간결하고 가독성이 높음
```

공식 문서의 표현을 인용하면: *"이것이 더 간결하고 읽기 쉽습니다."*

---

## 3. 문법 구조

```
[ 표현식   for 변수 in 이터러블   (if 조건)* ]
   ↑              ↑                   ↑
결과로 담을 값   반복 대상 정의      필터 조건 (선택, 복수 가능)
```

- **표현식(expression)**: 각 항목에 적용할 연산 또는 변환. 결과 리스트의 요소가 된다.
- **`for` 절**: 반복 대상 이터러블을 정의한다. 하나 이상 사용 가능하다.
- **`if` 절**: 조건을 만족하는 항목만 포함한다. 선택적이며 복수 사용 가능하다.

`for`와 `if`의 순서는 동등한 중첩 `for`/`if` 문의 순서와 동일하다.

---

## 4. 동작 과정 살펴보기

### 4-1. 기본 변환 — 모든 요소에 연산 적용

```python
>>> vec = [-4, -2, 0, 2, 4]

>>> [x*2 for x in vec]           # 각 요소를 2배
[-8, -4, 0, 4, 8]

>>> [abs(x) for x in vec]         # 각 요소에 함수 적용
[4, 2, 0, 2, 4]
```

```
[x*2 for x in [-4, -2, 0, 2, 4]]

-4 → -8
-2 → -4
 0 →  0
 2 →  4
 4 →  8
       ↓
[-8, -4, 0, 4, 8]
```

### 4-2. 필터링 — 조건을 만족하는 요소만 포함

```python
>>> vec = [-4, -2, 0, 2, 4]

>>> [x for x in vec if x >= 0]    # 0 이상인 요소만 추출
[0, 2, 4]
```

```
[x for x in [-4, -2, 0, 2, 4] if x >= 0]

-4 → x >= 0? ❌ 제외
-2 → x >= 0? ❌ 제외
 0 → x >= 0? ✅ 포함
 2 → x >= 0? ✅ 포함
 4 → x >= 0? ✅ 포함
              ↓
[0, 2, 4]
```

### 4-3. 메서드 호출 — 각 요소에 메서드 적용

```python
>>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
>>> [weapon.strip() for weapon in freshfruit]
['banana', 'loganberry', 'passion fruit']
```

### 4-4. 튜플 표현식 — 괄호 필수

표현식이 튜플인 경우 반드시 괄호로 감싸야 한다. 이것은 공식 문서가 명시적으로 짚는 문법 요건이다.

```python
>>> [(x, x**2) for x in range(6)]         # ✅ 괄호로 감싼 튜플
[(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

>>> [x, x**2 for x in range(6)]           # ❌ SyntaxError
  File "<stdin>", line 1
    [x, x**2 for x in range(6)]
     ^^^^^^^
SyntaxError: did you forget parentheses around the comprehension target?
```

### 4-5. 복잡한 표현식과 중첩 함수

리스트 컴프리헨션의 표현식 자리에는 임의의 복잡한 표현식이 올 수 있다.

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

---

## 5. 다중 for 절 — 두 이터러블의 조합

`for` 절이 두 개 이상일 때는 **중첩 `for` 루프와 동등**하다. 공식 문서는 두 코드 조각에서 `for`와 `if`의 순서가 동일함을 명시한다.

```python
>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
```

이것은 다음 중첩 루프와 완전히 동등하다.

```python
>>> combs = []
>>> for x in [1,2,3]:
...     for y in [3,1,4]:
...         if x != y:
...             combs.append((x, y))
```

```
다중 for 절의 실행 순서:

for x in [1,2,3]:          ← 바깥 루프 (왼쪽 for)
    for y in [3,1,4]:      ← 안쪽 루프 (오른쪽 for)
        if x != y:         ← 조건 필터
            결과에 (x, y) 추가

컴프리헨션 표현식 읽는 순서:
[(x, y)  for x in [1,2,3]  for y in [3,1,4]  if x != y]
   ↑           ↑                  ↑               ↑
 결과값      바깥 루프           안쪽 루프          조건
```

2차원 리스트를 1차원으로 평탄화(flatten)하는 패턴도 이 방식으로 구현된다.

```python
>>> vec = [[1,2,3], [4,5,6], [7,8,9]]
>>> [num for elem in vec for num in elem]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 6. 중첩된 리스트 컴프리헨션 (Nested List Comprehensions)

리스트 컴프리헨션의 첫 **표현식** 자리에 또 다른 리스트 컴프리헨션을 올 수 있다.

공식 문서의 예제: 3×4 행렬의 전치(transposition).

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

이것은 다음 중첩 루프와 동등하다.

```python
>>> transposed = []
>>> for i in range(4):                            # 바깥 루프
...     transposed.append([row[i] for row in matrix])   # 안쪽 컴프리헨션
```

또는 완전히 풀어쓰면:

```python
>>> transposed = []
>>> for i in range(4):
...     transposed_row = []
...     for row in matrix:
...         transposed_row.append(row[i])
...     transposed.append(transposed_row)
```

```
중첩 리스트 컴프리헨션 평가 순서:

[[row[i] for row in matrix] for i in range(4)]
                              ↑
                        바깥 for가 먼저 실행

i=0 → [row[0] for row in matrix] → [1, 5, 9]
i=1 → [row[1] for row in matrix] → [2, 6, 10]
i=2 → [row[2] for row in matrix] → [3, 7, 11]
i=3 → [row[3] for row in matrix] → [4, 8, 12]
                                      ↓
              [[1,5,9], [2,6,10], [3,7,11], [4,8,12]]
```

**공식 문서 주의사항**: 내부 리스트 컴프리헨션은 **뒤따르는 `for`의 문맥에서 값이 구해진다**. 즉, 중첩 컴프리헨션에서 내부 표현식의 평가는 바깥 `for` 변수에 의존한다.

실제 세상에서 행렬 전치와 같은 복잡한 작업은 내장 함수 `zip()`을 활용하는 것이 더 간결하다.

```python
>>> list(zip(*matrix))
[(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
```

---

## 7. 핵심 요약 및 주의점

**핵심 요약**

- 리스트 컴프리헨션은 `[표현식 for 변수 in 이터러블 (if 조건)*]` 구조다.
- `for`와 `if`의 순서는 동등한 중첩 루프의 순서와 **동일**하다.
- 표현식 자리에 튜플이 오는 경우 **반드시 괄호로 감싸야** 한다. 미준수 시 `SyntaxError`.
- 중첩 리스트 컴프리헨션에서 내부 컴프리헨션은 **바깥 `for`의 문맥에서 평가**된다.
- 루프 변수는 컴프리헨션 스코프 내에 한정되어 외부 변수를 오염시키지 않는다.

**성능 특성**

```
방식                       루프 변수 오염   가독성    메모리
────────────────────────────────────────────────────────
for 루프 + append()         오염됨           보통      즉시 리스트 생성
map() + lambda              오염 없음        낮음      즉시 리스트 생성
리스트 컴프리헨션            오염 없음        높음      즉시 리스트 생성
제너레이터 표현식 ()         오염 없음        높음      지연 평가 (메모리 효율)
```

**주의점**

```
상황                               올바른 방법                   잘못된 방법
──────────────────────────────────────────────────────────────────────────────
튜플을 요소로 생성                  [(x, x**2) for x in range(6)]  [x, x**2 for x in range(6)] → SyntaxError
다중 for 절의 순서 해석             중첩 루프 순서와 동일            역순으로 읽기
복잡한 중첩 컴프리헨션 사용         가독성 저하 시 루프로 풀어쓰기   복잡한 중첩 남발
대용량 데이터의 즉시 리스트 생성    제너레이터 표현식 () 사용        리스트 컴프리헨션 → 메모리 소진
```

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "리스트 컴프리헨션",
  "source_type": "docs",
  "style": [
    "theory",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```