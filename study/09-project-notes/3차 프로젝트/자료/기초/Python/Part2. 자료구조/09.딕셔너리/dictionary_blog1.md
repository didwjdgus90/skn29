# [Python 기초] 딕셔너리 (Dictionary)

---

# 링크
<https:https://coding-factory.tistory.com/973>

---

## 1. 한 줄 요약

딕셔너리는 **이름표(Key)와 값(Value)을 짝지어 저장하는 자료구조**다. 번호 대신 이름으로 값을 꺼낼 수 있어서, 의미 있는 데이터를 다룰 때 리스트보다 훨씬 직관적이다.

---

## 2. 왜 딕셔너리가 필요할까?

학생 한 명의 정보(이름, 나이, 점수)를 저장한다고 해보자.

리스트로 저장하면 이렇게 된다.

```python
student = ["김정민", 25, 92]
```

이 코드를 보고 바로 알 수 있는 게 없다. `student[0]`이 이름인지, 나이인지, 점수인지 외우고 있어야 한다. 항목이 늘어날수록 0번이 뭔지 2번이 뭔지 계속 헷갈린다.

딕셔너리로 저장하면 이렇다.

```python
student = {"name": "김정민", "age": 25, "score": 92}
```

`student["name"]`, `student["score"]`처럼 이름으로 꺼낸다. 코드를 처음 보는 사람도 무슨 값인지 바로 이해할 수 있다.

딕셔너리는 **"이게 뭔 값이야?"** 라는 질문이 생길 때 쓰는 자료구조다. 숫자 번호 대신 의미 있는 이름표를 붙여서 데이터를 저장한다.

---

## 3. 핵심 아이디어 — 딕셔너리는 "실제 사전"이다

딕셔너리(Dictionary)라는 이름은 영어 단어 "사전"에서 왔다. 실제 사전이 어떻게 작동하는지 생각해보자.

사전에서 "apple"이라는 단어를 찾으면 "사과"라는 뜻이 나온다. 단어를 알면 뜻을 바로 찾을 수 있다. 반대로 "사과"라는 뜻을 먼저 찾아서 "apple"이라는 단어를 알아내는 건 매우 어렵다.

파이썬 딕셔너리도 똑같다.

```
"apple"  →  "사과"
   ↑            ↑
  Key          Value
 (단어)         (뜻)
```

**Key(키)** 는 찾을 때 쓰는 이름표이고, **Value(값)** 는 그 이름표에 연결된 실제 데이터다. Key를 알면 Value를 즉시 꺼낼 수 있다.

```
딕셔너리 구조 시각화:

{
  "name"  : "김정민",    ←  Key: "name",  Value: "김정민"
  "age"   : 25,          ←  Key: "age",   Value: 25
  "score" : 92           ←  Key: "score", Value: 92
}
    ↑          ↑
   Key        Value
  (이름표)    (실제 데이터)
```

리스트가 **순서(번호)로 값을 찾는** 자료구조라면, 딕셔너리는 **이름표(Key)로 값을 찾는** 자료구조다.

---

## 4. 동작 과정 살펴보기

### 4-1. 딕셔너리 만들기

딕셔너리는 중괄호 `{ }`를 사용하고, Key와 Value를 콜론 `:`으로 연결하며, 각 쌍은 콤마 `,`로 구분한다.

```python
# 기본 생성
fruits = {"apple": 3, "banana": 5, "orange": 2}

# 다양한 타입도 섞어서 사용 가능
student = {
    "name" : "김정민",   # Key: 문자열, Value: 문자열
    "age"  : 25,         # Key: 문자열, Value: 정수
    "pass" : True        # Key: 문자열, Value: 불리언
}

# 빈 딕셔너리 — 나중에 값을 채울 때
empty = {}
```

