# 제목
[Java기초] 연산자

# 본문

## 1. 한 줄 요약

연산자는 Java에게 “이 값들로 어떤 일을 해줘”라고 알려주는 신호이다.

연산자를 배우면 계산기처럼 값을 계산하고, 저울처럼 값을 비교하고, 여러 조건을 함께 판단할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

가게에서 물건을 산다고 생각해 보자.

```text
가격 × 개수
총액 - 할인금액
총액이 50000원 이상인가?
회원이고 쿠폰도 있는가?
```

이런 판단과 계산을 Java 코드로 표현하려면 연산자가 필요하다.

```java
int total = price * count;
boolean canUseCoupon = isMember && hasCoupon;
```

연산자는 프로그램 안의 계산기 버튼, 비교 저울, 조건 연결 고리 역할을 한다.

---

## 3. 핵심 아이디어

산술 연산자는 계산기 버튼이다.

```text
+  더하기
-  빼기
*  곱하기
/  나누기
%  나머지
```

비교 연산자는 저울이다.

```text
10 > 5   → true
10 == 5  → false
```

논리 연산자는 조건을 묶는 접착제이다.

```text
회원이다 && 쿠폰이 있다
둘 다 참이면 할인 가능
```

```text
비가 온다 || 눈이 온다
둘 중 하나만 참이어도 우산 필요
```

---

## 4. 동작 과정 살펴보기

```java
int money = 10000;
int price = 3000;

boolean canBuy = money >= price;
```

### Step 1. 가지고 있는 돈 확인

```text
money ─────▶ 10000
price ─────▶ 3000
```

### Step 2. 비교 저울에 올리기

```text
10000 >= 3000
```

10000이 3000보다 크므로 결과는 참이다.

```text
결과: true
```

### Step 3. 조건 결과 저장

```text
canBuy ─────▶ true
```

이제 `canBuy`를 보고 물건을 살 수 있는지 판단할 수 있다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int applePrice = 1000;
        int appleCount = 5;

        int total = applePrice * appleCount;
        boolean enoughMoney = total <= 7000;

        boolean isMember = true;
        boolean hasPoint = true;
        boolean canDiscount = isMember && hasPoint;

        System.out.println("총 가격: " + total);
        System.out.println("돈이 충분한가? " + enoughMoney);
        System.out.println("할인 가능한가? " + canDiscount);
    }
}
```

### 코드 설명

```java
int total = applePrice * appleCount;
```

사과 가격과 개수를 곱한다.

```text
1000 × 5 = 5000
```

```java
boolean enoughMoney = total <= 7000;
```

총 가격이 7000 이하인지 확인한다.

```text
5000 <= 7000 → true
```

```java
boolean canDiscount = isMember && hasPoint;
```

회원이면서 포인트가 있을 때만 할인이 가능하다.

```text
true && true → true
```

---

## 6. 마지막 정리

연산자는 Java의 계산기 버튼이다.

비교 연산자는 결과로 `true` 또는 `false`를 만든다.

논리 연산자는 여러 조건을 합친다.

`&&`는 모두 참이어야 참이다.

`||`는 하나라도 참이면 참이다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 연산자",
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
