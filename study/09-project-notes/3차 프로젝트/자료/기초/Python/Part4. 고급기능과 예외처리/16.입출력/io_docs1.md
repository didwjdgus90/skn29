# 제목
[Python 기초] 입력과 출력 (Input and Output)

# 링크
https://docs.python.org/ko/3.11/tutorial/inputoutput.html

# 본문

## 1. 한 줄 요약

파이썬은 값을 출력하는 방법으로 **표현식 문장**, **`print()` 함수**, **파일 객체의 `write()` 메서드**를 제공하며, 입력은 **`input()` 함수**로 수행한다. 출력 포매팅에는 f-문자열, `str.format()`, `%` 연산자 세 가지 방식이 존재한다.

---

## 2. 출력 포매팅 방법의 분류

공식 문서는 출력 포매팅 방법을 다음 세 가지로 분류한다.

```
출력 포매팅 방법:

방법                     도입 버전   권장 여부
──────────────────────────────────────────────
f-문자열 (f-string)       3.6+       ✅ 현재 권장
str.format()              3.0+       ✅ 사용 가능
% 연산자 (printf 스타일)   구버전      ⚠ 레거시, 비권장
```

---

## 3. str()과 repr()의 구분

출력에 앞서 `str()`과 `repr()`의 차이를 명확히 구분해야 한다. 공식 문서의 정의에 따르면:

> `str()` 함수는 어느 정도 사람이 읽기에 적합한 형태로 값의 표현을 돌려주게 되어있습니다. 반면에 `repr()`은 인터프리터에 의해 읽힐 수 있는 형태를 만들게 되어있습니다.

```python
>>> s = 'Hello, world.'
>>> str(s)
'Hello, world.'       # 사람이 읽기에 적합한 형태
>>> repr(s)
"'Hello, world.'"     # 인터프리터가 읽을 수 있는 형태 (따옴표 포함)

>>> hello = 'hello, world\n'
>>> print(str(hello))
hello, world          # 개행 문자가 실제로 적용됨
>>> print(repr(hello))
'hello, world\n'      # 이스케이프 문자를 그대로 보여줌
```

```
str() vs repr() 비교:

항목          str()                    repr()
──────────────────────────────────────────────────────
목적          사람이 읽기 위한 표현      인터프리터용 표현
문자열 출력   따옴표 없음, 이스케이프 적용  따옴표 포함, 이스케이프 노출
디버깅 용도   부적합                    적합
```

---

## 4. 동작 과정 살펴보기

### 4-1. f-문자열 (Formatted String Literals)

공식 문서의 정의:

> 포맷 문자열 리터럴(간단히 f-문자열이라고도 합니다)은 문자열에 `f` 또는 `F` 접두어를 붙이고 표현식을 `{expression}`으로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있게 합니다.

```python
>>> year = 2016
>>> event = 'Referendum'
>>> f'Results of the {year} {event}'
'Results of the 2016 Referendum'
```

**포맷 지정자(format specifier)**: `:`뒤에 서식 명세를 작성한다.

```python
>>> import math
>>> print(f'The value of pi is approximately {math.pi:.3f}.')
The value of pi is approximately 3.142.
```

**열 너비 지정**: `:`뒤의 정수가 필드의 최소 문자 폭이 된다.

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print(f'{name:10} ==> {phone:10d}')
Sjoerd     ==>       4127
Jack       ==>       4098
Dcab       ==>       7678
```

**변환 플래그**: 포맷 적용 이전에 값을 변환한다.

```
변환 플래그  적용 함수   용도
────────────────────────────────────────
!s          str()       사람이 읽기에 적합한 표현
!r          repr()      디버깅용 표현 (따옴표, 이스케이프 포함)
!a          ascii()     비 ASCII 문자를 이스케이프 처리
```

```python
>>> animals = 'eels'
>>> print(f'My hovercraft is full of {animals}.')
My hovercraft is full of eels.
>>> print(f'My hovercraft is full of {animals!r}.')
My hovercraft is full of 'eels'.
```

**`=` 지정자**: 표현식 텍스트와 평가 결과를 함께 출력한다. 디버깅 시 유용하다. (Python 3.8+)

```python
>>> bugs = 'roaches'
>>> count = 13
>>> area = 'living room'
>>> print(f'Debugging {bugs=} {count=} {area=}')
Debugging bugs='roaches' count=13 area='living room'
```

---

### 4-2. str.format() 메서드

`str.format()`은 중괄호 `{}`를 자리 표시자로 사용한다. f-문자열보다 명시적 인자 전달이 필요하지만 동적인 템플릿 구성에 유용하다.

**위치 인자:**

```python
>>> print('We are the {} who say "{}!"'.format('knights', 'Ni'))
We are the knights who say "Ni!"

>>> print('{0} and {1}'.format('spam', 'eggs'))
spam and eggs
>>> print('{1} and {0}'.format('spam', 'eggs'))   # 순서 역전 가능
eggs and spam
```

**키워드 인자:**

```python
>>> print('This {food} is {adjective}.'.format(
...       food='spam', adjective='absolutely horrible'))
This spam is absolutely horrible.
```

**딕셔너리를 `**` 언패킹으로 전달:**

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
>>> print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))
Jack: 4098; Sjoerd: 4127; Dcab: 8637678
```

