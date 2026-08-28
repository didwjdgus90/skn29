# 제목
[Java기초] Deque

# 본문

## 1. 한 줄 요약

앞과 뒤 양쪽에서 값을 넣고 뺄 수 있는 자료구조이다.

Java에서 Deque은 코드의 구조화, 자료 처리, 성능 개선, 입력 파싱 등 실전 문제 해결에 중요한 역할을 한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

양방향 큐, 슬라이딩 윈도우, 앞뒤 처리가 모두 필요한 문제하는 상황에서 Deque을 사용할 수 있다.

단순 구현으로도 해결 가능한 경우가 있지만, 입력 크기와 코드 복잡도가 증가하면 더 체계적인 접근이 필요하다.

```text
분석 관점
- 데이터 접근 방식
- 삽입과 삭제의 위치
- 중복 허용 여부
- 정렬 또는 우선순위 기준
- 시간 복잡도
```

Deque은 이러한 요구 조건에 맞는 Java의 핵심 도구이다.

---

## 3. 핵심 아이디어

Deque을 사용할 때는 기능보다 먼저 처리 모델을 이해해야 한다.

```text
입력 데이터
   ↓
Deque의 규칙 또는 인터페이스
   ↓
처리 결과
```

기본 사용 예시는 다음과 같다.

```java
Deque<Integer> deque = new ArrayDeque<>();
        deque.offerFirst(1);
        deque.offerLast(2);
```

이 문법은 단순한 암기 대상이 아니라, 특정 문제 패턴에 대응하는 도구로 이해해야 한다.

관련 핵심 키워드는 다음과 같다.

```text
deque, double ended queue, arraydeque
```

---

## 4. 동작 과정 살펴보기

Deque의 처리 흐름은 다음처럼 분석할 수 있다.

```text
1. 자료 또는 기능을 초기화한다.
2. 입력값을 구조에 맞게 저장하거나 전달한다.
3. 필요한 연산을 수행한다.
4. 결과를 반환하거나 출력한다.
```

예제 코드의 사용 부분은 다음과 같다.

```java
System.out.println(deque.pollFirst());
```

이 코드는 내부적으로 Deque의 규칙에 따라 값을 처리한다.

문제 풀이에서는 이 규칙이 시간 복잡도와 코드 안정성에 영향을 준다.

---

## 5. 구현 코드 및 상세 설명

```java
import java.util.Deque;
import java.util.ArrayDeque;

public class Main {
    public static void main(String[] args) {
        Deque<Integer> deque = new ArrayDeque<>();
        deque.offerFirst(1);
        deque.offerLast(2);

        System.out.println(deque.pollFirst());
    }
}
```

### 코드 설명

```java
Deque<Integer> deque = new ArrayDeque<>();
```

Deque을 사용하기 위한 선언 또는 초기화 부분이다.

Java에서는 타입과 제네릭, 반환값, 예외 처리 여부 등을 함께 고려해야 한다.

```java
System.out.println(deque.pollFirst());
```

실제 연산을 수행하는 부분이다.

문제 해결 관점에서는 이 연산이 얼마나 자주 호출되는지, 각 호출 비용이 어느 정도인지 확인해야 한다.

```text
사용 빈도 × 연산 비용 = 전체 성능에 영향
```

---

## 6. 마지막 정리

Deque은 Java 문제 풀이에서 자주 등장하는 핵심 주제이다.

사용법뿐 아니라 내부 규칙과 시간 복잡도를 함께 이해해야 한다.

입력 크기가 커질수록 적절한 자료구조와 도구 선택이 중요하다.

코드의 가독성과 안정성을 높이려면 문제 요구 조건에 맞게 사용해야 한다.

전문적으로 접근하려면 선언 방식, 주요 메서드, 처리 비용을 함께 정리해야 한다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java Deque",
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
