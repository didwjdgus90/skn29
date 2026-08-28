# 제목
[Java기초] 배열

# 본문

## 1. 한 줄 요약

배열은 동일한 자료형의 원소를 연속적인 인덱스 구조로 저장하는 고정 길이 자료구조이다.

배열을 이해하면 인덱스 기반 데이터 접근과 순차 처리를 효율적으로 구현할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

동일한 성격의 데이터를 여러 개 다룰 때 개별 변수로 관리하는 방식은 확장성이 낮다.

```java
int a = 10;
int b = 20;
int c = 30;
```

배열을 사용하면 하나의 참조 변수로 여러 값을 관리할 수 있다.

```java
int[] numbers = {10, 20, 30};
```

배열은 특히 다음 작업에 적합하다.

```text
순서가 있는 데이터 저장
인덱스 기반 접근
반복문을 통한 전체 순회
누적 합, 최댓값, 최솟값 계산
```

---

## 3. 핵심 아이디어

배열은 생성 시 길이가 결정된다.

```java
int[] arr = new int[3];
```

```text
arr

[0] [0] [0]
 0   1   2
```

각 원소는 인덱스로 접근한다.

```java
arr[0] = 10;
arr[1] = 20;
```

배열의 인덱스 범위는 0부터 `length - 1`까지이다.

```text
길이 3 배열의 유효 인덱스: 0, 1, 2
```

범위를 벗어나면 실행 중 오류가 발생한다.

---

## 4. 동작 과정 살펴보기

```java
int[] arr = new int[3];
arr[0] = 10;
arr[1] = 20;
arr[2] = 30;
```

### Step 1. 배열 생성

```text
초기 상태

[0] [0] [0]
 0   1   2
```

정수 배열은 기본값 0으로 초기화된다.

### Step 2. 값 저장

```text
arr[0] = 10

[10] [0] [0]
```

### Step 3. 나머지 값 저장

```text
[10] [20] [30]
 0    1    2
```

### Step 4. 인덱스 접근

```java
arr[1]
```

```text
1번 인덱스 값: 20
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        int[] numbers = new int[5];

        for (int i = 0; i < numbers.length; i++) {
            numbers[i] = i + 1;
        }

        int sum = 0;
        int max = numbers[0];

        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];

            if (numbers[i] > max) {
                max = numbers[i];
            }
        }

        System.out.println("합계: " + sum);
        System.out.println("최댓값: " + max);
    }
}
```

### 코드 설명

```java
int[] numbers = new int[5];
```

길이가 5인 정수 배열을 생성한다.

초기값은 모두 0이다.

```java
numbers[i] = i + 1;
```

인덱스를 이용해 각 칸에 값을 저장한다.

```java
sum += numbers[i];
```

배열의 원소를 순회하며 합계를 누적한다.

```java
if (numbers[i] > max)
```

현재 값이 기존 최댓값보다 크면 최댓값을 갱신한다.

---

## 6. 마지막 정리

배열은 동일한 자료형의 값을 저장하는 고정 길이 구조이다.

배열 인덱스는 0부터 시작한다.

유효 인덱스 범위는 0부터 `length - 1`까지이다.

배열의 길이는 생성 후 변경할 수 없다.

배열은 반복문과 결합해 순차 처리에 자주 사용된다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 배열",
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
