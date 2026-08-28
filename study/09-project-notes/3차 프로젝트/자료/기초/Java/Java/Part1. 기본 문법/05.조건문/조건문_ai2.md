# 제목
[Java기초] 조건문

# 본문

## 1. 한 줄 요약

조건문은 갈림길에서 어느 길로 갈지 선택하게 해주는 Java 문법이다.

조건문을 배우면 프로그램이 상황을 보고 다르게 행동하도록 만들 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

아침에 밖에 나가기 전 날씨를 본다고 생각해 보자.

```text
비가 오면 → 우산 챙기기
비가 안 오면 → 그냥 나가기
```

프로그램도 이런 선택이 필요하다.

```java
if (isRainy) {
    System.out.println("우산 챙기기");
} else {
    System.out.println("그냥 나가기");
}
```

조건문은 컴퓨터가 상황에 따라 다른 길을 선택하게 한다.

---

## 3. 핵심 아이디어

조건문은 신호등과 비슷하다.

```text
초록불이면 건넌다.
빨간불이면 멈춘다.
```

Java는 조건을 확인하고 결과가 `true`인지 `false`인지 본다.

```text
조건 결과 true  → if 안으로 들어감
조건 결과 false → else로 감
```

```java
if (조건) {
    참일 때 실행
} else {
    거짓일 때 실행
}
```

---

## 4. 동작 과정 살펴보기

```java
int age = 17;

if (age >= 20) {
    System.out.println("성인");
} else {
    System.out.println("미성년자");
}
```

### Step 1. 나이 확인

```text
age ─────▶ 17
```

### Step 2. 조건 검사

```text
17 >= 20
   ↓
false
```

### Step 3. else 길로 이동

```text
if 길: 가지 않음
else 길: 이동
```

### Step 4. 결과 출력

```text
미성년자
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int money = 5000;
        int price = 3000;

        if (money >= price) {
            System.out.println("구매할 수 있습니다.");
            money = money - price;
            System.out.println("남은 돈: " + money);
        } else {
            System.out.println("돈이 부족합니다.");
        }
    }
}
```

### 코드 설명

```java
if (money >= price)
```

가진 돈이 물건 가격보다 크거나 같은지 확인한다.

```text
5000 >= 3000 → true
```

```java
money = money - price;
```

구매 후 남은 돈을 계산한다.

```text
5000 - 3000 = 2000
```

```java
else
```

돈이 부족할 때 실행될 길이다.

이번 예제에서는 조건이 참이므로 실행되지 않는다.

---

## 6. 마지막 정리

조건문은 프로그램의 갈림길이다.

조건 결과가 `true`이면 `if` 블록을 실행한다.

조건 결과가 `false`이면 `else` 블록을 실행한다.

여러 갈림길이 필요하면 `else if`를 사용한다.

조건문 블록은 중괄호 `{}`로 묶는다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 조건문",
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
