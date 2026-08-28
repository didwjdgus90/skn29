# [Python 기초] 정렬 (sort / sorted)

---

# 링크
<https://dev-records.tistory.com/entry/Python-%EB%A6%AC%EC%8A%A4%ED%8A%B8List-%EC%A0%95%EB%A0%AC%ED%95%98%EA%B8%B0-feat-sort-sorted>

---

## 1. 한 줄 요약

파이썬에서 리스트를 정렬하는 방법은 두 가지다. **`.sort()`는 원본 리스트를 직접 바꾸고**, **`sorted()`는 원본은 그대로 두고 정렬된 새 리스트를 반환한다.** 이 차이를 이해하는 것이 핵심이다.

---

## 2. 왜 정렬 방법이 두 가지일까?

정렬은 코딩 어디서나 자주 쓰인다. 성적 순서 나열, 가격 낮은 순 정렬, 이름 가나다순 출력 등 데이터를 다루다 보면 반드시 만나게 된다.

파이썬은 정렬하는 방법을 두 가지로 나눠놨다. **원본 데이터를 바꿔도 되는 상황**과 **원본은 유지하면서 정렬된 결과만 필요한 상황**이 각각 다르기 때문이다.

예를 들어, 학생 점수 목록이 있다고 하자. 순위를 출력할 때는 정렬된 복사본이 필요하고, 원본 목록은 그대로 남겨야 할 수 있다. 반대로 그냥 리스트를 정리해서 덮어써도 상관없는 경우도 있다.

이 두 상황을 위해 `.sort()`와 `sorted()`가 각각 존재한다.

---

## 3. 핵심 아이디어 — `.sort()` vs `sorted()`

두 함수의 차이를 가장 직관적으로 보여주는 비유가 있다.

> `.sort()`는 **책장을 직접 정리**하는 것이다. 책 순서가 바뀐다.
> `sorted()`는 **정리된 목록을 종이에 따로 적는** 것이다. 책장은 그대로다.

```
원본 리스트:  [3, 1, 4, 2, 5]

.sort() 사용:
  원본 → [1, 2, 3, 4, 5]   ← 원본 자체가 바뀜
  반환값 → None             ← 아무것도 돌려주지 않음

sorted() 사용:
  원본 → [3, 1, 4, 2, 5]   ← 원본 그대로 유지
  반환값 → [1, 2, 3, 4, 5]  ← 정렬된 새 리스트를 돌려줌
```

이 차이가 실수로 이어지는 경우가 많다. `.sort()`의 결과를 변수에 담으면 `None`이 저장되기 때문이다.

```python
nums = [3, 1, 4, 2, 5]

# ❌ 흔한 실수
result = nums.sort()
print(result)   # None ← .sort()는 반환값이 없음!

# ✅ 올바른 사용
nums.sort()
print(nums)     # [1, 2, 3, 4, 5] ← 원본이 직접 바뀜

# ✅ sorted()는 반환값을 변수에 담는다
result = sorted(nums)
print(result)   # [1, 2, 3, 4, 5]
print(nums)     # [3, 1, 4, 2, 5] ← 원본은 그대로
```

---

## 4. 동작 과정 살펴보기

### 4-1. 기본 정렬 — 오름차순

두 함수 모두 기본값은 **오름차순(작은 것부터 큰 것 순서)** 이다. 숫자는 크기순, 문자열은 알파벳·가나다 순서로 정렬된다.

```python
# 숫자 정렬
nums = [3, 1, 4, 2, 5]
nums.sort()
print(nums)   # [1, 2, 3, 4, 5]

# 문자 정렬 (알파벳 순서)
letters = ['y', 'a', 'd', 'k', 'f']
letters.sort()
print(letters)   # ['a', 'd', 'f', 'k', 'y']

# 문자열 정렬 (첫 글자 → 두 번째 글자 순서로 비교)
words = ['zah', 'abc', 'def', 'ag']
print(sorted(words))   # ['abc', 'ag', 'def', 'zah']
```

문자열 정렬은 사전처럼 동작한다. `'abc'`와 `'ag'`를 비교할 때 첫 글자 `'a'`가 같으면 두 번째 글자 `'b'`와 `'g'`를 비교한다. `'b'`가 `'g'`보다 알파벳 앞이므로 `'abc'`가 먼저 온다.

---

### 4-2. 내림차순 — `reverse=True`

오름차순과 반대 방향으로 정렬하려면 `reverse=True` 옵션을 넣어준다.

```python
nums = [3, 1, 4, 2, 5]

# 내림차순 정렬
nums.sort(reverse=True)
print(nums)   # [5, 4, 3, 2, 1]

# sorted()도 동일하게 사용
words = ['zah', 'abc', 'def', 'ag']
print(sorted(words, reverse=True))   # ['zah', 'def', 'ag', 'abc']
```

