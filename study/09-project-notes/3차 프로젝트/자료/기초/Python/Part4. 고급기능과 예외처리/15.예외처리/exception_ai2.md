# 제목
[Python 기초] 예외 처리 (Exception Handling)

# 본문

## 1. 한 줄 요약

예외처리는 프로그램 실행 중 오류가 발생해도 멈추지 않고 적절히 대응하도록 만드는 문법이다.

예외처리를 이해하면 예상 가능한 문제 상황을 안전하게 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 항상 정상적인 값만 받지 않는다.

사용자가 숫자를 입력해야 하는 곳에 문자를 입력할 수도 있다.

```python
age = int(input("나이를 입력하세요: "))
```

여기서 사용자가 `스무살`이라고 입력하면 파이썬은 숫자로 바꿀 수 없어서 오류를 발생시킨다.

오류가 처리되지 않으면 프로그램은 바로 멈춘다.

```text
입력: 스무살
숫자로 변환 실패
프로그램 종료
```

하지만 실제 서비스에서는 오류가 났다고 바로 꺼지면 안 된다.

사용자에게 다시 입력하라고 안내하거나, 기본값을 사용해야 한다.

예외처리는 이런 상황을 처리하기 위해 사용한다.

```python
try:
    age = int(input("나이를 입력하세요: "))
except ValueError:
    print("숫자로 입력해야 합니다.")
```

---

## 3. 핵심 아이디어

예외처리는 안전망과 비슷하다.

높은 곳에서 작업할 때 안전망이 있으면 실수해도 크게 다치지 않는다.

```text
일반 실행
   │
   ▼
문제 없음 → 계속 진행

문제 발생
   │
   ▼
안전망 except가 받아줌
```

파이썬에서는 문제가 생길 수 있는 코드를 `try` 안에 넣는다.

문제가 실제로 발생하면 `except`가 그 문제를 받아서 처리한다.

```python
try:
    위험할 수 있는 코드
except:
    문제가 생겼을 때 실행할 코드
```

예외처리는 오류를 없애는 문법이 아니다.

오류가 날 수 있다는 사실을 인정하고, 그 상황에 맞는 행동을 정해두는 문법이다.

---

## 4. 동작 과정 살펴보기

아래 코드를 보자.

```python
try:
    number = int("abc")
    print(number)
except ValueError:
    print("숫자로 바꿀 수 없습니다.")
```

### Step 1. try 블록에 들어간다

```text
try 시작
   │
   ▼
int("abc") 실행
```

`try` 안의 코드를 위에서 아래로 실행한다.

### Step 2. 오류가 발생한다

```text
"abc"를 숫자로 바꾸기 시도

"abc" → 숫자 변환 불가
```

`int("abc")`는 실패한다.

이때 `ValueError`라는 예외가 발생한다.

### Step 3. except 블록으로 이동한다

```text
ValueError 발생
   │
   ▼
except ValueError 실행
```

파이썬은 오류 종류와 맞는 `except`를 찾는다.

### Step 4. 오류 처리 코드를 실행한다

```text
출력 결과

숫자로 바꿀 수 없습니다.
```

오류가 발생했지만 프로그램은 갑자기 종료되지 않는다.

예외처리 덕분에 안내 메시지를 출력하고 정상적으로 흐름을 이어갈 수 있다.

---

## 5. 구현 코드 및 상세 설명

```python
user_input = input("숫자를 입력하세요: ")

try:
    number = int(user_input)
    result = 100 / number
    print("계산 결과:", result)

except ValueError:
    print("숫자 형태로 입력해야 합니다.")

except ZeroDivisionError:
    print("0으로는 나눌 수 없습니다.")

finally:
    print("프로그램을 종료합니다.")
```

### 코드 설명

```python
user_input = input("숫자를 입력하세요: ")
```

사용자로부터 값을 입력받는다.

입력값은 기본적으로 문자열이다.

```python
number = int(user_input)
```

문자열을 정수로 바꾼다.

이때 `"abc"`처럼 숫자가 아닌 값이면 `ValueError`가 발생한다.

```python
result = 100 / number
```

100을 입력받은 숫자로 나눈다.

만약 `number`가 0이면 0으로 나눌 수 없기 때문에 `ZeroDivisionError`가 발생한다.

```python
except ValueError:
```

숫자 변환에 실패했을 때 실행된다.

```python
except ZeroDivisionError:
```

0으로 나누려고 했을 때 실행된다.

```python
finally:
```

오류가 나든 나지 않든 마지막에 항상 실행된다.

파일 닫기, 연결 종료, 마무리 메시지 출력 등에 사용할 수 있다.

```text
정상 입력
try 실행 → finally 실행

문자 입력
try 실행 중 오류 → except 실행 → finally 실행

0 입력
try 실행 중 오류 → except 실행 → finally 실행
```

---

## 6. 마지막 정리

예외처리는 오류가 발생해도 프로그램이 갑자기 멈추지 않도록 돕는다.

`try`에는 오류가 발생할 수 있는 코드를 넣는다.

`except`에는 오류가 발생했을 때 처리할 코드를 넣는다.

오류 종류별로 `except`를 나누면 더 정확하게 대응할 수 있다.

`finally`는 오류 여부와 상관없이 항상 실행된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 예외처리",
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
