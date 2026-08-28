# [Python 기초] itertools (순열 / 조합 / 곱집합)

# 본문

## 1. 한 줄 요약

`itertools`는 반복 가능한 데이터에서 순열, 조합, 곱집합 같은 반복 패턴을 쉽게 만들 수 있게 해주는 표준 라이브러리이다.

`itertools`를 이해하면 완전탐색 문제에서 가능한 경우의 수를 깔끔하게 생성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

코딩 테스트에서는 가능한 경우를 모두 만들어 확인해야 하는 문제가 자주 나온다.

예를 들어 카드 `[1, 2, 3]` 중에서 2장을 뽑는 모든 경우를 생각해 보자.

```text
1, 2
1, 3
2, 3
```

직접 반복문으로 만들 수도 있다.

```python
cards = [1, 2, 3]

for i in range(len(cards)):
    for j in range(i + 1, len(cards)):
        print(cards[i], cards[j])
```

하지만 뽑는 개수가 늘어나거나 순서까지 고려해야 하면 코드가 복잡해진다.

`itertools`를 사용하면 이런 경우의 수 생성을 간단하게 표현할 수 있다.

```python
from itertools import combinations

cards = [1, 2, 3]
print(list(combinations(cards, 2)))
```

`itertools`는 **반복되는 경우의 수 생성을 도와주는 도구**이다.

---

## 3. 핵심 아이디어

`itertools`는 경우의 수를 자동으로 만들어주는 조합 기계라고 생각할 수 있다.

재료를 넣으면 가능한 묶음을 만들어준다.

```text
재료

[1] [2] [3]

조합 기계
   │
   ▼
(1, 2), (1, 3), (2, 3)
```

대표 기능은 다음과 같다.

```text
permutations   → 순서를 고려해서 뽑기
combinations   → 순서 없이 뽑기
product        → 여러 묶음에서 하나씩 뽑는 모든 경우
```

순열은 순서가 중요하다.

```text
(1, 2)와 (2, 1)을 다르게 봄
```

조합은 순서가 중요하지 않다.

```text
(1, 2)와 (2, 1)을 같은 경우로 봄
```

곱집합은 여러 선택지를 모두 조합한다.

```text
상의: 빨강, 파랑
하의: 검정, 흰색

빨강-검정
빨강-흰색
파랑-검정
파랑-흰색
```

---

## 4. 동작 과정 살펴보기

### 4-1. combinations로 조합 만들기

```python
from itertools import combinations

items = [1, 2, 3]
result = combinations(items, 2)
```

2개씩 뽑되 순서는 고려하지 않는다.

```text
items

[1] [2] [3]
```

가능한 조합은 다음과 같다.

```text
1과 2 → (1, 2)
1과 3 → (1, 3)
2와 3 → (2, 3)
```

결과는 다음과 같다.

```python
[(1, 2), (1, 3), (2, 3)]
```

### 4-2. permutations로 순열 만들기

```python
from itertools import permutations

items = [1, 2, 3]
result = permutations(items, 2)
```

2개씩 뽑고 순서도 고려한다.

```text
1 다음 2 → (1, 2)
2 다음 1 → (2, 1)

서로 다른 경우로 봄
```

가능한 결과는 다음과 같다.

```text
(1, 2), (1, 3)
(2, 1), (2, 3)
(3, 1), (3, 2)
```

### 4-3. product로 곱집합 만들기

```python
from itertools import product

colors = ["빨강", "파랑"]
sizes = ["S", "M"]
```

각 그룹에서 하나씩 고르는 모든 경우를 만든다.

```text
빨강 + S
빨강 + M
파랑 + S
파랑 + M
```

---

## 5. 구현 코드 및 상세 설명

```python
from itertools import combinations, permutations, product

items = [1, 2, 3]

# 조합: 순서를 고려하지 않고 2개 뽑기
comb = list(combinations(items, 2))
print("조합:", comb)

# 순열: 순서를 고려해서 2개 뽑기
perm = list(permutations(items, 2))
print("순열:", perm)

# 곱집합: 각 그룹에서 하나씩 뽑는 모든 경우
colors = ["빨강", "파랑"]
sizes = ["S", "M"]

cases = list(product(colors, sizes))
print("곱집합:", cases)

# 중복을 허용한 곱집합
dice = [1, 2, 3]
double_dice = list(product(dice, repeat=2))
print("주사위 두 번:", double_dice)
```

### 코드 설명

```python
combinations(items, 2)
```

`items`에서 2개를 뽑는 조합을 만든다.

순서를 고려하지 않기 때문에 `(1, 2)`와 `(2, 1)`은 같은 것으로 본다.

```python
permutations(items, 2)
```

`items`에서 2개를 뽑는 순열을 만든다.

순서를 고려하기 때문에 `(1, 2)`와 `(2, 1)`을 다른 경우로 본다.

```python
product(colors, sizes)
```

`colors`에서 하나, `sizes`에서 하나를 선택하는 모든 경우를 만든다.

```text
("빨강", "S")
("빨강", "M")
("파랑", "S")
("파랑", "M")
```

```python
product(dice, repeat=2)
```

`dice`를 두 번 반복해서 선택하는 모든 경우를 만든다.

주사위를 두 번 던지는 경우와 비슷하다.

```text
(1, 1), (1, 2), (1, 3)
(2, 1), (2, 2), (2, 3)
(3, 1), (3, 2), (3, 3)
```

---

## 6. 마지막 정리

`itertools`는 반복 패턴과 경우의 수를 쉽게 만들어주는 표준 라이브러리이다.

`combinations`는 순서를 고려하지 않고 뽑을 때 사용한다.

`permutations`는 순서를 고려해서 뽑을 때 사용한다.

`product`는 여러 선택지의 모든 조합을 만들 때 사용한다.

완전탐색 문제에서 가능한 경우를 만들 때 매우 유용하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 itertools",
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
