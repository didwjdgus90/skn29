# [Python 기초] 리스트 (List)

---

# 링크
<https://ctkim.tistory.com/entry/Python-%EC%9E%85%EB%AC%B8-%EA%B0%95%EC%A2%8C-8-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8List-%EC%A0%95%EB%A6%AC-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95>

---

## 1. 한 줄 요약

리스트는 **여러 값을 순서대로 담을 수 있는 바구니**다. 값을 추가하거나 지우거나 바꿀 수 있고, 순서(인덱스)로 꺼낼 수 있다.

---

## 2. 왜 리스트가 필요할까?

학생 5명의 점수를 저장한다면?

```python
# 리스트 없이 — 변수를 5개나 만들어야 함
score1 = 90
score2 = 85
score3 = 78
score4 = 92
score5 = 88
```

학생이 100명이면 변수가 100개다. 한꺼번에 처리도 안 된다.

```python
# 리스트 사용 — 하나의 변수에 모두 저장
scores = [90, 85, 78, 92, 88]

print(max(scores))  # 최고점: 92
print(sum(scores))  # 합계: 433
```

리스트는 **여러 값을 묶어서 한꺼번에 다룰 수 있게** 해준다.

---

## 3. 핵심 아이디어 — 리스트는 "번호 붙은 서랍"

리스트를 **번호가 붙어있는 서랍장**으로 생각하자.

```
fruits = ["사과", "바나나", "딸기", "포도"]

 서랍번호:  [  0  ] [  1  ] [  2  ] [  3  ]
 내용물:   [ 사과 ] [바나나] [ 딸기 ] [ 포도 ]
              ↑
          0번부터 시작!
```

- 번호(인덱스)로 원하는 서랍을 바로 열 수 있다.
- 서랍을 추가하거나, 빼거나, 내용을 바꿀 수 있다.
- 몇 번 서랍까지 있는지(길이)도 알 수 있다.

---

## 4. 동작 과정 살펴보기

### 4-1. 리스트 만들기

```python
# 기본 생성
numbers = [1, 2, 3, 4, 5]
fruits  = ["사과", "바나나", "딸기"]

# 여러 타입을 섞어도 됨
mixed = [1, "hello", 3.14, True]

# 빈 리스트
empty = []
empty2 = list()

# 리스트 안에 리스트 (중첩)
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
```

### 4-2. 인덱싱 — 원하는 위치 꺼내기

```python
fruits = ["사과", "바나나", "딸기", "포도"]
#인덱스:    0       1        2       3
#음수:     -4      -3       -2      -1

print(fruits[0])   # 사과   (첫 번째)
print(fruits[2])   # 딸기   (세 번째)
print(fruits[-1])  # 포도   (마지막)
print(fruits[-2])  # 딸기   (뒤에서 두 번째)
```

```
인덱스 시각화:

[ "사과" | "바나나" | "딸기" | "포도" ]
     0        1        2       3      ← 앞에서 셀 때
    -4       -3       -2      -1      ← 뒤에서 셀 때
```

> 💡 음수 인덱스는 **뒤에서부터** 센다. `-1`이 마지막, `-2`가 뒤에서 두 번째.

### 4-3. 슬라이싱 — 범위를 잘라내기

```python
nums = [1, 2, 3, 4, 5]

print(nums[1:3])   # [2, 3]     → 1번 이상 3번 미만
print(nums[:3])    # [1, 2, 3]  → 처음부터 3번 미만
print(nums[2:])    # [3, 4, 5]  → 2번부터 끝까지
print(nums[::2])   # [1, 3, 5]  → 2칸씩 건너뛰며
```

```
nums[1:3] 시각화:

[ 1 | 2 | 3 | 4 | 5 ]
  0   1   2   3   4
      ↑       ↑
   start    end (미포함!)

결과: [2, 3]
```

```
슬라이싱 규칙: list[start : end : step]
  start → 시작 인덱스 (포함)
  end   → 끝 인덱스 (미포함!)
  step  → 간격 (생략하면 1)
```

---

## 5. 구현 코드 및 상세 설명

### 5-1. 리스트 수정과 삭제

```python
a = [1, 2, 3, 4, 5]

# 값 수정
a[2] = 99
print(a)        # [1, 2, 99, 4, 5]

# del로 삭제
del a[2]
print(a)        # [1, 2, 4, 5]
```

