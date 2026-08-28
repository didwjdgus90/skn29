# 제목
[Java기초] 변수와 상수

# 본문

## 1. 한 줄 요약

변수는 특정 자료형의 값을 저장하기 위해 선언된 식별자이며, 상수는 `final`로 선언되어 재할당이 금지된 값이다.

변수와 상수는 Java 프로그램에서 데이터의 의미와 변경 가능성을 명확히 표현하는 기본 단위이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 데이터를 저장하고, 변경하고, 계산하는 방식으로 동작한다.

값을 직접 코드에 쓰는 방식은 단순하지만 유지보수성이 낮다.

```java
System.out.println(100 * 60 * 60);
```

이 식에서 각 숫자가 무엇을 의미하는지 명확하지 않다.

변수와 상수를 사용하면 값의 의미를 코드에 드러낼 수 있다.

```java
final int SECONDS_PER_MINUTE = 60;
final int MINUTES_PER_HOUR = 60;
int hours = 100;
```

상수는 변경되지 않는 기준값을 명확히 표현한다.

변수는 실행 흐름에서 변할 수 있는 상태를 표현한다.

---

## 3. 핵심 아이디어

Java의 변수 선언은 세 요소로 구성된다.

```text
자료형 변수명 = 초기값;
```

예시는 다음과 같다.

```java
int count = 10;
```

```text
int    → 저장 가능한 값의 종류
count  → 값에 접근하기 위한 이름
10     → 초기 저장 값
```

Java는 정적 타입 언어이다.

즉, 변수는 선언 시점에 자료형이 정해지고, 해당 자료형에 맞는 값만 저장할 수 있다.

```java
int age = 20;
age = "스무살"; // 불가능
```

상수는 `final` 키워드를 통해 재할당을 제한한다.

```java
final int MAX_SIZE = 100;
```

---

## 4. 동작 과정 살펴보기

```java
int count = 3;
count = count + 2;
```

### Step 1. 변수 선언

```text
count: int
value: 3
```

`count`라는 이름은 정수형 값을 저장할 수 있는 공간을 가리킨다.

### Step 2. 표현식 평가

```text
count + 2

현재 count 값: 3
3 + 2 = 5
```

대입 연산자 오른쪽의 표현식이 먼저 평가된다.

### Step 3. 재할당

```text
count: 3 → 5
```

계산된 결과가 다시 `count`에 저장된다.

### Step 4. 상수의 경우

```java
final int LIMIT = 10;
```

```text
LIMIT: int
value: 10
reassign: not allowed
```

`final` 변수는 초기화 이후 다른 값을 대입할 수 없다.

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        final int SECONDS_PER_MINUTE = 60;
        final int MINUTES_PER_HOUR = 60;

        int hours = 2;

        int totalMinutes = hours * MINUTES_PER_HOUR;
        int totalSeconds = totalMinutes * SECONDS_PER_MINUTE;

        System.out.println("시간: " + hours);
        System.out.println("분: " + totalMinutes);
        System.out.println("초: " + totalSeconds);
    }
}
```

### 코드 설명

```java
final int SECONDS_PER_MINUTE = 60;
```

1분이 60초라는 기준값을 상수로 선언한다.

프로그램 중간에 바뀌면 안 되는 값이므로 `final`이 적합하다.

```java
int hours = 2;
```

계산 대상이 되는 시간 값을 변수로 저장한다.

이 값은 상황에 따라 달라질 수 있으므로 일반 변수로 둔다.

```java
int totalMinutes = hours * MINUTES_PER_HOUR;
```

시간을 분으로 변환한다.

```text
2 × 60 = 120
```

```java
int totalSeconds = totalMinutes * SECONDS_PER_MINUTE;
```

분을 초로 변환한다.

```text
120 × 60 = 7200
```

---

## 6. 마지막 정리

Java 변수는 자료형과 함께 선언된다.

정적 타입 특성 때문에 변수에는 선언된 자료형에 맞는 값만 저장할 수 있다.

`final`은 변수의 재할당을 금지해 상수처럼 사용하게 한다.

상수는 보통 대문자와 밑줄로 이름을 작성한다.

변수와 상수를 구분하면 데이터의 의미와 변경 가능성이 명확해진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 변수와 상수",
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