**열 정렬 예시:**

```python
>>> for x in range(1, 11):
...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
 1   1    1
 2   4    8
 3   9   27
...
10 100 1000
```

---

### 4-3. 수동 문자열 포매팅

`str.rjust()`, `str.ljust()`, `str.center()`는 주어진 폭으로 문자열을 정렬한 새 문자열을 반환한다. 원본을 수정하지 않으며, 입력 문자열이 지정 폭보다 길면 잘라내지 않고 그대로 반환한다.

```python
>>> for x in range(1, 11):
...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
...     print(repr(x*x*x).rjust(4))
 1   1    1
 2   4    8
...
10 100 1000
```

`str.zfill(width)`: 숫자 문자열의 왼쪽을 `0`으로 채운다. 부호(+, -)를 인식한다.

```python
>>> '12'.zfill(5)
'00012'
>>> '-3.14'.zfill(7)
'-003.14'
>>> '3.14159265359'.zfill(5)
'3.14159265359'   # 지정 폭보다 길면 그대로 반환
```

---

### 4-4. % 연산자 (레거시 방식)

`%` 연산자는 C언어의 `printf` 스타일 포매팅을 제공한다. 공식 문서는 이 방식을 **레거시**로 분류하며 f-문자열 또는 `str.format()` 사용을 권장한다.

```python
>>> import math
>>> print('The value of pi is approximately %5.3f.' % math.pi)
The value of pi is approximately 3.142.
```

---

## 5. 구현 코드 및 상세 설명

### 5-1. 파일 읽고 쓰기

`open()` 함수는 파일 객체를 반환한다. 기본 호출 형식은 다음과 같다.

```
open(filename, mode, encoding=None)
```

**`mode` 인자 정의:**

```
mode   의미
────────────────────────────────────────────────────
'r'    읽기 전용 (기본값, 생략 가능)
'w'    쓰기 전용 (기존 파일 내용 삭제 후 새로 씀)
'a'    덧붙이기 (기존 파일 끝에 추가)
'r+'   읽기 + 쓰기
'b'    바이너리 모드 (다른 mode와 조합: 'rb', 'wb' 등)
```

**인코딩 지정**: 공식 문서는 `encoding="utf-8"` 명시를 권장한다. `encoding`을 지정하지 않으면 플랫폼 의존적 기본값이 사용된다.

```python
>>> f = open('workfile', 'w', encoding="utf-8")
```

---

### 5-2. with 문을 사용한 파일 처리

공식 문서는 파일 객체 처리 시 `with` 키워드 사용을 **명시적으로 권장**한다.

> 파일 객체를 다룰 때 `with` 키워드를 사용하는 것은 좋은 습관입니다. 혜택은 도중 예외가 발생하더라도 스위트가 종료될 때 파일이 올바르게 닫힌다는 것입니다.

```python
>>> with open('workfile', encoding="utf-8") as f:
...     read_data = f.read()

>>> f.closed
True    # with 블록 종료 후 자동으로 닫힘
```

`with`를 사용하지 않으면 `f.close()`를 명시적으로 호출해야 한다. 닫지 않은 채 `f.write()`를 호출하면 데이터가 디스크에 완전히 기록되지 않을 수 있다.

```
with문 vs 수동 close():

with open(...) as f:        f = open(...)
    f.write(...)            try:
                                f.write(...)
# 자동으로 닫힘              finally:
                                f.close()
```

닫힌 파일 객체에 대한 접근은 `ValueError`를 유발한다.

```python
>>> f.close()
>>> f.read()
ValueError: I/O operation on closed file.
```

---

### 5-3. 파일 객체의 주요 메서드

**`f.read(size)`**: 파일 내용을 읽어 문자열(텍스트 모드) 또는 바이트열(바이너리 모드)로 반환한다. `size` 생략 시 전체 내용을 읽는다. 파일 끝에 도달하면 빈 문자열 `''`을 반환한다.

```python
>>> f.read()
'This is the entire file.\n'
>>> f.read()
''             # 파일 끝 → 빈 문자열 반환
```

**`f.readline()`**: 한 줄을 읽는다. 개행 문자 `\n`은 결과에 보존된다. 반환값이 빈 문자열 `''`이면 파일 끝, `'\n'`이면 빈 줄이다.

```python
>>> f.readline()
'This is the first line of the file.\n'
>>> f.readline()
'Second line of the file\n'
>>> f.readline()
''             # 파일 끝
```

**`for` 루프를 이용한 줄 순회**: 공식 문서가 명시하는 가장 메모리 효율적인 방법이다.

```python
>>> for line in f:
...     print(line, end='')
This is the first line of the file.
Second line of the file
```

`f.readlines()` 또는 `list(f)`로 전체 줄을 리스트로 읽을 수도 있으나, 대용량 파일에서는 메모리 효율이 떨어진다.