딕셔너리는 Key에 어떤 타입이든 쓸 수 있고, Value도 어떤 타입이든 넣을 수 있다. 단, **Key는 변경 불가능한 타입**이어야 한다. 문자열, 정수, 튜플은 Key로 쓸 수 있지만, 리스트는 Key로 쓸 수 없다.

```python
# ✅ 유효한 Key 타입들
d = {
    "name": "정민",   # 문자열 Key
    1: "one",         # 정수 Key
    (0, 0): "원점"    # 튜플 Key
}

# ❌ 리스트는 Key로 사용 불가
d = {[1, 2]: "value"}   # TypeError!
```

왜 리스트는 안 될까? 딕셔너리는 Key로 값을 빠르게 찾아야 하는데, Key가 나중에 바뀌면 어디서 찾아야 할지 알 수 없게 되기 때문이다. 변경 가능한 리스트는 그 이유로 Key가 될 수 없다.

---

### 4-2. 값 꺼내기 — Key로 즉시 접근

리스트는 `student[0]`처럼 번호로 꺼내지만, 딕셔너리는 `student["name"]`처럼 Key 이름으로 꺼낸다.

```python
student = {"name": "김정민", "age": 25, "score": 92}

print(student["name"])    # 김정민
print(student["score"])   # 92
```

```
접근 방식 비교:

리스트:       student[0]       ← "0번이 뭐였지?" 외워야 함
딕셔너리:  student["name"]   ← 이름만 보면 바로 이해됨
```

주의할 점이 하나 있다. **없는 Key로 접근하면 KeyError가 발생**한다. 리스트에서 범위를 벗어난 인덱스를 쓰면 에러가 나듯, 딕셔너리에서도 등록되지 않은 Key를 쓰면 에러가 난다.

```python
print(student["grade"])   # ❌ KeyError: 'grade' 가 없음!
```

이 에러를 방지하는 안전한 방법이 있다. `get()` 메서드를 쓰면 Key가 없어도 에러 대신 기본값을 돌려준다.

```python
# get(Key, 없을 때 돌려줄 기본값)
print(student.get("grade", "없음"))   # 없음  — 에러 없이 처리됨
print(student.get("name", "없음"))    # 김정민 — Key가 있으면 Value 반환
```

실전에서는 `[ ]`보다 `get()`을 더 자주 쓴다. 딕셔너리에 Key가 있는지 확신할 수 없는 경우가 많기 때문이다.

---

### 4-3. 값 추가 · 수정 · 삭제

딕셔너리는 리스트처럼 값을 자유롭게 추가하고 수정하고 삭제할 수 있다.

**추가 — 새 Key에 값을 대입하면 자동으로 추가된다**

```python
fruits = {"apple": 3, "banana": 5}

fruits["orange"] = 2   # orange라는 Key가 없으니 새로 추가됨
print(fruits)          # {'apple': 3, 'banana': 5, 'orange': 2}
```

딕셔너리에서 추가할 때는 `append()` 같은 별도 메서드가 필요 없다. 그냥 새 Key에 값을 넣으면 된다. 이미 있는 Key에 값을 넣으면 기존 값이 덮어씌워진다.

**수정 — 기존 Key에 새 값을 대입하면 덮어씌워진다**

```python
fruits["apple"] = 10   # 기존 3에서 10으로 변경
print(fruits)          # {'apple': 10, 'banana': 5, 'orange': 2}
```

```
추가 vs 수정 구분 방법:

fruits["orange"] = 2   # "orange"가 없던 Key → 추가
fruits["apple"] = 10   # "apple"이 이미 있던 Key → 수정(덮어쓰기)
```

**삭제 — `del` 또는 `pop()`으로 삭제**

```python
fruits = {"apple": 10, "banana": 5, "orange": 2}

# del: 그냥 삭제
del fruits["banana"]
print(fruits)          # {'apple': 10, 'orange': 2}

# pop(): 삭제하면서 지운 값을 돌려줌
removed = fruits.pop("apple")
print(removed)         # 10   ← 삭제된 값이 반환됨
print(fruits)          # {'orange': 2}
```

