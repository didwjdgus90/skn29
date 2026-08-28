# 제목
[Python 기초] 클래스 (Class)

# 본문
데이터(속성)와 동작(메서드)을 하나로 묶은 설계도다.
클래스로부터 인스턴스(객체)를 만들어 사용한다.

클래스는 붕어빵 틀, 인스턴스는 붕어빵이라고 비유할 수 있다.
같은 클래스에서 만든 여러 인스턴스는 각자의 데이터를 독립적으로 갖는다.

객체 지향 프로그래밍(OOP)의 핵심 원칙인 캡슐화, 상속, 다형성을 파이썬에서 클래스로 구현한다.

## 클래스 변수 vs 인스턴스 변수

| 구분 | 선언 위치 | 공유 범위 |
|------|-----------|-----------|
| 클래스 변수 | 클래스 내부, 메서드 밖 | 모든 인스턴스 공유 |
| 인스턴스 변수 | __init__ 내부 self.xxx | 각 인스턴스 독립 |

## 메서드 3종류

인스턴스 메서드는 self를 받아 인스턴스 데이터에 접근한다.
클래스 메서드는 cls를 받아 클래스 데이터에 접근한다.
정적 메서드는 self/cls 없이 독립 함수처럼 동작한다.

<IMAGE>클래스 인스턴스 관계 및 메모리 구조 그림</IMAGE>

## 특수 메서드 (Magic Methods)

`__init__` 외에도 연산자 오버로딩을 위한 다양한 특수 메서드가 있다.
`__str__` 은 print()로 출력할 때, `__add__` 는 + 연산자를 사용할 때 호출된다.

## 수도코드(Pseudocode)

```
클래스_정의:
    class 이름:
        class_var = 공유값

        def __init__(self, 인수):
            self.instance_var = 인수  ← 각 인스턴스마다 독립

        def method(self):
            self.instance_var 접근/수정

인스턴스_생성:
    obj = 클래스명(인수)
    obj.method() 호출
```

## 구현 코드 (Python)

```python
class Person:
    species = "Human"   # 클래스 변수 (공유)

    def __init__(self, name, age):
        self.name = name   # 인스턴스 변수
        self.age = age

    def introduce(self):
        return f"저는 {self.name}이고 {self.age}살입니다."

    def __str__(self):
        return f"Person({self.name}, {self.age})"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

p1 = Person("홍길동", 30)
p2 = Person("김철수", 25)
print(p1.introduce())     # 저는 홍길동이고 30살입니다.
print(Person.species)     # Human
print(p1)                 # Person(홍길동, 30)

# 상속
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)   # 부모 생성자 호출
        self.grade = grade

    def introduce(self):             # 메서드 오버라이딩
        base = super().introduce()
        return f"{base} {self.grade}학년입니다."

s = Student("이영희", 20, 3)
print(s.introduce())   # 저는 이영희이고 20살입니다. 3학년입니다.
print(isinstance(s, Person))    # True
print(isinstance(s, Student))   # True

# 클래스 메서드 / 정적 메서드
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

    @staticmethod
    def about():
        return "카운터 클래스"

Counter()
Counter()
print(Counter.get_count())   # 2
print(Counter.about())       # 카운터 클래스

# 프로퍼티
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("절대 영도 이하!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

t = Temperature(25)
print(t.fahrenheit)   # 77.0
t.celsius = 100
print(t.fahrenheit)   # 212.0
```

## 실전 예제: 은행 계좌 클래스

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance
        self._history = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("입금액은 양수여야 합니다.")
        self._balance += amount
        self._history.append(f"+{amount}")
        return self

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("잔액 부족")
        self._balance -= amount
        self._history.append(f"-{amount}")
        return self

    @property
    def balance(self):
        return self._balance

    def __str__(self):
        return f"{self.owner}의 계좌: {self._balance:,}원"

acc = BankAccount("홍길동", 10000)
acc.deposit(5000).withdraw(3000)   # 메서드 체이닝
print(acc)   # 홍길동의 계좌: 12,000원
```

# 메타데이터
```json
{
  "category": "객체지향",
  "topic": "클래스",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 3,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "intermediate",
  "language": "python"
}
```