**`f.write(string)`**: 문자열을 파일에 쓰고 출력된 문자 수를 반환한다. 문자열이 아닌 객체는 사전에 변환해야 한다.

```python
>>> f.write('This is a test\n')
15

>>> value = ('the answer', 42)
>>> s = str(value)       # 튜플을 문자열로 변환
>>> f.write(s)
18
```

**`f.tell()`**: 파일의 현재 위치를 반환한다. 바이너리 모드에서는 파일 처음부터의 바이트 수, 텍스트 모드에서는 불투명한 정수값이다.

**`f.seek(offset, whence)`**: 파일 위치를 변경한다.

```
whence 값   기준점
─────────────────────────────
0 (기본값)   파일의 처음
1            현재 위치
2            파일의 끝
```

```python
>>> f = open('workfile', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)          # 6번째 바이트로 이동
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2)      # 파일 끝에서 3바이트 앞으로
13
>>> f.read(1)
b'd'
```

텍스트 모드에서 `seek()`는 `tell()`이 반환한 값이나 `seek(0)` (파일 처음) 또는 `seek(0, 2)` (파일 끝)만 허용된다.

---

### 5-4. JSON으로 구조적 데이터 저장

공식 문서는 복잡한 자료 구조의 파일 저장을 위해 `json` 모듈 사용을 권장한다.

```python
import json

# 직렬화: Python 객체 → JSON 문자열
>>> json.dumps([1, 'simple', 'list'])
'[1, "simple", "list"]'

# 파일에 쓰기
>>> with open('data.json', 'w', encoding='utf-8') as f:
...     json.dump([1, 'simple', 'list'], f)

# 파일에서 읽기 (역직렬화)
>>> with open('data.json', encoding='utf-8') as f:
...     data = json.load(f)
>>> data
[1, 'simple', 'list']
```

```
JSON 직렬화 대응 관계:

Python 타입     JSON 타입
─────────────────────────
dict            object {}
list, tuple     array []
str             string ""
int, float      number
True / False    true / false
None            null
```

JSON은 텍스트 기반의 언어 독립적 포맷이므로, 다른 언어나 플랫폼과의 데이터 교환에 적합하다. 단, 임의의 Python 클래스 인스턴스는 기본적으로 직렬화할 수 없다.

---

### 5-5. 사용자 입력 — input()

`input([prompt])` 함수는 표준 입력으로부터 한 줄을 읽어 **문자열**로 반환한다. 반환값은 항상 `str` 타입이다.

```python
>>> name = input('Enter your name: ')
Enter your name: 정민
>>> name
'정민'

>>> age = input('Enter your age: ')
Enter your age: 25
>>> type(age)
<class 'str'>          # 숫자를 입력해도 문자열로 반환됨
>>> age = int(age)     # 정수로 사용하려면 명시적 형변환 필요
```

```
input() 처리 흐름:

사용자 입력: "25"
      ↓
input() 반환값: "25"  (항상 str)
      ↓
int("25") = 25        (숫자로 사용하려면 형변환 필요)
```

코딩테스트 환경에서 대량 입력 처리 시 `input()`은 성능상 불리할 수 있다. 이 경우 `sys.stdin.readline`을 `input`으로 재할당하여 사용한다.

```python
import sys
input = sys.stdin.readline   # 이후 input() 호출이 모두 readline으로 처리됨
```

`sys.stdin.readline`은 개행 문자 `'\n'`을 포함하여 반환하므로, 필요 시 `.strip()`으로 제거해야 한다.

---

## 6. 핵심 요약 및 주의점

**출력 포매팅 방법 선택 기준**

```
상황                                      권장 방법
─────────────────────────────────────────────────────────
일반적인 변수 삽입 및 포매팅               f-문자열 (f-string)
동적 템플릿 / 외부 포맷 문자열 필요        str.format()
레거시 코드 유지보수                       % 연산자 (신규 작성 비권장)
디버깅 시 변수명과 값 동시 출력            f'{var=}' (Python 3.8+)
```

**파일 처리 주의점**

```
상황                                  올바른 방법                  잘못된 방법
────────────────────────────────────────────────────────────────────────────────
파일 자동 닫기                         with open(...) as f:         f.close() 수동 호출
                                                                    (예외 시 누락 가능)
대용량 파일 줄 순회                    for line in f:               f.readlines() → 전체 메모리 적재
비 ASCII 문자 포함 파일                encoding="utf-8" 명시         인코딩 생략 → 플랫폼 의존적 동작
바이너리 파일 처리                     open(..., 'rb') or 'wb'      텍스트 모드로 열기 → 데이터 손상
```

**`input()` 주의점**

- 반환값은 항상 `str`이다. 정수·실수로 사용하려면 `int()`, `float()` 형변환이 필요하다.
- `sys.stdin.readline` 사용 시 반환값에 개행 문자 `'\n'`이 포함된다. `.strip()`으로 제거해야 한다.

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "입출력",
  "source_type": "docs",
  "style": [
    "theory",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```