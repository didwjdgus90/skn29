# 제목
[Java기초] 연산자

# 본문

## 1. 한 줄 요약

연산자는 피연산자에 대해 산술, 비교, 논리, 대입 등의 작업을 수행하는 Java 문법 요소이다.

연산자를 이해하면 표현식의 평가 결과와 프로그램의 제어 흐름을 정확히 예측할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

Java 프로그램은 표현식의 평가를 통해 값을 계산하고 조건을 판단한다.

```java
int result = a + b * c;
boolean valid = score >= 60 && attendance >= 80;
```

위 코드에서 연산자는 값 사이의 관계와 처리 방식을 정의한다.

연산자의 우선순위와 결과 타입을 이해하지 못하면 예상과 다른 결과가 나올 수 있다.

예를 들어 정수 나눗셈은 소수점을 버린다.

```java
System.out.println(10 / 3); // 3
```

---

## 3. 핵심 아이디어

Java 연산자는 기능에 따라 분류된다.

```text
산술 연산자  + - * / %
비교 연산자  > < >= <= == !=
논리 연산자  && || !
대입 연산자  = += -= *= /=
증감 연산자  ++ --
```

연산자는 표현식을 만들고, 표현식은 하나의 값으로 평가된다.

```text
10 + 20 → 30
score >= 60 → true 또는 false
```

비교 연산과 논리 연산의 결과는 `boolean`이다.

이 결과는 조건문이나 반복문의 조건식에 자주 사용된다.

---

## 4. 동작 과정 살펴보기

```java
int a = 10;
int b = 3;

int q = a / b;
int r = a % b;
```

### Step 1. 정수 나눗셈

```text
10 / 3 = 3.333...
```

Java에서 `int / int` 결과는 정수이다.

```text
q = 3
```

### Step 2. 나머지 계산

```text
10 % 3 = 1
```

`%`는 나눗셈 후 남은 값을 반환한다.

### Step 3. 비교 표현식

```java
boolean check = q == 3;
```

```text
q == 3
3 == 3 → true
```

### Step 4. 논리 표현식

```java
boolean valid = q == 3 && r == 1;
```

```text
true && true → true
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;

        int quotient = a / b;
        int remainder = a % b;

        boolean isQuotientThree = quotient == 3;
        boolean isExact = remainder == 0;
        boolean condition = isQuotientThree && !isExact;

        System.out.println("몫: " + quotient);
        System.out.println("나머지: " + remainder);
        System.out.println("몫이 3인가? " + isQuotientThree);
        System.out.println("나누어떨어지는가? " + isExact);
        System.out.println("조건 결과: " + condition);
    }
}
```

### 코드 설명

```java
int quotient = a / b;
```

정수 나눗셈을 수행한다.

피연산자가 모두 `int`이므로 결과도 `int`로 평가된다.

```java
int remainder = a % b;
```

나머지 연산을 수행한다.

짝수 판별, 배수 판별, 순환 인덱스 계산 등에 자주 사용된다.

```java
boolean condition = isQuotientThree && !isExact;
```

`&&`는 두 조건이 모두 참일 때 참이다.

`!`는 논리값을 반대로 바꾼다.

---

## 6. 마지막 정리

연산자는 표현식을 구성하고 하나의 결과값을 만든다.

산술 연산자는 숫자 계산을 수행한다.

비교 연산자는 `boolean` 결과를 만든다.

논리 연산자는 `boolean` 값을 조합한다.

정수 나눗셈과 연산자 우선순위는 Java에서 특히 주의해야 한다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 연산자",
  "source_type": "generated",
  "style": [
    "theory",
    "code"
  ],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "mid",
  "language": "java"
}
```