### 5-2. 리스트 연산

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# 더하기 = 이어붙이기
print(list1 + list2)   # [1, 2, 3, 4, 5, 6]

# 곱하기 = 반복
print(list1 * 3)       # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

### 5-3. 자주 쓰는 함수들

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(nums))      # 8     — 요소 개수
print(max(nums))      # 9     — 최댓값
print(min(nums))      # 1     — 최솟값
print(sum(nums))      # 31    — 합계

# sorted() — 정렬된 새 리스트 반환 (원본 변경 없음)
print(sorted(nums))              # [1, 1, 2, 3, 4, 5, 6, 9]
print(sorted(nums, reverse=True))# [9, 6, 5, 4, 3, 2, 1, 1]
print(nums)                      # [3, 1, 4, 1, 5, 9, 2, 6] ← 원본 그대로!
```

### 5-4. 자주 쓰는 메서드들

```python
my_list = [1, 2, 3]

# append() — 맨 끝에 추가
my_list.append(4)
print(my_list)       # [1, 2, 3, 4]

# insert() — 원하는 위치에 추가
my_list.insert(1, 99)
print(my_list)       # [1, 99, 2, 3, 4]

# remove() — 값으로 삭제 (첫 번째 일치하는 것만)
my_list.remove(99)
print(my_list)       # [1, 2, 3, 4]

# pop() — 인덱스로 꺼내서 삭제 (꺼낸 값 반환)
val = my_list.pop()   # 마지막 꺼냄
print(val)           # 4
print(my_list)       # [1, 2, 3]

val = my_list.pop(0)  # 0번 꺼냄
print(val)           # 1
print(my_list)       # [2, 3]
```

```python
fruits = ["사과", "바나나", "사과", "포도"]

# count() — 특정 값의 개수
print(fruits.count("사과"))  # 2

# index() — 특정 값의 첫 번째 위치
print(fruits.index("바나나")) # 1

# reverse() — 원본을 뒤집기 (새 리스트 아님!)
fruits.reverse()
print(fruits)    # ['포도', '사과', '바나나', '사과']

# extend() — 다른 리스트를 이어붙이기
extra = ["딸기", "수박"]
fruits.extend(extra)
print(fruits)    # ['포도', '사과', '바나나', '사과', '딸기', '수박']
```

```
메서드 한눈에 보기:

append(값)     → 맨 뒤에 추가
insert(위치,값) → 원하는 위치에 추가
remove(값)     → 값으로 삭제 (첫 번째 일치)
pop(인덱스)    → 위치로 꺼내며 삭제
count(값)      → 값의 개수 세기
index(값)      → 값의 위치 찾기
reverse()      → 순서 뒤집기 (원본 변경)
extend(리스트) → 다른 리스트 이어붙이기
```

### 5-5. sorted() vs reverse() 헷갈리지 않기

```python
nums = [3, 1, 4, 1, 5]

# sorted() → 원본 그대로, 새 리스트 반환
new = sorted(nums)
print(nums)   # [3, 1, 4, 1, 5]  ← 원본 안 바뀜
print(new)    # [1, 1, 3, 4, 5]  ← 새 리스트

# .sort() → 원본 직접 변경, 반환값 없음
nums.sort()
print(nums)   # [1, 1, 3, 4, 5]  ← 원본이 바뀜

# reverse() → 원본 직접 뒤집기
nums.reverse()
print(nums)   # [5, 4, 3, 1, 1]  ← 원본이 바뀜
```

```
원본 유지   → sorted(), reversed()  (함수 형태)
원본 변경   → .sort(), .reverse()   (메서드 형태)
```

---

## 6. 마지막 정리

- 리스트는 `[값1, 값2, ...]` 형태로 만들고, **여러 타입을 섞어 담을 수 있다**.
- 인덱스는 **0부터 시작**, 음수 인덱스는 **뒤에서부터** 센다 (`-1`이 마지막).
- 슬라이싱 `[start:end]`에서 **end는 포함되지 않는다**.
- `append()`는 맨 뒤에, `insert(위치, 값)`은 원하는 위치에 추가한다.
- `sorted()`는 원본을 바꾸지 않고 새 리스트를 반환, `.sort()`는 원본을 직접 바꾼다.
- `len()`, `max()`, `min()`, `sum()`으로 길이·최댓값·최솟값·합계를 구할 수 있다.

---

# 메타데이터
```json
{
  "category": "언어 기초",
  "algorithm": "리스트",
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