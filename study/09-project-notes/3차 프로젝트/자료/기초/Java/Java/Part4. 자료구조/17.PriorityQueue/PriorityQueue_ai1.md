# 제목
[Java기초] PriorityQueue

# 본문

## 1. 한 줄 요약

우선순위가 높은 값이 먼저 나오는 큐이다.

Java에서 PriorityQueue을 이해하면 코딩 테스트에서 자주 나오는 데이터 처리와 코드 구조를 더 깔끔하게 작성할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

최솟값 반복 추출, 작업 우선순위 처리, 다익스트라할 때 PriorityQueue이 필요하다.

처음에는 변수와 반복문만으로도 코드를 작성할 수 있다.

하지만 데이터가 많아지거나 같은 처리가 반복되면 코드가 길어지고 실수하기 쉬워진다.

```text
문제 상황
- 같은 기능을 반복해서 사용함
- 여러 값을 순서대로 관리해야 함
- 빠르게 값을 찾거나 꺼내야 함
- 입력 데이터를 효율적으로 처리해야 함
```

PriorityQueue을 사용하면 이런 작업을 더 명확하고 안정적으로 표현할 수 있다.

---

## 3. 핵심 아이디어

PriorityQueue의 핵심은 다음과 같다.

```text
필요한 상황을 파악한다.
알맞은 Java 문법이나 클래스를 선택한다.
값을 넣고, 꺼내고, 처리하는 흐름을 이해한다.
```

작은 예제로 보면 훨씬 쉽다.

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(5);
        pq.offer(1);
```

위 코드는 PriorityQueue의 가장 기본적인 사용 형태이다.

중요한 것은 문법을 외우는 것보다 “값이 어떤 순서로 들어가고 나오는지” 이해하는 것이다.

---

## 4. 동작 과정 살펴보기

아래 흐름을 따라가 보자.

```text
Step 1. 필요한 객체 또는 기능을 준비한다.
Step 2. 값을 넣거나 메서드를 호출한다.
Step 3. Java가 정해진 규칙에 따라 값을 처리한다.
Step 4. 결과를 변수에 저장하거나 출력한다.
```

예를 들어 다음 코드가 실행된다고 하자.

```java
System.out.println(pq.poll());
```

동작 흐름은 다음과 같이 볼 수 있다.

```text
입력 또는 저장된 값
        ↓
PriorityQueue 문법/클래스가 처리
        ↓
결과값 생성
        ↓
출력 또는 다음 계산에 사용
```

---

## 5. 구현 코드 및 상세 설명

```java
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        pq.offer(5);
        pq.offer(1);

        System.out.println(pq.poll());
    }
}
```

### 코드 설명

```java
PriorityQueue<Integer> pq = new PriorityQueue<>();
```

PriorityQueue을 사용하기 위한 핵심 코드이다.

이 줄에서 필요한 값을 만들거나, 기능을 정의하거나, 자료구조를 준비한다.

```java
System.out.println(pq.poll());
```

준비한 기능이나 자료구조를 실제로 사용하는 부분이다.

코딩 테스트에서는 이 부분이 반복문, 조건문, 입력 처리와 함께 사용되는 경우가 많다.

```text
준비 → 값 처리 → 결과 확인
```

이 순서를 이해하면 같은 문법을 다른 문제에도 적용할 수 있다.

---

## 6. 마지막 정리

PriorityQueue은 Java 기초에서 자주 사용되는 중요한 주제이다.

문법만 외우기보다 값의 흐름을 이해하는 것이 중요하다.

작은 예제로 먼저 동작 과정을 확인하면 실수를 줄일 수 있다.

코딩 테스트에서는 입력 처리, 반복문, 조건문과 함께 자주 사용된다.

기본 사용법을 익힌 뒤 문제 유형에 맞게 응용하면 된다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java PriorityQueue",
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