`reverse=True`는 "정렬 방향을 뒤집어라"는 뜻이다. 오름차순으로 정렬한 결과를 다시 뒤집는 것과 같다.

---

## 5. 구현 코드 및 상세 설명

### 5-1. key — 정렬 기준 직접 지정하기

단순한 오름차순·내림차순이 아닌, **내가 원하는 기준**으로 정렬하고 싶을 때 `key` 옵션을 쓴다.

`key`에는 **"각 요소를 어떤 값으로 바꿔서 비교할지"를 정하는 함수**를 넣는다. 파이썬이 정렬할 때 각 요소에 이 함수를 적용한 결과를 기준으로 순서를 정한다.

비유하자면 이렇다. 사람들을 키 순서로 세우고 싶다면 각 사람의 키를 재서 비교한다. 이때 "키를 재는 방법"이 바로 `key` 함수다.

```
정렬 전:  ['apple', 'kiwi', 'banana', 'orange']
key=len 적용:
  'apple'  → len('apple')  = 5
  'kiwi'   → len('kiwi')   = 4
  'banana' → len('banana') = 6
  'orange' → len('orange') = 6
비교 결과: 4 < 5 < 6 = 6
정렬 후:  ['kiwi', 'apple', 'banana', 'orange']
```

```python
words = ['apple', 'kiwi', 'banana', 'orange']

# 문자열 길이순 정렬
words.sort(key=len)
print(words)   # ['kiwi', 'apple', 'banana', 'orange']

# 절댓값 기준 정렬
nums = [3, -6, 1, -8, 2, -5]
nums.sort(key=abs)
print(nums)   # [1, 2, 3, -5, -6, -8]
```

`len`은 "길이를 반환하는 함수", `abs`는 "절댓값을 반환하는 함수"다. `key=len`이라고 쓰면 "각 요소의 길이를 기준으로 비교해라"는 뜻이 된다.

---

### 5-2. lambda — 내가 직접 만드는 기준

`key`에 `len`이나 `abs` 같은 내장 함수 말고, **직접 만든 기준**을 넣고 싶을 때 `lambda`를 쓴다.

`lambda`는 **이름 없는 짧은 함수**다. 한 번만 쓸 간단한 함수를 만들 때 사용한다. 형태는 이렇다.

```
lambda 입력값 : 반환할 값

예시:
lambda x: x[1]   →  x를 받아서 x의 1번 요소를 반환하는 함수
lambda x: -x     →  x를 받아서 -x를 반환하는 함수
```

`lambda`를 처음 보면 낯설게 느껴진다. 하지만 "각 요소(x)를 받아서 비교 기준(반환 값)을 알려주는 함수"라고 이해하면 된다.

**예시 1: 튜플 리스트를 두 번째 요소 기준으로 정렬**

```python
fruits = [('apple', 3), ('banana', 1), ('kiwi', 2), ('orange', 4)]

# 두 번째 요소(수량)를 기준으로 오름차순 정렬
fruits.sort(key=lambda x: x[1])
print(fruits)
# [('banana', 1), ('kiwi', 2), ('apple', 3), ('orange', 4)]
```

```
lambda x: x[1] 동작:

('apple', 3)  → x = ('apple', 3) → x[1] = 3  (비교 기준)
('banana', 1) → x = ('banana',1) → x[1] = 1
('kiwi', 2)   → x = ('kiwi', 2)  → x[1] = 2
('orange', 4) → x = ('orange',4) → x[1] = 4

1 < 2 < 3 < 4  순서로 정렬
```

**예시 2: 내림차순에 lambda 사용**

내림차순은 `reverse=True`를 쓰거나, `lambda`에서 값에 `-`(마이너스)를 붙여도 같은 효과가 난다.

```python
items = [['apple', 3], ['banana', 1], ['kiwi', 2], ['orange', 4]]

# 방법 1: reverse=True
items.sort(key=lambda x: x[1], reverse=True)

# 방법 2: 값에 - 붙이기 (숫자일 때만 가능)
items.sort(key=lambda x: -x[1])

print(items)
# [['orange', 4], ['apple', 3], ['kiwi', 2], ['banana', 1]]
```

**예시 3: 두 가지 기준으로 동시에 정렬 (다중 정렬)**

여러 기준을 동시에 적용하고 싶을 때는 `lambda`에서 **튜플**로 여러 기준을 묶어서 반환한다. 파이썬은 튜플을 비교할 때 첫 번째 요소부터 순서대로 비교하기 때문이다.

