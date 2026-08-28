# 제목
[Java기초] 입출력

# 본문

## 1. 한 줄 요약

입출력은 프로그램이 사용자와 말을 주고받는 방법이다.

Java에서 입력은 값을 듣는 과정이고, 출력은 결과를 말해주는 과정이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

계산기가 숫자를 입력받지 못하면 쓸 수 없다.

```text
사용자: 3과 5를 더해줘
계산기: 8
```

프로그램도 마찬가지다.

값을 입력받고, 계산하고, 결과를 출력해야 한다.

```java
int a = sc.nextInt();
int b = sc.nextInt();
System.out.println(a + b);
```

입출력은 프로그램이 바깥세상과 소통하는 문이다.

---

## 3. 핵심 아이디어

`Scanner`는 귀 역할을 한다.

```text
사용자가 말함
   │
   ▼
Scanner가 들음
```

`System.out.println()`은 입 역할을 한다.

```text
프로그램 결과
   │
   ▼
화면에 말하기
```

```java
Scanner sc = new Scanner(System.in);
```

이 코드는 입력을 들을 준비를 하는 것이다.

```java
System.out.println("안녕");
```

이 코드는 화면에 `"안녕"`이라고 말하는 것이다.

---

## 4. 동작 과정 살펴보기

```java
Scanner sc = new Scanner(System.in);

String name = sc.next();
System.out.println("안녕하세요, " + name + "님");
```

### Step 1. 입력 준비

```text
Scanner 준비 완료
```

### Step 2. 이름 듣기

```text
입력: 민수

name ─────▶ "민수"
```

### Step 3. 문장 만들기

```text
"안녕하세요, " + "민수" + "님"
```

### Step 4. 출력하기

```text
안녕하세요, 민수님
```

---

## 5. 구현 코드 및 상세 설명

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String name = sc.next();
        int age = sc.nextInt();

        System.out.println("이름: " + name);
        System.out.println("나이: " + age);
        System.out.println(name + "님은 내년에 " + (age + 1) + "살입니다.");

        sc.close();
    }
}
```

### 코드 설명

```java
String name = sc.next();
```

공백 전까지의 문자열을 입력받는다.

예를 들어 `민수`를 입력하면 `name`에 저장된다.

```java
int age = sc.nextInt();
```

정수 하나를 입력받는다.

```java
System.out.println(...)
```

화면에 결과를 출력한다.

```java
(age + 1)
```

나이에 1을 더해 내년 나이를 계산한다.

---

## 6. 마지막 정리

입력은 프로그램이 값을 듣는 과정이다.

출력은 프로그램이 결과를 말하는 과정이다.

`Scanner`는 입력을 받을 때 사용한다.

`System.out.println()`은 출력할 때 사용한다.

`nextInt()`는 정수, `next()`는 문자열 한 단어를 입력받는다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 입출력",
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
