# [Python 기초] lambda (람다)

# 본문

## 1. 한 줄 요약

람다는 아주 짧은 함수를 이름 없이 즉석에서 만드는 방법이다.

람다를 배우면 잠깐만 필요한 간단한 기능을 한 줄로 만들 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

함수는 보통 이름을 붙여서 만든다.

```python
def double(x):
    return x * 2
```

이 함수는 숫자를 두 배로 만든다.

그런데 어떤 함수는 프로그램 전체에서 계속 쓰는 것이 아니라, 딱 한 번만 필요할 때가 있다.

예를 들어 정렬할 때 "점수만 보고 정렬해줘"라고 잠깐 알려주는 함수가 필요할 수 있다.

```python
students = [("민수", 80), ("지은", 95), ("현우", 70)]
```

이때 점수만 꺼내는 함수를 따로 길게 만드는 대신 람다를 쓸 수 있다.

```python
students.sort(key=lambda student: student[1])
```

람다는 **잠깐 쓰는 작은 메모지 같은 함수**이다.

오래 보관할 설명서는 `def`로 만들고, 잠깐 필요한 메모는 `lambda`로 만든다고 생각하면 쉽다.

---

## 3. 핵심 아이디어

람다는 즉석 사진기와 비슷하다.

일반 함수는 제대로 이름을 붙이고 보관하는 사진첩 같은 느낌이다.

```python
def add(a, b):
    return a + b
```

```text
이름: add
역할: a와 b를 더하기
보관: 나중에 계속 사용 가능
```

람다는 그 자리에서 바로 찍고 바로 쓰는 즉석 사진 같다.

```python
lambda a, b: a + b
```

```text
이름 없음
역할: a와 b를 더하기
사용: 짧게 바로 사용
```

람다의 모양은 다음과 같다.

```text
lambda 재료: 결과

lambda x: x * 2
       │    │
       │    └─ x를 두 배로 만든 결과
       └─ 들어오는 값
```

예를 들어 `lambda x: x * 2`는 "x가 들어오면 x를 두 배로 해서 돌려줘"라는 뜻이다.

```text
x = 3  → 3 * 2  → 6
x = 10 → 10 * 2 → 20
```

---

## 4. 동작 과정 살펴보기

아래 코드를 보자.

```python
double = lambda x: x * 2

print(double(4))
```

### Step 1. 람다 함수를 만든다

```text
lambda x: x * 2

입력: x
동작: x를 2배로 만들기
결과: x * 2
```

이 람다를 `double`이라는 변수에 저장한다.

```text
double ─────▶ lambda x: x * 2
```

### Step 2. 값을 넣는다

```python
double(4)
```

```text
x = 4
```

4가 람다 안의 `x`로 들어간다.

### Step 3. 오른쪽 식을 계산한다

```text
x * 2

4 * 2 = 8
```

### Step 4. 결과가 반환된다

```text
double(4) → 8
```

출력 결과는 다음과 같다.

```text
8
```

### 정렬에서 사용하는 경우

```python
students = [("민수", 80), ("지은", 95), ("현우", 70)]

students.sort(key=lambda student: student[1])
```

학생 정보는 다음과 같다.

```text
("민수", 80)
("지은", 95)
("현우", 70)
```

람다는 각 학생에서 점수를 꺼낸다.

```text
("민수", 80) → 80
("지은", 95) → 95
("현우", 70) → 70
```

그 점수를 기준으로 정렬한다.

```text
정렬 결과

[("현우", 70), ("민수", 80), ("지은", 95)]
```

---

## 5. 구현 코드 및 상세 설명

```python
# 숫자를 두 배로 만드는 람다
double = lambda x: x * 2

print(double(5))


# 두 숫자를 더하는 람다
add = lambda a, b: a + b

print(add(3, 7))


# 학생을 점수 기준으로 정렬하기
students = [("민수", 80), ("지은", 95), ("현우", 70)]

students.sort(key=lambda student: student[1])

print(students)


# 단어를 길이 기준으로 정렬하기
words = ["apple", "kiwi", "banana"]

words.sort(key=lambda word: len(word))

print(words)
```

### 코드 설명

```python
double = lambda x: x * 2
```

`x`를 입력받아 `x * 2`를 돌려주는 람다다.

```text
double(5)

x = 5
5 * 2 = 10
```

```python
add = lambda a, b: a + b
```

`a`와 `b`를 입력받아 두 값을 더한다.

```text
a = 3
b = 7

3 + 7 = 10
```

```python
students.sort(key=lambda student: student[1])
```

학생 정보를 점수 기준으로 정렬한다.

여기서 람다는 "학생 정보에서 점수를 꺼내는 역할"을 한다.

```text
student = ("민수", 80)

student[1] → 80
```

```python
words.sort(key=lambda word: len(word))
```

단어를 길이 기준으로 정렬한다.

람다는 각 단어의 길이를 알려준다.

```text
"apple"  → 5
"kiwi"   → 4
"banana" → 6
```

짧은 단어부터 정렬된다.

---

## 6. 마지막 정리

람다는 이름 없는 짧은 함수다.

`lambda 입력값: 결과값` 형태로 작성한다.

람다는 한 줄짜리 간단한 기능에 잘 어울린다.

정렬 기준을 정할 때 자주 사용된다.

내용이 복잡해지면 람다보다 `def`로 함수를 만드는 것이 더 좋다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 람다",
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
