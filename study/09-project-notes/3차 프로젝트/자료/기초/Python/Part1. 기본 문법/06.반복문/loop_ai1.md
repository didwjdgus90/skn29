# [Python 기초] 반복문 (while / for)

# 본문

## 1. 한 줄 요약

반복문은 같은 구조의 작업을 여러 번 실행하기 위해 사용하는 제어문이다.

반복문을 이해하면 여러 데이터에 동일한 처리를 적용하거나, 특정 조건이 만족될 때까지 작업을 자동으로 반복할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그래밍에서는 같은 작업을 여러 번 수행해야 하는 상황이 자주 발생한다.

예를 들어 학생 5명의 점수를 출력한다고 해보자.

```python
print(scores[0])
print(scores[1])
print(scores[2])
print(scores[3])
print(scores[4])
```

학생이 5명일 때는 가능해 보이지만, 학생이 100명이라면 같은 코드를 100줄 작성해야 한다.

이 방식은 비효율적이고, 수정이 어렵고, 실수 가능성이 높다.

반복문은 이런 문제를 해결한다.

```python
for score in scores:
    print(score)
```

반복문을 사용하면 데이터 개수와 상관없이 같은 규칙을 코드 한 덩어리로 표현할 수 있다.

즉, 반복문은 **중복 코드를 줄이고, 데이터 처리 흐름을 일반화하는 문법**이다.

---

## 3. 핵심 아이디어

반복문은 크게 두 가지 관점으로 이해할 수 있다.

첫 번째는 **순회**이다.

순회란 여러 값이 들어 있는 자료를 처음부터 끝까지 하나씩 꺼내 보는 것이다.

```text
scores = [80, 90, 70]

반복 흐름

80 꺼냄 → 처리
90 꺼냄 → 처리
70 꺼냄 → 처리
```

이때 사용하는 대표 문법이 `for`문이다.

두 번째는 **조건 기반 반복**이다.

조건이 참인 동안 계속 실행하고, 조건이 거짓이 되면 멈춘다.

```text
조건 확인
  │
  ├─ True  → 코드 실행 → 다시 조건 확인
  │
  └─ False → 반복 종료
```

이때 사용하는 대표 문법이 `while`문이다.

정리하면 `for`문은 반복 대상이 명확할 때, `while`문은 종료 조건이 중요할 때 적합하다.

---

## 4. 동작 과정 살펴보기

### 4-1. for문의 동작 과정

아래 예제를 보자.

```python
numbers = [1, 2, 3]

for number in numbers:
    print(number)
```

반복 대상은 리스트 `[1, 2, 3]`이다.

파이썬은 리스트에서 값을 하나씩 꺼내 `number`에 저장한다.

```text
numbers

[1] [2] [3]
 │
 ▼
number = 1
print(1)
```

첫 번째 반복에서는 `1`이 꺼내진다.

```text
[1] [2] [3]
     │
     ▼
number = 2
print(2)
```

두 번째 반복에서는 `2`가 꺼내진다.

```text
[1] [2] [3]
         │
         ▼
number = 3
print(3)
```

세 번째 반복에서는 `3`이 꺼내진다.

더 이상 꺼낼 값이 없으면 반복문은 종료된다.

```text
출력 결과

1
2
3
```

### 4-2. while문의 동작 과정

이번에는 `while`문을 보자.

```python
count = 1

while count <= 3:
    print(count)
    count += 1
```

`while`문은 조건을 먼저 검사한다.

```text
count = 1

count <= 3 ?
1 <= 3 → True
```

조건이 참이므로 코드를 실행한다.

```text
print(1)
count = count + 1
count = 2
```

다시 조건을 검사한다.

```text
count = 2

2 <= 3 → True
```

계속 반복한다.

```text
count = 3

3 <= 3 → True
print(3)
count = 4
```

이제 조건이 거짓이 된다.

```text
count = 4

4 <= 3 → False

반복 종료
```

---

## 5. 구현 코드 및 상세 설명

```python
# for문: 리스트의 값을 하나씩 처리
scores = [80, 95, 70, 100]

total = 0

for score in scores:
    total += score

average = total / len(scores)

print("총점:", total)
print("평균:", average)


# while문: 특정 조건이 만족될 때까지 반복
count = 1

while count <= 5:
    print(count)
    count += 1
```

### 코드 설명

```python
scores = [80, 95, 70, 100]
```

여러 점수를 리스트에 저장한다.

반복문은 이 리스트를 처음부터 끝까지 순회한다.

```python
total = 0
```

점수 합계를 저장할 변수를 준비한다.

반복이 진행될수록 이 변수에 점수가 누적된다.

```python
for score in scores:
```

`scores` 안의 값을 하나씩 꺼내 `score`에 저장한다.

```text
1회차: score = 80
2회차: score = 95
3회차: score = 70
4회차: score = 100
```

```python
total += score
```

현재 점수를 기존 합계에 더한다.

```text
처음 total = 0

0 + 80 = 80
80 + 95 = 175
175 + 70 = 245
245 + 100 = 345
```

```python
average = total / len(scores)
```

총점을 점수 개수로 나누어 평균을 계산한다.

```python
while count <= 5:
```

`count`가 5 이하인 동안 반복한다.

```python
count += 1
```

반복할 때마다 `count`를 1 증가시킨다.

이 코드가 없으면 `count` 값이 변하지 않아 반복이 끝나지 않을 수 있다.

---

## 6. 마지막 정리

반복문은 같은 작업을 여러 번 실행하기 위한 문법이다.

`for`문은 리스트, 문자열, range처럼 반복 가능한 대상을 순서대로 처리할 때 적합하다.

`while`문은 특정 조건이 참인 동안 반복해야 할 때 적합하다.

반복문 내부 코드는 들여쓰기로 구분한다.

`while`문에서는 반복 종료 조건이 반드시 변하도록 작성해야 무한 반복을 피할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 반복문",
  "source_type": "generated",
  "style": [
    "theory",
    "code"
  ],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "mid",
  "language": "python"
}
```
