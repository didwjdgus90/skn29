# 제목
[Java기초] 자료형

# 본문

## 1. 한 줄 요약

자료형은 변수에 어떤 종류의 값을 저장할 수 있는지 정하는 규칙이다.

Java에서 자료형을 이해하면 숫자, 문자, 참거짓, 문자열을 올바르게 저장하고 계산할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

컴퓨터는 값의 종류에 따라 다르게 처리한다.

`10`은 숫자라서 계산할 수 있지만, `"10"`은 문자열이라서 글자로 다뤄진다.

```java
System.out.println(10 + 20);
System.out.println("10" + "20");
```

출력 결과는 다르다.

```text
30
1020
```

Java는 변수를 만들 때 자료형을 반드시 정해야 한다.

```java
int age = 20;
String name = "민수";
boolean passed = true;
```

자료형은 변수에 들어갈 값의 종류를 미리 약속하는 역할을 한다.

---

## 3. 핵심 아이디어

자료형은 값을 담는 그릇의 종류이다.

```text
정수 그릇     → int
실수 그릇     → double
글자 한 개    → char
참/거짓 그릇  → boolean
문자열 그릇   → String
```

Java의 대표 자료형은 다음과 같다.

```text
int      정수
long     더 큰 정수
double   실수
char     문자 한 개
boolean  참 또는 거짓
String   문자열
```

Java에서는 자료형이 맞지 않으면 값을 넣을 수 없다.

```java
int age = "스무살"; // 불가능
```

이 규칙 덕분에 잘못된 값을 미리 발견할 수 있다.

---

## 4. 동작 과정 살펴보기

```java
int age = 20;
double height = 175.5;
char grade = 'A';
boolean isPassed = true;
String name = "민수";
```

### Step 1. 정수 저장

```text
age ─────▶ 20
자료형: int
```

`int`는 소수점 없는 정수를 저장한다.

### Step 2. 실수 저장

```text
height ─────▶ 175.5
자료형: double
```

`double`은 소수점이 있는 숫자를 저장한다.

### Step 3. 문자 한 개 저장

```text
grade ─────▶ 'A'
자료형: char
```

`char`는 문자 한 개만 저장한다.

작은따옴표를 사용한다.

### Step 4. 문자열 저장

```text
name ─────▶ "민수"
자료형: String
```

`String`은 여러 글자를 저장한다.

큰따옴표를 사용한다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int age = 20;
        long population = 50000000L;
        double height = 175.5;
        char grade = 'A';
        boolean isPassed = true;
        String name = "민수";

        System.out.println("이름: " + name);
        System.out.println("나이: " + age);
        System.out.println("인구: " + population);
        System.out.println("키: " + height);
        System.out.println("등급: " + grade);
        System.out.println("합격 여부: " + isPassed);
    }
}
```

### 코드 설명

```java
int age = 20;
```

정수 값을 저장한다.

나이처럼 소수점이 필요 없는 값에 적합하다.

```java
long population = 50000000L;
```

`long`은 `int`보다 더 큰 정수를 저장할 수 있다.

숫자 뒤에 `L`을 붙이는 경우가 많다.

```java
double height = 175.5;
```

소수점이 있는 숫자를 저장한다.

```java
char grade = 'A';
```

문자 한 개를 저장한다.

`char`는 작은따옴표를 사용한다.

```java
String name = "민수";
```

여러 글자로 이루어진 문자열을 저장한다.

`String`은 큰따옴표를 사용한다.

---

## 6. 마지막 정리

자료형은 변수에 저장할 값의 종류를 정한다.

Java는 변수를 선언할 때 자료형을 반드시 적는다.

`int`, `long`, `double`, `char`, `boolean`, `String`이 자주 사용된다.

`char`는 작은따옴표, `String`은 큰따옴표를 사용한다.

자료형을 잘 선택하면 오류를 줄이고 코드 의미가 명확해진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 자료형",
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