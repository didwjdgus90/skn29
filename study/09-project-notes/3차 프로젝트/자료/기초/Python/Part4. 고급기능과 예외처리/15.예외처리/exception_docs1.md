# 제목
[Python 기초] 에러와 예외 (Errors and Exceptions)

# 링크
https://docs.python.org/ko/3.11/tutorial/errors.html

# 본문

## 1. 한 줄 요약

파이썬의 에러는 **문법 에러(SyntaxError)** 와 **예외(Exception)** 두 가지로 구분된다. 문법 에러는 파싱 단계에서 감지되어 실행 자체가 불가능하고, 예외는 실행 중에 발생하며 `try`/`except` 구문으로 처리할 수 있다.

---

## 2. 에러의 두 가지 범주

공식 문서는 에러를 명확히 두 범주로 분류한다.

```
에러 분류:

문법 에러(SyntaxError)         예외(Exception)
──────────────────────────    ──────────────────────────────
파싱 단계에서 감지              실행 중에 발생
실행 자체 불가                  처리하지 않으면 프로그램 중단
코드 수정으로만 해결             try/except로 처리 가능
```

---

## 3. 문법 에러 (Syntax Errors)

문법 에러는 파싱 에러(parsing error)라고도 한다. 구문이 잘못되어 인터프리터가 코드를 읽는 단계에서 감지된다.

```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
               ^^^^^
SyntaxError: invalid syntax
```

파서는 오류가 감지된 위치를 화살표(`^`)로 표시한다. 오류는 표시된 토큰 *이전*에 누락된 요소(여기서는 콜론 `:`)로 인해 발생하는 경우도 있다. 파일 이름과 줄 번호도 함께 출력되어 스크립트에서 오류 위치를 특정할 수 있다.

---

## 4. 예외 (Exceptions)

문법적으로 올바른 코드라도 실행 중에 에러가 발생할 수 있다. 이를 **예외**라 부른다. 예외는 무조건 치명적이지는 않으며, 적절히 처리할 수 있다.

처리되지 않은 예외는 다음과 같이 트레이스백(traceback)을 출력한다.

```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined

>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

```
트레이스백 구조:

Traceback (most recent call last):    ← 스택 트레이스 시작
  File "<stdin>", line 1, in <module> ← 예외 발생 위치
ZeroDivisionError: division by zero   ← 예외 형(type): 상세 메시지
     ↑                                      ↑
 예외 클래스 이름                       원인 설명
```

에러 메시지의 마지막 줄이 핵심이다. `예외 형(type): 상세 메시지` 구조로, 예외 형은 발생한 내장 예외의 이름이다.

**주요 내장 예외:**

```
예외 클래스              발생 조건
─────────────────────────────────────────────────────
ZeroDivisionError       0으로 나누기
NameError               정의되지 않은 이름 참조
TypeError               타입 불일치 연산
ValueError              올바르지 않은 값
IndexError              시퀀스 인덱스 범위 초과
KeyError                딕셔너리에 없는 키 접근
FileNotFoundError       존재하지 않는 파일 열기
OSError                 OS 수준 에러 (파일, 네트워크 등)
AttributeError          존재하지 않는 어트리뷰트 참조
ImportError             모듈 임포트 실패
```

---

## 5. 예외 처리하기 (try / except)

### 5-1. 기본 구조와 실행 흐름

`try` 문은 예외를 처리하는 기본 구조다. 공식 문서의 실행 순서 정의는 다음과 같다.

1. `try` 절(`try`와 `except` 사이)이 먼저 실행된다.
2. 예외가 발생하지 않으면 `except` 절을 건너뛰고 `try` 문이 종료된다.
3. `try` 절 실행 중 예외가 발생하면, 절의 남은 부분을 건너뛰고 `except` 키워드 뒤의 예외 이름과 매치를 시도한다.
4. 매치되면 해당 `except` 절이 실행된다.
5. 매치되지 않으면 외부 `try` 문으로 전달되며, 처리기가 없으면 *처리되지 않은 예외*로 실행이 중단된다.

```python
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops! That was no valid number. Try again...")
```

```
실행 흐름 시각화:

