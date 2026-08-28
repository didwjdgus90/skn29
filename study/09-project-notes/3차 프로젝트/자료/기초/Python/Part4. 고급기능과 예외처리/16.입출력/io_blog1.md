# [Python 기초] 입출력 (Input / Output)

---

# 링크
<https://rebro.kr/126>

---

## 1. 한 줄 요약

파이썬에서 데이터를 **받아들이는(input)** 것과 **화면에 보여주는(print)** 것을 다루는 방법이다. 코딩테스트에서는 정해진 형식으로 값을 입력받고 출력하는 것이 필수이므로, 다양한 입출력 패턴을 익혀두는 것이 중요하다.

---

## 2. 입력 — input()

### 2-1. 기본 입력

파이썬에서 사용자 입력은 `input()` 함수로 받는다. 가장 중요한 특징이 있다.

> **`input()`은 입력되는 모든 것을 문자열(str)로 받는다.**

숫자 `123`을 입력해도 파이썬은 이것을 문자열 `"123"`으로 처리한다. 따라서 숫자로 쓰고 싶다면 반드시 타입을 변환해야 한다.

```python
a = input()         # 모든 입력이 문자열로 저장됨

# 정수로 받기
a = int(input())

# 실수로 받기
a = float(input())
```

```
입력: 42

input()       → "42"   (문자열)
int(input())  → 42     (정수)
```

### 2-2. 여러 값을 한 줄에 입력받기 — split()과 map()

코딩테스트에서 가장 자주 나오는 입력 형태다. 한 줄에 공백으로 구분된 여러 숫자가 주어질 때 이렇게 처리한다.

```
입력 예시: 1 2 3 4 5
```

단계별로 어떻게 처리되는지 보자.

```python
# 1단계: input()으로 받으면 문자열 하나
a = input()
print(a)   # "1 2 3 4 5"

# 2단계: split()으로 공백 기준 분리 → 문자열 리스트
a = input().split()
print(a)   # ['1', '2', '3', '4', '5']

# 3단계: map(int, ...)으로 전체를 정수로 변환
a = list(map(int, input().split()))
print(a)   # [1, 2, 3, 4, 5]
```

```
처리 흐름:

"1 2 3 4 5"
    ↓ .split()
['1', '2', '3', '4', '5']  (문자열 리스트)
    ↓ map(int, ...)
[1, 2, 3, 4, 5]            (정수 리스트)
```

**여러 변수에 동시에 받기 (다중 할당)**

```python
# 입력: 3 5
a, b = map(int, input().split())
print(a)   # 3
print(b)   # 5
```

이렇게 하면 map 결과가 a, b에 각각 하나씩 할당된다. 이 패턴은 코딩테스트에서 매우 자주 쓰인다. 변수 개수와 입력값 개수가 반드시 일치해야 한다.

### 2-3. 다양한 입력 패턴

**N을 먼저 받고, N개의 값을 받는 경우**

```python
# 입력:
# 5
# 1 2 3 4 5
n = int(input())
nums = list(map(int, input().split()))
print(n)     # 5
print(nums)  # [1, 2, 3, 4, 5]
```

**여러 줄을 한꺼번에 받기 (리스트 컴프리헨션 활용)**