```python
data = [
    ['apple',  1, 300],
    ['banana', 2, 150],
    ['kiwi',   2, 400],
    ['orange', 1, 1000]
]

# 두 번째 요소 내림차순, 두 번째가 같으면 세 번째 요소 오름차순
data.sort(key=lambda x: (-x[1], x[2]))
print(data)
# [['banana', 2, 150], ['kiwi', 2, 400], ['apple', 1, 300], ['orange', 1, 1000]]
```

```
정렬 기준 설명:

(-x[1], x[2]) 형태의 튜플을 비교:
  1순위: -x[1] (두 번째 요소의 음수 → 내림차순)
  2순위: x[2]  (세 번째 요소 → 오름차순)

banana: (-2, 150)
kiwi:   (-2, 400)  ← -2로 같으니 150 vs 400 비교 → banana 먼저
apple:  (-1, 300)
orange: (-1, 1000) ← -1로 같으니 300 vs 1000 비교 → apple 먼저

최종 순서: banana → kiwi → apple → orange
```

---

### 5-3. 뒤집기 — `reverse()`와 `reversed()`

정렬과 별개로, 현재 순서를 그냥 **뒤집기만** 하고 싶을 때는 `reverse()`와 `reversed()`를 쓴다. 정렬하는 게 아니라 순서만 반전시키는 것이다.

```python
nums = [1, 3, 2, 5, 4]

# .reverse() — 원본을 직접 뒤집음 (.sort()와 같은 방식)
nums.reverse()
print(nums)   # [4, 5, 2, 3, 1]

# reversed() — 원본 그대로, 뒤집힌 결과를 반환 (sorted()와 같은 방식)
nums = [1, 3, 2, 5, 4]
result = list(reversed(nums))   # 반환값을 list()로 감싸야 리스트로 받을 수 있음
print(result)   # [4, 5, 2, 3, 1]
print(nums)     # [1, 3, 2, 5, 4] ← 원본은 그대로
```

---

### 5-4. 문자열 정렬 — 대소문자 처리 주의

문자열을 정렬할 때 파이썬은 대문자가 소문자보다 앞에 온다. 알파벳 소문자 `'a'`와 대문자 `'A'`를 비교하면 `'A'`가 먼저다.

```python
words = ['banana', 'Apple', 'cherry', 'Blueberry']
words.sort()
print(words)   # ['Apple', 'Blueberry', 'banana', 'cherry']
# 대문자로 시작하는 단어가 소문자보다 앞에 옴!
```

대소문자를 무시하고 알파벳순으로만 정렬하고 싶다면 `key=str.lower`를 사용한다.

```python
words = ['banana', 'Apple', 'cherry', 'Blueberry']
words.sort(key=str.lower)
print(words)   # ['Apple', 'banana', 'Blueberry', 'cherry']
# 대소문자 구분 없이 알파벳 순서로 정렬됨
```

`key=str.lower`는 각 문자열을 소문자로 바꿔서 비교하되, 실제 리스트에 저장된 값은 원래 대소문자 그대로 유지된다는 점을 기억하자.

---

## 6. sort() vs sorted() 정리

```
비교 항목          .sort()               sorted()
──────────────────────────────────────────────────────
원본 변경 여부     변경됨 ❗              변경 안 됨 ✅
반환값             None                  정렬된 새 리스트
사용 형태          리스트.sort()          sorted(리스트)
사용 가능 대상     리스트만              리스트, 튜플, 문자열 등 모두

언제 쓰나:
  .sort()  → 원본을 정렬된 상태로 바꿔도 될 때 (메모리 효율적)
  sorted() → 원본은 남겨두고 정렬된 결과만 따로 필요할 때
```

---

## 7. 마지막 정리

- `.sort()`는 **원본을 직접 바꾸고 반환값은 없다(None)**. `result = lst.sort()`처럼 결과를 받으면 `None`이 저장된다.
- `sorted()`는 **원본은 그대로 두고 정렬된 새 리스트를 반환**한다. 반드시 변수에 담아 써야 한다.
- `reverse=True` 옵션으로 **내림차순** 정렬을 할 수 있다.
- `key` 옵션에 함수를 넣어 **원하는 기준**으로 정렬할 수 있다. `len`, `abs` 같은 내장 함수나 `lambda`를 활용한다.
- `lambda x: x[1]`은 "각 요소의 1번 인덱스 값을 기준으로 삼아라"는 뜻이다.
- 여러 기준을 동시에 적용하려면 `lambda`에서 **튜플로 여러 기준을 묶어** 반환한다.
- **대소문자 구분 없이** 문자열을 정렬하려면 `key=str.lower`를 사용한다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "정렬",
  "source_type": "blog",
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