try:
  코드 실행
      │
      ├── 예외 없음 ──────────────────────→ except 건너뜀 → 종료
      │
      └── 예외 발생
              │
              ├── except와 일치 ──→ except 절 실행 → try 블록 이후로
              │
              └── except와 불일치 ──→ 외부 try로 전달 → 처리기 없으면 중단
```

### 5-2. 다중 except 절

하나의 `try` 문은 여러 `except` 절을 가질 수 있다. **최대 하나의 처리기만 실행**된다. 여러 예외를 하나의 `except`로 묶으려면 튜플을 사용한다.

```python
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error:", err)
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise   # 예외를 다시 일으킴
```

```python
# 여러 예외를 하나의 절로 처리
except (RuntimeError, TypeError, NameError):
    pass
```

### 5-3. 예외 클래스의 상속 관계와 매칭

`except` 절의 예외 클래스는 **해당 클래스이거나 그 베이스 클래스(부모 클래스)인 예외와 호환**된다. 반대 방향은 성립하지 않는다.

```python
class B(Exception): pass
class C(B): pass
class D(C): pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")

# 출력: B, C, D
# except 절 순서가 역전되면 (except B가 먼저) → B, B, B 출력
```

`except B`가 먼저 위치하면 `C`, `D`도 `B`의 서브클래스이므로 모두 `B` 절에서 처리된다. **구체적인 예외를 먼저, 일반적인 예외를 나중에** 배치해야 한다.

### 5-4. as 절로 예외 인스턴스 접근

`except 예외형 as 변수` 형식으로 예외 인스턴스를 변수에 바인딩할 수 있다. 예외 인스턴스는 `args` 어트리뷰트에 인자를 저장한다.

```python
>>> try:
...     raise Exception('spam', 'eggs')
... except Exception as inst:
...     print(type(inst))     # <class 'Exception'>
...     print(inst.args)      # ('spam', 'eggs')
...     print(inst)           # ('spam', 'eggs')
...     x, y = inst.args
...     print('x =', x)       # x = spam
...     print('y =', y)       # y = eggs
```

### 5-5. else 절

`else` 절은 `try` 절이 **예외 없이 완료**되었을 때 실행된다. 모든 `except` 절 뒤에 위치해야 한다.

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

공식 문서의 설명:

> `else` 절의 사용이 `try` 절에 코드를 추가하는 것보다 좋은데, `try...except` 문에 의해 보호되고 있는 코드가 일으키지 않은 예외를 우연히 잡게 되는 것을 방지하기 때문입니다.

```
try / except / else / finally 실행 순서:

try:        → 항상 실행
except:     → 예외 발생 시만 실행
else:       → 예외 없이 완료 시만 실행
finally:    → 항상 실행 (예외 여부 무관)
```

### 5-6. 예외 처리기의 전파 범위

예외 처리기는 `try` 절에 직접 등장한 예외뿐만 아니라, `try` 절에서 **간접적으로 호출되는 함수 내부**의 예외도 처리한다.

```python
>>> def this_fails():
...     x = 1/0
...
>>> try:
...     this_fails()
... except ZeroDivisionError as err:
...     print('Handling run-time error:', err)
...
Handling run-time error: division by zero
```

---

## 6. 예외 일으키기 (raise)

`raise` 문은 프로그래머가 명시적으로 예외를 발생시킨다. 인자는 예외 인스턴스이거나 예외 클래스(`BaseException`을 계승하는 클래스)여야 한다. 예외 클래스가 전달되면 인자 없이 생성자를 호출해 인스턴스를 생성한다.

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere

>>> raise ValueError   # raise ValueError() 와 동등
```

**예외를 잡되 처리하지 않고 다시 발생시키려면 인자 없는 `raise`를 사용한다.**

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise              # 원래 예외를 그대로 재발생
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

---

## 7. 예외 연쇄 (Exception Chaining)

