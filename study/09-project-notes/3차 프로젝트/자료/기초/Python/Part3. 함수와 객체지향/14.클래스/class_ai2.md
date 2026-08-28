# 제목
[Python 기초] 클래스 (Class)

# 본문

## 1. 한 줄 요약

클래스는 관련 있는 데이터와 기능을 하나로 묶어 새로운 자료형처럼 사용하는 문법이다.

클래스를 이해하면 학생, 계좌, 캐릭터처럼 속성과 행동을 함께 가진 대상을 코드로 표현할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

학생 정보를 저장한다고 해보자.

이름, 나이, 점수를 각각 변수로 만들 수 있다.

```python
name = "민수"
age = 20
score = 85
```

학생이 한 명일 때는 괜찮다.

하지만 학생이 여러 명이면 변수 이름이 계속 늘어난다.

```python
name1 = "민수"
age1 = 20
score1 = 85

name2 = "지은"
age2 = 21
score2 = 90
```

이 방식은 관리하기 어렵다.

학생이라는 하나의 대상 안에 이름, 나이, 점수를 함께 묶으면 더 자연스럽다.

```python
student = Student("민수", 20, 85)
```

클래스는 이렇게 **하나의 대상을 코드로 표현하기 위한 설계도**이다.

---

## 3. 핵심 아이디어

클래스는 붕어빵 틀과 비슷하다.

붕어빵 틀은 하나지만, 그 틀로 여러 붕어빵을 만들 수 있다.

```text
붕어빵 틀
   │
   ├─ 팥 붕어빵
   ├─ 슈크림 붕어빵
   └─ 고구마 붕어빵
```

클래스도 마찬가지다.

```text
Student 클래스
   │
   ├─ 민수 학생 객체
   ├─ 지은 학생 객체
   └─ 현우 학생 객체
```

클래스는 설계도이고, 그 설계도로 만든 실제 대상은 객체라고 부른다.

학생 객체는 이름, 나이, 점수 같은 데이터를 가진다.

이런 데이터를 속성이라고 한다.

또 학생 정보를 출력하거나 합격 여부를 판단하는 기능도 가질 수 있다.

이런 기능을 메서드라고 한다.

```text
Student 객체

속성
- name
- age
- score

메서드
- introduce()
- is_passed()
```

---

## 4. 동작 과정 살펴보기

아래 클래스를 기준으로 살펴보자.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
```

### Step 1. 클래스라는 설계도를 만든다

```text
Student 설계도

필요한 값
- name
- score
```

`class Student:`는 Student라는 설계도를 만들겠다는 뜻이다.

### Step 2. 객체를 만든다

```python
student1 = Student("민수", 85)
```

```text
Student("민수", 85)
        │     │
        ▼     ▼
      name  score
```

객체가 만들어질 때 `__init__` 메서드가 실행된다.

### Step 3. 속성이 저장된다

```text
student1 객체

name  ─────▶ "민수"
score ─────▶ 85
```

`self.name`은 이 객체가 가진 이름을 의미한다.

`self.score`는 이 객체가 가진 점수를 의미한다.

### Step 4. 객체의 값을 꺼내 쓴다

```python
print(student1.name)
print(student1.score)
```

```text
student1.name  → "민수"
student1.score → 85
```

객체 안에 저장된 속성은 점 `.`을 사용해서 접근한다.

---

## 5. 구현 코드 및 상세 설명

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        print("안녕하세요. 저는", self.name, "입니다.")

    def is_passed(self):
        return self.score >= 60


student1 = Student("민수", 85)
student2 = Student("지은", 55)

student1.introduce()
print("합격 여부:", student1.is_passed())

student2.introduce()
print("합격 여부:", student2.is_passed())
```

### 코드 설명

```python
class Student:
```

`Student`라는 클래스를 만든다.

학생이라는 대상을 코드로 표현하기 위한 설계도이다.

```python
def __init__(self, name, score):
```

`__init__`은 객체가 만들어질 때 자동으로 실행되는 특별한 메서드다.

초기값을 설정하는 역할을 한다.

```python
self.name = name
self.score = score
```

객체 안에 이름과 점수를 저장한다.

```text
student1

name  → "민수"
score → 85
```

```python
def introduce(self):
```

학생이 자기소개를 하는 기능이다.

클래스 안에 있는 함수는 메서드라고 부른다.

```python
def is_passed(self):
    return self.score >= 60
```

점수가 60 이상이면 `True`, 아니면 `False`를 반환한다.

객체가 가진 `score` 값을 사용해 판단한다.

---

## 6. 마지막 정리

클래스는 객체를 만들기 위한 설계도이다.

객체는 클래스로 만든 실제 데이터 묶음이다.

속성은 객체가 가진 데이터이고, 메서드는 객체가 할 수 있는 기능이다.

`__init__`은 객체가 만들어질 때 초기값을 설정한다.

클래스를 사용하면 관련 데이터와 기능을 하나로 묶어 관리할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 클래스",
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
