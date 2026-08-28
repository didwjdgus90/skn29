# 제목
[Python 기초] 딕셔너리 (Dictionary)

# 링크
https://docs.python.org/ko/3.11/tutorial/datastructures.html#dictionaries

# 본문

## 1. 한 줄 요약

딕셔너리는 **해시 가능한 키(key)와 임의의 값(value)을 쌍으로 저장하는 가변(mutable) 매핑(mapping) 자료형**이다. 시퀀스 자료형이 정수 인덱스로 색인되는 것과 달리, 딕셔너리는 *키(key)* 로 색인된다.

---

## 2. 딕셔너리의 정의와 특성

파이썬 공식 문서의 정의에 따르면:

> 딕셔너리를 연상시키는 것으로는 *연관 메모리(associative memories)* 또는 *연관 배열(associative arrays)* 이 있습니다. 숫자 범위를 키로 사용하는 시퀀스와 달리, 딕셔너리는 *키(key)* 로 색인됩니다. 키는 문자열이나 숫자처럼 불변인 형이면 됩니다. 튜플은 문자열, 숫자 또는 다른 튜플만을 포함하면 키로 사용될 수 있습니다. 리스트는 직접 또는 간접적으로 가변 객체를 포함하기 때문에 키로 사용할 수 없습니다.

딕셔너리의 핵심 특성은 다음과 같다.

```
딕셔너리(dict)의 핵심 특성:

1. 키-값 쌍(key-value pair)  — 각 항목은 키와 값으로 구성됨
2. 키 유일성(unique key)     — 동일한 키는 하나만 유지 (중복 시 덮어씀)
3. 삽입 순서 보장(Python 3.7+) — 항목은 삽입된 순서로 순회됨
4. 가변(mutable)             — 키-값 쌍의 추가·수정·삭제 가능
5. 키 제약                  — 키는 해시 가능한(hashable) 불변 객체여야 함
```

공식 문서는 딕셔너리를 **순서 없는 키:값 쌍의 집합**으로 기술하며, 이 요건이 성립하는 한 키는 고유해야 한다고 명시한다. Python 3.7부터는 삽입 순서가 보장된다.

---

## 3. 핵심 아이디어

### 해시 테이블 기반의 O(1) 키 조회

딕셔너리는 내부적으로 **해시 테이블(hash table)** 로 구현된다. 키를 해시값으로 변환해 저장 위치를 결정하므로, 키에 의한 값 조회(`d[key]`)가 리스트의 O(n) 순차 탐색과 달리 **평균 O(1)**에 수행된다.

이 구조적 특성이 딕셔너리를 대용량 데이터에서 빠른 조회가 필요한 경우에 적합하게 만든다.

```
리스트 vs 딕셔너리 조회 비교:

자료형        조회 방식          평균 시간복잡도
─────────────────────────────────────────────
list          순차 탐색(in)      O(n)
dict          해시 조회(d[key])  O(1)
```

### 키의 해시 가능성 제약

딕셔너리 키는 반드시 **해시 가능한(hashable) 불변 객체**여야 한다. 가변 객체인 리스트나 딕셔너리는 키로 사용할 수 없다.

```
키(key) 사용 가능 여부:

타입               해시 가능   딕셔너리 키
────────────────────────────────────────
int, float, str    ✅          ✅
tuple (불변 요소만) ✅          ✅
list               ❌ (가변)   ❌ → TypeError
dict               ❌ (가변)   ❌ → TypeError
```

---

## 4. 동작 과정 살펴보기

### 4-1. 딕셔너리 생성

딕셔너리는 중괄호 `{ }` 안에 `key: value` 쌍을 쉼표로 구분하여 생성하거나, `dict()` 생성자를 사용한다.

```python
>>> tel = {'jack': 4098, 'sape': 4139}
>>> tel['guido'] = 4127      # 새 키-값 쌍 추가
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127}
```

**`dict()` 생성자를 이용한 다양한 생성 방법:**

```python
# 키워드 인자를 이용한 생성 — 키가 단순 문자열인 경우
>>> dict(sape=4139, guido=4127, jack=4098)
{'sape': 4139, 'guido': 4127, 'jack': 4098}

# (key, value) 튜플의 시퀀스로부터 생성
>>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
{'sape': 4139, 'guido': 4127, 'jack': 4098}
```

