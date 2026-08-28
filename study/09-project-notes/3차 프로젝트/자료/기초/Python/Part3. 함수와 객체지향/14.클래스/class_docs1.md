# 제목
[Python 기초] 클래스 (Class)

# 링크
https://docs.python.org/ko/3/tutorial/classes.html

# 본문

## 1. 한 줄 요약

클래스는 **데이터(변수)와 기능(함수)을 하나로 묶어서 새로운 형(type)을 만드는 설계도**다. 이 설계도로 찍어낸 실체를 **인스턴스(instance)** 라고 한다.

---

## 2. 왜 클래스가 필요한가?

학생 여러 명의 이름과 점수를 관리한다고 해보자.

```python
# 클래스 없이
name1 = "철수"
score1 = 90
name2 = "영희"
score2 = 85
```

학생이 100명이라면 변수가 200개가 된다. 더 심각한 문제는 이 변수들이 **서로 관계가 있다는 사실을 코드에서 알아보기 어렵다**는 것이다.

클래스를 쓰면 관련 데이터와 기능을 하나의 **묶음**으로 정의하고, 그 묶음을 도장 찍듯 여러 개 만들 수 있다.

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("철수", 90)
s2 = Student("영희", 85)
```

---

## 3. 핵심 아이디어

### 클래스는 "붕어빵 틀", 인스턴스는 "붕어빵"이다

```
클래스 (설계도, 붕어빵 틀)
      │
      │  찍어내기
      ↓
인스턴스 (실체, 붕어빵)
  ├─ 인스턴스 1: 팥붕어빵
  ├─ 인스턴스 2: 크림붕어빵
  └─ 인스턴스 3: 슈크림붕어빵
```

같은 틀(클래스)에서 만들어도 **내용물(데이터)은 각자 독립적**이다. `s1.name`을 바꿔도 `s2.name`은 영향받지 않는다.

파이썬 공식 문서의 표현을 빌리면:
> 클래스는 데이터와 기능을 함께 묶는 방법을 제공합니다. 새 클래스를 만드는 것은 객체의 새 *형* 을 만들어서, 그 형의 새 *인스턴스* 를 만들 수 있도록 합니다.

---

## 4. 동작 과정 살펴보기

### 4-1. 클래스 정의와 인스턴스 만들기

```python
class MyClass:
    """A simple example class"""   # 클래스 설명 (독스트링)
    i = 12345                      # 클래스 변수

    def f(self):
        return 'hello world'       # 메서드
```

클래스를 만든 뒤 **함수처럼 호출**하면 인스턴스가 생성된다.

```python
x = MyClass()     # 인스턴스 생성
print(x.i)        # 12345
print(x.f())      # hello world
```

```
MyClass 정의
    │
    │  x = MyClass() 호출
    ↓
인스턴스 x 생성
    ├─ x.i  → 12345
    └─ x.f() → 'hello world'
```

---

### 4-2. `__init__()` — 인스턴스를 만들 때 자동 실행되는 초기화 메서드

클래스를 호출해 인스턴스를 만들 때 **자동으로 `__init__()`이 실행**된다. 초기값을 지정하고 싶을 때 이 메서드를 사용한다.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)   # 3.0 -4.5
```

```
Complex(3.0, -4.5) 호출 흐름:

1단계: 빈 인스턴스 생성
2단계: __init__(self, 3.0, -4.5) 자동 실행
       → self.r = 3.0
       → self.i = -4.5
3단계: 완성된 인스턴스 반환 → x에 저장
```

---

### 4-3. self — 나 자신을 가리키는 첫 번째 인자

메서드의 첫 번째 인자는 관례적으로 `self`라고 쓴다. **이 메서드를 호출한 인스턴스 자신**을 가리킨다.

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + ": 왈왈!")

d1 = Dog("초코")
d2 = Dog("바둑이")

d1.bark()   # 초코: 왈왈!
d2.bark()   # 바둑이: 왈왈!
```

```
d1.bark() 호출 시:
  self = d1
  self.name = "초코"
  → "초코: 왈왈!" 출력

