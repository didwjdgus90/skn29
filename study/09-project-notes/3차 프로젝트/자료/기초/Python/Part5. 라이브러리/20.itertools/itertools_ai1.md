# 제목
[Python 고급] 이터레이터와 제너레이터 (Iterator & Generator)

# 본문
이터레이터는 `__iter__` 와 `__next__` 를 구현해 하나씩 꺼낼 수 있는 객체다.
for문이 내부적으로 이터레이터의 `__next__` 를 반복 호출하는 방식으로 동작한다.

제너레이터는 `yield` 를 사용해 값을 하나씩 생성하는 특별한 함수다.
일반 함수와 달리 호출 즉시 실행되지 않고, next()를 호출할 때마다 yield 지점까지만 실행된다.

메모리 효율이 핵심 장점이다. 리스트는 모든 값을 메모리에 올리지만,
제너레이터는 요청할 때마다 하나씩 계산해 반환한다.
수백만 개 데이터도 메모리 부담 없이 처리할 수 있다.

## 이터레이터 vs 이터러블

이터러블(iterable)은 for문에 쓸 수 있는 객체다 (리스트, 튜플, 문자열 등).
이터레이터(iterator)는 이터러블에 iter()를 적용해 만들며, next()로 하나씩 꺼낼 수 있다.

<IMAGE>이터러블 → 이터레이터 변환 및 next() 동작 그림</IMAGE>

## yield의 동작 원리

yield를 만나면 함수 실행이 일시 정지되고 값을 반환한다.
다음에 next()가 호출되면 그 지점에서 이어서 실행된다.

<IMAGE>yield 실행 흐름 및 상태 저장 그림</IMAGE>

## 제너레이터 표현식

리스트 컴프리헨션과 문법이 같지만 대괄호 대신 소괄호를 쓴다.
생성 즉시 메모리에 올리지 않아서 대용량 데이터에 유리하다.

## 수도코드(Pseudocode)

```
제너레이터_함수():
    while 조건:
        yield 값       ← 여기서 멈추고 값 반환
                        ← 다음 next() 호출 시 이 지점부터 재개

이터레이터_프로토콜:
    __iter__() → self 반환
    __next__() → 다음 값 반환 또는 StopIteration 발생
```

## 구현 코드 (Python)

```python
# 이터레이터 직접 구현
class Range:
    def __init__(self, start, stop):
        self.current = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        val = self.current
        self.current += 1
        return val

for i in Range(1, 5):
    print(i, end=" ")   # 1 2 3 4

# iter() / next() 직접 사용
lst = [1, 2, 3]
it = iter(lst)
print(next(it))   # 1
print(next(it))   # 2

# 기본 제너레이터
def count_up(n):
    i = 0
    while i < n:
        yield i
        i += 1

for v in count_up(5):
    print(v, end=" ")   # 0 1 2 3 4

# 피보나치 제너레이터 (무한)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
print([next(fib) for _ in range(10)])
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 제너레이터 표현식
gen = (x**2 for x in range(10))   # () 사용
lst = [x**2 for x in range(10)]   # [] 사용

print(type(gen))   # <class 'generator'>
print(sum(gen))    # 285

# yield from: 다른 이터러블 위임
def chain(*iterables):
    for it in iterables:
        yield from it

print(list(chain([1,2], [3,4], [5,6])))   # [1,2,3,4,5,6]
```

## 실전 예제: 대용량 CSV 파일 처리

```python
def read_large_csv(filepath, encoding="utf-8"):
    """대용량 파일을 한 줄씩 생성 (메모리 효율적)"""
    with open(filepath, "r", encoding=encoding) as f:
        header = f.readline().strip().split(",")
        for line in f:
            values = line.strip().split(",")
            yield dict(zip(header, values))

# 사용: 수백만 행도 메모리 부담 없이 처리
for row in read_large_csv("large_data.csv"):
    if row.get("status") == "active":
        print(row["name"])
```

# 메타데이터
```json
{
  "category": "고급문법",
  "topic": "이터레이터/제너레이터",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 3,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "intermediate",
  "language": "python"
}
```
