# 제목
[Java기초] 자료형

# 본문

## 1. 한 줄 요약

자료형은 값이 들어갈 상자의 종류를 정하는 규칙이다.

Java에서는 상자에 어떤 값을 넣을지 미리 정해야 하므로 자료형을 꼭 알아야 한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

옷장에 옷을 정리한다고 생각해 보자.

양말은 양말 칸에, 외투는 외투 칸에 넣는다.

```text
양말 칸  → 양말
외투 칸  → 외투
모자 칸  → 모자
```

프로그래밍에서도 값마다 알맞은 칸이 있다.

```text
20        → 숫자 칸
175.5     → 소수 칸
'A'       → 문자 한 개 칸
"민수"    → 문자열 칸
true      → 참/거짓 칸
```

Java는 이 칸의 종류를 먼저 정한 뒤 값을 넣는다.

```java
int age = 20;
```

`int`라는 정수 칸에 20을 넣는다는 뜻이다.

---

## 3. 핵심 아이디어

자료형은 값 전용 상자이다.

```text
int 상자
┌────┐
│ 20 │
└────┘
```

정수 상자에는 정수를 넣는다.

```java
int score = 90;
```

소수 상자에는 소수점이 있는 값을 넣는다.

```java
double temperature = 36.5;
```

문자 한 개 상자에는 글자 하나만 넣는다.

```java
char firstLetter = 'A';
```

글자 여러 개는 문자열 상자에 넣는다.

```java
String message = "Hello";
```

참과 거짓은 boolean 상자에 넣는다.

```java
boolean isOpen = true;
```

---

## 4. 동작 과정 살펴보기

```java
int count = 3;
String menu = "김밥";
boolean isSoldOut = false;
```

### Step 1. 정수 상자 만들기

```text
count 상자

[3]
```

`count`는 개수를 담으므로 정수형 `int`가 적합하다.

### Step 2. 문자열 상자 만들기

```text
menu 상자

["김밥"]
```

메뉴 이름은 글자 여러 개이므로 `String`을 사용한다.

### Step 3. 참거짓 상자 만들기

```text
isSoldOut 상자

[false]
```

품절 여부는 참 또는 거짓으로 표현할 수 있다.

그래서 `boolean`을 사용한다.

### Step 4. 자료형이 맞아야 한다

```java
int count = "세 개";
```

```text
int 상자에는 숫자를 넣어야 함
문자열은 들어갈 수 없음
```

Java는 자료형이 맞지 않으면 컴파일 단계에서 오류를 알려준다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        String menu = "라면";
        int price = 4500;
        double rating = 4.5;
        char size = 'M';
        boolean isAvailable = true;

        System.out.println("메뉴: " + menu);
        System.out.println("가격: " + price);
        System.out.println("평점: " + rating);
        System.out.println("크기: " + size);
        System.out.println("판매 여부: " + isAvailable);
    }
}
```

### 코드 설명

```java
String menu = "라면";
```

메뉴 이름은 글자 여러 개이므로 `String`에 담는다.

```java
int price = 4500;
```

가격은 소수점이 없는 숫자이므로 `int`가 적합하다.

```java
double rating = 4.5;
```

평점은 소수점이 있으므로 `double`을 사용한다.

```java
char size = 'M';
```

크기 표시가 문자 하나이므로 `char`를 사용한다.

```java
boolean isAvailable = true;
```

판매 가능 여부는 참 또는 거짓으로 나타낼 수 있으므로 `boolean`을 사용한다.

---

## 6. 마지막 정리

자료형은 값을 담는 상자의 종류이다.

Java에서는 변수 이름 앞에 자료형을 적는다.

정수는 `int`, 실수는 `double`, 참거짓은 `boolean`을 자주 사용한다.

문자 한 개는 `char`, 글자 여러 개는 `String`을 사용한다.

자료형을 맞게 사용하면 Java가 실수를 미리 잡아준다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 자료형",
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