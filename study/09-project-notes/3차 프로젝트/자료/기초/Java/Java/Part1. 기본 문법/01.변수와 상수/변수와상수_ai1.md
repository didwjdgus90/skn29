# 제목
[Java기초] 변수와 상수

# 본문

## 1. 한 줄 요약

변수는 값을 저장해두는 이름 있는 공간이고, 상수는 한 번 정하면 바꾸지 않기로 한 값이다.

Java에서 변수와 상수를 이해하면 숫자, 문자열, 계산 결과를 이름으로 관리하면서 더 읽기 좋은 코드를 작성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램에서는 같은 값을 여러 번 사용해야 하는 경우가 많다.

예를 들어 상품 가격, 개수, 배송비를 계산한다고 해보자.

```java
System.out.println(15000 * 3 + 2500);
```

이 코드는 계산은 되지만, `15000`, `3`, `2500`이 각각 무엇을 의미하는지 바로 알기 어렵다.

변수를 사용하면 값에 의미 있는 이름을 붙일 수 있다.

```java
int price = 15000;
int count = 3;
int deliveryFee = 2500;
```

상수는 프로그램 실행 중 바뀌면 안 되는 값을 표현할 때 사용한다.

```java
final int DELIVERY_FEE = 2500;
```

---

## 3. 핵심 아이디어

변수는 값에 붙이는 이름표이다.

```text
값: 15000
↓
price = 15000
```

Java에서는 변수를 만들 때 반드시 자료형을 함께 적는다.

```text
int price = 15000;

int    → 어떤 종류의 값인지
price  → 변수 이름
15000  → 실제 값
```

상수는 변수와 비슷하지만 한 번 값을 넣으면 다시 바꿀 수 없다.

Java에서는 `final` 키워드를 사용한다.

```java
final double PI = 3.14;
```

```text
PI ─────▶ 3.14

이후 PI 값을 다른 값으로 변경 불가
```

---

## 4. 동작 과정 살펴보기

아래 코드를 단계별로 보자.

```java
int score = 80;
score = score + 10;
System.out.println(score);
```

### Step 1. 변수 만들기

```text
score
  │
  ▼
 80
```

`int score = 80;`은 정수 값을 담을 수 있는 `score`라는 변수를 만들고 80을 저장한다.

### Step 2. 오른쪽 계산 먼저 수행

```text
score = score + 10

오른쪽 score는 현재 값 80

80 + 10 = 90
```

대입문에서는 오른쪽이 먼저 계산된다.

### Step 3. 결과를 다시 저장

```text
기존

score ─────▶ 80

변경 후

score ─────▶ 90
```

계산 결과 90이 다시 `score`에 저장된다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int price = 15000;
        int count = 3;
        final int DELIVERY_FEE = 2500;

        int totalPrice = price * count;
        int finalPrice = totalPrice + DELIVERY_FEE;

        System.out.println("상품 가격: " + price);
        System.out.println("구매 개수: " + count);
        System.out.println("총 상품 금액: " + totalPrice);
        System.out.println("배송비: " + DELIVERY_FEE);
        System.out.println("최종 결제 금액: " + finalPrice);
    }
}
```

### 코드 설명

```java
int price = 15000;
```

정수형 변수 `price`를 만들고 상품 가격을 저장한다.

Java에서는 변수 앞에 `int`처럼 자료형을 적어야 한다.

```java
final int DELIVERY_FEE = 2500;
```

`final`이 붙었으므로 이 값은 이후 변경할 수 없다.

상수 이름은 관례적으로 대문자와 밑줄을 사용한다.

```java
int totalPrice = price * count;
```

상품 가격과 개수를 곱해 총 상품 금액을 계산한다.

```text
15000 × 3 = 45000
```

```java
int finalPrice = totalPrice + DELIVERY_FEE;
```

총 상품 금액에 배송비를 더한다.

```text
45000 + 2500 = 47500
```

---

## 6. 마지막 정리

변수는 값을 저장하고 다시 사용하기 위한 이름 있는 공간이다.

Java에서는 변수를 만들 때 자료형을 반드시 적는다.

상수는 `final`을 사용해 만든다.

상수 이름은 보통 대문자로 작성한다.

의미 있는 변수 이름을 사용하면 코드가 훨씬 읽기 쉬워진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 변수와 상수",
  "source_type": "generated",
  "style": [
    "easy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "java"
}
```