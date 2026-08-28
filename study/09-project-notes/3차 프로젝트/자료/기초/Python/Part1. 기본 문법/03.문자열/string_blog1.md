# [Python 기초] 문자열 처리 (String)

---

# 링크
<https://ctkim.tistory.com/entry/Python-%EC%9E%85%EB%AC%B8-%EA%B0%95%EC%A2%8C-10-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%AC%B8%EC%9E%90%EC%97%B4-%EC%9D%B8%EB%8D%B1%EC%8B%B1%EA%B3%BC-%EC%8A%AC%EB%9D%BC%EC%9D%B4%EC%8B%B1>

---

## 1. 한 줄 요약

문자열은 **글자들이 순서대로 나열된 자료형**이다. 리스트처럼 인덱스로 글자를 꺼내거나 범위를 잘라낼 수 있고, 다양한 메서드로 검색·변환·분리 등 텍스트를 자유롭게 가공할 수 있다.

---

## 2. 문자열은 "글자들의 줄"이다

문자열(String)을 이해하는 가장 좋은 방법은 **글자 하나하나가 번호를 가진 칸에 들어있는 줄**로 상상하는 것이다.

`"Hello"` 라는 문자열은 이렇게 생겼다.

```
문자열:   H    e    l    l    o
인덱스:   0    1    2    3    4
음수:    -5   -4   -3   -2   -1
```

각 글자가 칸 번호(인덱스)를 갖고 있고, 번호를 알면 그 글자를 바로 꺼낼 수 있다. 이 구조를 이해하면 인덱싱과 슬라이싱이 자연스럽게 이해된다.

중요한 특징이 하나 있다. **문자열은 한 번 만들면 내용을 바꿀 수 없다.** 리스트는 `lst[0] = "x"`처럼 특정 위치를 바꿀 수 있지만, 문자열은 그렇게 하면 에러가 난다. 수정이 필요하면 원하는 형태의 새 문자열을 만들어야 한다.

```python
s = "Hello"
s[0] = "J"   # ❌ TypeError: 'str' object does not support item assignment
```

---

## 3. 문자열 연산 — 문자열도 더하고 곱할 수 있다

### 3-1. `+` 로 이어붙이기

두 문자열을 `+`로 연결하면 하나로 합쳐진 새 문자열이 만들어진다. 마치 레고 블록처럼 이어 붙이는 것이다.

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)   # Hello World
```

주의할 점은 문자열끼리만 이어붙일 수 있다는 것이다. 문자열과 숫자를 `+`로 연결하면 에러가 난다. 숫자를 함께 쓰려면 `str()`로 문자열로 먼저 바꿔야 한다.

```python
name = "정민"
age = 25

print("이름: " + name)           # ✅ 이름: 정민
print("나이: " + age)            # ❌ TypeError: 문자열 + 숫자 불가
print("나이: " + str(age))       # ✅ 나이: 25
print(f"나이: {age}")            # ✅ 나이: 25  ← f-string이 더 편리
```

### 3-2. `*` 로 반복하기

문자열에 정수를 곱하면 그 문자열이 지정된 횟수만큼 반복된 새 문자열이 만들어진다.

```python
s = "Hi! "
print(s * 3)   # Hi! Hi! Hi!

# 구분선 만들 때 자주 쓰임
print("-" * 20)   # --------------------
```

### 3-3. `in` 으로 포함 여부 확인하기

문자열 안에 특정 문자나 단어가 들어있는지 확인할 때 `in`을 쓴다. 결과는 `True` 또는 `False`로 반환된다.

```python
s = "Hello World"

print("World" in s)    # True  — "World"가 포함됨
print("Python" in s)   # False — "Python"은 없음
print("hello" in s)    # False — 대소문자 구분! "hello"와 "Hello"는 다름
```

`in`은 조건문과 함께 자주 쓰인다.

```python
email = "user@example.com"
if "@" in email:
    print("유효한 이메일 형식입니다.")
