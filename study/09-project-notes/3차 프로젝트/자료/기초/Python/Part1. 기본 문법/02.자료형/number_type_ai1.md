# 제목
[Python 기초] 숫자형 (Number Type)

# 본문
파이썬에서 숫자를 표현하는 자료형이다.
정수(int), 실수(float), 복소수(complex), 8진수, 16진수를 모두 포함한다.

파이썬의 정수형은 크기 제한이 없어 아무리 큰 수도 표현할 수 있다.
실수형은 부동소수점 방식으로 저장되며, 연산 시 미세한 오차가 생길 수 있다.

## 숫자형의 종류

| 항목 | 예시 | 설명 |
|------|------|------|
| 정수 | 123, -345, 0 | int 타입 |
| 실수 | 1.2, 4.24e10 | float 타입 |
| 복소수 | 1+2j, -3j | complex 타입 |
| 8진수 | 0o34, 0o25 | 접두사 0o |
| 16진수 | 0x2A, 0xFF | 접두사 0x |

## 부동소수점 오류

실수형 연산에서는 이진수 변환 과정에서 미세한 오차가 발생할 수 있다.
0.1 + 0.2의 결과가 정확히 0.3이 아닌 이유가 여기에 있다.

<IMAGE>부동소수점 오차 원리 그림</IMAGE>

해결책으로는 round() 함수 또는 decimal 모듈을 사용한다.

## 연산자 종류

| 연산자 | 설명 | 예시 | 결과 |
|--------|------|------|------|
| + | 더하기 | 3 + 4 | 7 |
| - | 빼기 | 5 - 2 | 3 |
| * | 곱하기 | 3 * 4 | 12 |
| / | 나누기 | 7 / 2 | 3.5 |
| // | 정수 나누기(몫) | 7 // 2 | 3 |
| % | 나머지 | 7 % 2 | 1 |
| ** | 거듭제곱 | 2 ** 10 | 1024 |

`/` 는 항상 실수를 반환하고, `//` 는 소수점 이하를 버린 정수를 반환한다.
`**` 는 다른 언어의 `^` 연산자와 다르게 거듭제곱을 의미한다.

## 수도코드(Pseudocode)

```
숫자형_선언(값):
    정수면 → int 타입으로 저장
    실수면 → float 타입으로 저장 (IEEE 754 방식)
    연산 수행 시:
        / 연산 → 항상 float 반환
        // 연산 → int 반환 (소수점 버림)
        ** 연산 → 거듭제곱 수행
```

## 구현 코드 (Python)

```python
# 정수형
a = 123
b = -178
c = 0
print(type(a))   # <class 'int'>

# 실수형
x = 1.2
y = 4.24e10      # 4.24 × 10^10
print(type(x))   # <class 'float'>

# 부동소수점 오류 예시
print(0.1 + 0.2)              # 0.30000000000000004
print(round(0.1 + 0.2, 1))   # 0.3  (해결)

# 기본 연산
a = 7
b = 2
print(a + b)    # 9
print(a - b)    # 5
print(a * b)    # 14
print(a / b)    # 3.5  → 항상 float
print(a // b)   # 3    → 소수점 버림
print(a % b)    # 1
print(a ** b)   # 49

# 복소수
c = 1 + 2j
print(c.real)         # 1.0
print(c.imag)         # 2.0
print(c.conjugate())  # (1-2j)

# 수학 함수
import math
print(abs(-5))           # 5
print(pow(2, 10))        # 1024
print(round(3.567, 2))   # 3.57
print(math.sqrt(16))     # 4.0
print(math.floor(3.7))   # 3
print(math.ceil(3.2))    # 4
```

## 실전 예제: 몫과 나머지 활용

```python
# 시간 단위 변환 (초 → 시:분:초)
def seconds_to_hms(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

h, m, s = seconds_to_hms(3661)
print(f"{h}시간 {m}분 {s}초")   # 1시간 1분 1초

# 짝수/홀수 판별
def is_even(n):
    return n % 2 == 0

print(is_even(4))   # True
print(is_even(7))   # False
```

# 메타데이터
```json
{
  "category": "자료형",
  "topic": "숫자형",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "beginner",
  "language": "python"
}
```
