# 제목
[Python 기초] 연산자 (Operators)

# 링크
https://gostart.tistory.com/206

# 본문

## 0. 연산자(Operators) 란?

연산자는 **변수 및 값에 대한 수정·변환 작업을 할 때 사용**한다.

파이썬에서 연산자는 아래와 같은 유형으로 나눌 수 있다.

```
연산자 유형:

1. 산술 연산자   (Arithmetic Operators)   — 수학 연산 (+, -, *, /)
2. 할당 연산자   (Assignment Operators)   — 변수에 값 대입 (=, +=, -=, ...)
3. 비교 연산자   (Comparison Operators)   — 두 값 비교 (==, !=, >, <, ...)
4. 논리 연산자   (Logical Operators)      — 조건 결합 (and, or, not)
5. 아이덴티 연산자 (Identity Operators)  — 동일 객체 여부 (is, is not)
6. 멤버십 연산자  (Membership Operators)  — 시퀀스 포함 여부 (in, not in)
7. 비트와이즈 연산자 (Bitwise Operators)  — 이진수 비트 연산 (&, |, ^, ~, <<, >>)
```

---

## 1. 산술 연산자 (Arithmetic Operators)

산술 연산자는 일반적인 수학 연산을 수행하기 위해 **숫자와 함께 사용**한다.

```
연산자   이름               설명                                    예시
──────────────────────────────────────────────────────────────────────
+        Addition           연산자의 양쪽 값을 더한 값을 구한다.     x + y
-        Subtraction        연산자의 왼쪽 값에서 오른쪽 값을 뺀다.   x - y
*        Multiplication     연산자의 양쪽 값을 곱한 값을 구한다.     x * y
/        Division           왼쪽 값을 오른쪽 값으로 나눈다.          x / y
%        Modulus            나눈 나머지를 구한다.                    x % y
**       Exponentiation     왼쪽 값을 오른쪽 값으로 거듭제곱한다.    x ** y
//       Floor division     나눈 몫의 정수 부분을 구한다.            x // y
```

> **주의**: `/` 는 항상 **실수(float)** 를 반환한다. 정수 나누기 결과가 필요하면 `//` 를 사용한다.
> 또한 `//` 는 소수점 이하를 **버리는** 것이지, 반올림이 아니다.

### 산술 연산자 예제

```python
# 05_01_00_PythonArthmeticOperators

# 기본 할당
FirstValue = 3
SecondValue = 2

# 덧셈 연산
print(FirstValue + SecondValue)     # 5

# 뺄셈 연산
print(FirstValue - SecondValue)     # 1

# 곱셈 연산
print(FirstValue * SecondValue)     # 6

# 나눗셈 연산 — 결과는 항상 float
print(FirstValue / SecondValue)     # 1.5

# 나머지 연산
modValue = FirstValue % SecondValue
print(modValue)                     # 1

# 몫 연산 (소수점 이하 버림)
floorValue = FirstValue // SecondValue
print(floorValue)                   # 1

# 거듭제곱 연산
expValue = FirstValue ** SecondValue
print(expValue)                     # 9  (3의 2승 = 3 × 3)
```

```
동작 시각화 (FirstValue=3, SecondValue=2):

3 + 2 = 5
3 - 2 = 1
3 * 2 = 6
3 / 2 = 1.5   ← 항상 float 반환
3 % 2 = 1     ← 3 ÷ 2 = 1 나머지 1
3 // 2 = 1    ← 1.5에서 소수점 버림
3 ** 2 = 9    ← 3 × 3
```

---

## 2. 할당 연산자 (Assignment Operators)

할당 연산자는 **변수에 값을 대입할 때 사용**한다. `x += y` 는 `x = x + y` 와 동일하다. 즉, **연산과 대입을 한 번에** 처리하는 복합 대입 연산자다.

```
연산자   설명                                                        예시
──────────────────────────────────────────────────────────────────────────
=        오른쪽 값을 왼쪽에 할당한다.                                x = y
+=       왼쪽 값과 오른쪽 값을 더하여 왼쪽에 할당한다.               x += y
-=       왼쪽 값에서 오른쪽 값을 뺀 값을 왼쪽에 할당한다.            x -= y
*=       왼쪽 값과 오른쪽 값을 곱한 값을 왼쪽에 할당한다.            x *= y
/=       왼쪽 값을 오른쪽 값으로 나눈 값을 왼쪽에 할당한다.          x /= y
%=       나눈 나머지를 왼쪽에 할당한다.                              x %= y
**=      거듭제곱한 값을 왼쪽에 할당한다.                            x **= y
//=      나눈 몫(정수부)을 왼쪽에 할당한다.                          x //= y
&=       비트 논리곱 한 값을 왼쪽에 할당한다.                        x &= y
|=       비트 논리합 한 값을 왼쪽에 할당한다.                        x |= y
^=       비트 배타적 논리합 한 값을 왼쪽에 할당한다.                  x ^= y
>>=      오른쪽으로 비트 이동한 값을 왼쪽에 할당한다.                x >>= y
<<=      왼쪽으로 비트 이동한 값을 왼쪽에 할당한다.                  x <<= y
```

