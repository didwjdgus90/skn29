# 제목
[Python 기초] 정규 표현식 (Regular Expression)

# 본문
문자열에서 특정 패턴을 찾거나 치환하는 강력한 도구다.
전화번호, 이메일, URL, 날짜 등 형식이 정해진 문자열을 검색/검증할 때 활용한다.

파이썬은 `re` 모듈로 정규표현식을 지원한다.
패턴 앞에 `r` 을 붙여 raw string으로 쓰면 백슬래시 이스케이프 문제를 피할 수 있다.

## 기본 패턴 문자

| 패턴 | 의미 | 예시 |
|------|------|------|
| . | 임의의 문자 1개 | a.c → abc, aXc |
| * | 앞 문자 0회 이상 | ab* → a, ab, abb |
| + | 앞 문자 1회 이상 | ab+ → ab, abb |
| ? | 앞 문자 0~1회 | ab? → a, ab |
| ^ | 문자열 시작 | ^Hello |
| $ | 문자열 끝 | world$ |
| {n} | 정확히 n회 | a{3} → aaa |
| {n,m} | n~m회 | a{2,4} |
| \d | 숫자 [0-9] | \d+ → 하나 이상의 숫자 |
| \w | 단어문자 [a-zA-Z0-9_] | \w+ |
| \s | 공백 문자 | \s+ |
| [abc] | a, b, c 중 하나 | [aeiou] → 모음 |
| [^abc] | a, b, c 제외 | [^0-9] → 숫자 아닌 것 |

## re 모듈 주요 함수

| 함수 | 설명 | 반환 |
|------|------|------|
| re.match() | 문자열 시작부터 매칭 | Match 객체 또는 None |
| re.search() | 전체에서 첫 번째 매칭 | Match 객체 또는 None |
| re.findall() | 모든 매칭 찾기 | 문자열 리스트 |
| re.finditer() | 모든 매칭 이터레이터 | Match 이터레이터 |
| re.sub() | 매칭 부분 치환 | 새 문자열 |
| re.split() | 패턴으로 분리 | 문자열 리스트 |

<IMAGE>match vs search 차이 설명 그림</IMAGE>

## match vs search 차이

match는 문자열 처음부터 패턴이 맞아야 하고,
search는 문자열 어디서든 패턴을 찾는다.
대부분의 경우 search를 더 많이 사용한다.

## 수도코드(Pseudocode)

```
정규표현식_탐색(pattern, text):
    compiled = re.compile(pattern)   ← 패턴 컴파일 (반복 사용 시 성능 향상)
    match = compiled.search(text)
    if match:
        print(match.group())         ← 매칭된 문자열
        print(match.start(), match.end())  ← 위치
```

## 구현 코드 (Python)

```python
import re

text = "Python 3.11이 2023년 1월에 출시되었습니다."

# search: 전체에서 첫 번째 매칭
m = re.search(r"\d+\.\d+", text)
print(m.group())    # "3.11"
print(m.start())    # 7

# findall: 모든 매칭
nums = re.findall(r"\d+", text)
print(nums)   # ['3', '11', '2023', '1']

# sub: 치환
result = re.sub(r"\d+", "N", text)
print(result)   # "Python N.N이 N년 N월에 출시되었습니다."

# split: 분리
parts = re.split(r"\s+", "hello   world   python")
print(parts)   # ['hello', 'world', 'python']

# 그룹 캡처 ()
pattern = r"(\d{4})-(\d{2})-(\d{2})"
m = re.search(pattern, "날짜: 2024-01-15")
if m:
    print(m.group(0))   # "2024-01-15"
    print(m.group(1))   # "2024"
    print(m.group(2))   # "01"

# 이름 있는 그룹
pattern = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
m = re.search(pattern, "2024-01-15")
print(m.group("year"))    # "2024"
print(m.groupdict())      # {'year':'2024', 'month':'01', 'day':'15'}

# 컴파일 (반복 사용 시 성능 향상)
compiled = re.compile(r"\d+")
print(compiled.findall("abc123def456"))   # ['123', '456']
```

## 실전 예제: 이메일 / 전화번호 유효성 검사

```python
import re

def validate_email(email):
    """이메일 유효성 검사"""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))

def validate_phone(phone):
    """한국 휴대폰 번호 유효성 검사"""
    pattern = r"^01[016789]-?\d{3,4}-?\d{4}$"
    return bool(re.match(pattern, phone))

# 테스트
emails = ["user@example.com", "invalid@", "test.user@mail.co.kr"]
for e in emails:
    print(f"{e}: {validate_email(e)}")

phones = ["010-1234-5678", "01012345678", "02-1234-5678"]
for p in phones:
    print(f"{p}: {validate_phone(p)}")
```

# 메타데이터
```json
{
  "category": "문자열처리",
  "topic": "정규표현식",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 2,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "intermediate",
  "language": "python"
}
```
