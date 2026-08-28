# 제목
[Python 기초] 문자열 자료형 (String Type)

# 링크
<https://wikidocs.net/13>

# 본문
문자, 단어 등으로 구성된 문자들의 집합이다.
파이썬의 문자열은 불변(immutable)이어서 한 번 만들면 내부를 수정할 수 없다.
수정이 필요하면 새로운 문자열을 만들어야 한다.

문자열은 큰따옴표, 작은따옴표, 삼중따옴표로 만들 수 있다.

## 문자열 만들기

| 방법 | 예시 | 특징 |
|------|------|------|
| 큰따옴표 | "Hello" | 기본 |
| 작은따옴표 | 'Hello' | 기본 |
| 삼중 큰따옴표 | """여러 줄""" | 줄바꿈 포함 가능 |
| 삼중 작은따옴표 | '''여러 줄''' | 줄바꿈 포함 가능 |

## 인덱싱과 슬라이싱

문자열의 각 문자는 인덱스로 접근할 수 있다.
양수 인덱스는 왼쪽부터, 음수 인덱스는 오른쪽부터 센다.

<IMAGE>문자열 인덱스 번호 설명 그림</IMAGE>

슬라이싱은 `[시작:끝:간격]` 형식으로 부분 문자열을 추출한다.
끝 인덱스는 결과에 포함되지 않는다.

## 포매팅 방식 3가지

오래된 순서대로 % 포맷 → format() 메서드 → f-string 순서로 발전했다.
현재는 f-string이 가장 현대적이고 권장되는 방식이다.

<IMAGE>파이썬 버전별 문자열 포맷 방법 비교 그림</IMAGE>

## 이스케이프 코드

| 코드 | 설명 |
|------|------|
| \n | 줄바꿈 |
| \t | 탭 |
| \\ | 백슬래시 |
| \' | 작은따옴표 |
| \" | 큰따옴표 |

## 수도코드(Pseudocode)

```
문자열_슬라이싱(s, start, end, step):
    start 생략 시 → 0
    end 생략 시   → len(s)
    step 생략 시  → 1
    step이 음수면 → 역방향 탐색
    반환: s[start:end:step]
```

## 구현 코드 (Python)

```python
# 문자열 생성
a = "Hello World"
b = 'Python is fun'
c = """여러 줄
문자열"""

# 인덱싱
s = "Python"
print(s[0])    # 'P'
print(s[-1])   # 'n'  (맨 뒤)

# 슬라이싱
print(s[0:3])   # 'Pyt'
print(s[::2])   # 'Pto'
print(s[::-1])  # 'nohtyP'  역순

# 연산
print("Hello" + " World")   # "Hello World"
print("Hi" * 3)              # "HiHiHi"
print(len("Hello"))          # 5

# f-string (권장)
name = "홍길동"
age = 30
print(f"이름: {name}, 나이: {age}")     # 이름: 홍길동, 나이: 30
print(f"점수: {95.678:.2f}")            # 점수: 95.68
print(f"{'hello':>10}")                 # "     hello"

# 자주 쓰는 메서드
s = "  hello, Python!  "
print(s.strip())                        # "hello, Python!"
print(s.upper())                        # "  HELLO, PYTHON!  "
print(s.replace("Python", "World"))     # "  hello, World!  "
print("a,b,c".split(","))              # ['a', 'b', 'c']
print("-".join(["a","b","c"]))         # "a-b-c"
print("hello".startswith("he"))        # True
print("l" in "hello")                  # True
print("hello".count("l"))              # 2
print("hello".find("l"))               # 2  (-1이면 없음)
```

## 실전 예제: 문자열 뒤집기 & 회문 판별

```python
def is_palindrome(s):
    """회문(앞뒤가 같은 문자열) 판별"""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))        # True
print(is_palindrome("Hello"))          # False
print(is_palindrome("A man a plan"))   # False
```

# 메타데이터
```json
{
  "category": "자료형",
  "topic": "문자열",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "beginner",
  "language": "python"
}
```
