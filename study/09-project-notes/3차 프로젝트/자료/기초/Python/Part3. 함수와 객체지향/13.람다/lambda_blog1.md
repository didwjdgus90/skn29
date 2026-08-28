# [Python 기초] lambda (람다)

---

# 링크
<https://coding-factory.tistory.com/990>

---

## 1. 한 줄 요약

lambda는 **이름 없이 한 줄로 만드는 간이 함수**다. `def`로 함수를 만드는 것과 같은 역할을 하지만, 이름을 붙이지 않아도 되고 한 줄로 끝나는 간단한 함수를 만들 때 사용한다.

---

## 2. 왜 lambda가 필요할까?

두 수를 더하는 함수가 필요하다고 해보자. 일반적으로는 `def`로 정의한다.

```python
def add(x, y):
    return x + y

result = add(3, 5)
print(result)   # 8
```

그런데 이 함수가 딱 한 번만 쓰이고 다시 쓸 일이 없다면? 굳이 이름을 붙이고 여러 줄을 쓰는 게 번거롭다. lambda를 쓰면 한 줄로 끝낼 수 있다.

```python
add = lambda x, y: x + y
print(add(3, 5))   # 8
```

lambda의 진짜 장점은 **변수에 저장하는 용도**보다, `sorted()`, `map()`, `filter()` 같은 함수에 **인자로 바로 넘길 때** 빛난다. 이름이 필요 없는 짧은 함수를 그 자리에서 만들어서 바로 사용하는 것이다.

```python
# 이름이 없어도 바로 쓸 수 있다
numbers = [3, 1, 4, 1, 5]
numbers.sort(key=lambda x: -x)   # 내림차순 정렬
print(numbers)   # [5, 4, 3, 1, 1]
```

---

## 3. 핵심 아이디어 — lambda는 "즉석 함수"다

lambda를 **즉석 조리 식품**으로 비유해보자.

정식 함수(`def`)는 레시피를 적고, 이름을 붙이고, 언제든 꺼내 쓸 수 있게 만들어두는 것이다. lambda는 **지금 딱 한 번만 쓸 간단한 요리를 즉석에서 만드는 것**이다. 레시피를 따로 적을 필요 없이 바로 만들어서 쓰고 끝낸다.

```
def 함수:                         lambda:
  def add(x, y):          vs      lambda x, y: x + y
      return x + y
  (여러 줄, 이름 있음)             (한 줄, 이름 없음)
```

둘 다 "함수"라는 본질은 같다. 차이는 이름이 있느냐 없느냐, 그리고 여러 줄을 쓸 수 있느냐 없느냐다.

---

## 4. 동작 과정 살펴보기

### 4-1. 기본 구조

```
lambda  매개변수  :  반환할 표현식
   ↑        ↑              ↑
키워드    입력값         결과값 (자동으로 return됨)
```

`def` 함수와 나란히 비교하면 구조가 명확해진다.

```python
# def 함수
def square(x):
    return x ** 2

# lambda 함수 (완전히 동일한 기능)
square = lambda x: x ** 2

print(square(4))   # 16
```

```
대응 구조:

def  square  (x)  :  return x ** 2
     이름    인자          표현식

lambda       (x)  :         x ** 2
  (이름 없음) 인자          표현식 (자동 return)
```

lambda는 `return`을 직접 쓰지 않아도 콜론(`:`) 오른쪽의 표현식이 자동으로 반환된다.

### 4-2. 매개변수 다양하게 쓰기

```python
# 매개변수 없음
greet = lambda: "안녕하세요!"
print(greet())   # 안녕하세요!

# 매개변수 1개
double = lambda x: x * 2
print(double(5))   # 10

# 매개변수 여러 개
add = lambda x, y: x + y
print(add(3, 4))   # 7

# 기본값 지정
power = lambda x, n=2: x ** n
print(power(3))     # 9  (기본값 n=2)
print(power(3, 3))  # 27 (n=3으로 지정)
```

### 4-3. 조건식 사용하기

lambda 안에서 조건에 따라 다른 값을 반환하려면 `if-else` 삼항 표현식을 쓴다. 이전에 배운 리스트 컴프리헨션의 `값 if 조건 else 값`과 같은 형태다.

