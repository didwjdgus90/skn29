# 제목
[Python 기초] 연산자 (Operators)

# 본문

## 1. 한 줄 요약

연산자는 값들을 계산하거나 비교하거나 조건을 조합할 때 사용하는 기호와 키워드이다.

연산자를 이해하면 숫자 계산, 값 비교, 조건 판단 같은 프로그램의 기본 동작을 만들 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 값을 저장만 하지 않는다.

저장한 값을 더하고, 비교하고, 조건에 따라 판단해야 한다.

예를 들어 쇼핑몰 프로그램에서는 다음과 같은 계산이 필요하다.

```text
상품 가격 × 개수
총 금액이 50000원 이상인지 확인
쿠폰을 사용했는지 확인
```

이때 사용하는 것이 연산자다.

```python
total = price * count
is_free_delivery = total >= 50000
can_discount = is_member and has_coupon
```

연산자가 없다면 계산이나 비교를 코드로 표현하기 어렵다.

연산자는 프로그램에게 "이 값들로 어떤 작업을 할지" 알려주는 신호라고 볼 수 있다.

---

## 3. 핵심 아이디어

연산자는 계산기 버튼과 비슷하다.

계산기에서 `+`, `-`, `×`, `÷` 버튼을 누르면 숫자 사이의 관계가 정해진다.

```text
10  +  3  = 13
10  -  3  = 7
10  ×  3  = 30
```

파이썬에서도 연산자는 값과 값 사이에 들어가서 일을 한다.

```text
값  연산자  값

10    +     3
10    >     3
True and False
```

연산자는 크게 다음처럼 나눌 수 있다.

```text
산술 연산자  → 계산하기
비교 연산자  → 크기나 같음을 비교하기
논리 연산자  → 여러 조건을 함께 판단하기
대입 연산자  → 변수에 값 저장하기
```

연산자는 문장의 동사처럼 값 사이에서 실제 행동을 담당한다.

---

## 4. 동작 과정 살펴보기

아래 상황을 생각해 보자.

```python
price = 10000
count = 3
point = 5000
```

### Step 1. 산술 연산자로 계산하기

```python
total = price * count
```

```text
price ─────▶ 10000
count ─────▶ 3

10000 * 3 = 30000

total ─────▶ 30000
```

`*`는 곱하기 연산자다.

상품 가격과 개수를 곱해서 총 금액을 만든다.

### Step 2. 비교 연산자로 판단하기

```python
total >= 30000
```

```text
total = 30000

30000 >= 30000
      ↓
True
```

`>=`는 왼쪽 값이 오른쪽 값보다 크거나 같은지 확인한다.

결과는 `True` 또는 `False`이다.

### Step 3. 논리 연산자로 조건 합치기

```python
total >= 30000 and point >= 1000
```

```text
조건 1: total >= 30000
30000 >= 30000 → True

조건 2: point >= 1000
5000 >= 1000 → True

True and True → True
```

`and`는 두 조건이 모두 참일 때만 참이 된다.

### Step 4. 대입 연산자로 결과 저장하기

```python
can_use_coupon = total >= 30000 and point >= 1000
```

```text
계산 결과: True
      ↓
can_use_coupon ─────▶ True
```

계산과 비교를 통해 나온 결과를 변수에 저장할 수 있다.

---

## 5. 구현 코드 및 상세 설명

```python
price = 12000
count = 4
point = 3000

# 산술 연산자
total_price = price * count
discount_price = total_price - point

print("총 금액:", total_price)
print("포인트 적용 후 금액:", discount_price)

# 비교 연산자
is_free_delivery = total_price >= 50000
print("무료 배송 여부:", is_free_delivery)

# 논리 연산자
is_member = True
has_coupon = False

can_discount = is_member and has_coupon
print("할인 가능 여부:", can_discount)

# 대입 연산자
score = 80
score += 10
print("최종 점수:", score)
```

### 코드 설명

```python
total_price = price * count
```

`price`와 `count`를 곱한다.

```text
12000 * 4 = 48000
```

계산 결과 `48000`이 `total_price`에 저장된다.

```python
discount_price = total_price - point
```

총 금액에서 포인트를 뺀다.

```text
48000 - 3000 = 45000
```

```python
is_free_delivery = total_price >= 50000
```

총 금액이 50000 이상인지 비교한다.

```text
48000 >= 50000
      ↓
False
```

결과는 `False`이므로 무료 배송이 아니다.

```python
can_discount = is_member and has_coupon
```

회원이면서 쿠폰도 있어야 할인이 가능하다고 가정한다.

```text
is_member  = True
has_coupon = False

True and False → False
```

둘 중 하나라도 거짓이면 `and` 결과는 거짓이다.

```python
score += 10
```

`score = score + 10`과 같은 의미다.

```text
score = 80
score + 10 = 90
score = 90
```

---

## 6. 마지막 정리

연산자는 값으로 계산, 비교, 판단을 할 때 사용한다.

산술 연산자는 더하기, 빼기, 곱하기, 나누기 같은 계산을 담당한다.

비교 연산자는 결과로 `True` 또는 `False`를 만든다.

논리 연산자는 여러 조건을 하나로 합칠 때 사용한다.

`+=` 같은 대입 연산자는 기존 변수 값을 바꿔 저장할 때 유용하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 연산자",
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
