# [Python 기초] 정렬 (sort / sorted)

# 본문

## 1. 한 줄 요약

파이썬 정렬은 데이터를 원하는 기준에 따라 순서대로 배치하는 기능이며, `sort()`와 `sorted()`를 주로 사용한다.

정렬을 이해하면 숫자, 문자열, 튜플, 객체를 기준에 맞게 나열할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

데이터는 항상 원하는 순서로 주어지지 않는다.

예를 들어 학생 점수가 다음처럼 섞여 있다고 해보자.

```python
scores = [70, 100, 80, 90]
```

최저 점수부터 확인하거나, 높은 점수 순으로 등수를 매기려면 정렬이 필요하다.

```text
원본
[70, 100, 80, 90]

오름차순
[70, 80, 90, 100]

내림차순
[100, 90, 80, 70]
```

정렬을 직접 구현할 수도 있지만, 파이썬은 이미 편리한 정렬 기능을 제공한다.

리스트 자체를 바꿀 때는 `sort()`를 사용한다.

새로운 정렬 결과를 만들 때는 `sorted()`를 사용한다.

---

## 3. 핵심 아이디어

정렬은 책장을 정리하는 것과 비슷하다.

책이 아무렇게나 꽂혀 있으면 원하는 책을 찾기 어렵다.

```text
정리 전

[국어] [과학] [수학] [영어]
```

기준을 정하면 책을 보기 좋게 나열할 수 있다.

```text
가나다순 정렬
[과학] [국어] [수학] [영어]
```

파이썬 정렬도 마찬가지다.

기준을 정하지 않으면 기본적으로 작은 값에서 큰 값으로 정렬한다.

```python
numbers = [3, 1, 4, 2]
numbers.sort()
```

```text
[1, 2, 3, 4]
```

정렬 기준을 직접 정하고 싶으면 `key`를 사용한다.

```python
words.sort(key=len)
```

```text
단어 길이를 기준으로 정렬
```

---

## 4. 동작 과정 살펴보기

아래 리스트를 정렬해 보자.

```python
numbers = [3, 1, 4, 2]
numbers.sort()
```

### Step 1. 원본 리스트가 준비된다

```text
numbers

[3] [1] [4] [2]
```

### Step 2. 작은 값부터 순서를 정한다

```text
값 비교

1이 가장 작음
그다음 2
그다음 3
그다음 4
```

### Step 3. 리스트 자체가 바뀐다

```text
sort() 실행 후

numbers
[1] [2] [3] [4]
```

`sort()`는 원본 리스트를 직접 수정한다.

### sorted의 경우

```python
numbers = [3, 1, 4, 2]
result = sorted(numbers)
```

```text
원본 numbers
[3] [1] [4] [2]

새 결과 result
[1] [2] [3] [4]
```

`sorted()`는 원본을 그대로 두고 새 리스트를 만든다.

---

## 5. 구현 코드 및 상세 설명

```python
numbers = [3, 1, 4, 2]

# sort(): 원본 리스트를 직접 정렬
numbers.sort()
print("sort 결과:", numbers)


numbers = [3, 1, 4, 2]

# sorted(): 정렬된 새 리스트 반환
sorted_numbers = sorted(numbers)
print("원본:", numbers)
print("sorted 결과:", sorted_numbers)


# 내림차순 정렬
numbers.sort(reverse=True)
print("내림차순:", numbers)


# 문자열 길이 기준 정렬
words = ["banana", "cat", "apple"]
words.sort(key=len)
print("길이 기준:", words)


# 튜플의 두 번째 값 기준 정렬
students = [("민수", 80), ("지은", 95), ("현우", 70)]
students.sort(key=lambda student: student[1])
print("점수 기준:", students)
```

### 코드 설명

```python
numbers.sort()
```

리스트 `numbers` 자체를 오름차순으로 바꾼다.

별도의 새 리스트를 반환하지 않는다.

```python
sorted_numbers = sorted(numbers)
```

원본 리스트는 그대로 두고, 정렬된 새 리스트를 만든다.

원본 보존이 필요하면 `sorted()`가 더 적합하다.

```python
numbers.sort(reverse=True)
```

`reverse=True`를 사용하면 내림차순으로 정렬한다.

```text
[4, 3, 2, 1]
```

```python
words.sort(key=len)
```

문자열 자체가 아니라 문자열 길이를 기준으로 정렬한다.

```text
"cat"    → 길이 3
"apple"  → 길이 5
"banana" → 길이 6
```

```python
students.sort(key=lambda student: student[1])
```

튜플의 두 번째 값인 점수를 기준으로 정렬한다.

```text
("민수", 80) → 80
("지은", 95) → 95
("현우", 70) → 70
```

---

## 6. 마지막 정리

`sort()`는 리스트 원본을 직접 정렬한다.

`sorted()`는 정렬된 새 리스트를 반환한다.

기본 정렬은 오름차순이다.

`reverse=True`를 사용하면 내림차순 정렬이 가능하다.

`key`를 사용하면 길이, 점수, 특정 위치 값 등 원하는 기준으로 정렬할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "파이썬 정렬 sort sorted",
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