### 할당 연산자 예제

```python
# 05_02_00_PythonAssignmentOperators

# = 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue = SecondValue
print(FirstValue)       # 2

# += 할당 연산자  (FirstValue = FirstValue + SecondValue)
FirstValue = 3; SecondValue = 2
FirstValue += SecondValue
print(FirstValue)       # 5

# -= 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue -= SecondValue
print(FirstValue)       # 1

# *= 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue *= SecondValue
print(FirstValue)       # 6

# /= 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue /= SecondValue
print(FirstValue)       # 1.5

# %= 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue %= SecondValue
print(FirstValue)       # 1

# //= 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue //= SecondValue
print(FirstValue)       # 1

# **= 할당 연산자
FirstValue = 3; SecondValue = 2
FirstValue **= SecondValue
print(FirstValue)       # 9

# &= 할당 연산자 (비트 AND)
FirstValue = 3; SecondValue = 2
FirstValue &= SecondValue
print(FirstValue)       # 2   (0b11 & 0b10 = 0b10)

# |= 할당 연산자 (비트 OR)
FirstValue = 3; SecondValue = 2
FirstValue |= SecondValue
print(FirstValue)       # 3   (0b11 | 0b10 = 0b11)

# ^= 할당 연산자 (비트 XOR)
FirstValue = 3; SecondValue = 2
FirstValue ^= SecondValue
print(FirstValue)       # 1   (0b11 ^ 0b10 = 0b01)

# >>= 할당 연산자 (오른쪽 비트 이동)
FirstValue = 3; SecondValue = 2
FirstValue >>= SecondValue
print(FirstValue)       # 0   (0b11 >> 2 = 0b00)

# <<= 할당 연산자 (왼쪽 비트 이동)
FirstValue = 3; SecondValue = 2
FirstValue <<= SecondValue
print(FirstValue)       # 12  (0b11 << 2 = 0b1100)
```

---

## 3. 비교 연산자 (Comparison Operators)

비교 연산자는 **두 값을 비교하는 데 사용**한다. 결과는 항상 **`True` 또는 `False`** 로 반환된다.

```
연산자   설명                                             예시
──────────────────────────────────────────────────────────────
==       왼쪽 값과 오른쪽 값이 같으면 True 반환           x == y
!=       왼쪽 값과 오른쪽 값이 다르면 True 반환           x != y
>        왼쪽 값이 오른쪽 값보다 크면 True 반환            x > y
<        왼쪽 값이 오른쪽 값보다 작으면 True 반환          x < y
>=       왼쪽 값이 오른쪽 값보다 크거나 같으면 True 반환   x >= y
<=       왼쪽 값이 오른쪽 값보다 작거나 같으면 True 반환   x <= y
```

> **주의**: `=` 은 **대입** 연산자이고, `==` 는 **같음 비교** 연산자다. 이 둘을 혼동하는 실수가 자주 발생한다.

### 비교 연산자 예제

```python
# 05_03_00_PythonComparisonOperators

xZero = 0
xNotZero = 1
yZero = 0
yNotZero = 1

# 불리언 값 검증 (0은 False, 1은 True와 같다)
print(xZero == True)        # False
print(xZero == False)       # True
print(xNotZero == True)     # True
print(xNotZero == False)    # False

# == 연산자
print(xZero == yZero)       # True
print(xZero == yNotZero)    # False

# != 연산자
print(xZero != yZero)       # False
print(xZero != yNotZero)    # True

# > 연산자
print(xZero > yZero)        # False
print(xNotZero > yZero)     # True

# < 연산자
print(xZero < yZero)        # False
print(xZero < yNotZero)     # True

# >= 연산자
print(xZero >= yZero)       # True
print(xNotZero >= yZero)    # True

# <= 연산자
print(xZero <= yZero)       # True
print(xZero <= yNotZero)    # True
```

---

## 4. 논리 연산자 (Logical Operators)