```

---

## 4. 인덱싱 — 원하는 글자 한 개 꺼내기

인덱싱은 문자열에서 **특정 위치의 글자 하나**를 꺼내는 방법이다. 대괄호 `[ ]` 안에 번호를 넣으면 된다.

```
s = "Hello World"

 H  e  l  l  o     W  o  r  l  d
 0  1  2  3  4  5  6  7  8  9  10   ← 앞에서부터
-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1   ← 뒤에서부터
```

```python
s = "Hello World"

print(s[0])    # H  — 첫 번째 글자
print(s[6])    # W  — 7번째 글자 (0부터 세니까)
print(s[-1])   # d  — 마지막 글자
print(s[-5])   # W  — 뒤에서 5번째 글자
```

**음수 인덱스**는 뒤에서부터 센다. `-1`이 마지막 글자, `-2`가 뒤에서 두 번째 글자다. 문자열의 마지막 글자를 꺼낼 때 길이를 몰라도 항상 `s[-1]`로 꺼낼 수 있어서 매우 유용하다.

```python
filename = "report_2024.pdf"
print(filename[-3:])   # pdf — 확장자 꺼내기 (슬라이싱과 함께 활용)
```

> ⚠️ 인덱스 범위를 벗어나면 `IndexError`가 난다. `s = "Hi"`일 때 `s[10]`을 쓰면 에러다.

---

## 5. 슬라이싱 — 원하는 범위 잘라내기

슬라이싱은 문자열의 **일부 범위를 잘라서** 새 문자열로 꺼내는 방법이다. `[시작:끝:간격]` 형식으로 쓴다.

```
s[start : end : step]
  시작     끝    간격
         (미포함)  (생략하면 1)
```

**end는 해당 인덱스를 포함하지 않는다.** `s[0:3]`이면 0, 1, 2번 글자만 가져오고 3번 글자는 포함되지 않는다. 처음 배울 때 가장 많이 실수하는 부분이니 꼭 기억하자.

```python
s = "Hello World"
#    0123456789...

print(s[0:5])    # Hello  — 0번부터 4번까지 (5번 미포함)
print(s[6:11])   # World  — 6번부터 10번까지
print(s[6:])     # World  — 6번부터 끝까지 (끝 생략 가능)
print(s[:5])     # Hello  — 처음부터 4번까지 (시작 생략 가능)
print(s[:])      # Hello World  — 전체 복사
```

```
s[0:5] 동작 시각화:

 H  e  l  l  o     W  o  r  l  d
 0  1  2  3  4  5  6  7  8  9  10
 ↑              ↑
start=0       end=5 (미포함)

결과: "Hello"
```

`step`으로 건너뛰는 간격을 지정할 수 있다.

```python
s = "Hello World"

print(s[::2])    # HloWrd  — 2칸씩 건너뛰며
print(s[::-1])   # dlroW olleH  — 문자열 뒤집기! (step이 음수면 역방향)
```

`s[::-1]`은 문자열을 뒤집는 파이썬의 관용적인 표현이다. 팰린드롬(앞뒤가 같은 문자열) 검사 같은 문제에 자주 쓰인다.

```python
word = "racecar"
if word == word[::-1]:
    print("팰린드롬입니다!")   # 팰린드롬입니다!
```

---

## 6. 자주 쓰는 문자열 메서드

메서드는 문자열에 점(`.`)을 붙여서 호출하는 기능들이다. 문자열은 수정이 불가능하기 때문에 **모든 메서드는 원본을 바꾸지 않고 새 문자열을 반환**한다.

### 6-1. 찾기 — `find()`, `count()`

`find()`는 특정 문자열이 처음 나오는 위치(인덱스)를 반환한다. 찾는 문자열이 없으면 `-1`을 반환한다. `-1`을 반환한다는 점이 중요하다. 에러가 나지 않으니 항상 결과를 확인해야 한다.

```python
s = "Hello World"

