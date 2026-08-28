# 제목
[Java기초] 입출력

# 본문

## 1. 한 줄 요약

Java 입출력은 표준 입력 스트림에서 데이터를 읽고 표준 출력 스트림으로 결과를 내보내는 과정이다.

입출력을 이해하면 코딩 테스트와 콘솔 프로그램에서 데이터 흐름을 정확히 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

알고리즘 문제는 대부분 입력 데이터를 기반으로 결과를 계산한다.

```text
입력 → 파싱 → 처리 → 출력
```

Java에서는 간단한 입력에 `Scanner`를 사용할 수 있다.

하지만 입력량이 많은 문제에서는 `BufferedReader`와 `StringTokenizer`를 사용하는 것이 더 효율적이다.

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```

입출력 방식 선택은 실행 시간에 영향을 줄 수 있다.

---

## 3. 핵심 아이디어

Java의 표준 입력은 `System.in`, 표준 출력은 `System.out`이다.

```text
System.in   → 입력
System.out  → 출력
```

`Scanner`는 사용하기 쉽지만 상대적으로 느릴 수 있다.

`BufferedReader`는 한 줄 단위로 빠르게 읽는다.

공백 기준으로 문자열을 나누려면 `StringTokenizer`를 자주 사용한다.

```text
"3 5"
  │
  ▼
StringTokenizer
  │
  ├─ "3"
  └─ "5"
```

---

## 4. 동작 과정 살펴보기

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
String line = br.readLine();
StringTokenizer st = new StringTokenizer(line);

int a = Integer.parseInt(st.nextToken());
int b = Integer.parseInt(st.nextToken());
```

### Step 1. 한 줄 읽기

```text
입력: 3 5

line = "3 5"
```

### Step 2. 공백 기준 분리

```text
"3 5" → "3", "5"
```

### Step 3. 문자열을 정수로 변환

```text
"3" → 3
"5" → 5
```

### Step 4. 계산과 출력

```text
3 + 5 = 8
```

---

## 5. 구현 코드 및 상세 설명

```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        System.out.println(a + b);
    }
}
```

### 코드 설명

```java
BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
```

표준 입력을 빠르게 읽기 위한 객체를 생성한다.

```java
br.readLine()
```

입력 한 줄을 문자열로 읽는다.

```java
StringTokenizer st = new StringTokenizer(...)
```

문자열을 공백 기준으로 나누기 위한 도구이다.

```java
Integer.parseInt(st.nextToken())
```

다음 토큰을 꺼내 정수로 변환한다.

`readLine()`의 결과는 문자열이므로 숫자 계산을 위해 변환이 필요하다.

---

## 6. 마지막 정리

Java 표준 입력은 `System.in`, 표준 출력은 `System.out`이다.

`Scanner`는 간단하고 사용하기 쉽다.

`BufferedReader`는 많은 입력을 빠르게 처리하는 데 적합하다.

`StringTokenizer`는 공백 기준 분리에 자주 사용된다.

문자열 숫자는 `Integer.parseInt()`로 정수 변환해야 한다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 입출력",
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
