# [Python 기초] lambda (람다)

# 본문

## 1. 한 줄 요약

람다는 이름 없는 짧은 함수를 한 줄로 정의하는 파이썬 문법이다.

람다를 이해하면 정렬 기준, 간단한 변환 함수, 일회성 함수가 필요한 상황에서 코드를 간결하게 작성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

파이썬에서는 함수를 값처럼 전달해야 하는 상황이 있다.

대표적인 예가 정렬 기준을 지정하는 경우다.

```python
students = [("민수", 80), ("지은", 95), ("현우", 70)]
```

이 리스트를 점수 기준으로 정렬하고 싶다면, 각 학생 데이터에서 점수만 꺼내는 함수가 필요하다.

일반 함수로 작성하면 다음과 같다.

```python
def get_score(student):
    return student[1]

students.sort(key=get_score)
```

이 함수는 한 번만 사용되고, 동작도 매우 단순하다.

이럴 때 매번 `def`로 함수를 만드는 것은 코드가 다소 길게 느껴질 수 있다.

람다를 사용하면 같은 내용을 한 줄로 표현할 수 있다.

```python
students.sort(key=lambda student: student[1])
```

즉, 람다는 **짧고 단순한 함수를 임시로 만들어 전달해야 할 때** 유용하다.

---

## 3. 핵심 아이디어

람다는 일반 함수의 축약형이다.

아래 두 코드는 거의 같은 의미를 가진다.

```python
def add(a, b):
    return a + b
```

```python
lambda a, b: a + b
```

구조를 나누면 다음과 같다.

```text
lambda 입력값: 반환값

lambda a, b: a + b
       │       │
       │       └─ 함수가 돌려줄 결과
       └─ 함수가 받을 값
```

일반 함수는 이름을 가진다.

```text
add ─────▶ 두 값을 더하는 함수
```

람다는 이름 없이 바로 만들어진다.

```text
lambda a, b: a + b

이름 없는 함수
```

람다는 주로 변수에 저장하거나, 다른 함수의 인자로 바로 전달한다.

```python
add = lambda a, b: a + b
```

하지만 복잡한 로직을 람다로 작성하는 것은 좋지 않다.

람다는 짧고 명확한 계산에 사용할 때 가장 적합하다.

---

## 4. 동작 과정 살펴보기

아래 예제를 분석해 보자.

```python
students = [("민수", 80), ("지은", 95), ("현우", 70)]

students.sort(key=lambda student: student[1])
```

### Step 1. 정렬할 데이터가 준비된다

```text
students

[("민수", 80)] [("지은", 95)] [("현우", 70)]
```

각 학생 데이터는 튜플이다.

```text
("민수", 80)
  │     │
 이름   점수
```

### Step 2. 정렬 기준 함수가 필요하다

그냥 정렬하면 파이썬은 앞의 값부터 비교한다.

하지만 여기서는 이름이 아니라 점수를 기준으로 정렬하고 싶다.

그래서 각 학생 데이터에서 점수만 꺼내는 기준 함수가 필요하다.

```text
("민수", 80) → 80
("지은", 95) → 95
("현우", 70) → 70
```

### Step 3. 람다가 점수를 꺼낸다

```python
lambda student: student[1]
```

이 람다는 학생 튜플 하나를 받아서 1번 위치의 값을 반환한다.

```text
student = ("민수", 80)

student[1] → 80
```

```text
student = ("지은", 95)

student[1] → 95
```

```text
student = ("현우", 70)

student[1] → 70
```

### Step 4. 점수를 기준으로 정렬된다

```text
정렬 기준값

("민수", 80) → 80
("지은", 95) → 95
("현우", 70) → 70
```

오름차순 정렬 결과는 다음과 같다.

```text
[("현우", 70), ("민수", 80), ("지은", 95)]
```

---

## 5. 구현 코드 및 상세 설명

```python
# 숫자 두 개를 더하는 람다
add = lambda a, b: a + b

print(add(3, 5))


# 학생 정보를 점수 기준으로 정렬
students = [("민수", 80), ("지은", 95), ("현우", 70)]

students.sort(key=lambda student: student[1])

print(students)


# 문자열 길이를 기준으로 정렬
words = ["banana", "cat", "apple"]

words.sort(key=lambda word: len(word))

print(words)
```

### 코드 설명

```python
add = lambda a, b: a + b
```

두 값을 입력받아 더한 결과를 반환하는 람다 함수다.

일반 함수로 쓰면 다음과 같다.

```python
def add(a, b):
    return a + b
```

람다는 `return`을 직접 쓰지 않는다.

콜론 오른쪽 표현식의 결과가 자동으로 반환된다.

```python
students.sort(key=lambda student: student[1])
```

학생 리스트를 정렬한다.

이때 `key`에는 정렬 기준을 만드는 함수가 들어간다.

```text
("민수", 80) → 80
("지은", 95) → 95
("현우", 70) → 70
```

파이썬은 이 기준값을 이용해 학생들을 정렬한다.

```python
words.sort(key=lambda word: len(word))
```

문자열의 길이를 기준으로 정렬한다.

```text
"banana" → 6
"cat"    → 3
"apple"  → 5
```

정렬 결과는 길이가 짧은 순서가 된다.

```text
["cat", "apple", "banana"]
```

---

## 6. 마지막 정리

람다는 이름 없는 짧은 함수를 만드는 문법이다.

기본 구조는 `lambda 매개변수: 반환값`이다.

람다는 `return`을 쓰지 않고 콜론 오른쪽 결과를 자동으로 반환한다.

정렬 기준을 지정할 때 자주 사용된다.

복잡한 로직은 람다보다 일반 함수로 작성하는 것이 읽기 좋다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 람다",
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