```python
# 짝수면 True, 홀수면 False
is_even = lambda x: True if x % 2 == 0 else False
print(is_even(4))   # True
print(is_even(7))   # False

# 양수면 "양수", 음수면 "음수", 0이면 "영"
classify = lambda x: "양수" if x > 0 else ("음수" if x < 0 else "영")
print(classify(5))    # 양수
print(classify(-3))   # 음수
print(classify(0))    # 영
```

> ⚠️ lambda 안에는 `if-else` 표현식은 쓸 수 있지만, 일반 `if`문(블록 형태)이나 `for`문 같은 복잡한 문장은 쓸 수 없다. 한 줄로 표현이 안 되면 `def` 함수를 쓰자.

---

## 5. 구현 코드 및 상세 설명

### 5-1. sorted()와 함께 — 정렬 기준 지정

lambda가 가장 자주 쓰이는 패턴이다. `sorted()`나 `.sort()`의 `key` 인자에 넣어 정렬 기준을 직접 지정한다.

```python
# 절댓값 기준 정렬
nums = [3, -7, 1, -2, 5]
sorted(nums, key=lambda x: abs(x))
# [1, -2, 3, 5, -7]

# 문자열 길이순 정렬
words = ["banana", "kiwi", "apple", "cherry"]
sorted(words, key=lambda x: len(x))
# ['kiwi', 'apple', 'banana', 'cherry']

# 딕셔너리 리스트를 특정 키 기준으로 정렬
students = [
    {"name": "철수", "score": 85},
    {"name": "영희", "score": 92},
    {"name": "민수", "score": 78},
]
sorted(students, key=lambda s: s["score"], reverse=True)
# [{"name": "영희", ...}, {"name": "철수", ...}, {"name": "민수", ...}]
```

```
key=lambda x: abs(x) 동작:

nums = [3, -7, 1, -2, 5]
각 요소에 lambda 적용:
  3  → abs(3)  = 3
 -7  → abs(-7) = 7
  1  → abs(1)  = 1
 -2  → abs(-2) = 2
  5  → abs(5)  = 5
비교 기준: 1 < 2 < 3 < 5 < 7
결과: [1, -2, 3, 5, -7]
```

---

### 5-2. map()과 함께 — 모든 요소에 함수 적용

`map(함수, 목록)`은 목록의 **모든 요소에 함수를 적용**한 결과를 반환한다. 컨베이어 벨트 위의 물건들을 하나씩 같은 가공 작업을 거쳐 내보내는 것과 같다.

```
map() 동작 원리:

입력: [1, 2, 3, 4, 5]
함수: lambda x: x ** 2 (각 요소를 제곱)
       ↓  ↓  ↓  ↓  ↓
출력: [1, 4, 9, 16, 25]
```

```python
numbers = [1, 2, 3, 4, 5]

# 각 요소를 제곱
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]

# 각 요소를 문자열로 변환
str_nums = list(map(lambda x: str(x) + "점", numbers))
print(str_nums)   # ['1점', '2점', '3점', '4점', '5점']
```

`map()`은 결과를 바로 리스트로 주지 않고 `map` 객체를 반환한다. 그래서 `list()`로 감싸줘야 리스트로 볼 수 있다.

같은 결과를 리스트 컴프리헨션으로도 쓸 수 있다. 어떤 게 더 읽기 편한지 상황에 따라 선택하면 된다.

```python
# map + lambda
list(map(lambda x: x ** 2, numbers))

# 리스트 컴프리헨션 (같은 결과)
[x ** 2 for x in numbers]
```

---

### 5-3. filter()와 함께 — 조건에 맞는 요소만 걸러내기

`filter(함수, 목록)`은 목록에서 **함수가 True를 반환하는 요소만** 골라낸다. 체에 거르는 것과 같다. 조건을 만족하는 것만 통과한다.

```
filter() 동작 원리:

입력: [1, 2, 3, 4, 5, 6, 7, 8, 9]
함수: lambda x: x % 2 == 0 (짝수만 통과)
   1 ❌  2 ✅  3 ❌  4 ✅  5 ❌  6 ✅  7 ❌  8 ✅  9 ❌
출력: [2, 4, 6, 8]
```

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 짝수만 걸러내기
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6, 8]

