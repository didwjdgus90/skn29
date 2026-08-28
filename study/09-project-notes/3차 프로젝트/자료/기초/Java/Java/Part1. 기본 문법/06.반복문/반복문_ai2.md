# 제목
[Java기초] 반복문

# 본문

## 1. 한 줄 요약

반복문은 컴퓨터에게 “이 일을 여러 번 반복해줘”라고 부탁하는 문법이다.

반복문을 배우면 똑같은 코드를 여러 번 쓰지 않아도 된다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

운동장에서 줄넘기를 10번 한다고 생각해 보자.

```text
1번 뛰기
2번 뛰기
3번 뛰기
...
10번 뛰기
```

사람은 마음속으로 횟수를 세며 같은 행동을 반복한다.

Java에서도 같은 코드를 여러 번 실행해야 할 때 반복문을 사용한다.

```java
for (int i = 1; i <= 10; i++) {
    System.out.println("줄넘기 " + i + "번");
}
```

---

## 3. 핵심 아이디어

반복문은 세탁기와 비슷하다.

세탁기는 정해진 조건이 끝날 때까지 같은 동작을 반복한다.

```text
물 넣기
돌리기
헹구기
탈수하기
```

`for`문은 “몇 번 반복할지” 정해져 있을 때 좋다.

```text
1번부터 5번까지 반복
```

`while`문은 “언제까지 반복할지” 조건이 중요할 때 좋다.

```text
배터리가 남아 있는 동안 반복
```

---

## 4. 동작 과정 살펴보기

```java
for (int i = 1; i <= 3; i++) {
    System.out.println("안녕");
}
```

### Step 1. 1부터 시작

```text
i = 1
```

### Step 2. 조건 확인

```text
1 <= 3 → true
```

### Step 3. 출력

```text
안녕
```

### Step 4. 숫자 증가

```text
i = 2
```

반복 결과는 다음과 같다.

```text
i = 1 → 안녕
i = 2 → 안녕
i = 3 → 안녕
i = 4 → 조건 false, 종료
```

---

## 5. 구현 코드 및 상세 설명

```java
public class Main {
    public static void main(String[] args) {
        for (int i = 1; i <= 5; i++) {
            System.out.println(i + "번째 인사");
        }

        int cookie = 3;

        while (cookie > 0) {
            System.out.println("쿠키를 먹었습니다.");
            cookie--;
        }

        System.out.println("쿠키가 없습니다.");
    }
}
```

### 코드 설명

```java
for (int i = 1; i <= 5; i++)
```

1부터 5까지 숫자를 하나씩 늘리며 반복한다.

```java
System.out.println(i + "번째 인사");
```

현재 몇 번째 반복인지 함께 출력한다.

```java
while (cookie > 0)
```

쿠키가 남아 있는 동안 반복한다.

```java
cookie--;
```

쿠키를 하나 먹었으므로 개수를 줄인다.

이 코드가 없으면 쿠키 수가 줄지 않아 계속 반복된다.

---

## 6. 마지막 정리

반복문은 같은 일을 여러 번 할 때 사용한다.

`for`문은 횟수가 정해져 있을 때 편하다.

`while`문은 조건이 참인 동안 반복한다.

반복을 멈추려면 조건이 언젠가 거짓이 되어야 한다.

반복문은 배열이나 입력 처리에서 자주 사용된다.


# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "Java 반복문",
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
