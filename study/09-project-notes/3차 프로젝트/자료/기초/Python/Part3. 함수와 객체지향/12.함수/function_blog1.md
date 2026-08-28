# [Python 기초] 함수 (Function)

---

# 링크
<https://velog.io/@chappi/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%EB%B0%B0%EC%9B%8C%EB%B3%B4%EC%9E%90-9%EC%9D%BC%EC%B0%A8-%EB%B0%98%EB%B3%B5%EB%AC%B8while-for>

---

## 1. 한 줄 요약

함수는 **반복되는 작업에 이름을 붙여서 재사용할 수 있게 만든 코드 묶음**이다. 한번 만들어두면 필요할 때마다 이름만 불러서 실행할 수 있다.

---

## 2. 왜 함수가 필요할까?

두 수를 더하는 코드를 여러 곳에서 써야 한다면?

```python
# 함수 없이 — 같은 코드가 계속 반복됨
result1 = 3 + 5
print(result1)

result2 = 7 + 2
print(result2)

result3 = 10 + 4
print(result3)
```

덧셈 방식을 "곱셈"으로 바꾸려면 세 곳을 모두 수정해야 한다. 100곳이라면?

```python
# 함수 사용 — 한 곳만 고치면 모두 바뀜
def add(a, b):
    return a + b

print(add(3, 5))
print(add(7, 2))
print(add(10, 4))
```

함수는 **"반복을 줄이고, 수정을 쉽게"** 만드는 도구다.

---

## 3. 핵심 아이디어 — 함수는 "자판기"다

함수를 **자판기**로 생각해보자.

```
     입력(동전 + 버튼)
           ↓
   ┌───────────────┐
   │   자판기 내부  │  ← 어떻게 처리하는지는 안에 숨겨져 있음
   │  (제조 과정)   │
   └───────────────┘
           ↓
     출력(음료수)
```

- **입력** → 함수에 넣는 값 (매개변수)
- **내부 처리** → 함수 안의 코드
- **출력** → `return`으로 돌려주는 결과

자판기를 쓸 때 내부 구조를 몰라도 되듯, 함수도 안이 어떻게 동작하는지 몰라도 쓸 수 있다.

---

## 4. 동작 과정 살펴보기

### 4-1. 함수 만들기와 호출하기

```python
# 함수 정의 (자판기 만들기)
def greet(name):
    message = name + "님, 안녕하세요!"
    return message

# 함수 호출 (자판기 사용하기)
result = greet("정민")
print(result)
```

```
실행 흐름:

1. greet("정민") 호출
        ↓
2. 함수 안으로 진입: name = "정민"
        ↓
3. message = "정민님, 안녕하세요!" 계산
        ↓
4. return message → "정민님, 안녕하세요!" 를 돌려줌
        ↓
5. result = "정민님, 안녕하세요!"
        ↓
6. print(result) → 출력

출력: 정민님, 안녕하세요!
```

### 4-2. 함수의 구조 한눈에 보기

```
def  함수이름 ( 매개변수1, 매개변수2 ) :
 ↑       ↑           ↑
정의     이름        입력값

    실행할 코드   ← 들여쓰기 필수!
    return 결과값
              ↑
           출력값
```

---

## 5. 구현 코드 및 상세 설명

### 5-1. 입력(매개변수) 다양하게 쓰기

```python
# 매개변수 없음
def say_hello():
    print("안녕하세요!")

# 매개변수 1개
def square(x):
    return x * x

# 매개변수 여러 개
def add(a, b, c):
    return a + b + c

say_hello()          # 안녕하세요!
print(square(4))     # 16
print(add(1, 2, 3))  # 6
```

```python
# 기본값 지정 — 입력 안 해도 기본값으로 동작
def greet(name, greeting="안녕하세요"):
    print(f"{name}님, {greeting}!")

greet("정민")              # 정민님, 안녕하세요!
greet("정민", "반갑습니다") # 정민님, 반갑습니다!
```

> 💡 `매개변수=기본값` 형태로 쓰면, 호출할 때 해당 값을 생략해도 된다.

