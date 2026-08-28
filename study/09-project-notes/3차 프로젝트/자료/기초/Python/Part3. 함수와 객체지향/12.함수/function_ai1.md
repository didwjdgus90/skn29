# 제목
[Python 기초] 함수 (Function)

# 본문
반복되는 코드를 묶어서 이름을 붙인 것이다.
`def` 키워드로 정의하고 `return` 으로 값을 반환한다.

파이썬 함수의 핵심 특징은 일급 객체(first-class object)라는 점이다.
변수에 할당하고, 다른 함수의 인수로 전달하고, 함수에서 반환할 수 있다.

## 매개변수 종류 4가지

| 종류 | 문법 | 설명 |
|------|------|------|
| 기본값 | def f(x, y=0) | 인수 없으면 기본값 사용 |
| 가변 인수 | def f(*args) | 튜플로 받음 |
| 가변 키워드 | def f(**kwargs) | 딕셔너리로 받음 |
| 키워드 전용 | def f(*, key) | 반드시 키워드로 전달 |

## 스코프 (변수 범위)

함수 안에서 만든 변수는 그 함수 안에서만 살아있다.
전역 변수를 함수 안에서 수정하려면 `global` 키워드가 필요하다.
중첩 함수에서 바깥 함수 변수를 수정하려면 `nonlocal` 이 필요하다.

<IMAGE>전역 변수와 지역 변수 스코프 범위 그림</IMAGE>

## lambda 함수

한 줄짜리 익명 함수다. `lambda 매개변수: 표현식` 형태로 쓴다.
sorted(), map(), filter() 의 key 인수로 자주 활용된다.

## 수도코드(Pseudocode)

```
함수_정의(이름, 매개변수, 기본값):
    def 이름(매개변수=기본값):
        실행문
        return 반환값

가변_인수_처리(*args):
    args는 튜플로 들어옴
    for arg in args: 처리

가변_키워드_처리(**kwargs):
    kwargs는 딕셔너리로 들어옴
    for k, v in kwargs.items(): 처리
```

## 구현 코드 (Python)

```python
# 기본 함수
def greet(name):
    return f"안녕하세요, {name}님!"

print(greet("홍길동"))   # 안녕하세요, 홍길동님!

# 기본값 매개변수
def power(base, exp=2):
    return base ** exp

print(power(3))     # 9   (exp=2 사용)
print(power(3, 3))  # 27

# 키워드 인수
def info(name, age, city="서울"):
    print(f"{name}, {age}세, {city}")

info("홍길동", 30)
info(age=25, name="김철수")   # 순서 무관

# 가변 인수 *args
def total(*args):
    return sum(args)

print(total(1, 2, 3))       # 6
print(total(1, 2, 3, 4, 5)) # 15

# 가변 키워드 **kwargs
def profile(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

profile(name="홍길동", age=30, city="서울")

# 여러 값 반환 (튜플로 반환)
def min_max(lst):
    return min(lst), max(lst)

lo, hi = min_max([3, 1, 4, 1, 5])
print(lo, hi)   # 1 5

# lambda
add = lambda x, y: x + y
print(add(3, 4))   # 7

# 정렬 key로 활용
data = [{"name": "Bob", "age": 25}, {"name": "Alice", "age": 30}]
data.sort(key=lambda x: x["age"])

# map / filter
nums = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, nums))   # [1,4,9,16,25]
evens = list(filter(lambda x: x%2==0, nums)) # [2, 4]

# 재귀 함수
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))   # 120
```

## 실전 예제: 데코레이터 — 실행 시간 측정

```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} 실행시간: {time.time()-start:.4f}초")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

slow_sum(1000000)   # slow_sum 실행시간: 0.0321초
```

# 메타데이터
```json
{
  "category": "함수",
  "topic": "함수 기초",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 4,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "beginner",
  "language": "python"
}
```