**빈 딕셔너리 생성:**

```python
empty1 = {}        # 빈 딕셔너리
empty2 = dict()    # 동일
```

`{}`는 빈 **딕셔너리**를 생성한다. 집합과 달리 빈 중괄호는 딕셔너리로 해석된다.

### 4-2. 항목 접근, 추가, 수정, 삭제

```python
>>> tel = {'jack': 4098, 'sape': 4139, 'guido': 4127}

# 키로 값 접근
>>> tel['jack']
4098

# 새 키-값 쌍 추가
>>> tel['irv'] = 4127
>>> tel
{'jack': 4098, 'sape': 4139, 'guido': 4127, 'irv': 4127}

# 기존 키의 값 수정 (키가 이미 존재하면 덮어씀)
>>> tel['jack'] = 9999
>>> tel['jack']
9999

# del로 특정 항목 삭제
>>> del tel['sape']
>>> tel
{'jack': 9999, 'guido': 4127, 'irv': 4127}
```

존재하지 않는 키로 접근하면 `KeyError`가 발생한다.

```python
>>> tel['nonexistent']
KeyError: 'nonexistent'
```

```
키-값 쌍 조작 흐름:

tel = {'jack': 4098, 'sape': 4139}

tel['guido'] = 4127   →  키 없음 → 새 항목 추가
tel['jack'] = 9999    →  키 있음 → 기존 값 덮어씀
del tel['sape']       →  키 있음 → 항목 제거
tel['ghost']          →  키 없음 → KeyError 발생
```

### 4-3. 키 존재 여부 확인

`in` 연산자로 특정 키가 딕셔너리에 존재하는지 확인한다.

```python
>>> 'guido' in tel
True
>>> 'jack' not in tel
False
```

---

## 5. 구현 코드 및 상세 설명

### 5-1. 주요 메서드

**`keys()`, `values()`, `items()`**

딕셔너리의 뷰 객체(view object)를 반환한다. 뷰 객체는 딕셔너리 변경 사항을 실시간으로 반영한다.

```python
>>> tel = {'jack': 4098, 'guido': 4127}
>>> list(tel.keys())
['jack', 'guido']

>>> list(tel.values())
[4098, 4127]

>>> list(tel.items())
[('jack', 4098), ('guido', 4127)]
```

`keys()`는 Python 3.7+에서 삽입 순서가 보장된 뷰를 반환한다. 정렬이 필요한 경우 `sorted(d.keys())`를 사용한다.

```python
>>> sorted(tel.keys())
['guido', 'jack']
```

**`get(key, default)`**

키가 존재하지 않을 때 `KeyError` 대신 기본값을 반환한다. 안전한 값 조회 시 `d[key]` 대신 사용한다.

```python
>>> tel.get('jack', -1)
4098               # 키 존재 → 해당 값 반환

>>> tel.get('ghost', -1)
-1                 # 키 없음 → 기본값 -1 반환

>>> tel.get('ghost')
None               # 기본값 미지정 시 None 반환
```

**`pop(key, default)`**

키에 해당하는 항목을 삭제하고 값을 반환한다. `default`를 지정하면 키가 없을 때 `KeyError` 대신 기본값을 반환한다.

```python
>>> tel.pop('jack')
4098               # 항목 삭제 후 값 반환

>>> tel.pop('ghost', -1)
-1                 # 없는 키, 기본값 반환

>>> tel.pop('ghost')
KeyError: 'ghost'  # 기본값 없으면 KeyError 발생
```

**`update()`**

다른 딕셔너리 또는 키-값 쌍의 이터러블로 딕셔너리를 갱신한다. 기존 키는 덮어쓰고, 새 키는 추가된다.

```python
>>> d = {'a': 1, 'b': 2}
>>> d.update({'b': 99, 'c': 3})
>>> d
{'a': 1, 'b': 99, 'c': 3}   # 'b' 덮어씀, 'c' 추가
```

---

### 5-2. 딕셔너리 컴프리헨션

집합 컴프리헨션과 유사하게, 딕셔너리도 컴프리헨션 문법으로 생성할 수 있다.

```python
# 키와 그 제곱으로 이루어진 딕셔너리 생성
>>> {x: x**2 for x in range(6)}
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# 조건 필터링 포함
>>> {x: x**2 for x in range(10) if x % 2 == 0}
{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}
```

---

