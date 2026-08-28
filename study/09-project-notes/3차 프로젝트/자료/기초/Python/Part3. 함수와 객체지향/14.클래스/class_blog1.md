# [Python 기초] 클래스 (Class)

---

# 링크
<https://all-the-meaning.tistory.com/54>

---

## 1. 한 줄 요약

클래스는 **관련된 변수와 함수를 하나로 묶어서 만드는 설계도**다. 이 설계도로 찍어낸 실체를 **객체(object)** 라고 한다.

---

## 2. 왜 클래스가 필요할까?

학생 3명의 이름과 점수를 관리한다고 해보자.

```python
# 클래스 없이 — 변수가 뒤죽박죽
name1 = "철수"
score1 = 90
name2 = "영희"
score2 = 85
name3 = "민수"
score3 = 78

# 학생이 100명이라면? 변수가 200개...
```

클래스로 묶으면 훨씬 깔끔하다.

```python
# 클래스 사용 — 하나의 묶음으로 관리
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("철수", 90)
s2 = Student("영희", 85)
s3 = Student("민수", 78)
```

클래스는 코드가 커질수록, 관련 데이터가 많을수록 그 진가를 발휘한다.

---

## 3. 핵심 아이디어 — 클래스는 "붕어빵 틀", 객체는 "붕어빵"

클래스(설계도)와 객체(실체)의 관계를 **붕어빵 틀과 붕어빵**으로 생각하자.

```
     붕어빵 틀 (클래스)
    ┌──────────────┐
    │  모양 정의   │  ← 어떤 속성·기능을 가질지 정해둠
    │  팥 넣는 법  │
    └──────────────┘
          │
    틀로 찍어내기 (객체 생성)
     ↙        ↘
붕어빵1      붕어빵2
(팥 가득)   (크림 가득)
← 같은 틀이지만 내용물은 다를 수 있음!
```

- **클래스** = 붕어빵 틀 (설계도, 한 번만 만듦)
- **객체** = 붕어빵 (실체, 여러 개 찍어낼 수 있음)

---

## 4. 동작 과정 살펴보기

### 4-1. 클래스 기본 구조

```python
class Dog:                        # 클래스 이름 (대문자로 시작하는 게 관례)
    def __init__(self, name, age): # 생성자: 객체 만들 때 자동 실행
        self.name = name           # self.변수 = 클래스 전체에서 쓸 수 있는 변수
        self.age = age

    def bark(self):                # 메서드(클래스 안의 함수)
        print(f"{self.name}가 짖는다: 왈왈!")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}살")

# 객체 생성 (붕어빵 찍기)
dog1 = Dog("초코", 3)
dog2 = Dog("바둑이", 5)

dog1.bark()   # 초코가 짖는다: 왈왈!
dog2.info()   # 이름: 바둑이, 나이: 5살
```

```
실행 흐름:

Dog("초코", 3) 호출
    → __init__(self, "초코", 3) 자동 실행
    → self.name = "초코"
    → self.age = 3
    → dog1 객체 완성

dog1.bark() 호출
    → bark(self) 실행 (self = dog1)
    → "초코가 짖는다: 왈왈!" 출력
```

### 4-2. self가 뭔가요?

`self`는 **"나 자신(이 객체)"** 을 가리키는 말이다.

```python
class Cat:
    def __init__(self, name):
        self.name = name     # 이 객체의 name

    def meow(self):
        print(self.name + ": 야옹~")  # 이 객체의 name 사용

cat1 = Cat("나비")
cat2 = Cat("루시")

cat1.meow()  # 나비: 야옹~   (self = cat1)
cat2.meow()  # 루시: 야옹~   (self = cat2)
```

```
cat1.meow() 호출 시:
  self = cat1
  self.name = "나비"

cat2.meow() 호출 시:
  self = cat2
  self.name = "루시"
```

> 💡 `self`를 붙여야 같은 클래스 내 다른 메서드에서도, 클래스 밖에서도 그 변수에 접근할 수 있다. 붙이지 않으면 그 함수 안에서만 유효한 일반 변수가 된다.

---

## 5. 구현 코드 및 상세 설명

### 5-1. 절차지향 vs 객체지향 비교

