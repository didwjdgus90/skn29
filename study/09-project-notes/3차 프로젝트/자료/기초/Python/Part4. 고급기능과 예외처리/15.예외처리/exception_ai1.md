# 제목
[Python 기초] 예외 처리 (Exception Handling)

# 본문
프로그램 실행 중 발생하는 오류(예외)를 처리하는 구문이다.
예외를 처리하지 않으면 프로그램이 강제 종료된다.

try-except 구조로 예외를 잡아서 적절히 처리하면 프로그램이 비정상 종료되는 것을 막을 수 있다.
예외도 객체이므로 사용자가 직접 클래스로 정의할 수 있다.

## 주요 내장 예외 종류

| 예외 | 발생 상황 |
|------|-----------|
| ValueError | 잘못된 값 (int("abc")) |
| TypeError | 잘못된 타입 ("1" + 1) |
| IndexError | 인덱스 범위 초과 |
| KeyError | 딕셔너리에 없는 키 |
| ZeroDivisionError | 0으로 나누기 |
| FileNotFoundError | 파일 없음 |
| AttributeError | 없는 속성/메서드 접근 |
| NameError | 정의 안 된 변수 사용 |

## try-except-else-finally 구조

try: 오류가 날 수 있는 코드를 넣는다.
except: 특정 예외가 발생했을 때 처리 코드를 넣는다.
else: 예외 없이 try가 완료됐을 때 실행된다.
finally: 예외 여부와 관계없이 항상 실행된다. (자원 정리에 사용)

<IMAGE>try-except-else-finally 실행 흐름도 그림</IMAGE>

## raise와 사용자 정의 예외

raise로 직접 예외를 발생시킬 수 있다.
Exception을 상속받아 사용자 정의 예외 클래스를 만들 수 있다.
사용자 정의 예외는 예외 종류를 명확히 표현할 때 유용하다.

## 수도코드(Pseudocode)

```
예외처리(코드):
    try:
        위험한 코드 실행
    except 예외타입 as e:
        예외 처리
    else:
        정상 실행 후 처리
    finally:
        항상 실행 (파일 닫기, 연결 해제 등)
```

## 구현 코드 (Python)

```python
# 기본 try-except
try:
    x = int(input("숫자: "))
    result = 10 / x
    print(f"결과: {result}")
except ValueError:
    print("숫자를 입력하세요!")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다!")
except Exception as e:
    print(f"예상치 못한 오류: {type(e).__name__}: {e}")
else:
    print("정상 처리 완료")
finally:
    print("항상 실행됨")

# 여러 예외 한 번에 처리
try:
    pass
except (ValueError, TypeError) as e:
    print(f"값 또는 타입 오류: {e}")

# raise로 직접 발생
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("나누는 수는 0이 될 수 없습니다.")
    return a / b

# 사용자 정의 예외
class InsufficientFundsError(Exception):
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"잔액 부족: 잔액 {balance}원, 필요 {amount}원"
        )

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(amount, self.balance)
        self.balance -= amount

try:
    acc = BankAccount(1000)
    acc.withdraw(2000)
except InsufficientFundsError as e:
    print(e)   # 잔액 부족: 잔액 1000원, 필요 2000원
```

## 실전 예제: 안전한 파일 읽기

```python
def safe_read(filepath, encoding="utf-8"):
    """파일을 안전하게 읽어 내용 반환. 실패 시 None 반환"""
    try:
        with open(filepath, "r", encoding=encoding) as f:
            return f.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없음: {filepath}")
    except PermissionError:
        print(f"파일 접근 권한 없음: {filepath}")
    except UnicodeDecodeError:
        print(f"인코딩 오류. 다른 인코딩을 시도하세요.")
    return None

content = safe_read("data.txt")
if content:
    print(content[:100])
```

# 메타데이터
```json
{
  "category": "예외처리",
  "topic": "try-except",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 4,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "intermediate",
  "language": "python"
}
```