d2.bark() 호출 시:
  self = d2
  self.name = "바둑이"
  → "바둑이: 왈왈!" 출력
```

공식 문서의 설명처럼: `d1.bark()`는 내부적으로 `Dog.bark(d1)`과 동등하다. 즉, **인스턴스 객체가 함수의 첫 번째 인자로 자동 전달**된다.

> `self`는 문법적 강제가 아니라 **강력한 관례**다. 이름 `self`는 파이썬에서 아무런 특별한 의미를 갖지 않는다. 하지만 이 규칙을 따르지 않으면 다른 파이썬 프로그래머들이 코드를 읽기 불편하다.

---

### 4-4. 클래스 변수 vs 인스턴스 변수

가장 많이 실수하는 부분이다. 공식 문서의 예제를 그대로 살펴보자.

**클래스 변수**: 그 클래스의 **모든 인스턴스가 공유**하는 변수  
**인스턴스 변수**: **각 인스턴스마다 고유한** 변수

```python
class Dog:
    kind = 'canine'         # 클래스 변수 — 모든 인스턴스가 공유

    def __init__(self, name):
        self.name = name    # 인스턴스 변수 — 각 인스턴스에 고유

d = Dog('Fido')
e = Dog('Buddy')

print(d.kind)   # canine  ← 공유됨
print(e.kind)   # canine  ← 공유됨
print(d.name)   # Fido    ← d만의 값
print(e.name)   # Buddy   ← e만의 값
```

```
      Dog 클래스
   ┌──────────────────┐
   │ kind = 'canine'  │  ← 모든 인스턴스가 공유
   └──────────────────┘
        ↓         ↓
  인스턴스 d    인스턴스 e
  name='Fido'  name='Buddy'   ← 각자 고유
```

⚠️ **주의**: 리스트나 딕셔너리를 클래스 변수로 쓰면 모든 인스턴스가 **같은 리스트를 공유**하는 실수가 생긴다.

```python
# ❌ 잘못된 설계
class Dog:
    tricks = []             # 모든 인스턴스가 이 리스트를 공유!

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)   # ['roll over', 'play dead']  ← e가 추가한 것까지 보임!

# ✅ 올바른 설계
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # 인스턴스마다 독립된 리스트

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)   # ['roll over']
print(e.tricks)   # ['play dead']
```

---

## 5. 구현 코드 및 상세 설명

### 5-1. 상속 — 기존 클래스 기능 물려받기

상속은 이미 만든 클래스(부모)의 기능을 그대로 가져와 새 클래스(자식)를 만드는 방법이다.

```python
class DerivedClassName(BaseClassName):
    ...
```

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name}이(가) 소리를 냅니다.")

class Dog(Animal):          # Animal을 상속
    def fetch(self):
        print(f"{self.name}이(가) 공을 가져옵니다.")

d = Dog("초코")
d.speak()    # 초코이(가) 소리를 냅니다.  ← 부모 메서드 그대로 사용
d.fetch()    # 초코이(가) 공을 가져옵니다. ← 자식 고유 메서드
```

```
메서드 탐색 순서:

d.speak() 호출
    ↓
Dog 클래스에서 speak 찾기 → 없음
    ↓
Animal 클래스에서 speak 찾기 → 있음! → 실행
```

공식 문서의 설명대로: 요청된 어트리뷰트가 클래스에서 발견되지 않으면 **베이스 클래스로 검색을 계속**한다.

**메서드 오버라이딩** — 자식 클래스에서 같은 이름의 메서드를 재정의하면 부모 메서드를 대체한다.

```python
class Cat(Animal):
    def speak(self):        # Animal.speak()를 덮어씀
        print(f"{self.name}: 야옹!")

c = Cat("나비")
c.speak()   # 나비: 야옹!   ← Cat만의 버전 실행
```

**`isinstance()`와 `issubclass()`** — 상속 관계를 확인한다.

