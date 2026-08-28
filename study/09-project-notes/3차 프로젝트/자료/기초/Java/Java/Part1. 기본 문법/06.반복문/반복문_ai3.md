# 제목
[Java기초] 반복문

# 본문

## 1. 한 줄 요약

반복문은 조건식이 참인 동안 특정 블록을 반복 실행하는 Java의 제어 구조이다.

반복문을 이해하면 순차 데이터 처리와 누적 계산을 체계적으로 구현할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

반복문은 동일한 로직을 여러 데이터에 적용해야 할 때 사용된다.

대표적인 예시는 다음과 같다.

```text
배열 전체 순회
합계 누적
최댓값 탐색
입력 N개 처리
조건 만족 시까지 반복
```

반복문이 없으면 데이터 개수만큼 코드를 직접 작성해야 하며, 이는 유지보수성과 확장성을 떨어뜨린다.

---

## 3. 핵심 아이디어

Java의 반복문은 주로 `for`, `while`, 향상된 `for`문으로 나눌 수 있다.

```text
for         → 인덱스 기반 반복
while       → 조건 기반 반복
enhanced for → 배열이나 컬렉션의 값 순회
```

`for`문은 초기식, 조건식, 증감식으로 구성된다.

```java
for (int i = 0; i < n; i++) {
    ...
}
```

`while`문은 조건식이 참인 동안 반복한다.

```java
while (condition) {
    ...
}
```

반복문의 핵심은 종료 조건을 명확히 설계하는 것이다.

---

## 4. 동작 과정 살펴보기

```java
int sum = 0;

for (int i = 1; i <= 3; i++) {
    sum += i;
}
```

### Step 1. 초기 상태

```text
sum = 0
i = 1
```

### Step 2. 1회차

```text
i <= 3 → true
sum = sum + i = 0 + 1 = 1
```

### Step 3. 2회차

```text
i = 2
sum = 1 + 2 = 3
```

### Step 4. 3회차

```text
i = 3
sum = 3 + 3 = 6
```

### Step 5. 종료

```text
i = 4
4 <= 3 → false
반복 종료
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int[] numbers = {3, 5, 2, 8};

        int sum = 0;
        int max = numbers[0];

        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];

            if (numbers[i] > max) {
                max = numbers[i];
            }
        }

        for (int number : numbers) {
            System.out.println(number);
        }

        System.out.println("합계: " + sum);
        System.out.println("최댓값: " + max);
    }
}
```

### 코드 설명

```java
for (int i = 0; i < numbers.length; i++)
```

배열의 모든 인덱스를 0부터 마지막까지 순회한다.

```java
sum += numbers[i];
```

현재 원소를 누적 합계에 더한다.

```java
if (numbers[i] > max)
```

현재 원소가 기존 최댓값보다 크면 최댓값을 갱신한다.

```java
for (int number : numbers)
```

향상된 `for`문이다.

인덱스가 필요 없고 값만 순회할 때 적합하다.

---

## 6. 마지막 정리

반복문은 반복 실행을 표현하는 제어 구조이다.

`for`문은 인덱스 제어에 적합하다.

`while`문은 조건 중심 반복에 적합하다.

향상된 `for`문은 배열이나 컬렉션의 값 순회에 적합하다.

종료 조건이 잘못되면 무한 반복이 발생할 수 있다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 반복문",
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
