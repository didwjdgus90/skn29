# [Python 기초] itertools (순열 / 조합 / 곱집합)

---

# 링크
<https://0171-cloud.tistory.com/17>

---

## 1. 한 줄 요약

`itertools`는 **순열, 조합, 곱집합처럼 "모든 경우의 수"를 생성하는 작업을 한 줄로 해결**해주는 모듈이다. 코딩테스트에서 완전탐색(브루트포스) 문제를 풀 때 자주 사용한다.

---

## 2. 왜 itertools가 필요할까?

1, 2, 3 세 숫자로 만들 수 있는 모든 순열을 구하려면 어떻게 할까?

```python
# itertools 없이 — 직접 중첩 for문으로 구현
result = []
nums = [1, 2, 3]
for a in nums:
    for b in nums:
        for c in nums:
            if a != b and b != c and a != c:
                result.append((a, b, c))
```

숫자가 4개, 5개로 늘어날수록 for문도 4중, 5중으로 늘어난다. 코드가 복잡하고 실수하기 쉽다.

`itertools`를 쓰면 한 줄로 끝난다.

```python
from itertools import permutations
list(permutations([1, 2, 3]))
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
```

---

## 3. 핵심 개념 — 순열, 조합, 곱집합의 차이

세 가지 개념이 헷갈리면 요리 메뉴 비유로 기억하자.

재료가 `["치킨", "피자", "파스타"]` 3가지 있을 때:

```
순열 (permutations):
  "순서가 있는 나열"
  치킨→피자→파스타와 피자→치킨→파스타는 다른 경우
  → (치킨,피자), (피자,치킨) 둘 다 포함

조합 (combinations):
  "순서 없는 선택"
  치킨과 피자를 고르는 건 하나의 경우
  → (치킨,피자)만 포함, (피자,치킨)은 중복으로 제외

곱집합 (product):
  "두 그룹에서 각각 하나씩 선택"
  메뉴 × 음료 = 가능한 세트 메뉴 조합 전체
  → (치킨, 콜라), (치킨, 사이다), (피자, 콜라), ...
```

---

## 4. 동작 과정 살펴보기

### 4-1. permutations — 순열 (순서 있음)

**순열**은 n개의 요소에서 r개를 골라 **순서를 고려해서** 나열하는 모든 경우다.

```python
from itertools import permutations

items = [1, 2, 3]

# 전체 순열 (3개 모두 사용)
list(permutations(items))
# [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
# → 3! = 6가지

# 2개씩 뽑는 순열
list(permutations(items, 2))
# [(1,2), (1,3), (2,1), (2,3), (3,1), (3,2)]
# → 3P2 = 6가지
```

```
permutations([1,2,3], 2) 동작:

1을 첫 번째로: (1,2), (1,3)
2를 첫 번째로: (2,1), (2,3)
3을 첫 번째로: (3,1), (3,2)

→ (1,2)와 (2,1)은 순서가 다르므로 둘 다 포함!
```

### 4-2. combinations — 조합 (순서 없음)

**조합**은 n개의 요소에서 r개를 골라 **순서를 고려하지 않고** 선택하는 모든 경우다.

```python
from itertools import combinations

items = [1, 2, 3]

# 2개씩 뽑는 조합
list(combinations(items, 2))
# [(1,2), (1,3), (2,3)]
# → 3C2 = 3가지

# 3개씩 뽑는 조합
list(combinations(items, 3))
# [(1,2,3)]
# → 3C3 = 1가지
```

```
combinations([1,2,3], 2) 동작:

(1,2) ✅  (1,3) ✅  (2,3) ✅
(2,1) ❌  (3,1) ❌  (3,2) ❌  ← 순서만 다른 중복은 제외

→ (1,2)와 (2,1)은 같은 선택으로 취급 → (1,2)만 포함
```

### 4-3. product — 곱집합 (여러 그룹에서 각각 선택)

**곱집합(데카르트 곱)**은 여러 그룹에서 **각각 하나씩 선택**한 모든 조합이다. 중첩 for문을 한 줄로 대체한다.

```python
from itertools import product

colors = ["빨강", "파랑"]
sizes  = ["S", "M", "L"]

list(product(colors, sizes))
# [('빨강','S'), ('빨강','M'), ('빨강','L'),
#  ('파랑','S'), ('파랑','M'), ('파랑','L')]
# → 2 × 3 = 6가지
```

```
product 동작 — 중첩 for문과 동일:

for color in colors:
    for size in sizes:
        결과에 (color, size) 추가

빨강-S, 빨강-M, 빨강-L
파랑-S, 파랑-M, 파랑-L
```

