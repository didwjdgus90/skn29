# [Python 기초] 리스트 컴프리헨션 (List Comprehension)

# 본문

## 1. 한 줄 요약

리스트 컴프리헨션은 반복문을 사용해 새 리스트를 짧고 읽기 좋게 만드는 문법이다.

리스트 컴프리헨션을 이해하면 기존 리스트를 바탕으로 값을 변환하거나 필터링하는 코드를 간결하게 작성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

리스트의 모든 숫자를 제곱해서 새 리스트를 만들고 싶다고 해보자.

일반 반복문으로는 다음처럼 작성할 수 있다.

```python
numbers = [1, 2, 3, 4]
squares = []

for number in numbers:
    squares.append(number * number)
```

이 코드는 명확하지만, 새 리스트를 만드는 과정이 여러 줄로 나뉜다.

파이썬에서는 이런 패턴이 매우 자주 등장한다.

```text
기존 리스트에서 하나씩 꺼낸다.
값을 바꾼다.
새 리스트에 넣는다.
```

리스트 컴프리헨션을 사용하면 이 과정을 한 줄로 표현할 수 있다.

```python
squares = [number * number for number in numbers]
```

즉, 리스트 컴프리헨션은 **반복해서 새 리스트를 만드는 코드를 짧게 정리하는 문법**이다.

---

## 3. 핵심 아이디어

리스트 컴프리헨션은 "재료 리스트를 넣으면 결과 리스트가 나오는 작은 공장"이라고 생각할 수 있다.

```text
재료 리스트

[1] [2] [3] [4]
 │   │   │   │
 ▼   ▼   ▼   ▼
제곱하기
 │   │   │   │
 ▼   ▼   ▼   ▼
[1] [4] [9] [16]
```

일반 반복문은 공장의 작업 과정을 한 줄씩 자세히 적는 방식이다.

```python
squares = []

for number in numbers:
    squares.append(number * number)
```

리스트 컴프리헨션은 같은 작업을 한 문장으로 압축한다.

```python
squares = [number * number for number in numbers]
```

구조를 나누면 다음과 같다.

```text
[결과값 for 변수 in 반복대상]

number * number  for number in numbers
     │                │          │
     │                │          └─ 꺼낼 대상
     │                └─ 하나씩 꺼낸 값
     └─ 새 리스트에 넣을 값
```

조건을 붙이면 원하는 값만 골라 새 리스트를 만들 수도 있다.

```python
even_numbers = [number for number in numbers if number % 2 == 0]
```

---

## 4. 동작 과정 살펴보기

아래 예제를 살펴보자.

```python
numbers = [1, 2, 3, 4]
squares = [number * number for number in numbers]
```

### Step 1. 반복 대상이 준비된다

```text
numbers

[1] [2] [3] [4]
```

### Step 2. 값을 하나씩 꺼낸다

```text
1번째 반복

number = 1
number * number = 1
```

새 리스트에 `1`이 들어간다.

```text
결과 리스트

[1]
```

### Step 3. 다음 값을 처리한다

```text
2번째 반복

number = 2
number * number = 4
```

```text
결과 리스트

[1] [4]
```

### Step 4. 마지막 값까지 반복한다

```text
3번째 반복

number = 3
number * number = 9

결과 리스트
[1] [4] [9]
```

```text
4번째 반복

number = 4
number * number = 16

결과 리스트
[1] [4] [9] [16]
```

최종 결과는 다음과 같다.

```python
[1, 4, 9, 16]
```

### 조건이 있는 경우

```python
evens = [number for number in numbers if number % 2 == 0]
```

```text
number = 1 → 1 % 2 == 0 ? False → 제외
number = 2 → 2 % 2 == 0 ? True  → 포함
number = 3 → 3 % 2 == 0 ? False → 제외
number = 4 → 4 % 2 == 0 ? True  → 포함

결과: [2, 4]
```

---

## 5. 구현 코드 및 상세 설명

```python
numbers = [1, 2, 3, 4, 5]

# 각 숫자를 제곱한 리스트 만들기
squares = [number * number for number in numbers]

# 짝수만 골라내기
evens = [number for number in numbers if number % 2 == 0]

# 짝수만 제곱하기
even_squares = [number * number for number in numbers if number % 2 == 0]

print("원본:", numbers)
print("제곱:", squares)
print("짝수:", evens)
print("짝수 제곱:", even_squares)
```

### 코드 설명

```python
squares = [number * number for number in numbers]
```

`numbers`에서 숫자를 하나씩 꺼낸다.

꺼낸 숫자를 제곱한 뒤 새 리스트에 넣는다.

```text
1 → 1
2 → 4
3 → 9
4 → 16
5 → 25
```

```python
evens = [number for number in numbers if number % 2 == 0]
```

숫자를 하나씩 꺼내고, 짝수인지 확인한다.

조건이 참인 값만 새 리스트에 들어간다.

```text
1 → 제외
2 → 포함
3 → 제외
4 → 포함
5 → 제외
```

```python
even_squares = [number * number for number in numbers if number % 2 == 0]
```

짝수만 골라서 제곱한다.

```text
2 → 4
4 → 16

결과: [4, 16]
```

리스트 컴프리헨션은 짧지만, 너무 복잡하게 쓰면 오히려 읽기 어려워질 수 있다.

처음 배우는 단계에서는 한 줄에 한 가지 작업만 담는 것이 좋다.

---

## 6. 마지막 정리

리스트 컴프리헨션은 새 리스트를 만드는 짧은 문법이다.

기본 구조는 `[결과값 for 변수 in 반복대상]`이다.

조건을 붙이면 `[결과값 for 변수 in 반복대상 if 조건]` 형태가 된다.

반복문과 `append()`로 작성하던 코드를 간결하게 바꿀 수 있다.

너무 복잡한 리스트 컴프리헨션은 가독성을 떨어뜨릴 수 있으므로 적당히 사용해야 한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 리스트 컴프리헨션",
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
