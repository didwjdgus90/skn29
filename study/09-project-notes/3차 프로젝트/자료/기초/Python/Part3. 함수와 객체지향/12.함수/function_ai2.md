# 제목
[Python 기초] 함수 (Function)

# 본문

## 1. 한 줄 요약

함수는 자주 사용하는 코드를 이름 붙여 묶어두고, 필요할 때 다시 호출해서 사용하는 문법이다.

함수를 이해하면 중복 코드를 줄이고, 프로그램을 작은 기능 단위로 나누어 관리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램을 만들다 보면 같은 계산이나 같은 동작을 여러 번 해야 할 때가 있다.

예를 들어 두 숫자를 더한 뒤 결과를 출력하는 코드가 여러 곳에서 필요하다고 해보자.

```python
a = 10
b = 20
print(a + b)

x = 3
y = 5
print(x + y)
```

동작은 비슷한데 변수 이름만 다르다.

이런 코드가 많아지면 수정하기 어렵고, 실수하기 쉽다.

함수를 사용하면 같은 동작을 하나로 묶을 수 있다.

```python
def add(a, b):
    return a + b
```

이제 숫자 두 개를 더해야 할 때마다 `add()`를 호출하면 된다.

```python
print(add(10, 20))
print(add(3, 5))
```

함수는 **자주 쓰는 작업을 저장해두는 도구함**이라고 볼 수 있다.

---

## 3. 핵심 아이디어

함수는 자판기와 비슷하다.

자판기에 돈과 음료 번호를 넣으면 음료가 나온다.

```text
입력
돈, 음료 번호
   │
   ▼
자판기
   │
   ▼
출력
음료
```

함수도 비슷하다.

값을 넣으면 정해진 작업을 수행하고 결과를 돌려준다.

```text
입력값
a, b
 │
 ▼
add 함수
 │
 ▼
a + b 결과
```

파이썬 함수는 보통 다음 구조를 가진다.

```python
def 함수이름(매개변수):
    실행할 코드
    return 결과값
```

`def`는 함수를 만들겠다는 뜻이다.

매개변수는 함수 안으로 들어오는 값을 담는 변수다.

`return`은 함수가 만든 결과를 밖으로 돌려주는 역할을 한다.

---

## 4. 동작 과정 살펴보기

아래 함수를 보자.

```python
def add(a, b):
    result = a + b
    return result

answer = add(3, 5)
print(answer)
```

### Step 1. 함수가 정의된다

```text
add 함수 준비 완료

입력: a, b
동작: a + b
출력: result
```

함수를 정의했다고 해서 바로 실행되는 것은 아니다.

함수는 호출해야 실행된다.

### Step 2. 함수를 호출한다

```python
answer = add(3, 5)
```

```text
add(3, 5)

3 ─────▶ a
5 ─────▶ b
```

3과 5가 함수 안으로 전달된다.

### Step 3. 함수 안에서 계산한다

```python
result = a + b
```

```text
a = 3
b = 5

3 + 5 = 8

result = 8
```

### Step 4. 결과를 반환한다

```python
return result
```

```text
add 함수의 결과
   │
   ▼
8
```

`return`된 값이 함수 호출 위치로 돌아간다.

```python
answer = add(3, 5)
```

이 코드는 실제로는 다음처럼 이해할 수 있다.

```python
answer = 8
```

---

## 5. 구현 코드 및 상세 설명

```python
# 두 숫자를 더하는 함수
def add(a, b):
    result = a + b
    return result


# 점수가 합격인지 판단하는 함수
def is_passed(score):
    if score >= 60:
        return True
    else:
        return False


sum_result = add(10, 20)
print("더한 결과:", sum_result)

score = 75
passed = is_passed(score)
print("합격 여부:", passed)
```

### 코드 설명

```python
def add(a, b):
```

`add`라는 함수를 만든다.

이 함수는 `a`와 `b`라는 두 값을 입력으로 받는다.

```python
result = a + b
```

입력받은 두 값을 더한다.

```text
a = 10
b = 20

10 + 20 = 30
```

```python
return result
```

계산 결과를 함수 밖으로 돌려준다.

`return`이 없으면 함수 안에서 계산한 결과를 밖에서 사용하기 어렵다.

```python
def is_passed(score):
```

점수를 입력받아 합격 여부를 판단하는 함수다.

```python
if score >= 60:
    return True
else:
    return False
```

점수가 60 이상이면 `True`, 아니면 `False`를 반환한다.

```text
score = 75
75 >= 60 → True

반환값: True
```

함수를 사용하면 코드의 목적이 이름으로 드러난다.

`is_passed(score)`는 "이 점수가 합격인지 확인하는구나"라고 읽을 수 있다.

---

## 6. 마지막 정리

함수는 코드를 기능 단위로 묶어 이름을 붙인 것이다.

`def`를 사용해 함수를 정의한다.

매개변수는 함수 안으로 들어오는 값을 받는 변수다.

`return`은 함수가 만든 결과를 밖으로 돌려준다.

함수를 사용하면 중복 코드를 줄이고 코드의 의미를 더 쉽게 이해할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 함수",
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
