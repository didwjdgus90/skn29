# [Python 기초] 입출력 (Input / Output)

# 본문

## 1. 한 줄 요약

입출력은 프로그램이 외부에서 값을 입력받고, 처리 결과를 화면에 출력하는 방법이다.

입출력을 이해하면 사용자 입력이나 코딩 테스트 입력 데이터를 받아 원하는 결과를 출력할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 혼자서만 동작하지 않는다.

대부분의 프로그램은 외부에서 값을 받아 처리한다.

```text
사용자 입력
   │
   ▼
프로그램 처리
   │
   ▼
결과 출력
```

예를 들어 두 숫자를 입력받아 더하는 프로그램을 생각해 보자.

```text
입력
3 5

출력
8
```

입출력을 모르면 프로그램 안에 값을 직접 써야 한다.

```python
a = 3
b = 5
print(a + b)
```

하지만 실제 문제에서는 입력값이 매번 달라진다.

따라서 외부에서 값을 받아오는 방법이 필요하다.

파이썬에서는 기본적으로 `input()`으로 입력을 받고, `print()`로 출력한다.

---

## 3. 핵심 아이디어

입출력은 식당 주문과 비슷하다.

손님이 주문을 말하면 식당은 주문을 받아 음식을 만든다.

그리고 완성된 음식을 손님에게 전달한다.

```text
손님 주문
   │
   ▼
주방 처리
   │
   ▼
음식 제공
```

프로그램도 비슷하다.

```text
입력값
   │
   ▼
계산 또는 처리
   │
   ▼
출력값
```

`input()`은 바깥에서 값을 받는 창구이다.

`print()`는 처리 결과를 바깥으로 보여주는 창구이다.

중요한 점은 `input()`으로 받은 값은 기본적으로 문자열이라는 것이다.

```python
value = input()
```

```text
입력: 10

value ─────▶ "10"
```

숫자로 계산하려면 `int()`로 바꿔야 한다.

---

## 4. 동작 과정 살펴보기

아래 코드를 보자.

```python
a = int(input())
b = int(input())

print(a + b)
```

### Step 1. 첫 번째 입력을 받는다

```text
사용자 입력

3
```

```python
input()
```

입력값은 문자열 `"3"`으로 들어온다.

```text
input 결과 → "3"
int("3") → 3
a = 3
```

### Step 2. 두 번째 입력을 받는다

```text
사용자 입력

5
```

```text
input 결과 → "5"
int("5") → 5
b = 5
```

### Step 3. 두 숫자를 더한다

```text
a = 3
b = 5

3 + 5 = 8
```

### Step 4. 결과를 출력한다

```python
print(a + b)
```

```text
출력

8
```

### 한 줄 입력 처리

코딩 테스트에서는 한 줄에 여러 값이 들어오는 경우가 많다.

```text
입력
3 5
```

이때는 `split()`을 사용한다.

```python
a, b = map(int, input().split())
```

```text
input() → "3 5"
split() → ["3", "5"]
map(int, ...) → 3, 5
a = 3
b = 5
```

---

## 5. 구현 코드 및 상세 설명

```python
# 한 줄에 숫자 하나 입력
number = int(input())
print("입력한 숫자:", number)


# 한 줄에 숫자 두 개 입력
a, b = map(int, input().split())
print("합:", a + b)


# 여러 개의 숫자를 리스트로 입력
numbers = list(map(int, input().split()))
print("리스트:", numbers)
print("최댓값:", max(numbers))


# 반복 입력
n = int(input())

for _ in range(n):
    value = int(input())
    print("입력값:", value)
```

### 코드 설명

```python
number = int(input())
```

입력값 하나를 받는다.

`input()` 결과는 문자열이므로 정수 계산을 위해 `int()`로 변환한다.

```python
a, b = map(int, input().split())
```

한 줄에 들어온 두 숫자를 나누어 받는다.

```text
입력: 10 20

input()   → "10 20"
split()   → ["10", "20"]
map(int)  → 10, 20
```

```python
numbers = list(map(int, input().split()))
```

여러 숫자를 리스트로 받는다.

```text
입력: 1 2 3 4

결과: [1, 2, 3, 4]
```

```python
for _ in range(n):
```

입력 개수 `n`만큼 반복해서 값을 받는다.

`_`는 반복 변수의 값 자체를 사용하지 않을 때 자주 쓰는 이름이다.

---

## 6. 마지막 정리

`input()`은 사용자 입력을 문자열로 받는다.

숫자로 계산하려면 `int()` 또는 `float()`로 변환해야 한다.

`print()`는 값을 화면에 출력한다.

한 줄에 여러 값이 들어오면 `split()`으로 나눈다.

코딩 테스트에서는 `map(int, input().split())` 형태가 매우 자주 사용된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 입출력",
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