```python
# 입력 (3줄):
# 1 2 3
# 4 5 6
# 7 8 9
matrix = [list(map(int, input().split())) for _ in range(3)]
print(matrix)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

이 패턴은 2차원 배열(격자, 지도)을 입력받을 때 자주 쓰인다.

**한 줄씩 문자열로 받기**

```python
# 입력 (5줄):
# AAAAA
# BBBBB
# ...
lines = [input() for _ in range(5)]
print(lines)   # ['AAAAA', 'BBBBB', ...]
```

**문자 하나씩 분리해서 2차원 배열로**

```python
# 입력:
# ABCDE
# FGHIJ
grid = [list(input()) for _ in range(2)]
print(grid)
# [['A','B','C','D','E'], ['F','G','H','I','J']]
```

### 2-4. 빠른 입력 — sys.stdin.readline

`input()`은 편리하지만 **대량의 데이터를 반복해서 받을 때는 느리다.** 코딩테스트에서 입력이 수만 개 이상이면 시간 초과가 날 수 있다. 이때는 `sys.stdin.readline`을 쓴다.

```python
import sys
input = sys.stdin.readline   # input을 빠른 버전으로 교체
```

이 한 줄을 코드 맨 위에 추가하면, 이후 `input()`을 쓰는 모든 곳이 자동으로 빠른 버전으로 바뀐다.

```python
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
```

> ⚠️ `sys.stdin.readline`은 줄 끝에 `\n`(줄바꿈 문자)이 포함되어 반환된다. 문자열 비교 등에서 문제가 생길 수 있으니, 필요하면 `.strip()`을 붙여 제거하자.

```python
s = input().strip()   # 줄바꿈 문자 제거
```

---

## 3. 출력 — print()

### 3-1. 기본 출력

```python
print("Hello World")   # Hello World
print(42)              # 42
print(3.14)            # 3.14
```

### 3-2. 여러 값 한꺼번에 출력하기

콤마(`,`)로 여러 값을 넣으면 **공백으로 구분해서** 한 줄에 출력된다.

```python
print(1, 2, 3)         # 1 2 3
a, b, c = 10, 20, 30
print(a, b, c)         # 10 20 30
```

**`sep` — 구분자 바꾸기**

콤마 대신 다른 구분자를 쓰고 싶을 때 `sep`을 사용한다.

```python
print(1, 2, 3, sep=',')    # 1,2,3
print(1, 2, 3, sep=' / ')  # 1 / 2 / 3
print(1, 2, 3, sep='')     # 123
print(1, 2, 3, sep='\n')   # 1
                            # 2
                            # 3
```

### 3-3. 줄바꿈 제어 — end

`print()`는 기본적으로 출력 후 줄바꿈(`\n`)을 한다. `end` 옵션으로 이를 바꿀 수 있다.

```python
print(1, 2, 3, end=' ')
print(4, 5, 6)
# 1 2 3 4 5 6  ← 두 print가 같은 줄에 이어짐

# 리스트를 공백 구분해서 한 줄로 출력
nums = [1, 2, 3, 4, 5]
for n in nums:
    print(n, end=' ')
# 1 2 3 4 5
```

### 3-4. f-string — 변수를 문자열 안에 넣기

f-string은 문자열 앞에 `f`를 붙이고 `{변수명}`으로 값을 바로 넣는 방법이다. 가장 깔끔하고 직관적인 출력 방식이다.

```python
name = "정민"
score = 92

print(f"이름: {name}, 점수: {score}점")
# 이름: 정민, 점수: 92점

# 수식도 바로 계산 가능
print(f"합격 여부: {'합격' if score >= 60 else '불합격'}")
# 합격 여부: 합격
```

---

## 4. 자주 쓰는 입출력 패턴 모음

코딩테스트에서 반복적으로 등장하는 패턴을 정리했다.

```python
# 패턴 1: 정수 하나 입력
n = int(input())

# 패턴 2: 공백으로 구분된 두 정수
a, b = map(int, input().split())

# 패턴 3: 공백으로 구분된 정수 리스트
nums = list(map(int, input().split()))

# 패턴 4: 첫 줄에 n, 다음 줄에 n개의 수
n = int(input())
nums = list(map(int, input().split()))

# 패턴 5: n줄에 걸쳐 두 정수씩 입력
n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]

# 패턴 6: n×m 격자 입력
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 패턴 7: 빠른 입력 (대량 데이터)
import sys
input = sys.stdin.readline
```

---

## 5. 마지막 정리

- `input()`은 **모든 입력을 문자열**로 받는다. 숫자로 쓰려면 `int()` 또는 `float()`로 감싸야 한다.
- **공백으로 구분된 여러 값**은 `map(int, input().split())`으로 한 번에 받을 수 있다.
- **여러 변수에 동시 할당**: `a, b = map(int, input().split())` — 코테에서 가장 자주 쓰이는 패턴.
- **여러 줄 입력**: `[list(map(int, input().split())) for _ in range(n)]` — 2차원 배열 입력에 활용.
- **대량 입력**은 `import sys; input = sys.stdin.readline`으로 속도를 높인다.
- **`sep`** 으로 구분자, **`end`** 로 줄바꿈 문자를 바꿀 수 있다.
- **f-string** `f"값: {변수}"` 이 출력 형식 중 가장 간결하고 읽기 쉽다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "입출력",
  "source_type": "blog",
  "style": [
    "easy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```