`except` 블록 내에서 처리되지 않은 예외가 발생하면, 처리 중이던 예외가 새 예외에 연결되어 에러 메시지에 포함된다.

```python
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

RuntimeError: unable to handle error
```

**`raise ... from` 으로 명시적 연쇄를 표현한다.** 예외 변환 시 원인을 명확히 하는 데 유용하다.

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
ConnectionError

The above exception was the direct cause of the following exception:

RuntimeError: Failed to open database
```

**`from None`으로 자동 연쇄를 비활성화할 수 있다.** 원인 예외를 숨기고 새 예외만 표시한다.

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```

```
예외 연쇄 방식 비교:

상황                         구문                  메시지
──────────────────────────────────────────────────────────────────────
except 내에서 자연 발생       (암시적)              "During handling of..."
명시적 원인 연결              raise B from A        "The above exception was the direct cause of..."
연쇄 비활성화                 raise B from None     원인 예외 없이 B만 표시
```

---

## 8. 사용자 정의 예외 (User-defined Exceptions)

새 예외 클래스를 정의함으로써 프로그램 고유의 예외에 이름을 붙일 수 있다. 예외는 직접적으로나 간접적으로 **`Exception` 클래스를 계승**해야 한다. 관례상 이름은 `Error`로 끝난다.

```python
class InsufficientFundsError(Exception):
    """잔액 부족 시 발생하는 예외."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(
            f"잔액 {balance}원으로 {amount}원 출금 불가"
        )

try:
    raise InsufficientFundsError(1000, 5000)
except InsufficientFundsError as e:
    print(e)            # 잔액 1000원으로 5000원 출금 불가
    print(e.balance)    # 1000
    print(e.amount)     # 5000
```

공식 문서의 지침:

> 예외 클래스는 보통 간단하게 유지합니다. 종종 예외 처리기가 에러에 관한 정보를 추출할 수 있도록 하기 위한 몇 가지 어트리뷰트들을 제공하기만 합니다.

---

## 9. finally 절 — 뒷정리 동작

`finally` 절은 `try` 문 완료 전에 **항상** 실행된다. 예외 발생 여부와 무관하다.

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")   # 항상 실행

>>> divide(2, 1)
result is 2.0
executing finally clause

>>> divide(2, 0)
division by zero!
executing finally clause

>>> divide("2", "1")
executing finally clause           # finally 먼저 실행
TypeError: unsupported operand type(s) for /: 'str' and 'str'  # 이후 재발생
```

**`finally` 절의 실행 규칙 (공식 문서):**

- `try` 절 실행 중 예외 발생 → `except`에서 처리되지 않으면 `finally` 실행 후 예외 재발생
- `except` 또는 `else` 실행 중 예외 발생 → `finally` 실행 후 예외 재발생
- `finally`에서 `break`, `continue`, `return` 실행 → 예외가 재발생하지 않음
- `try` 절이 `break`, `continue`, `return`에 도달 → 그 직전에 `finally` 실행
- `finally`에 `return`이 있으면 → `try`의 `return` 값을 **대체**함

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False   # try의 return True를 대체
...
>>> bool_return()
False
```

**실용적 관점**: `finally`는 파일, 네트워크 연결 등 외부 자원을 성공 여부와 무관하게 반납하는 데 사용된다.

---

## 10. with 문 — 미리 정의된 뒷정리 동작

`with` 문은 컨텍스트 관리자 프로토콜(`__enter__`, `__exit__`)을 구현한 객체에 대해 자동으로 뒷정리를 수행한다. 파일 처리가 대표적 사례다.