`del`과 `pop()`의 차이는 간단하다. 그냥 지우기만 하면 `del`, 지우면서 그 값을 변수에 담아 활용해야 하면 `pop()`을 쓴다.

---

## 5. 구현 코드 및 상세 설명

### 5-1. Key 존재 여부 확인하기

딕셔너리에서 값을 꺼내기 전에 해당 Key가 있는지 먼저 확인하고 싶을 때는 `in` 키워드를 쓴다. 결과는 `True` 또는 `False`로 돌아온다.

```python
fruits = {"apple": 5, "banana": 3}

print("apple" in fruits)    # True  — apple이 있음
print("orange" in fruits)   # False — orange가 없음
```

이걸 조건문과 함께 쓰면 KeyError를 예방하면서 안전하게 값을 다룰 수 있다.

```python
key = "orange"

if key in fruits:
    print(fruits[key])
else:
    print(f"{key}는 딕셔너리에 없습니다.")
```

실전에서는 이 패턴보다 앞서 소개한 `get()`이 더 간결해서 자주 쓰인다.

```python
# 위 if-else를 한 줄로 줄인 것과 같음
print(fruits.get("orange", "없음"))
```

---

### 5-2. 전체 Key, Value, 쌍(items) 꺼내기

딕셔너리에 담긴 모든 Key나 Value를 한꺼번에 꺼내야 할 때가 자주 생긴다. 세 가지 메서드가 이 역할을 한다.

```python
fruits = {"apple": 5, "banana": 3, "orange": 2}

print(fruits.keys())    # dict_keys(['apple', 'banana', 'orange'])
print(fruits.values())  # dict_values([5, 3, 2])
print(fruits.items())   # dict_items([('apple', 5), ('banana', 3), ('orange', 2)])
```

`keys()`는 모든 Key만, `values()`는 모든 Value만, `items()`는 (Key, Value) 쌍을 묶은 튜플들을 돌려준다.

이 메서드들이 가장 빛나는 순간은 `for` 반복문과 함께 쓸 때다. 딕셔너리 전체를 순서대로 처리할 수 있다.

```python
# 모든 Key만 순회
for key in fruits.keys():
    print(key)
# apple
# banana
# orange

# 모든 Value만 순회
for value in fruits.values():
    print(value)
# 5
# 3
# 2

# Key와 Value를 동시에 순회 (가장 많이 쓰는 패턴)
for key, value in fruits.items():
    print(f"{key}: {value}개")
# apple: 5개
# banana: 3개
# orange: 2개
```

`for key, value in fruits.items():`가 실전에서 딕셔너리를 순회할 때 가장 자주 쓰이는 패턴이다. `items()`가 (Key, Value) 튜플을 돌려주고, 언패킹으로 `key`와 `value`에 각각 담기 때문이다.

---

### 5-3. 딕셔너리 주의사항 — Key 중복

딕셔너리에서 **같은 Key를 두 번 쓰면 나중 값이 이전 값을 덮어씌운다.** 에러는 나지 않으니 조용히 데이터가 사라지는 버그가 생길 수 있다.

```python
d = {"apple": 3, "apple": 10}   # apple이 두 번 등장
print(d)   # {'apple': 10}      ← 3은 사라지고 10만 남음
```

"아, 이미 있는 Key구나"를 파이썬이 알려주지 않기 때문에, 딕셔너리를 직접 작성할 때는 Key가 겹치지 않는지 주의해야 한다.

---

### 5-4. 리스트로부터 딕셔너리 만들기 — `zip()` 활용

Key 목록과 Value 목록이 따로 있을 때, `zip()`으로 묶어서 딕셔너리로 변환할 수 있다. `zip()`은 두 리스트를 같은 위치끼리 짝지어주는 함수다.

