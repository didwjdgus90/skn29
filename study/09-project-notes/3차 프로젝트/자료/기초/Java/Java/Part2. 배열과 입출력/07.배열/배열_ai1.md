# 제목
[Java기초] 배열

# 본문

## 1. 한 줄 요약

배열은 같은 자료형의 여러 값을 하나의 이름으로 묶어 저장하는 자료구조이다.

Java 배열을 이해하면 여러 개의 점수, 숫자, 이름을 순서대로 관리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

학생 5명의 점수를 저장한다고 해보자.

변수를 따로 만들면 다음처럼 된다.

```java
int score1 = 80;
int score2 = 90;
int score3 = 70;
```

학생이 많아질수록 변수도 계속 늘어난다.

배열을 사용하면 여러 값을 하나로 묶을 수 있다.

```java
int[] scores = {80, 90, 70};
```

배열은 같은 종류의 값을 순서대로 저장할 때 사용한다.

---

## 3. 핵심 아이디어

배열은 번호가 붙은 보관함이다.

```text
scores

인덱스:  0   1   2
값:     80  90  70
```

Java 배열의 인덱스는 0부터 시작한다.

```java
scores[0] // 80
scores[1] // 90
```

배열의 길이는 `length`로 확인한다.

```java
scores.length
```

---

## 4. 동작 과정 살펴보기

```java
int[] scores = {80, 90, 70};
```

### Step 1. 배열 생성

```text
scores

[80] [90] [70]
 0    1    2
```

### Step 2. 값 꺼내기

```java
scores[0]
```

```text
0번 칸 → 80
```

### Step 3. 값 수정하기

```java
scores[2] = 100;
```

```text
수정 전: [80] [90] [70]
수정 후: [80] [90] [100]
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int[] scores = {80, 90, 70};

        System.out.println(scores[0]);

        scores[2] = 100;

        int total = 0;

        for (int i = 0; i < scores.length; i++) {
            total += scores[i];
        }

        double average = (double) total / scores.length;

        System.out.println("총점: " + total);
        System.out.println("평균: " + average);
    }
}
```

### 코드 설명

```java
int[] scores = {80, 90, 70};
```

정수 여러 개를 담는 배열을 만든다.

```java
scores[0]
```

0번 인덱스의 값을 꺼낸다.

```java
scores[2] = 100;
```

2번 인덱스의 값을 100으로 수정한다.

```java
scores.length
```

배열의 길이를 의미한다.

반복문과 함께 배열 전체를 순회할 때 자주 사용한다.

---

## 6. 마지막 정리

배열은 같은 자료형의 값을 여러 개 저장한다.

배열 인덱스는 0부터 시작한다.

배열 길이는 `length`로 확인한다.

배열 값은 인덱스를 통해 읽고 수정한다.

배열은 반복문과 함께 사용할 때 가장 유용하다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 배열",
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