`repeat` 옵션으로 **같은 목록에서 반복 선택**도 가능하다.

```python
# 동전을 2번 던질 때 모든 경우
list(product(["앞", "뒤"], repeat=2))
# [('앞','앞'), ('앞','뒤'), ('뒤','앞'), ('뒤','뒤')]
```

---

## 5. 구현 코드 및 상세 설명

### 5-1. combinations_with_replacement — 중복 조합

일반 `combinations`는 같은 요소를 두 번 선택할 수 없다. **중복 허용** 조합이 필요하다면 `combinations_with_replacement`를 쓴다.

```python
from itertools import combinations_with_replacement

# 1,2,3에서 중복을 허용해서 2개 선택
list(combinations_with_replacement([1, 2, 3], 2))
# [(1,1), (1,2), (1,3), (2,2), (2,3), (3,3)]
# → 일반 combinations의 (1,2),(1,3),(2,3)에 (1,1),(2,2),(3,3) 추가됨
```

### 5-2. 결과를 리스트로 변환하기

`itertools` 함수들은 **이터레이터(iterator)** 를 반환한다. 이터레이터란 값을 하나씩 꺼낼 수 있는 객체인데, 바로 출력하면 주소값만 보인다. `list()`로 감싸면 리스트로 변환되어 볼 수 있다.

```python
from itertools import permutations

result = permutations([1, 2, 3])
print(result)         # <itertools.permutations object at 0x...>  ← 주소값
print(list(result))   # [(1,2,3), (1,3,2), ...]  ← 실제 값
```

이터레이터는 한 번 소비하면 다시 쓸 수 없다. `list()`로 변환한 뒤 사용하는 것이 안전하다.

### 5-3. 코딩테스트 활용 예제

**예제 1: 자물쇠 번호판 — 0~9에서 4자리 중복 없는 모든 조합**

```python
from itertools import permutations

digits = list(range(10))   # [0, 1, 2, ..., 9]
all_codes = list(permutations(digits, 4))
print(len(all_codes))   # 5040가지 (10P4)
```

**예제 2: 팀 구성 — 5명 중 2명 뽑기**

```python
from itertools import combinations

members = ["A", "B", "C", "D", "E"]
teams = list(combinations(members, 2))
print(teams)
# [('A','B'), ('A','C'), ('A','D'), ('A','E'),
#  ('B','C'), ('B','D'), ('B','E'),
#  ('C','D'), ('C','E'), ('D','E')]
print(len(teams))   # 10가지 (5C2)
```

**예제 3: 메뉴 세트 — 음식 × 음료 × 디저트 모든 조합**

```python
from itertools import product

food    = ["치킨", "피자"]
drink   = ["콜라", "사이다"]
dessert = ["아이스크림"]

all_sets = list(product(food, drink, dessert))
for s in all_sets:
    print(" + ".join(s))
# 치킨 + 콜라 + 아이스크림
# 치킨 + 사이다 + 아이스크림
# 피자 + 콜라 + 아이스크림
# 피자 + 사이다 + 아이스크림
```

---

## 6. 순열 vs 조합 vs 곱집합 비교

```
함수                          설명                순서   중복   경우의 수
───────────────────────────────────────────────────────────────────────
permutations(lst, r)         순열                있음   없음   nPr
combinations(lst, r)         조합                없음   없음   nCr
combinations_with_replacement 중복 조합           없음   있음   nHr
product(lst1, lst2, ...)     곱집합 (각 그룹에서 1개씩)  있음   가능   n1 × n2 × ...
product(lst, repeat=r)       중복 순열            있음   있음   n^r
```

---

## 7. 마지막 정리

- `itertools`는 순열·조합·곱집합 등 **모든 경우의 수를 자동으로 생성**해주는 모듈이다.
- **순열** `permutations(lst, r)` — 순서 있음, 중복 없음. (A→B)와 (B→A)는 다른 경우.
- **조합** `combinations(lst, r)` — 순서 없음, 중복 없음. (A,B)와 (B,A)는 같은 경우.
- **곱집합** `product(lst1, lst2)` — 여러 그룹에서 각각 하나씩 선택. 중첩 for문 대체.
- 결과는 **이터레이터**로 반환되므로 `list()`로 변환해서 사용해야 한다.
- 코딩테스트 완전탐색(브루트포스) 문제에서 **경우의 수를 직접 구현하는 대신** itertools를 쓰면 훨씬 간결하다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "itertools",
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