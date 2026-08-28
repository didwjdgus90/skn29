# 제목
[Java기초] 자료형

# 본문

## 1. 한 줄 요약

자료형은 변수에 저장 가능한 값의 종류와 크기, 해석 방식을 정의하는 Java의 기본 타입 체계이다.

자료형을 이해하면 메모리 사용, 연산 방식, 타입 안정성을 고려해 적절한 데이터를 표현할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

Java는 정적 타입 언어이다.

따라서 모든 변수는 선언 시점에 자료형이 결정된다.

```java
int count = 10;
double average = 85.5;
```

이 방식은 코드 작성이 조금 엄격하게 느껴질 수 있다.

하지만 잘못된 값을 저장하는 실수를 컴파일 단계에서 발견할 수 있다는 장점이 있다.

```java
int count = "ten"; // 타입 불일치
```

자료형은 다음 질문에 답한다.

```text
이 변수는 어떤 종류의 값을 저장하는가?
이 값은 어떤 연산이 가능한가?
이 값은 어느 정도 범위를 표현할 수 있는가?
```

---

## 3. 핵심 아이디어

Java 자료형은 크게 기본형과 참조형으로 나눌 수 있다.

```text
기본형
- int
- long
- double
- char
- boolean

참조형
- String
- 배열
- 클래스 객체
```

기본형은 실제 값을 직접 저장하는 데 사용된다.

참조형은 객체의 위치를 참조하는 값으로 이해할 수 있다.

입문 단계에서는 다음 구분이 중요하다.

```text
정수       → int, long
실수       → double
문자 한 개 → char
참/거짓    → boolean
문자열     → String
```

자료형에 따라 사용할 수 있는 연산도 다르다.

```java
int a = 10;
int b = 3;

System.out.println(a / b); // 3
```

정수끼리 나누면 결과도 정수로 처리된다.

```java
double x = 10.0;
double y = 3.0;

System.out.println(x / y); // 3.333...
```

실수 연산은 소수점 결과를 보존한다.

---

## 4. 동작 과정 살펴보기

```java
int a = 10;
int b = 3;
double c = 3.0;
```

### Step 1. 정수 변수 선언

```text
a: int → 10
b: int → 3
```

두 변수 모두 정수형이다.

### Step 2. 정수 나눗셈

```java
a / b
```

```text
10 / 3 = 3.333...

int / int 결과는 정수
결과: 3
```

Java는 정수 나눗셈에서 소수 부분을 버린다.

### Step 3. 실수 나눗셈

```java
a / c
```

```text
10 / 3.0

int와 double 연산
결과는 double
3.333333...
```

연산에 실수형이 포함되면 실수 연산으로 처리된다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int a = 10;
        int b = 3;
        double c = 3.0;

        int intResult = a / b;
        double doubleResult = a / c;

        char grade = 'A';
        boolean passed = true;
        String name = "Java";

        System.out.println("정수 나눗셈: " + intResult);
        System.out.println("실수 나눗셈: " + doubleResult);
        System.out.println("등급: " + grade);
        System.out.println("합격 여부: " + passed);
        System.out.println("언어 이름: " + name);
    }
}
```

### 코드 설명

```java
int intResult = a / b;
```

`a`와 `b`가 모두 정수형이므로 결과도 정수형으로 계산된다.

소수점 아래는 버려진다.

```java
double doubleResult = a / c;
```

`c`가 `double`이므로 연산 결과는 실수형으로 처리된다.

```java
char grade = 'A';
```

`char`는 문자 한 개를 저장한다.

문자 하나에는 작은따옴표를 사용한다.

```java
String name = "Java";
```

`String`은 문자열을 저장하는 참조형 자료형이다.

문자열에는 큰따옴표를 사용한다.

---

## 6. 마지막 정리

Java 자료형은 변수에 저장할 값의 종류를 정의한다.

기본형에는 `int`, `long`, `double`, `char`, `boolean` 등이 있다.

`String`은 문자열을 다루는 참조형이다.

정수 나눗셈과 실수 나눗셈의 결과는 다를 수 있다.

자료형 선택은 연산 결과와 코드 안정성에 직접적인 영향을 준다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 자료형",
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