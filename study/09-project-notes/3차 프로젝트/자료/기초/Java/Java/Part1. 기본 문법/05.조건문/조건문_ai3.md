# 제목
[Java기초] 조건문

# 본문

## 1. 한 줄 요약

조건문은 `boolean` 표현식의 평가 결과에 따라 실행 경로를 분기하는 제어문이다.

조건문을 이해하면 프로그램의 제어 흐름을 논리적으로 설계할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 입력값이나 상태에 따라 다른 처리 경로를 가져야 한다.

예를 들어 점수에 따른 등급 분류, 권한 검사, 입력값 유효성 검사는 모두 조건 분기 문제이다.

```java
if (score >= 60) {
    pass = true;
} else {
    pass = false;
}
```

조건문은 단일 흐름으로는 표현하기 어려운 선택 구조를 제공한다.

---

## 3. 핵심 아이디어

Java의 조건문은 조건식이 `boolean`이어야 한다.

```java
if (score >= 60)
```

`score >= 60`은 비교 연산이며 결과는 `true` 또는 `false`이다.

다중 조건은 `else if`로 구성할 수 있다.

```text
if       → 첫 번째 조건
else if  → 이전 조건이 거짓일 때 추가 검사
else     → 모든 조건이 거짓일 때 기본 처리
```

조건은 위에서 아래로 평가된다.

처음 참이 되는 블록 하나만 실행된다.

---

## 4. 동작 과정 살펴보기

```java
int score = 82;
String grade;

if (score >= 90) {
    grade = "A";
} else if (score >= 80) {
    grade = "B";
} else {
    grade = "C";
}
```

### Step 1. 조건 1 평가

```text
82 >= 90 → false
```

### Step 2. 조건 2 평가

```text
82 >= 80 → true
```

### Step 3. 값 대입

```text
grade = "B"
```

### Step 4. 나머지 분기 생략

```text
else 블록은 평가 대상이 아님
```

조건문은 순서가 중요하다.

넓은 조건을 먼저 쓰면 좁은 조건이 실행되지 않을 수 있다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int score = 82;
        String grade;

        if (score < 0 || score > 100) {
            grade = "잘못된 점수";
        } else if (score >= 90) {
            grade = "A";
        } else if (score >= 80) {
            grade = "B";
        } else if (score >= 70) {
            grade = "C";
        } else {
            grade = "D";
        }

        System.out.println("등급: " + grade);
    }
}
```

### 코드 설명

```java
score < 0 || score > 100
```

점수 범위가 잘못되었는지 먼저 검사한다.

유효성 검사를 앞에 두면 이후 조건을 더 안전하게 처리할 수 있다.

```java
else if (score >= 90)
```

90점 이상을 A로 분류한다.

```java
else if (score >= 80)
```

이 조건에 도달했다는 것은 이미 90점 미만이라는 뜻이다.

따라서 80 이상 90 미만이 B가 된다.

---

## 6. 마지막 정리

조건문은 `boolean` 조건식에 따라 실행 경로를 선택한다.

`else if` 체인은 위에서 아래로 순차 평가된다.

처음 참인 블록 하나만 실행된다.

조건의 순서는 결과에 직접 영향을 준다.

유효성 검사는 일반적으로 주요 분기보다 먼저 처리하는 것이 안전하다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 조건문",
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
