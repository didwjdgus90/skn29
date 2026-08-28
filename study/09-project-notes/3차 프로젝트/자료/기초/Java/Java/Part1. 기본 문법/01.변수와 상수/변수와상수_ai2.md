# 제목
[Java기초] 변수와 상수

# 본문

## 1. 한 줄 요약

변수는 물건을 담아두는 상자이고, 상수는 한 번 붙이면 바꿀 수 없는 고정 라벨이 붙은 상자이다.

Java에서 변수와 상수를 배우면 값을 헷갈리지 않게 이름으로 관리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

요리할 때 재료를 아무 그릇에나 담아두면 무엇이 소금이고 무엇이 설탕인지 헷갈릴 수 있다.

그래서 그릇에 이름표를 붙인다.

```text
[소금]
[설탕]
[밀가루]
```

프로그래밍에서도 숫자만 덩그러니 쓰면 의미를 알기 어렵다.

```java
System.out.println(10000 * 2);
```

`10000`이 가격인지 점수인지 알 수 없다.

변수를 사용하면 값에 이름표를 붙일 수 있다.

```java
int price = 10000;
int count = 2;
```

상수는 절대 바꾸면 안 되는 중요한 값에 붙이는 고정 이름표이다.

```java
final int MAX_SCORE = 100;
```

---

## 3. 핵심 아이디어

변수는 이름 붙은 상자이다.

```text
상자 이름: age
상자 안 값: 20

age ─────▶ 20
```

Java에서는 상자를 만들 때 어떤 종류의 물건을 넣을지도 정해야 한다.

```text
int age = 20;

int  → 숫자 전용 상자
age  → 상자 이름
20   → 상자 안의 값
```

상수는 잠긴 상자라고 생각하면 된다.

```java
final int MAX_COUNT = 10;
```

```text
MAX_COUNT ─────▶ 10
      🔒
```

한 번 10을 넣으면 다른 값으로 바꿀 수 없다.

---

## 4. 동작 과정 살펴보기

```java
int money = 5000;
money = money + 2000;
System.out.println(money);
```

### Step 1. 돈 상자를 만든다

```text
money 상자

[5000]
```

### Step 2. 기존 값을 꺼내 계산한다

```text
money + 2000

5000 + 2000 = 7000
```

오른쪽의 `money`는 상자 안에 있던 5000을 의미한다.

### Step 3. 계산 결과를 다시 넣는다

```text
기존 상자
[5000]

변경 후 상자
[7000]
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        String menu = "김밥";
        int price = 3500;
        int count = 2;
        final int DISCOUNT = 500;

        int total = price * count;
        int pay = total - DISCOUNT;

        System.out.println("메뉴: " + menu);
        System.out.println("결제 금액: " + pay);
    }
}
```

### 코드 설명

```java
String menu = "김밥";
```

`menu`라는 상자에 글자 데이터를 담는다.

글자는 Java에서 `String`으로 표현한다.

```java
int price = 3500;
```

`price`라는 숫자 상자에 가격을 담는다.

```java
final int DISCOUNT = 500;
```

할인 금액은 바꾸지 않겠다는 뜻으로 `final`을 붙였다.

```java
int total = price * count;
```

가격과 개수를 곱한다.

```text
3500 × 2 = 7000
```

```java
int pay = total - DISCOUNT;
```

총 금액에서 할인 금액을 뺀다.

```text
7000 - 500 = 6500
```

---

## 6. 마지막 정리

변수는 값을 담는 이름 붙은 상자이다.

Java에서는 상자를 만들 때 자료형을 먼저 정해야 한다.

`int`는 정수, `String`은 문자열을 담는다.

`final`을 붙이면 값을 바꿀 수 없는 상수가 된다.

상수 이름은 보통 대문자로 작성한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 변수와 상수",
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
  "language": "java"
}
```