논리 연산자는 **조건문을 결합할 때 사용**한다.

```
연산자   설명                                              예시
──────────────────────────────────────────────────────────────────
and      왼쪽과 오른쪽 값이 모두 참이면 참을 반환한다.     x and y
or       왼쪽과 오른쪽 중 하나라도 참이면 참을 반환한다.   x or y
not      참이면 거짓을, 거짓이면 참을 반환한다.            not(x)
```

> **파이썬 논리 연산자의 특징 — 단락 평가(Short-circuit Evaluation)**
> - `and` : 왼쪽 값이 **거짓이면** 오른쪽을 평가하지 않고 왼쪽 값을 반환한다.
> - `or`  : 왼쪽 값이 **참이면** 오른쪽을 평가하지 않고 왼쪽 값을 반환한다.
> - 따라서 반환값이 `True/False`가 아닌 **원래 값** 그대로 나올 수 있다.

```
and 진리표:          or 진리표:          not 진리표:
────────────────     ────────────────     ────────────
A    B    결과        A    B    결과        A    결과
0    0    0           0    0    0           0    True
1    0    0           1    0    1           1    False
0    1    0           0    1    1
1    1    1           1    1    1
```

### 논리 연산자 예제

```python
# 05_04_00_PythonLogicalOperators

xZero = 0
xNotZero = 1
yTrue = True
yFalse = False

# And 연산 — 둘 다 참이어야 참 반환
print(xZero and xNotZero)       # 0      ← xZero(0)가 거짓이므로 xZero 반환
print(xNotZero and xNotZero)    # 1
print(xNotZero and yTrue)       # True
print(xNotZero and yFalse)      # False
print(yFalse and xNotZero)      # False

# Or 연산 — 하나라도 참이면 참 반환
print(xZero or xZero)           # 0      ← 둘 다 거짓
print(xZero or xNotZero)        # 1      ← xNotZero가 참이므로 xNotZero 반환
print(xZero or yTrue)           # True
print(yFalse or xZero)          # 0
print(yFalse or yFalse)         # False

# Not 연산 — 참/거짓 반전
print(not xZero)                # True
print(not xNotZero)             # False
print(not yTrue)                # False
print(not yFalse)               # True
```

---

## 5. 아이덴티 연산자 (Identity Operators)

아이덴티 연산자는 **두 객체가 동일한 객체인지를 비교**한다.

`==` 는 **값이 같은지**를 비교하고, `is` 는 **메모리 주소(id)가 같은지**를 비교한다는 점에서 다르다.

```
연산자      설명                                      예시
─────────────────────────────────────────────────────────────
is          두 값이 동일한 객체이면 True 반환          x is y
is not      두 값이 동일한 객체가 아니면 True 반환     x is not y
```

```
== vs is 비교:

a = [1, 2, 3]
b = [1, 2, 3]

a == b   → True   (값이 같음)
a is b   → False  (다른 객체, 메모리 주소가 다름)
```

### 아이덴티 연산자 예제

```python
# 05_05_00_PythonIdentityOperators

FirstIdentity = 10
SecondIdentity = 10
ThiredIdentity = 10.0

# 파이썬은 작은 정수(-5 ~ 256)를 캐싱하므로 같은 값이면 같은 객체를 가리킴
print(id(FirstIdentity))                              # 140720180926400
print(id(SecondIdentity))                             # 140720180926400 (동일!)
print(id(ThiredIdentity))                             # 3028251405232   (float는 다름)

print(FirstIdentity is SecondIdentity)                # True  (같은 객체)
print(id(FirstIdentity) == id(SecondIdentity))        # True

SecondIdentity = 20
print(FirstIdentity is SecondIdentity)                # False (이제 다른 객체)
print(id(FirstIdentity) == id(SecondIdentity))        # False
print(FirstIdentity is not SecondIdentity)            # True
print(id(FirstIdentity) != id(SecondIdentity))        # True
```

---

## 6. 멤버십 연산자 (Membership Operators)

멤버십 연산자는 **시퀀스 데이터 유형의 아이템이 존재하는지를 비교하는 데 사용**한다.

주의할 것은 **멤버 자체를 하나의 객체로 인식**한다는 부분이다.

```
연산자      설명                                      예시
─────────────────────────────────────────────────────────────
in          동일한 아이템을 찾을 경우 True 반환         x in y
not in      동일한 아이템을 찾지 못할 경우 True 반환    x not in y
```

> 멤버십 연산자는 **리스트(list), 튜플(tuple), 집합(set), 문자열(str), 딕셔너리(dict)** 등 모든 시퀀스/컬렉션 자료형에서 사용할 수 있다.

