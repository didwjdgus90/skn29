# 제목
[Java기초] Stack

# 본문

## 1. 한 줄 요약

나중에 넣은 값이 먼저 나오는 LIFO 구조이다.

쉽게 말해 Stack은 접시를 쌓아두고 맨 위 접시부터 꺼내는 구조라고 생각하면 된다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

생활 속에서 물건을 정리하거나 일을 처리할 때 규칙이 필요하다.

```text
먼저 온 사람부터 처리하기
중복된 이름은 한 번만 적기
급한 일부터 처리하기
같은 일을 하나의 버튼으로 만들기
```

프로그래밍에서도 똑같다.

되돌리기, 괄호 검사, DFS처럼 최근 값을 먼저 처리해야 할 때 Stack을 사용하면 코드가 훨씬 이해하기 쉬워진다.

---

## 3. 핵심 아이디어

Stack은 접시를 쌓아두고 맨 위 접시부터 꺼내는 구조이다.

```text
상황 발생
   ↓
정해진 규칙에 따라 처리
   ↓
필요한 결과 얻기
```

예를 들어 Stack을 사용할 때는 다음처럼 생각할 수 있다.

```text
무엇을 넣을까?
어떤 순서로 처리될까?
무엇이 결과로 나올까?
```

문법을 통째로 외우기보다, 값이 움직이는 모습을 그려보는 것이 좋다.

---

## 4. 동작 과정 살펴보기

작은 예제로 흐름을 보자.

```java
Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
```

동작을 그림으로 표현하면 다음과 같다.

```text
값 준비
  │
  ▼
Stack에 전달
  │
  ▼
규칙에 따라 처리
  │
  ▼
결과 확인
```

실제로 사용하는 코드는 다음과 같다.

```java
System.out.println(stack.pop());
```

처음에는 코드가 낯설 수 있지만, 핵심은 간단하다.

```text
넣는다 → 처리한다 → 꺼낸다
```

---

## 5. 구현 코드 및 상세 설명

```java
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);

        System.out.println(stack.pop());
    }
}
```

### 코드 설명

```java
Stack<Integer> stack = new Stack<>();
```

Stack을 사용하기 위한 준비 단계이다.

생활 비유로 보면 도구를 꺼내거나 상자를 준비하는 과정이다.

```java
System.out.println(stack.pop());
```

준비한 도구를 실제로 사용하는 부분이다.

결과를 출력하거나 다음 계산에 넘길 수 있다.

```text
도구 준비 완료
   ↓
값 넣기
   ↓
결과 꺼내기
```

---

## 6. 마지막 정리

Stack은 접시를 쌓아두고 맨 위 접시부터 꺼내는 구조처럼 이해하면 쉽다.

처음에는 작은 예제부터 따라 해보는 것이 좋다.

값이 들어가고 나오는 순서를 그림처럼 생각하면 이해가 빠르다.

코딩 테스트에서는 자주 쓰이는 기본 도구이다.

문법보다 “왜 쓰는지”와 “어떻게 동작하는지”를 먼저 기억하자.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java Stack",
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
