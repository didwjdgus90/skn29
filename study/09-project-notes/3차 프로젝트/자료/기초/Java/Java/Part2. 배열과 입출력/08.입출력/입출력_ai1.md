# 제목
[Java기초] 입출력

# 본문

## 1. 한 줄 요약

입출력은 프로그램이 외부에서 값을 입력받고 처리 결과를 화면에 출력하는 방법이다.

Java 입출력을 이해하면 사용자 입력이나 코딩 테스트 입력 데이터를 받아 원하는 결과를 출력할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 고정된 값만 처리하지 않는다.

사용자가 입력한 값이나 문제에서 주어진 값을 받아 처리해야 한다.

```text
입력
3 5

출력
8
```

Java에서는 간단한 입력에 `Scanner`를 사용할 수 있다.

```java
Scanner sc = new Scanner(System.in);
int a = sc.nextInt();
```

출력은 `System.out.println()`을 사용한다.

---

## 3. 핵심 아이디어

입출력은 대화와 비슷하다.

```text
사용자 → 프로그램: 값 전달
프로그램 → 사용자: 결과 출력
```

`Scanner`는 입력을 읽는 도구이다.

```java
Scanner sc = new Scanner(System.in);
```

자주 쓰는 입력 메서드는 다음과 같다.

```text
nextInt()     정수 입력
nextDouble()  실수 입력
next()        공백 전까지 문자열 입력
nextLine()    한 줄 전체 입력
```

---

## 4. 동작 과정 살펴보기

```java
Scanner sc = new Scanner(System.in);

int a = sc.nextInt();
int b = sc.nextInt();

System.out.println(a + b);
```

### Step 1. 입력 도구 준비

```text
Scanner 준비
```

### Step 2. 첫 번째 정수 읽기

```text
입력: 3 5
a = 3
```

### Step 3. 두 번째 정수 읽기

```text
b = 5
```

### Step 4. 결과 출력

```text
a + b = 8

출력: 8
```

---

## 5. 구현 코드 및 상세 설명

```java
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();

        int sum = a + b;

        System.out.println(sum);

        sc.close();
    }
}
```

### 코드 설명

```java
import java.util.Scanner;
```

`Scanner`를 사용하기 위해 불러온다.

```java
Scanner sc = new Scanner(System.in);
```

키보드 입력을 읽는 Scanner 객체를 만든다.

```java
int a = sc.nextInt();
```

정수 하나를 입력받는다.

```java
System.out.println(sum);
```

계산 결과를 한 줄로 출력한다.

```java
sc.close();
```

입력 도구 사용을 마무리한다.

---

## 6. 마지막 정리

Java에서 간단한 입력은 `Scanner`를 사용할 수 있다.

정수 입력은 `nextInt()`를 사용한다.

문자열 한 단어 입력은 `next()`를 사용한다.

출력은 `System.out.println()`을 사용한다.

코딩 테스트에서는 입력량이 많을 때 `BufferedReader`도 자주 사용한다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 입출력",
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