```python
d = Dog("초코")
print(isinstance(d, Dog))     # True  — d는 Dog의 인스턴스
print(isinstance(d, Animal))  # True  — 상속 관계도 인식
print(issubclass(Dog, Animal))# True  — Dog는 Animal의 자식
```

---

### 5-2. 비공개 변수 — 이름 맹글링

파이썬에는 완전한 `private` 키워드가 없다. 대신 두 가지 관례가 있다.

**`_변수명`** (밑줄 하나): "내부용이니 직접 쓰지 마세요"라는 관례적 신호

**`__변수명`** (밑줄 두 개): **이름 맹글링(name mangling)** 적용. `_클래스명__변수명`으로 자동 변환되어, 서브클래스에서 실수로 덮어쓰는 것을 방지한다.

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)    # _Mapping__update 로 저장됨

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # update의 원래 버전을 __update로 보존

class MappingSubclass(Mapping):
    def update(self, keys, values):   # update를 재정의해도
        for item in zip(keys, values):
            self.items_list.append(item)
        # __init__ 안의 self.__update는 여전히 원래 update를 가리킴
        # (이름 맹글링 덕분에 _Mapping__update 로 분리되어 있음)
```

---

### 5-3. 스코프와 이름 공간 — 변수를 찾는 순서

파이썬은 변수 이름을 찾을 때 **안쪽에서 바깥 방향으로** 순서대로 탐색한다.

```
탐색 순서 (안 → 바깥):

┌─────────────────────────────────┐
│  1. 지역(Local)                  │  ← 현재 함수 안
│  ┌───────────────────────────┐  │
│  │  2. 둘러싸는(Enclosing)    │  │  ← 바깥 함수 (중첩함수인 경우)
│  │  ┌─────────────────────┐  │  │
│  │  │  3. 전역(Global)    │  │  │  ← 모듈(파일) 수준
│  │  │  ┌───────────────┐  │  │  │
│  │  │  │ 4. 내장       │  │  │  │  ← print, len 같은 내장 함수
│  │  │  └───────────────┘  │  │  │
│  │  └─────────────────────┘  │  │
│  └───────────────────────────┘  │
└─────────────────────────────────┘
```

```python
def scope_test():
    def do_local():
        spam = "local spam"      # 지역 변수만 바꿈

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"   # 둘러싸는 스코프의 spam 변경

    def do_global():
        global spam
        spam = "global spam"     # 전역 스코프의 spam 변경

    spam = "test spam"
    do_local()
    print("After local:", spam)       # test spam  ← 지역 대입은 영향 없음
    do_nonlocal()
    print("After nonlocal:", spam)    # nonlocal spam
    do_global()
    print("After global:", spam)      # nonlocal spam  ← 전역이 바뀌었지만 여긴 nonlocal

scope_test()
print("In global scope:", spam)       # global spam
```

핵심: **대입은 데이터를 복사하지 않는다 — 이름을 단지 객체에 연결할 뿐이다.**

---

## 6. 마지막 정리

- 클래스는 **데이터와 기능을 묶는 설계도**다. `class` 키워드로 정의하고, 이름을 호출해서 *인스턴스(실체)* 를 만든다.
- `__init__(self, ...)`은 인스턴스 생성 시 **자동으로 호출되는 초기화 메서드**다.
- `self`는 **관례적 이름**으로, 메서드를 호출한 인스턴스 자신을 가리킨다. `x.f()`는 내부적으로 `MyClass.f(x)`와 동등하다.
- **클래스 변수**는 모든 인스턴스가 공유, **인스턴스 변수**(`self.변수`)는 각 인스턴스가 독립 소유한다. 리스트·딕셔너리는 클래스 변수로 쓰지 말자.
- **상속** `class Child(Parent):`으로 부모 기능을 물려받고, 같은 이름의 메서드를 재정의(오버라이딩)할 수 있다.
- **`__변수명`** 은 `_클래스명__변수명`으로 맹글링되어 서브클래스의 실수 덮어쓰기를 방지한다.

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "클래스",
  "source_type": "docs",
  "style": [
    "easy",
    "analogy",
    "code",
    "theory"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "python"
}
```