```python
keys   = ["name", "age", "score"]
values = ["김정민", 25, 92]

student = dict(zip(keys, values))
print(student)
# {'name': '김정민', 'age': 25, 'score': 92}
```

```
zip() 동작 시각화:

keys   = ["name",   "age", "score"]
values = ["김정민",   25,     92  ]
            ↓          ↓       ↓
zip()  → [("name","김정민"), ("age",25), ("score",92)]
            ↓
dict() → {"name": "김정민", "age": 25, "score": 92}
```

데이터를 처리하다 보면 Key 리스트와 Value 리스트가 따로 주어지는 상황이 자주 생기는데, 이 패턴을 알아두면 매우 유용하다.

---

### 5-5. 종합 예제 — 과일 재고 관리

지금까지 배운 내용을 하나의 시나리오로 합쳐보자. 과일 가게의 재고를 딕셔너리로 관리하는 예제다.

```python
# 초기 재고 설정
stock = {"apple": 10, "banana": 5, "orange": 3}

# 1. 재고 확인
print(stock.get("apple", 0))    # 10
print(stock.get("grape", 0))    # 0  ← 없는 과일은 0으로 처리

# 2. 새 과일 입고 (추가)
stock["mango"] = 7
print(stock)   # {'apple': 10, 'banana': 5, 'orange': 3, 'mango': 7}

# 3. 재고 수량 변경 (수정)
stock["banana"] = 8
print(stock["banana"])   # 8

# 4. 과일 판매 종료 (삭제)
del stock["orange"]
print(stock)   # {'apple': 10, 'banana': 8, 'mango': 7}

# 5. 전체 재고 현황 출력
print("=== 현재 재고 ===")
for name, count in stock.items():
    print(f"  {name}: {count}개")

# 출력:
# === 현재 재고 ===
#   apple: 10개
#   banana: 8개
#   mango: 7개
```

---

## 6. 리스트 vs 딕셔너리 — 언제 뭘 쓸까?

둘 중 어느 것을 써야 할지 판단하는 기준은 간단하다. **"값을 꺼낼 때 번호로 찾을까, 이름으로 찾을까?"**

```
항목              리스트 [ ]           딕셔너리 { }
────────────────────────────────────────────────────
값을 찾는 방법    번호(인덱스)          이름표(Key)
순서              있음                  있음 (Python 3.7+)
값 수정           가능                  가능
중복 값 허용      가능                  Value는 가능, Key는 불가
언제 쓰나         같은 종류의 값 목록   이름이 붙은 데이터 묶음

예시:
  리스트  → 학생 점수 목록 [90, 85, 78, 92]
  딕셔너리 → 한 학생의 정보 {"name": "정민", "score": 92}
```

쉽게 정리하면, **비슷한 종류의 값을 여러 개 늘어놓는다면 리스트**, **한 대상에 대한 여러 속성을 묶는다면 딕셔너리**다.

---

## 7. 마지막 정리

- 딕셔너리는 `{"Key": Value}` 형태로, **이름표(Key)로 값을 찾는** 자료구조다.
- `dict["Key"]`로 값을 꺼내고, 없는 Key를 쓰면 `KeyError`가 난다. 안전하게 꺼내려면 `get(Key, 기본값)`을 쓰자.
- **있는 Key에 값을 대입하면 수정**, **없는 Key에 값을 대입하면 추가**가 된다.
- 삭제는 `del dict["Key"]` 또는 `pop("Key")`로 하며, `pop()`은 삭제한 값을 반환한다.
- `keys()`, `values()`, `items()`로 전체 Key·Value·쌍을 꺼낼 수 있고, `for key, value in dict.items():`가 순회할 때 가장 자주 쓰이는 패턴이다.
- **같은 Key를 두 번 쓰면 나중 값이 이전 값을 덮어씌운다.** 조용히 데이터가 사라질 수 있으니 주의하자.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "딕셔너리",
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