### 5-2. 출력(return) 이해하기

```python
def add(a, b):
    return a + b          # 결과를 돌려줌

result = add(3, 5)        # 돌려받은 값을 변수에 저장
print(result)             # 8
print(add(10, 20) + 5)    # 35 — return값을 바로 계산에 사용 가능
```

```python
# return이 없으면 None을 돌려줌
def just_print(x):
    print(x)              # 출력만 하고 return 없음

result = just_print(5)    # 5 출력됨
print(result)             # None
```

```
return 있음:  add(3,5) → 8    → 변수에 저장·계산에 활용 가능
return 없음:  just_print(5)   → None  → 값으로 활용 불가
```

### 5-3. 변수의 범위 (scope) — 함수 안팎의 변수

가장 많이 헷갈리는 부분이다. 핵심 규칙만 기억하자.

```
규칙 1: 함수 안에서 만든 변수는 함수 밖에서 쓸 수 없다.
규칙 2: 함수 밖에서 만든 변수(전역 변수)는 함수 안에서 읽을 수 있다.
규칙 3: 함수 안팎에 같은 이름의 변수가 있어도 서로 다른 변수다.
```

```python
a = 10  # 전역 변수

def my_func():
    b = 20          # 함수 내부 변수 (밖에서 접근 불가)
    print(a)        # ✅ 전역 변수 a는 안에서 읽기 가능
    print(b)        # ✅ 내부 변수 b

my_func()
print(a)            # ✅ 10
print(b)            # ❌ 에러! b는 함수 밖에서 접근 불가
```

```python
# 같은 이름이어도 안팎은 별개!
x = 100             # 전역 변수 x

def change():
    x = 999         # 이건 전역 x를 바꾸는 게 아니라
    print(x)        # 함수 내부에 새로운 x를 만드는 것!

change()            # 999
print(x)            # 100 — 전역 x는 그대로!
```

```
시각화:

┌─────────────────────────┐
│ 전역 영역               │
│   a = 10                │  ← 전역 변수
│                         │
│  ┌───────────────────┐  │
│  │ my_func() 내부    │  │
│  │   b = 20          │  │  ← 함수 내부 변수 (여기서만 유효)
│  │   a 읽기 가능 ✅   │  │
│  └───────────────────┘  │
│                         │
│  b 접근 불가 ❌          │
└─────────────────────────┘
```

> 💡 혼란을 줄이는 가장 좋은 방법 — **전역 변수를 함수 안에서 직접 쓰지 말고, 매개변수로 넘겨서 사용하자.**

```python
# ❌ 나쁜 방식: 전역 변수를 함수 안에서 직접 참조
total = 0
def bad_add(x):
    return total + x   # total이 바뀌면 함수 동작도 달라짐

# ✅ 좋은 방식: 필요한 값은 매개변수로 받기
def good_add(a, b):
    return a + b       # 입력값만 보고 동작 — 예측 가능
```

### 5-4. 함수 안에서 함수 호출하기

```python
def multiply(a, b):
    return a * b

def square_sum(x, y):
    sq_x = multiply(x, x)   # 다른 함수를 가져다 씀
    sq_y = multiply(y, y)
    return sq_x + sq_y

print(square_sum(3, 4))  # 9 + 16 = 25
```

```
실행 흐름:

square_sum(3, 4) 호출
    → multiply(3, 3) 호출 → 9 반환
    → multiply(4, 4) 호출 → 16 반환
    → 9 + 16 = 25 반환
```

---

## 6. 마지막 정리

- 함수는 **반복되는 코드에 이름을 붙여 재사용**하는 도구다.
- `def 함수명(매개변수):` 로 정의하고, 함수명()으로 **호출**한다.
- `return`으로 결과를 돌려주고, 없으면 `None`이 반환된다.
- 함수 **안에서 만든 변수는 밖에서 쓸 수 없다**.
- 전역 변수는 함수 안에서 읽을 수 있지만, **매개변수로 받아서 쓰는 게 좋은 습관**이다.
- 함수 안에서 **다른 함수를 호출**하는 것도 가능하다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "함수",
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