print(s.find("World"))   # 6  — "World"가 6번 인덱스에서 시작
print(s.find("Python"))  # -1 — 없으면 -1 반환 (에러 아님!)
print(s.find("l"))       # 2  — 첫 번째로 나오는 위치만 반환
```

`count()`는 특정 문자열이 몇 번 등장하는지 셀 때 쓴다.

```python
s = "banana"
print(s.count("a"))   # 3 — "a"가 세 개
print(s.count("na"))  # 2 — "na"가 두 번
```

### 6-2. 바꾸기 — `replace()`

`replace(찾을 문자열, 바꿀 문자열)`로 문자열 안의 특정 부분을 다른 내용으로 교체한다. 원본은 바뀌지 않고 바뀐 새 문자열을 반환한다.

```python
s = "Hello World"

new_s = s.replace("World", "Python")
print(new_s)   # Hello Python
print(s)       # Hello World  ← 원본은 그대로!

# 빈 문자열로 바꾸면 삭제 효과
new_s = s.replace("Hello ", "")
print(new_s)   # World
```

### 6-3. 대소문자 변환 — `upper()`, `lower()`, `capitalize()`

영어 텍스트를 다룰 때 대소문자를 통일해야 하는 경우가 자주 생긴다. 예를 들어 사용자 입력에서 "Yes", "YES", "yes"를 모두 같은 값으로 처리하고 싶을 때 유용하다.

```python
s = "Hello World"

print(s.upper())       # HELLO WORLD  — 모두 대문자
print(s.lower())       # hello world  — 모두 소문자
print(s.capitalize())  # Hello world  — 첫 글자만 대문자, 나머지 소문자

# 실용 예시: 대소문자 구분 없이 입력 처리
answer = input("계속하시겠습니까? (yes/no): ")
if answer.lower() == "yes":
    print("계속합니다.")
```

### 6-4. 공백 제거 — `strip()`, `lstrip()`, `rstrip()`

사용자가 입력하거나 파일에서 읽어온 데이터에는 앞뒤로 공백이 섞여 있는 경우가 많다. `strip()`으로 깔끔하게 제거할 수 있다.

```python
s = "   Hello World   "

print(s.strip())    # "Hello World"  — 앞뒤 공백 모두 제거
print(s.lstrip())   # "Hello World   "  — 왼쪽(앞) 공백만 제거
print(s.rstrip())   # "   Hello World"  — 오른쪽(뒤) 공백만 제거
```

### 6-5. 분리와 결합 — `split()`, `join()`

`split()`과 `join()`은 세트로 기억하면 좋다. `split()`이 문자열을 리스트로 쪼개면, `join()`은 리스트를 다시 문자열로 합친다.

**`split()`** — 구분자를 기준으로 문자열을 리스트로 분리한다.

```python
s = "apple,banana,cherry"
fruits = s.split(",")       # 쉼표를 기준으로 분리
print(fruits)               # ['apple', 'banana', 'cherry']

sentence = "Hello World Python"
words = sentence.split()    # 구분자 생략 시 공백 기준 분리
print(words)                # ['Hello', 'World', 'Python']
```

```
"apple,banana,cherry".split(",")

"apple,banana,cherry"
        ↓ 쉼표 기준으로 자르기
["apple", "banana", "cherry"]
```

**`join()`** — 리스트의 문자열들을 하나로 합친다. `"연결문자".join(리스트)` 형식으로 쓴다.

```python
fruits = ["apple", "banana", "cherry"]

print(", ".join(fruits))    # apple, banana, cherry
print(" / ".join(fruits))   # apple / banana / cherry
print("".join(fruits))      # applebananacherry  — 구분자 없이 합치기
```

`split()`과 `join()`을 함께 쓰면 문자열 가공이 매우 강력해진다.

```python
# 문장에서 공백을 언더바로 바꾸기
sentence = "Hello World Python"
result = "_".join(sentence.split())
print(result)   # Hello_World_Python
```

### 6-6. 시작·끝 확인 — `startswith()`, `endswith()`

문자열이 특정 문자열로 시작하거나 끝나는지 확인할 때 쓴다. `find()`를 써도 되지만, 이 메서드가 의도를 더 명확하게 표현한다.

```python
filename = "report_2024.pdf"

