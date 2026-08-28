# 제목
[Java기초] 연산자

# 본문

## 1. 한 줄 요약

연산자는 값들을 계산하거나 비교하거나 조건을 조합할 때 사용하는 기호이다.

Java에서 연산자를 이해하면 숫자 계산, 값 비교, 조건 판단, 변수 값 변경을 코드로 표현할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 값을 저장만 하지 않는다.

저장한 값을 더하고, 빼고, 비교하고, 조건에 따라 판단해야 한다.

```java
int total = price * count;
boolean isFreeDelivery = total >= 50000;
boolean canDiscount = isMember && hasCoupon;
```

이 코드에서 `*`, `>=`, `&&`가 모두 연산자이다.

연산자가 없다면 “가격과 개수를 곱한다”, “총액이 50000 이상인지 확인한다” 같은 동작을 표현하기 어렵다.

---

## 3. 핵심 아이디어

연산자는 계산기 버튼과 비슷하다.

```text
10 + 3  → 13
10 - 3  → 7
10 > 3  → true
```

Java의 주요 연산자는 다음과 같다.

```text
산술 연산자  → +, -, *, /, %
비교 연산자  → >, <, >=, <=, ==, !=
논리 연산자  → &&, ||, !
대입 연산자  → =, +=, -=
```

연산자는 값과 값 사이에 들어가서 “무슨 일을 할지” 정한다.

---

## 4. 동작 과정 살펴보기

```java
int price = 10000;
int count = 3;
int total = price * count;
```

### Step 1. 변수에 값 저장

```text
price ─────▶ 10000
count ─────▶ 3
```

### Step 2. 곱셈 연산

```text
price * count
10000 * 3 = 30000
```

### Step 3. 결과 저장

```text
total ─────▶ 30000
```

### Step 4. 비교 연산

```java
boolean result = total >= 30000;
```

```text
30000 >= 30000
      ↓
true
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int price = 12000;
        int count = 4;
        int point = 3000;

        int total = price * count;
        int pay = total - point;

        boolean isFreeDelivery = total >= 50000;

        boolean isMember = true;
        boolean hasCoupon = false;
        boolean canDiscount = isMember && hasCoupon;

        int score = 80;
        score += 10;

        System.out.println("총 금액: " + total);
        System.out.println("결제 금액: " + pay);
        System.out.println("무료 배송 여부: " + isFreeDelivery);
        System.out.println("할인 가능 여부: " + canDiscount);
        System.out.println("최종 점수: " + score);
    }
}
```

### 코드 설명

```java
int total = price * count;
```

`*`는 곱셈 연산자이다.

상품 가격과 개수를 곱해 총 금액을 계산한다.

```java
boolean isFreeDelivery = total >= 50000;
```

`>=`는 왼쪽 값이 오른쪽 값보다 크거나 같은지 확인한다.

결과는 `true` 또는 `false`이다.

```java
boolean canDiscount = isMember && hasCoupon;
```

`&&`는 두 조건이 모두 참일 때만 참이 된다.

```java
score += 10;
```

`score = score + 10;`과 같은 의미이다.

---

## 6. 마지막 정리

연산자는 값을 계산하고 비교하고 판단하는 데 사용한다.

산술 연산자는 숫자 계산에 사용한다.

비교 연산자의 결과는 `boolean`이다.

논리 연산자는 여러 조건을 연결한다.

`+=` 같은 복합 대입 연산자는 기존 값을 갱신할 때 편리하다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 연산자",
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
