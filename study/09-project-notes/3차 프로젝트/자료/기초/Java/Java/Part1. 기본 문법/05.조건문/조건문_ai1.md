# 제목
[Java기초] 조건문

# 본문

## 1. 한 줄 요약

조건문은 조건의 참과 거짓에 따라 실행할 코드를 선택하는 문법이다.

Java 조건문을 이해하면 점수, 나이, 로그인 여부처럼 상황에 따라 다른 동작을 만들 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 항상 같은 동작만 하지 않는다.

```text
점수가 60점 이상이면 합격
아니면 불합격

나이가 20세 이상이면 성인
아니면 미성년자
```

이런 판단을 코드로 표현할 때 조건문을 사용한다.

```java
if (score >= 60) {
    System.out.println("합격");
} else {
    System.out.println("불합격");
}
```

조건문은 프로그램에게 선택 능력을 주는 문법이다.

---

## 3. 핵심 아이디어

조건문은 조건식의 결과를 확인한다.

조건식의 결과는 항상 `true` 또는 `false`이다.

```text
score >= 60
75 >= 60 → true
```

`if`는 조건이 참일 때 실행된다.

`else`는 조건이 거짓일 때 실행된다.

여러 조건을 순서대로 검사하려면 `else if`를 사용한다.

---

## 4. 동작 과정 살펴보기

```java
int score = 85;

if (score >= 90) {
    System.out.println("A");
} else if (score >= 80) {
    System.out.println("B");
} else {
    System.out.println("C");
}
```

### Step 1. 첫 번째 조건 검사

```text
85 >= 90 → false
```

첫 조건은 거짓이므로 다음 조건으로 넘어간다.

### Step 2. 두 번째 조건 검사

```text
85 >= 80 → true
```

조건이 참이므로 `B`를 출력한다.

### Step 3. 나머지는 건너뜀

```text
실행된 블록: else if
else 블록: 실행 안 됨
```

조건문은 위에서 아래로 검사하고 처음 참인 블록만 실행한다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int score = 75;

        if (score >= 90) {
            System.out.println("A 등급");
        } else if (score >= 80) {
            System.out.println("B 등급");
        } else if (score >= 70) {
            System.out.println("C 등급");
        } else {
            System.out.println("재시험");
        }
    }
}
```

### 코드 설명

```java
if (score >= 90)
```

가장 먼저 90점 이상인지 검사한다.

```java
else if (score >= 80)
```

앞 조건이 거짓일 때만 검사된다.

```java
else
```

모든 조건이 거짓일 때 실행된다.

조건식 없이 마지막 선택지를 담당한다.

---

## 6. 마지막 정리

조건문은 상황에 따라 실행할 코드를 선택한다.

`if`는 첫 조건을 검사한다.

`else if`는 추가 조건을 검사한다.

`else`는 모든 조건이 거짓일 때 실행된다.

Java에서는 조건문 블록을 중괄호 `{}`로 감싼다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 조건문",
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