### 멤버십 연산자 예제

```python
# 05_06_00_PythonMembershipOperators

FirstMember = 10
SecondMember = 20

list = [10, 11]
lists = [10, 11, 12, 13, 14]
listx = [[10, 11], 12, 13, 14]    # 리스트를 요소로 가진 리스트

sets = (10, 11, 12, 13, 14)

# 리스트에서 동작
print(FirstMember in lists)             # True
print(FirstMember not in lists)         # False
print(SecondMember in lists)            # False
print(SecondMember not in lists)        # True

# 튜플에서도 동일하게 동작
print(FirstMember in sets)              # True
print(FirstMember not in sets)          # False
print(SecondMember in sets)             # False
print(SecondMember not in sets)         # True

# 리스트 객체 자체는 비교 불가 (요소 단위로 비교)
print(list in lists)                    # False  ← [10,11] 전체를 하나의 요소로 찾음
print(list not in lists)                # True
print(list in listx)                    # True   ← listx에 [10,11]이 요소로 있음
print(list not in listx)                # False
```

---

## 7. 비트와이즈 연산자 (Bitwise Operators)

비트 연산자는 **이진수(비트) 단위로 숫자를 비교하고 연산**하는 데 사용한다.

```
연산자   이름                    설명                             예시
───────────────────────────────────────────────────────────────────────
&        AND                     비트 논리곱을 반환한다.           x & y
|        OR                      비트 논리합을 반환한다.           x | y
^        XOR                     배타적 논리합을 반환한다.         x ^ y
~        NOT                     비트 반전(2의 보수)을 반환한다.   ~x
<<       Zero fill left shift    비트를 왼쪽으로 이동한다.         x << y
>>       Signed right shift      비트를 오른쪽으로 이동한다.       x >> y
```

### 비트 연산 진리표

```
AND (&):              OR (|):               XOR (^):
X  Y  결과            X  Y  결과            X  Y  결과
0  0   0              0  0   0              0  0   0
1  0   0              1  0   1              1  0   1
0  1   0              0  1   1              0  1   1
1  1   1              1  1   1              1  1   0
                                            ↑ 같으면 0, 다르면 1
```

### NOT 연산자 규칙

```
양수 N  →  ~N = -(N+1)
음수 -N →  ~(-N) = N-1

예:
~0  = -1     (-(0+1))
~1  = -2     (-(1+1))
~10 = -11    (-(10+1))
~(-1) = 0    (1-1)
~(-10) = 9   (10-1)
```

### 비트와이즈 연산자 예제

```python
# 05_07_00_PythonBitwiseOperators

bitPositive10 = 10
bitPositiveOne = 1
bitZero = 0
bitNegativeOne = -1
bitNegative10 = -10

# 이진수 출력 (bin() 함수)
print(bin(bitPositive10))                                   # 0b1010

# 8자리 이진수로 출력
print('{0:b}'.format(bitPositive10).zfill(8))               # 00001010
print('{0:b}'.format(bitPositiveOne).zfill(8))              # 00000001
print('{0:b}'.format(bitZero).zfill(8))                     # 00000000
print('{0:b}'.format(bitNegativeOne).zfill(8))              # -0000001
print('{0:b}'.format(bitNegative10).zfill(8))               # -0001010

# AND 연산 (&) — 같은 자리가 모두 1일 때만 1
print('{0:b}'.format(bitZero & bitPositive10).zfill(8))     # 00000000
print('{0:b}'.format(bitPositive10 & bitPositive10).zfill(8))# 00001010
# 양수와 음수 AND (2의 보수 방식 적용)
print('{0:b}'.format(bitPositive10 & bitNegative10).zfill(8))# 00000010

# OR 연산 (|) — 같은 자리에 하나라도 1이면 1
print('{0:b}'.format(bitZero | bitPositive10).zfill(8))     # 00001010
print('{0:b}'.format(bitPositive10 | bitPositive10).zfill(8))# 00001010
print('{0:b}'.format(bitPositive10 | bitNegative10).zfill(8))# -0000010

# XOR 연산 (^) — 같은 자리가 다를 때만 1
print('{0:b}'.format(bitZero ^ bitPositive10).zfill(8))     # 00001010
print('{0:b}'.format(bitPositive10 ^ bitPositive10).zfill(8))# 00000000 (같으면 0)
print('{0:b}'.format(bitPositive10 ^ bitNegative10).zfill(8))# -0000100

# NOT 연산 (~) — 비트 반전 (양수 N → -(N+1))
print('{0:b}'.format(~bitZero).zfill(8))                    # -0000001  (~0  = -1)
print('{0:b}'.format(~bitPositiveOne).zfill(8))             # -0000010  (~1  = -2)
print('{0:b}'.format(~bitPositive10).zfill(8))              # -0001011  (~10 = -11)
print('{0:b}'.format(~bitNegativeOne).zfill(8))             # 00000000  (~-1 = 0)
print('{0:b}'.format(~bitNegative10).zfill(8))              # 00001001  (~-10 = 9)

# Left Shift (<<) — 비트를 왼쪽으로 N칸 이동 (2^N 배)
print('{0:b}'.format(bitPositiveOne << 2).zfill(8))         # 00000100  (1 << 2 = 4)
print('{0:b}'.format(bitPositive10 << 2).zfill(8))          # 00101000  (10 << 2 = 40)
print('{0:b}'.format(bitNegativeOne << 2).zfill(8))         # -0000100  (부호 영향 없음)

# Right Shift (>>) — 비트를 오른쪽으로 N칸 이동 (2^N 으로 나눔)
print('{0:b}'.format(bitPositiveOne >> 2).zfill(8))         # 00000000  (1 >> 2 = 0)
print('{0:b}'.format(bitPositive10 >> 2).zfill(8))          # 00000010  (10 >> 2 = 2)
print('{0:b}'.format(bitNegativeOne >> 2).zfill(8))         # -0000001
```