### 5-3. for 루프와의 연동

공식 문서는 딕셔너리를 루프로 순회하는 관용적 패턴을 다음과 같이 제시한다.

**`items()`로 키와 값을 동시에 순회:**

```python
>>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
>>> for k, v in knights.items():
...     print(k, v)
...
gallahad the pure
robin the brave
```

**`enumerate()`와의 조합 — 인덱스가 필요한 경우:**

```python
for idx, (key, value) in enumerate(d.items()):
    print(idx, key, value)
```

순회 도중 딕셔너리 크기를 변경(항목 추가·삭제)하는 것은 `RuntimeError`를 유발한다. 수정이 필요한 경우 복사본(`d.copy()` 또는 `dict(d)`)을 순회하거나, 수정할 키 목록을 별도 수집 후 루프 외부에서 처리해야 한다.

```python
# ❌ 순회 중 크기 변경 → RuntimeError
for k in d:
    del d[k]

# ✅ 복사본 순회
for k in list(d.keys()):
    del d[k]
```

---

### 5-4. 딕셔너리 병합 — Python 3.9+

Python 3.9부터 `|` 연산자와 `|=` 연산자로 딕셔너리를 병합할 수 있다.

```python
d1 = {'a': 1, 'b': 2}
d2 = {'b': 99, 'c': 3}

# | 연산자: 새 딕셔너리 반환, 원본 불변
merged = d1 | d2
print(merged)   # {'a': 1, 'b': 99, 'c': 3} — d2가 우선

# |= 연산자: 원본 제자리 갱신
d1 |= d2
print(d1)       # {'a': 1, 'b': 99, 'c': 3}
```

중복 키가 있는 경우 **오른쪽 피연산자의 값이 우선**한다.

---

### 5-5. 키 유일성과 중복 처리

공식 문서는 딕셔너리에 동일한 키가 두 번 이상 저장될 수 없다고 명시한다. 리터럴에서 중복 키를 지정하면 마지막 값만 유지된다.

```python
>>> d = {'a': 1, 'b': 2, 'a': 99}
>>> d
{'a': 99, 'b': 2}    # 'a'는 마지막 값 99만 유지됨
```

이 동작은 에러 없이 조용히 처리되므로, 딕셔너리 리터럴 작성 시 중복 키가 의도치 않게 포함되지 않도록 주의해야 한다.

---

## 6. 핵심 요약 및 주의점

**핵심 요약**

- 딕셔너리는 **키-값 쌍의 매핑 자료형**이다. 정수 인덱스가 아닌 키로 값에 접근한다.
- **키는 해시 가능한 불변 객체**여야 한다. 리스트·딕셔너리는 키로 사용 불가.
- **키 중복 불허**: 동일한 키를 재지정하면 기존 값이 조용히 덮어써진다.
- **Python 3.7+**: 삽입 순서가 보장된다.
- `d[key]`는 키 부재 시 `KeyError`, `d.get(key, default)`는 기본값을 반환한다. 안전한 조회에는 `get()`을 사용한다.
- `keys()`, `values()`, `items()`는 딕셔너리의 변경을 실시간 반영하는 **뷰 객체**를 반환한다.

**주요 메서드 요약**

```
메서드                    설명                         키 부재 시
──────────────────────────────────────────────────────────────────
d[key]                   값 조회                       KeyError
d.get(key, default)      안전한 값 조회                default 반환
d[key] = value           추가 또는 수정               —
del d[key]               항목 삭제                     KeyError
d.pop(key, default)      삭제 후 값 반환               default 또는 KeyError
key in d                 키 존재 여부 확인             —
d.keys()                 키 뷰 반환                   —
d.values()               값 뷰 반환                   —
d.items()                (키, 값) 뷰 반환              —
d.update(other)          다른 딕셔너리로 갱신          —
```

**주의점**

```
상황                              올바른 방법              잘못된 방법
─────────────────────────────────────────────────────────────────────────
없는 키 안전 조회                  get(key, default)        d[key] → KeyError
순회 중 항목 삭제                  list(d.keys()) 순회       for k in d: del d[k] → RuntimeError
중복 키 지정                      의도적으로 피할 것         리터럴 중복 → 조용한 덮어쓰기
빈 집합 생성 혼동                  set() 사용               {} → 빈 딕셔너리
```

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "딕셔너리",
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