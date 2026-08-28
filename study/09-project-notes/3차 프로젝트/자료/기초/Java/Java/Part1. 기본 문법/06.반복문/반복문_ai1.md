# 제목
[Java기초] 반복문

# 본문

## 1. 한 줄 요약

반복문은 같은 코드를 여러 번 실행하기 위한 제어문이다.

Java의 반복문을 이해하면 배열 출력, 누적 합 계산, 일정 횟수 반복 같은 작업을 효율적으로 처리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

학생 점수 5개를 출력한다고 해보자.

```java
System.out.println(scores[0]);
System.out.println(scores[1]);
System.out.println(scores[2]);
System.out.println(scores[3]);
System.out.println(scores[4]);
```

학생이 100명이라면 같은 코드를 100줄 작성해야 한다.

반복문을 사용하면 같은 구조의 작업을 짧게 표현할 수 있다.

```java
for (int i = 0; i < scores.length; i++) {
    System.out.println(scores[i]);
}
```

---

## 3. 핵심 아이디어

반복문은 정해진 조건이 만족되는 동안 코드를 반복한다.

Java에서 자주 사용하는 반복문은 `for`와 `while`이다.

```text
for    → 반복 횟수가 비교적 명확할 때
while  → 조건이 참인 동안 반복할 때
```

`for`문의 기본 구조는 다음과 같다.

```java
for (초기식; 조건식; 증감식) {
    반복할 코드
}
```

```text
초기식 → 조건 확인 → 코드 실행 → 증감식 → 조건 확인 → ...
```

---

## 4. 동작 과정 살펴보기

```java
for (int i = 1; i <= 3; i++) {
    System.out.println(i);
}
```

### Step 1. 초기식 실행

```text
i = 1
```

### Step 2. 조건 확인

```text
i <= 3
1 <= 3 → true
```

### Step 3. 코드 실행

```text
출력: 1
```

### Step 4. 증감식 실행

```text
i++ → i = 2
```

이 과정을 조건이 거짓이 될 때까지 반복한다.

```text
출력 결과

1
2
3
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int[] scores = {80, 90, 70, 100};

        int total = 0;

        for (int i = 0; i < scores.length; i++) {
            total += scores[i];
        }

        double average = (double) total / scores.length;

        System.out.println("총점: " + total);
        System.out.println("평균: " + average);

        int count = 1;

        while (count <= 3) {
            System.out.println("count: " + count);
            count++;
        }
    }
}
```

### 코드 설명

```java
for (int i = 0; i < scores.length; i++)
```

`i`를 0부터 시작해 배열 길이보다 작을 때까지 반복한다.

배열 인덱스가 0부터 시작하기 때문이다.

```java
total += scores[i];
```

현재 점수를 합계에 더한다.

```java
while (count <= 3)
```

`count`가 3 이하인 동안 반복한다.

```java
count++;
```

반복이 끝날 수 있도록 값을 증가시킨다.

---

## 6. 마지막 정리

반복문은 같은 작업을 여러 번 실행할 때 사용한다.

`for`문은 반복 횟수가 명확할 때 적합하다.

`while`문은 조건 중심 반복에 적합하다.

배열은 반복문과 함께 자주 사용된다.

`while`문에서는 조건을 변화시키지 않으면 무한 반복이 발생할 수 있다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 반복문",
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