같은 기능을 두 방식으로 구현해보자.

```python
# 절차지향 — 함수와 변수가 흩어져 있음
def get_area(width, height):
    return width * height

width = 5
height = 10
print("넓이:", get_area(width, height))
```

```python
# 객체지향 — 관련된 것을 하나로 묶음
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print("넓이:", rect.get_area())
```

코드가 짧을 때는 차이가 작아 보이지만, 규모가 커지면 객체지향 방식이 훨씬 관리하기 쉬워진다.

### 5-2. 클래스 상속 — 기존 클래스 기능을 물려받기

상속은 **이미 만든 클래스의 기능을 그대로 이어받아 새 클래스를 만드는 것**이다.

```
    Animal (부모 클래스)
    ├─ name 속성
    └─ eat() 메서드
          │
          ↓ 상속
    Dog (자식 클래스)
    ├─ (Animal의 기능 그대로 사용 가능)
    └─ bark() 메서드 (Dog만의 추가 기능)
```

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name}가 밥을 먹는다.")

class Dog(Animal):               # Animal을 상속받음
    def __init__(self, name):
        super().__init__(name)   # 부모 클래스 생성자 호출 (필수!)

    def bark(self):
        print(f"{self.name}가 짖는다: 왈왈!")

dog = Dog("초코")
dog.eat()    # ✅ 부모의 eat() 사용 가능: 초코가 밥을 먹는다.
dog.bark()   # ✅ 자식의 bark() 사용:    초코가 짖는다: 왈왈!
```

```python
# 메서드 오버라이드 — 부모 기능을 자식이 덮어씌우기
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def eat(self):                         # 부모의 eat()를 새로 정의
        print(f"{self.name}는 깔끔하게 먹는다.")

cat = Cat("나비")
cat.eat()   # 나비는 깔끔하게 먹는다.  ← Cat만의 버전으로 실행됨
```

> 💡 `super().__init__()` — 자식 클래스 생성자에서 **반드시** 부모 생성자를 먼저 호출해야 한다. 안 하면 부모의 `self.변수`들이 초기화되지 않아 에러가 발생한다.

### 5-3. 종합 예제 — 출석부 & 성적부

```python
class StudentAttendance:            # 출석부 (부모)
    def __init__(self, student_list=[]):
        self.student_list = student_list

    def add_student(self, name):
        self.student_list.append(name)

    def call_attendance(self):
        for i, name in enumerate(self.student_list):
            print(f"{i+1}번: {name}")


class StudentScore(StudentAttendance):  # 성적부 (자식, 출석부 상속)
    def __init__(self, student_list=[]):
        super().__init__(student_list)
        self.scores = [-1] * len(self.student_list)  # 초기 점수 -1

    def write_score(self, name, score):
        idx = self.student_list.index(name)
        self.scores[idx] = score

    def show_score(self):
        for name, score in zip(self.student_list, self.scores):
            print(f"{name}: {score}점")
```

```python
# 사용 예시
gradebook = StudentScore(["철수", "영희"])
gradebook.add_student("민수")

gradebook.write_score("철수", 90)
gradebook.write_score("영희", 85)
gradebook.write_score("민수", 78)

gradebook.call_attendance()   # 출석부 기능 (부모에서 상속)
# 1번: 철수
# 2번: 영희
# 3번: 민수

gradebook.show_score()        # 성적부 기능 (자식에서 추가)
# 철수: 90점
# 영희: 85점
# 민수: 78점
```

---

## 6. 마지막 정리

- **클래스**는 설계도, **객체**는 그 설계도로 만든 실체다. (붕어빵 틀 / 붕어빵)
- `__init__`은 **생성자** — 객체가 만들어질 때 자동으로 실행된다.
- `self`는 **"이 객체 자신"** 을 가리킨다. `self.변수`로 클래스 전체에서 접근 가능한 변수를 만든다.
- **상속**으로 부모 클래스의 기능을 그대로 물려받고, 필요한 기능만 추가하거나 덮어쓸 수 있다.
- 자식 클래스 생성자에서는 **`super().__init__()`으로 부모 생성자를 반드시 호출**해야 한다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "클래스",
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