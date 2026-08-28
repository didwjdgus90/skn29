# 제목
[Java기초] 배열

# 본문

## 1. 한 줄 요약

배열은 같은 종류의 물건을 번호가 붙은 칸에 차례대로 넣어두는 보관함이다.

Java 배열을 배우면 여러 값을 하나의 이름으로 깔끔하게 관리할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

사물함에 학생들의 점수를 넣는다고 생각해 보자.

```text
0번 칸: 80점
1번 칸: 90점
2번 칸: 70점
```

각 점수를 따로 들고 다니는 것보다 하나의 사물함에 넣어두면 관리하기 쉽다.

Java 배열도 이와 같다.

```java
int[] scores = {80, 90, 70};
```

`scores`라는 이름 하나로 점수 여러 개를 관리한다.

---

## 3. 핵심 아이디어

배열은 번호가 붙은 기차 칸과 비슷하다.

```text
scores

[80] [90] [70]
 0    1    2
```

첫 번째 칸 번호는 1이 아니라 0이다.

```text
0번 칸 → 첫 번째 값
1번 칸 → 두 번째 값
2번 칸 → 세 번째 값
```

원하는 칸 번호를 말하면 그 값을 꺼낼 수 있다.

```java
scores[1]
```

결과는 90이다.

---

## 4. 동작 과정 살펴보기

```java
String[] fruits = {"사과", "바나나", "포도"};
```

### Step 1. 과일 보관함 생성

```text
fruits

[사과] [바나나] [포도]
  0      1      2
```

### Step 2. 1번 칸 확인

```java
fruits[1]
```

```text
1번 칸: 바나나
```

### Step 3. 값 바꾸기

```java
fruits[2] = "딸기";
```

```text
수정 전
[사과] [바나나] [포도]

수정 후
[사과] [바나나] [딸기]
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        String[] fruits = {"사과", "바나나", "포도"};

        System.out.println(fruits[0]);
        System.out.println(fruits[1]);

        fruits[2] = "딸기";

        for (int i = 0; i < fruits.length; i++) {
            System.out.println(i + "번 과일: " + fruits[i]);
        }
    }
}
```

### 코드 설명

```java
String[] fruits = {"사과", "바나나", "포도"};
```

문자열 여러 개를 담는 배열을 만든다.

```java
fruits[0]
```

첫 번째 칸의 값을 꺼낸다.

```java
fruits[2] = "딸기";
```

2번 칸의 값을 `"딸기"`로 바꾼다.

```java
for (int i = 0; i < fruits.length; i++)
```

0번 칸부터 마지막 칸까지 순서대로 확인한다.

---

## 6. 마지막 정리

배열은 번호가 붙은 보관함이다.

Java 배열은 같은 자료형의 값만 담을 수 있다.

첫 번째 칸 번호는 0이다.

배열 길이는 `length`로 확인한다.

배열 전체를 볼 때는 반복문을 자주 사용한다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 배열",
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