# 5보다 큰 수만 걸러내기
big = list(filter(lambda x: x > 5, numbers))
print(big)   # [6, 7, 8, 9]

# 빈 문자열 제거
words = ["apple", "", "banana", "", "kiwi"]
non_empty = list(filter(lambda x: x != "", words))
print(non_empty)   # ['apple', 'banana', 'kiwi']
```

`filter()`도 `map()`처럼 `filter` 객체를 반환하므로, `list()`로 감싸서 리스트로 변환해야 한다.

---

### 5-4. map vs filter vs 리스트 컴프리헨션

세 가지 모두 리스트를 처리하는 도구다. 각각의 역할과 리스트 컴프리헨션과의 관계를 정리하면 이렇다.

```
도구         역할              리스트 컴프리헨션으로 표현
─────────────────────────────────────────────────────────────────
map()       모두 변환         [f(x) for x in lst]
filter()    조건으로 걸러내기  [x for x in lst if 조건]
둘 다       변환 + 필터링     [f(x) for x in lst if 조건]
```

```python
nums = [1, 2, 3, 4, 5, 6]

# 짝수만 제곱 — filter + map 조합
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))

# 리스트 컴프리헨션으로 같은 결과 (더 읽기 쉬움)
result = [x**2 for x in nums if x % 2 == 0]

print(result)   # [4, 16, 36]
```

대부분의 경우 리스트 컴프리헨션이 더 읽기 쉽다. `map`과 `filter`를 중첩해서 쓰면 오히려 복잡해진다. 실전에서는 **lambda + `sorted(key=...)`** 조합이 가장 자주 쓰인다.

---

## 6. def 함수 vs lambda — 언제 뭘 쓸까?

lambda는 강력하지만, 무조건 쓰는 게 좋은 건 아니다.

```
항목              def 함수                 lambda
────────────────────────────────────────────────────────────
이름              있음                     없음
줄 수             여러 줄 가능             한 줄만
복잡한 로직       가능                     불가
재사용            이름으로 여러 번 호출    주로 그 자리에서 1회 사용
가독성            복잡한 경우 명확         너무 길면 오히려 난해
```

**lambda를 쓰면 좋은 경우**

- `sorted()`, `map()`, `filter()`의 `key`나 인자로 바로 넘길 때
- 한 번만 쓰는 아주 간단한 함수일 때
- 함수에 이름을 붙일 가치가 없을 만큼 짧고 명확할 때

**def 함수를 쓰는 게 나은 경우**

- 같은 함수를 여러 곳에서 재사용해야 할 때
- 로직이 복잡해서 여러 줄이 필요할 때
- 함수에 의미 있는 이름을 붙이면 코드가 더 읽기 쉬울 때

```python
# ❌ lambda를 굳이 변수에 저장할 이유가 없다
add = lambda x, y: x + y   # def 함수가 더 낫다

# ✅ lambda가 빛나는 순간 — 정렬 기준으로 바로 넘기기
students.sort(key=lambda s: s["score"])

# ❌ 너무 복잡한 lambda — 읽기 어려움
f = lambda x: x**2 if x > 0 else (-x)**2 if x < 0 else 0

# ✅ 이런 경우엔 def가 낫다
def f(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return (-x) ** 2
    else:
        return 0
```

---

## 7. 마지막 정리

- lambda는 `lambda 매개변수: 표현식` 형태로 **이름 없는 간이 함수**를 만든다.
- 콜론(`:`) 오른쪽의 표현식이 **자동으로 반환**된다. `return`을 쓰지 않는다.
- lambda 안에서는 **한 줄 표현식만** 쓸 수 있다. 복잡한 로직은 `def` 함수를 쓰자.
- **`sorted(key=lambda ...)`** 조합이 실전에서 가장 자주 쓰인다.
- `map(lambda, 목록)`은 모든 요소를 **변환**, `filter(lambda, 목록)`은 조건에 맞는 요소만 **필터링**한다.
- 대부분의 `map/filter` 작업은 **리스트 컴프리헨션**으로 더 읽기 쉽게 쓸 수 있다.
- lambda를 **변수에 저장해서 재사용**할 거라면 그냥 `def` 함수를 만드는 게 낫다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "lambda",
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