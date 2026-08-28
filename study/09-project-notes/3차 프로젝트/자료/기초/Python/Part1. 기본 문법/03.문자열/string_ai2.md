# [Python 기초] 문자열 (String)

# 본문

## 1. 한 줄 요약

문자열은 글자를 순서대로 담은 자료형이며, 파이썬에서는 따옴표로 감싸서 표현한다.

문자열을 이해하면 이름, 문장, 입력값, 파일 경로처럼 글자로 된 데이터를 다룰 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램은 숫자만 다루지 않는다.

사용자 이름, 이메일, 비밀번호, 문장, 메뉴 이름처럼 글자 데이터도 많이 다룬다.

```text
이름: 민수
이메일: minsu@example.com
문장: Python is fun
```

이런 글자 데이터를 저장하고 처리하려면 문자열이 필요하다.

예를 들어 사용자의 이름을 출력하고 싶다면 아래처럼 쓸 수 있다.

```python
name = "민수"
print("안녕하세요, " + name + "님")
```

문자열을 사용하면 글자를 저장하고, 붙이고, 자르고, 검색할 수 있다.

코딩 테스트에서도 문자열 문제는 자주 나온다.

예를 들어 문자를 뒤집거나, 특정 문자가 몇 번 나오는지 세거나, 단어를 나누는 문제에 사용된다.

---

## 3. 핵심 아이디어

문자열은 글자들이 줄을 서 있는 모습이라고 생각하면 쉽다.

```text
"Python"

P   y   t   h   o   n
0   1   2   3   4   5
```

각 글자는 순서가 있고, 그 순서를 인덱스라고 부른다.

인덱스는 위치 번호라고 생각하면 된다.

파이썬에서는 첫 번째 글자의 인덱스가 `0`이다.

```text
문자열:  "cat"

c   a   t
0   1   2
```

문자열은 한 글자씩 꺼낼 수도 있고, 여러 글자를 잘라낼 수도 있다.

```python
word = "cat"
print(word[0])
print(word[1])
```

```text
출력
c
a
```

문자열은 글자들의 기차라고 볼 수 있다.

```text
[ P ][ y ][ t ][ h ][ o ][ n ]
  0    1    2    3    4    5
```

원하는 칸 번호를 말하면 그 위치의 글자를 꺼낼 수 있다.

---

## 4. 동작 과정 살펴보기

아래 문자열을 사용해 보자.

```python
word = "apple"
```

### Step 1. 문자열이 저장된다

```text
word ─────▶ "apple"

문자열 내부

a   p   p   l   e
0   1   2   3   4
```

`word`라는 변수는 `"apple"`이라는 문자열을 가리킨다.

문자열 안의 각 글자는 순서를 가진다.

### Step 2. 한 글자 꺼내기

```python
word[0]
```

```text
a   p   p   l   e
↑
0번 위치
```

결과는 `"a"`이다.

```python
word[3]
```

```text
a   p   p   l   e
            ↑
          3번 위치
```

결과는 `"l"`이다.

### Step 3. 여러 글자 자르기

```python
word[1:4]
```

```text
a   p   p   l   e
    └───────┘
     1  2  3

결과: "ppl"
```

`1:4`는 1번부터 4번 전까지를 의미한다.

즉, 1번, 2번, 3번 글자를 가져온다.

### Step 4. 문자열 붙이기

```python
first = "Hello"
second = "Python"

message = first + " " + second
```

```text
"Hello" + " " + "Python"
          ↓
"Hello Python"
```

`+`는 문자열끼리 붙일 때 사용할 수 있다.

---

## 5. 구현 코드 및 상세 설명

```python
text = "Python"

# 문자열 길이 확인
print(len(text))

# 인덱스로 한 글자 꺼내기
print(text[0])
print(text[1])

# 슬라이싱으로 일부 문자열 자르기
print(text[0:3])
print(text[3:6])

# 문자열 붙이기
language = "Python"
message = "I love " + language
print(message)

# 특정 글자 개수 세기
print(text.count("o"))

# 소문자로 바꾸기
print(text.lower())
```

### 코드 설명

```python
text = "Python"
```

`text` 변수에 문자열 `"Python"`을 저장한다.

문자열은 따옴표로 감싸야 한다.

```python
len(text)
```

문자열의 길이를 구한다.

```text
P   y   t   h   o   n
1   2   3   4   5   6

길이: 6
```

```python
text[0]
```

0번 위치의 글자를 꺼낸다.

```text
P   y   t   h   o   n
↑
0번
```

결과는 `"P"`이다.

```python
text[0:3]
```

0번부터 3번 전까지 자른다.

```text
P   y   t   h   o   n
└───────┘
 0  1  2

결과: "Pyt"
```

```python
message = "I love " + language
```

문자열 두 개를 이어 붙인다.

중간에 공백이 필요하면 `" "`처럼 공백 문자열을 직접 넣어야 한다.

```python
text.count("o")
```

문자열 안에서 `"o"`가 몇 번 등장하는지 센다.

```python
text.lower()
```

문자열을 모두 소문자로 바꾼다.

---

## 6. 마지막 정리

문자열은 글자들이 순서대로 모인 자료형이다.

파이썬 문자열은 작은따옴표나 큰따옴표로 감싸서 만든다.

인덱스는 0부터 시작한다.

`문자열[시작:끝]`은 시작 위치부터 끝 위치 전까지 자른다.

문자열은 붙이기, 길이 확인, 개수 세기, 대소문자 변경 같은 작업에 자주 사용된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 문자열",
  "source_type": "generated",
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
