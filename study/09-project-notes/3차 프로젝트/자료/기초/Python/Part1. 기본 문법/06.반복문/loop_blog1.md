# [Python 기초] 반복문 (while / for)

---

# 링크
<https://gmlwjd9405.github.io/2018/08/15/algorithm-bfs.html>

---

## 1. 한 줄 요약

반복문은 **같은 작업을 여러 번 자동으로 반복**시키는 방법이다. "1부터 100까지 더해라"처럼 사람이 일일이 하기 귀찮은 반복 작업을 코드 몇 줄로 해결할 수 있다.

---

## 2. 왜 반복문이 필요할까?

"안녕하세요"를 5번 출력하고 싶다면?

```python
# 반복문 없이
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
print("안녕하세요")
```

100번이라면? 1000번이라면? 직접 쓰는 건 불가능에 가깝다.

```python
# 반복문 있으면
for i in range(5):
    print("안녕하세요")
```

단 2줄로 끝난다. 반복 횟수를 5에서 1000으로 바꾸기만 하면 1000번도 거뜬하다.

---

## 3. 핵심 아이디어

### while — "조건이 참인 동안 계속 돌아라"

**자동문**처럼 생각하자. 사람이 가까이 오면(조건 True) 문이 열리고, 멀어지면(조건 False) 문이 닫힌다.

```
조건 확인
    │
   True? ──→ 본문 실행 ──→ 다시 조건 확인
    │
  False? ──→ 반복 종료
```

### for — "목록을 하나씩 꺼내서 처리해라"

**컨베이어 벨트**처럼 생각하자. 벨트 위의 물건(리스트, range 등)을 하나씩 꺼내서 작업하고, 마지막 물건까지 처리하면 끝난다.

```
[1, 2, 3, 4, 5]  ← 컨베이어 벨트
  ↓  ↓  ↓  ↓  ↓
  차례대로 하나씩 꺼내서 처리
```

---

## 4. 동작 과정 살펴보기

### 4-1. while문 기본

```python
# 형식
while 조건:
    반복할 코드
```

```python
# 예시: 1부터 5까지 출력
count = 1

while count <= 5:
    print(count)
    count += 1
```

```
실행 흐름:

count = 1
────────────────────────
라운드 1: count <= 5? → 1 <= 5 → True  ✅ → print(1) → count = 2
라운드 2: count <= 5? → 2 <= 5 → True  ✅ → print(2) → count = 3
라운드 3: count <= 5? → 3 <= 5 → True  ✅ → print(3) → count = 4
라운드 4: count <= 5? → 4 <= 5 → True  ✅ → print(4) → count = 5
라운드 5: count <= 5? → 5 <= 5 → True  ✅ → print(5) → count = 6
라운드 6: count <= 5? → 6 <= 5 → False ❌ → 반복 종료
────────────────────────
출력: 1 2 3 4 5
```

> ⚠️ while문을 쓸 때는 반드시 **조건을 False로 만드는 코드**(`count += 1`)가 있어야 한다. 없으면 영원히 반복되는 **무한 루프**에 빠진다!

---

### 4-2. for문 기본

```python
# 형식
for 변수 in 목록:
    반복할 코드
```

```python
# 예시: 리스트 항목 하나씩 출력
fruits = ["사과", "바나나", "딸기"]

for fruit in fruits:
    print(fruit)
```

```
실행 흐름:

["사과", "바나나", "딸기"]
    ↓
라운드 1: fruit = "사과"  → print("사과")
라운드 2: fruit = "바나나" → print("바나나")
라운드 3: fruit = "딸기"  → print("딸기")
→ 목록 끝 → 반복 종료

출력: 사과
     바나나
     딸기
```

---

### 4-3. range() — 숫자 목록을 자동으로 만들어주는 도구

매번 리스트를 직접 만들기 불편하니, `range()`로 숫자 범위를 자동 생성한다.

```
range(end)            → 0 부터 end-1 까지
range(start, end)     → start 부터 end-1 까지
range(start, end, step) → start 부터 end-1 까지, step 간격으로
```

```python
for i in range(5):
    print(i, end=" ")
# 출력: 0 1 2 3 4

for i in range(1, 6):
    print(i, end=" ")
# 출력: 1 2 3 4 5

for i in range(0, 10, 2):
    print(i, end=" ")
# 출력: 0 2 4 6 8
```

```
range(1, 6) 시각화:

시작(1)              끝(6, 미포함)
  │                     │
  1 ── 2 ── 3 ── 4 ── 5 ✗6
  ↑         ↑
포함        포함     마지막(6)은 미포함!
```

> 💡 `range(end)`에서 **end값은 포함되지 않는다**. `range(5)`는 0~4, `range(1, 6)`은 1~5다.

---

## 5. break와 continue — 반복 흐름 제어

### break — 반복문 즉시 탈출

원하는 조건에서 반복을 **바로 멈추고 싶을 때** 사용한다.

```python
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

# 출력: 0 1 2 3 4
```

```
흐름 시각화:

0 → print ✅
1 → print ✅
2 → print ✅
3 → print ✅
4 → print ✅
5 → break! 🛑 → 반복 즉시 종료 (5는 출력 안 됨)
```