```python
# with 없이 — 예외 발생 시 파일이 닫히지 않을 수 있음
for line in open("myfile.txt"):
    print(line, end="")

# with 사용 — 예외 발생 여부와 무관하게 파일이 항상 닫힘
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

`with` 문은 동등한 `try...finally` 블록보다 간결하며, 예외가 발생하더라도 블록 종료 시 파일이 올바르게 닫힘을 보장한다.

---

## 11. 복수 예외 처리 — ExceptionGroup (Python 3.11+)

Python 3.11부터 여러 관련 없는 예외를 하나로 묶어 발생시킬 수 있다. `ExceptionGroup`은 예외 인스턴스의 리스트를 래핑한다.

```python
>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
```

`except*` 구문으로 그룹 내 특정 타입의 예외만 선택적으로 처리한다. 매칭되지 않은 예외는 다른 절로 전파된다.

```python
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
```

> `ExceptionGroup`에 중첩된 예외들은 타입이 아닌 **인스턴스**여야 한다. 이미 발생하고 처리된 예외들을 수집하는 패턴이 일반적이다.

---

## 12. 예외에 노트 추가 — add_note() (Python 3.11+)

예외를 잡은 후 추가 정보를 첨부할 수 있다. `add_note(str)` 메서드는 예외의 노트 리스트에 문자열을 추가하며, 트레이스백 출력 시 추가된 순서대로 표시된다.

```python
>>> try:
...     raise TypeError('bad type')
... except Exception as e:
...     e.add_note('Add some information')
...     e.add_note('Add some more information')
...     raise
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: bad type
Add some information
Add some more information
```

`ExceptionGroup`과 함께 사용 시 각 예외에 발생 맥락 정보를 첨부하는 데 유용하다.

---

## 13. 예외 계층 구조

공식 문서에 따르면 `BaseException`이 모든 예외의 공통 베이스 클래스다.

```
BaseException
  ├─ SystemExit              ← sys.exit() 호출 시
  ├─ KeyboardInterrupt       ← 사용자 인터럽트 (Ctrl+C)
  ├─ GeneratorExit
  └─ Exception               ← 비치명적 예외의 베이스 클래스
       ├─ ArithmeticError
       │    └─ ZeroDivisionError
       ├─ LookupError
       │    ├─ IndexError
       │    └─ KeyError
       ├─ ValueError
       ├─ TypeError
       ├─ OSError
       │    └─ FileNotFoundError
       ├─ NameError
       ├─ AttributeError
       └─ ...
```

`SystemExit`, `KeyboardInterrupt`는 `Exception`의 서브클래스가 아니므로, `except Exception`으로는 잡히지 않는다. 이는 의도된 설계로, 이 예외들은 **프로그램이 종료되어야 함을 나타내기 때문**이다.

---

## 14. 핵심 요약 및 주의점

**핵심 요약**

- 문법 에러는 실행 전 파싱 단계에서 감지된다. `try`/`except`로 처리할 수 없다.
- 예외는 실행 중에 발생하며 `try`/`except`/`else`/`finally` 구문으로 처리한다.
- `except` 절은 위에서 아래로 순서대로 매칭된다. **구체적인 예외를 먼저** 배치해야 한다.
- `else` 절은 `try` 절이 예외 없이 완료될 때만 실행된다.
- `finally` 절은 예외 발생 여부와 무관하게 **항상** 실행된다.
- `raise` 단독 사용으로 현재 예외를 재발생시킨다. `raise B from A`로 예외 연쇄를 명시한다.
- 사용자 정의 예외는 `Exception`을 계승하고 이름은 관례상 `Error`로 끝낸다.

**주의점**

```
상황                                올바른 방법                     잘못된 방법
──────────────────────────────────────────────────────────────────────────────────────
예외 포착 순서                      구체적 → 일반적 순서            except B 먼저 → C, D도 B로 처리됨
모든 예외 무차별 포착                가능한 한 구체적으로 지정         except Exception → 예상치 못한 예외 은폐
except 블록 내 재발생               raise (인자 없음)               raise e → 트레이스백 변경 가능
finally의 return                   주의해서 사용                    try의 return 값을 대체함
SystemExit/KeyboardInterrupt 처리   except BaseException 사용       except Exception → 잡히지 않음
```

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "예외처리",
  "source_type": "docs",
  "style": [
    "theory",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "mid",
  "language": "python"
}
```