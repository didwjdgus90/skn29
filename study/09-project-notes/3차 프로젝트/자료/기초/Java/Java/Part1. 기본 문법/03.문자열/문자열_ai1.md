# 제목
[Java기초] 문자열

# 본문

## 1. 한 줄 요약

문자열은 여러 글자를 하나로 묶어 표현하는 자료형이며, Java에서는 `String`을 사용한다.

문자열을 이해하면 이름, 문장, 입력값, 메시지 같은 글자 데이터를 저장하고 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 숫자뿐 아니라 글자도 많이 다룬다.

```text
사용자 이름
이메일 주소
비밀번호
문제 입력 문자열
출력 메시지
```

이런 글자 데이터를 저장하려면 문자열이 필요하다.

Java에서는 문자열을 큰따옴표로 감싸고 `String` 타입에 저장한다.

```java
String name = "민수";
String message = "Hello Java";
```

문자열을 사용하면 글자를 붙이고, 길이를 구하고, 특정 위치의 문자를 확인할 수 있다.

---

## 3. 핵심 아이디어

문자열은 글자들이 순서대로 줄 서 있는 구조이다.

```text
"Java"

J   a   v   a
0   1   2   3
```

각 글자에는 위치 번호가 있다.

이 번호를 인덱스라고 한다.

Java에서도 인덱스는 0부터 시작한다.

```java
String word = "Java";
System.out.println(word.charAt(0));
```

```text
word.charAt(0) → 'J'
```

문자열의 길이는 `length()`로 구한다.

```java
word.length()
```

```text
"Java"의 길이 → 4
```

---

## 4. 동작 과정 살펴보기

```java
String word = "Code";
```

### Step 1. 문자열 저장

```text
word ─────▶ "Code"

C   o   d   e
0   1   2   3
```

`word`는 `"Code"`라는 문자열을 가리킨다.

### Step 2. 길이 구하기

```java
word.length()
```

```text
C o d e
1 2 3 4

길이: 4
```

### Step 3. 특정 문자 꺼내기

```java
word.charAt(1)
```

```text
C   o   d   e
    ↑
   1번
```

결과는 `'o'`이다.

### Step 4. 문자열 붙이기

```java
String result = word + " Test";
```

```text
"Code" + " Test"
        ↓
"Code Test"
```

`+`를 사용하면 문자열을 이어 붙일 수 있다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        String word = "Java";

        System.out.println("문자열: " + word);
        System.out.println("길이: " + word.length());
        System.out.println("첫 번째 문자: " + word.charAt(0));
        System.out.println("두 번째 문자: " + word.charAt(1));

        String greeting = "Hello";
        String language = "Java";
        String message = greeting + " " + language;

        System.out.println(message);
        System.out.println(word.substring(1, 3));
        System.out.println(word.equals("Java"));
    }
}
```

### 코드 설명

```java
String word = "Java";
```

문자열 `"Java"`를 `word` 변수에 저장한다.

```java
word.length()
```

문자열의 길이를 구한다.

`"Java"`는 글자 4개이므로 결과는 4이다.

```java
word.charAt(0)
```

0번 위치의 문자를 꺼낸다.

결과는 `'J'`이다.

```java
String message = greeting + " " + language;
```

문자열을 이어 붙인다.

중간에 공백을 넣기 위해 `" "`를 사용했다.

```java
word.substring(1, 3)
```

1번 위치부터 3번 위치 전까지 잘라낸다.

```text
J   a   v   a
    └───┘
    1  2

결과: "av"
```

```java
word.equals("Java")
```

문자열 내용이 같은지 비교한다.

Java에서 문자열 내용 비교는 `==`보다 `equals()`를 사용하는 것이 안전하다.

---

## 6. 마지막 정리

Java 문자열은 `String`으로 표현한다.

문자열은 큰따옴표로 감싼다.

문자열 인덱스는 0부터 시작한다.

`length()`는 문자열 길이를 구한다.

문자열 내용 비교에는 `equals()`를 사용한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 문자열",
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