### continue — 이번 라운드만 건너뛰기

특정 조건일 때만 **그 라운드를 건너뛰고** 다음으로 넘어가고 싶을 때 사용한다.

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")

# 출력: 1 3 5 7 9
```

```
흐름 시각화:

0 → 짝수 → continue ↩ (건너뜀)
1 → 홀수 → print ✅
2 → 짝수 → continue ↩ (건너뜀)
3 → 홀수 → print ✅
4 → 짝수 → continue ↩ (건너뜀)
5 → 홀수 → print ✅
...
```

```
break vs continue 차이:

break    → 🛑 반복문 전체 종료
continue → ↩ 이번 라운드만 건너뛰고, 다음 라운드 계속
```

---

## 6. 구현 코드 및 상세 설명

### 구구단 출력 (while 버전 vs for 버전)

```python
# while 버전
dan = 3
i = 1
while i <= 9:
    print(f"{dan} x {i} = {dan * i}")
    i += 1
```

```python
# for 버전 (훨씬 간결)
dan = 3
for i in range(1, 10):
    print(f"{dan} x {i} = {dan * i}")
```

```
출력:
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 9 = 27
```

코드 설명:
- `range(1, 10)` → 1부터 9까지 (10 미포함)
- `f"{dan} x {i} = {dan * i}"` → f-string으로 값을 문자열 안에 바로 넣기
- for문이 while문보다 **간결하고 실수가 적다** (`i += 1` 빠뜨릴 위험이 없음)

---

### 리스트 컴프리헨션 — for문을 한 줄로 줄이기

반복문으로 리스트를 만드는 패턴이 자주 등장한다. 이걸 한 줄로 쓰는 방법이 **리스트 컴프리헨션**이다.

```python
# 일반 for문
squares = []
for i in range(1, 6):
    squares.append(i * i)
print(squares)  # [1, 4, 9, 16, 25]

# 리스트 컴프리헨션 (한 줄로!)
squares = [i * i for i in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

조건을 붙이는 것도 가능하다.

```python
# 홀수만 골라서 제곱
result = [i * i for i in range(1, 10) if i % 2 == 1]
print(result)  # [1, 9, 25, 49, 81]
```

```
읽는 방법:

[i * i  for i in range(1, 10)  if i % 2 == 1]
  ↑            ↑                     ↑
무엇을 담을까  어디서 꺼낼까       조건 (조건 맞는 것만)
```

> 💡 리스트 컴프리헨션은 간결하지만, 너무 복잡해지면 오히려 읽기 어렵다. for문 2개 이상이 중첩되는 경우엔 일반 for문으로 풀어 쓰는 게 낫다.

---

### enumerate() — 순서 번호가 필요할 때

for문으로 리스트를 순회하면서 **몇 번째인지도 함께 알고 싶을 때** 사용한다.

```python
fruits = ["사과", "바나나", "딸기"]

# enumerate 없이 (번거로움)
i = 0
for fruit in fruits:
    print(i, fruit)
    i += 1

# enumerate 사용 (깔끔!)
for i, fruit in enumerate(fruits):
    print(i, fruit)
```

```
출력:
0 사과
1 바나나
2 딸기
```

```
enumerate 동작 원리:

["사과", "바나나", "딸기"]
     ↓
[(0, "사과"), (1, "바나나"), (2, "딸기")]  ← (번호, 값) 쌍으로 변환
     ↓
for i, fruit in ...
  i = 번호, fruit = 값  으로 각각 받음
```

1번부터 시작하고 싶다면 `enumerate(fruits, 1)`처럼 시작 번호를 지정할 수 있다.

```python
for i, fruit in enumerate(fruits, 1):
    print(f"{i}번: {fruit}")
# 출력:
# 1번: 사과
# 2번: 바나나
# 3번: 딸기
```

---

## 7. while vs for 언제 뭘 쓸까?

```
while 쓰는 경우:
  - 반복 횟수를 미리 모를 때
  - "조건이 만족되는 동안" 계속 반복할 때
  예) 사용자가 'quit'을 입력할 때까지 반복
  예) 게임에서 체력이 0이 될 때까지 반복

for 쓰는 경우:
  - 반복 횟수가 정해져 있을 때
  - 리스트, 문자열 등 목록을 순서대로 처리할 때
  예) 리스트의 모든 항목 출력
  예) 1부터 100까지 합산
```

---

## 8. 마지막 정리

- `while`은 **조건이 True인 동안** 계속 반복한다. 조건을 False로 만드는 코드가 없으면 무한 루프에 빠진다.
- `for`는 **목록(리스트, range 등)을 하나씩 꺼내** 처리한다. 목록이 끝나면 자동으로 종료된다.
- `range(start, end, step)`으로 숫자 범위를 만들 수 있고, **end값은 포함되지 않는다**.
- `break`는 반복문을 **즉시 탈출**, `continue`는 **이번 라운드만 건너뛰고** 다음으로 넘어간다.
- **리스트 컴프리헨션**으로 for문 + 리스트 생성을 한 줄로 표현할 수 있다.
- `enumerate()`를 쓰면 **순서 번호와 값을 동시에** 꺼낼 수 있다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "반복문",
  "style": [
    "easy",
    "analogy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```