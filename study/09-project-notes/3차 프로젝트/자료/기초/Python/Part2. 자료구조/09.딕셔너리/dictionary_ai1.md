# 제목
[Python 기초] 딕셔너리 자료형 (Dictionary Type)

# 본문
Key-Value 쌍으로 데이터를 저장하는 자료형이다.
중괄호 `{}` 로 만들며, Key와 Value를 콜론 `:` 으로 구분한다.

딕셔너리의 Key는 불변 타입(str, int, tuple)만 가능하다.
Value에는 어떤 타입이든 올 수 있다.
Python 3.7 이후부터는 삽입 순서가 유지된다.

딕셔너리 탐색은 해시 테이블 기반이라 O(1)로 매우 빠르다.
이 특성 덕분에 빈도 계산, 캐싱, 매핑 등 다양한 곳에 활용된다.

## Key로 사용 가능한 타입

| 가능 | 불가능 |
|------|--------|
| str "name" | list [1,2] |
| int 42 | dict {} |
| tuple (1, 2) | set {1, 2} |
| bool True | - |

## get() vs [] 접근 차이

`d["key"]` 는 키가 없으면 KeyError가 발생한다.
`d.get("key", 기본값)` 은 키가 없으면 기본값을 반환해 더 안전하다.

<IMAGE>딕셔너리 내부 해시 테이블 구조 그림</IMAGE>

## 수도코드(Pseudocode)

```
딕셔너리_탐색(d, key):
    key의 해시값 계산 → 해시 테이블에서 위치 찾기
    O(1) 시간에 값 반환 (충돌 없을 때)

딕셔너리_순회(d):
    for key in d:           → 키만 순회
    for key, val in d.items(): → 키-값 쌍 순회
```

## 구현 코드 (Python)

```python
# 생성
d = {}                              # 빈 딕셔너리
d = {"name": "홍길동", "age": 30}
d = {1: "one", 2: "two"}

# 접근
print(d["name"])                    # "홍길동"
print(d.get("age"))                 # 30
print(d.get("score", 0))            # 0  (없으면 기본값)

# 추가 / 수정
d["city"] = "서울"                  # 추가
d["age"] = 31                       # 수정

# 삭제
del d["city"]                       # 특정 키 삭제
popped = d.pop("age", None)         # 제거 후 반환
d.clear()                           # 전체 삭제

# 순회
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key, d[key])

for key, val in d.items():
    print(f"{key}: {val}")

# 주요 메서드
print(d.keys())     # dict_keys(['a', 'b', 'c'])
print(d.values())   # dict_values([1, 2, 3])
print(d.items())    # dict_items([...])

# 키 존재 확인
print("a" in d)     # True
print("z" in d)     # False

# 병합
d1 = {"a": 1}
d2 = {"b": 2}
merged = {**d1, **d2}           # {'a':1, 'b':2}
d1.update(d2)                   # d1에 d2 병합

# 딕셔너리 컴프리헨션
squares = {x: x**2 for x in range(1, 6)}
print(squares)   # {1:1, 2:4, 3:9, 4:16, 5:25}

# 키-값 뒤집기
inv = {v: k for k, v in d.items()}
```

## 실전 예제: 글자 빈도 세기

```python
def char_frequency(text):
    """문자별 등장 횟수를 딕셔너리로 반환"""
    freq = {}
    for char in text:
        if char != " ":
            freq[char] = freq.get(char, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: -x[1]))

result = char_frequency("hello world")
print(result)   # {'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1}
```

# 메타데이터
```json
{
  "category": "자료형",
  "topic": "딕셔너리",
  "source_type": "ai",
  "style": ["theory", "code"],
  "intuition_score": 4,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "beginner",
  "language": "python"
}
```