> **음수의 비트 연산**: 음수 값의 비트를 연산할 경우 계산 패턴이 특이한 경우를 보이는데, 이는 **2의 보수(Two's Complement)** 표현 방식과 연관되어 있다.

---

## 8. 연산자 우선순위

여러 연산자가 한 식에 섞일 때, **우선순위가 높은 연산자부터 먼저 계산**된다. 우선순위가 같은 연산자는 **왼쪽에서 오른쪽** 순서로 계산한다.

```
순위    연산자                설명
──────────────────────────────────────────────────────
1       **                   지수 연산
2       ~ + -                보수, 단항 더하기/빼기
3       * / % //             곱하기, 나누기, 나머지, 몫
4       + -                  덧셈, 뺄셈
5       >> <<                좌우 비트 시프트
6       &                    비트 논리곱
7       ^ |                  배타적 논리합, 비트 논리합
8       <= < > >=            비교 연산자
9       <> == !=             동등 연산자
10      = %= /= //= += -=    할당 연산자
        ^= **=
11      is  is not           아이덴티 연산자
12      in  not in           멤버십 연산자
13      not or and           논리 연산자
```

> **괄호 `()`를 사용하면 우선순위를 명시적으로 제어**할 수 있다. 복잡한 식에서는 괄호를 적극 활용하는 것이 가독성에 좋다.

```python
# 우선순위 예시
print(2 + 3 * 4)        # 14  — * 가 먼저 (3*4=12, 2+12=14)
print((2 + 3) * 4)      # 20  — 괄호가 우선 (2+3=5, 5*4=20)
print(2 ** 3 ** 2)      # 512 — ** 는 오른쪽부터 (3**2=9, 2**9=512)
print(10 > 5 and 3 < 7) # True — 비교 후 and 계산
```

---

## 9. 마지막 정리

- **산술 연산자**: `+`, `-`, `*`, `/`, `%`, `**`, `//` — 기본 수학 연산. `/`는 항상 `float` 반환.
- **할당 연산자**: `=`, `+=`, `-=` 등 — 연산과 대입을 동시에 처리.
- **비교 연산자**: `==`, `!=`, `>`, `<`, `>=`, `<=` — 결과는 항상 `True/False`. `=`(대입)와 `==`(비교)를 혼동하지 말 것.
- **논리 연산자**: `and`, `or`, `not` — 조건 결합. 파이썬은 단락 평가를 적용하여 원래 값을 반환.
- **아이덴티 연산자**: `is`, `is not` — **값이 같은지**(`==`)가 아니라 **같은 객체인지**(메모리 주소)를 비교.
- **멤버십 연산자**: `in`, `not in` — 시퀀스/컬렉션 내 포함 여부 확인. 리스트 객체 자체는 하나의 요소로 인식.
- **비트 연산자**: `&`, `|`, `^`, `~`, `<<`, `>>` — 이진수 단위 연산. 음수 처리 시 2의 보수 방식 적용.

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "연산자",
  "source_type": "blog",
  "style": [
    "easy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```