print(filename.endswith(".pdf"))     # True
print(filename.startswith("report")) # True

# 파일 확장자 확인에 자주 쓰임
if filename.endswith((".jpg", ".png")):
    print("이미지 파일입니다.")
```

### 6-7. 문자열 검사 — `isdigit()`, `isalpha()`, `isalnum()`

문자열이 어떤 문자로 이루어져 있는지 확인할 때 쓴다. 사용자 입력을 검증할 때 유용하다.

```python
print("1234".isdigit())     # True  — 모두 숫자
print("Hello".isalpha())    # True  — 모두 알파벳
print("Hello123".isalnum()) # True  — 알파벳과 숫자로만 구성
print("  ".isspace())       # True  — 모두 공백

print("Hello!".isalpha())   # False — 특수문자가 포함됨
print("12.34".isdigit())    # False — 점(.)이 포함됨
```

---

## 7. 자주 쓰는 내장 함수

문자열에 직접 붙이는 메서드 외에도, 파이썬 내장 함수로 문자열을 다룰 수 있다.

```python
s = "Hello World"

print(len(s))     # 11  — 문자열 길이 (공백 포함)
print(max(s))     # r   — 사전순으로 가장 뒤에 있는 문자
print(min(s))     # " " — 사전순으로 가장 앞 (공백이 알파벳보다 앞)

# list()로 문자열을 글자 단위 리스트로 변환
chars = list("Hello")
print(chars)      # ['H', 'e', 'l', 'l', 'o']
```

`len()`은 특히 자주 쓰인다. 슬라이싱과 조합하면 강력해진다.

```python
s = "Hello World"

# 마지막 5글자 꺼내기
print(s[-5:])          # World
print(s[len(s)-5:])    # World  — 같은 결과, 음수 인덱스가 더 간결
```

---

## 8. 종합 예제 — 이메일 주소 분석

지금까지 배운 내용을 하나의 시나리오로 합쳐보자.

```python
email = "  user.name@example.com  "

# 1. 앞뒤 공백 제거
email = email.strip()
print(email)   # user.name@example.com

# 2. @ 포함 여부 확인
if "@" not in email:
    print("유효하지 않은 이메일입니다.")
else:
    # 3. @ 위치 찾기
    at_pos = email.find("@")
    print(f"@ 위치: {at_pos}번")   # @ 위치: 9번

    # 4. 슬라이싱으로 아이디와 도메인 분리
    user_id = email[:at_pos]
    domain  = email[at_pos+1:]
    print(f"아이디: {user_id}")    # 아이디: user.name
    print(f"도메인: {domain}")     # 도메인: example.com

    # 5. 도메인이 .com으로 끝나는지 확인
    if domain.endswith(".com"):
        print("일반 도메인(.com)입니다.")

    # 6. 대문자로 변환
    print(email.upper())   # USER.NAME@EXAMPLE.COM
```

---

## 9. 마지막 정리

- 문자열은 **글자들의 줄**이다. 각 글자는 0부터 시작하는 번호(인덱스)를 갖는다.
- 문자열은 **수정 불가**하다. 바꾸고 싶으면 새 문자열을 만들어야 한다.
- **인덱싱** `s[n]`으로 글자 하나를, **슬라이싱** `s[start:end]`으로 범위를 꺼낸다. `end`는 포함되지 않는다.
- `s[::-1]`은 문자열을 **뒤집는** 관용 표현이다.
- **`split()`** 은 문자열 → 리스트로, **`join()`** 은 리스트 → 문자열로 변환한다. 이 두 메서드는 세트로 기억하자.
- 모든 메서드는 **원본을 바꾸지 않고 새 값을 반환**한다. 결과를 변수에 저장해야 한다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "문자열 처리",
  "source_type": "blog",
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