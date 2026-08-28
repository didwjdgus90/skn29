# 제목
[Python 기초] 리스트 자료형 (List Type)

# 본문
여러 값을 순서 있게 저장하는 가변(mutable) 자료형이다.
다른 언어의 배열(Array)과 유사하지만, 서로 다른 타입의 값을 섞어 저장할 수 있다.
또한 중첩 리스트(리스트 안에 리스트)도 가능하다.

리스트는 대괄호 `[]` 로 만들며, 요소들은 쉼표로 구분한다.
가변(mutable)이므로 인덱싱을 통해 요소를 직접 수정할 수 있다.

## 리스트 vs 문자열

| 구분 | 리스트 | 문자열 |
|------|--------|--------|
| 생성 | [] | "" |
| 변경 가능 | 가능 (mutable) | 불가 (immutable) |
| 요소 타입 | 뭐든 가능 | 문자만 |

## 참조와 복사

리스트를 `=` 로 대입하면 복사가 아닌 같은 객체를 가리키는 참조가 된다.
진짜 복사가 필요하면 `.copy()` 또는 `copy.deepcopy()`를 사용해야 한다.

<IMAGE>참조 vs 복사 메모리 구조 그림</IMAGE>

중첩 리스트는 얕은 복사(shallow copy)로는 내부 리스트까지 복사되지 않는다.
내부 객체까지 완전히 복사하려면 깊은 복사(deep copy)를 써야 한다.

## 리스트 컴프리헨션

리스트 컴프리헨션은 for문과 조건문을 한 줄로 압축해 리스트를 만드는 방법이다.
일반 for문보다 속도가 빠르고 코드가 간결해진다.

```
[표현식 for 변수 in 이터러블 if 조건]
```

## 수도코드(Pseudocode)

```
리스트_순회(lst):
    for i in range(len(lst)):
        현재 요소: lst[i]
        수정 가능: lst[i] = 새값

리스트_복사(lst):
    얕은 복사: lst.copy() 또는 lst[:]
    깊은 복사: copy.deepcopy(lst)  ← 중첩 리스트에 필요
```

## 구현 코드 (Python)

```python
# 생성
a = [1, 2, 3]
b = [1, "hello", 3.14, True]    # 혼합 가능
c = [1, [2, 3], [4, 5, 6]]      # 중첩 가능

# 인덱싱 / 슬라이싱
lst = [1, 2, 3, 4, 5]
print(lst[0])       # 1
print(lst[-1])      # 5
print(lst[1:3])     # [2, 3]
print(lst[::-1])    # [5, 4, 3, 2, 1]

# 수정
lst[0] = 99
print(lst)   # [99, 2, 3, 4, 5]

# 주요 메서드
a = [3, 1, 4, 1, 5]
a.append(9)          # 맨 뒤에 추가      → [3,1,4,1,5,9]
a.insert(0, 0)       # 인덱스 0에 삽입   → [0,3,1,4,1,5,9]
a.extend([7, 8])     # 여러 개 추가      → [0,3,1,4,1,5,9,7,8]
a.remove(1)          # 첫 번째 1 제거
a.pop()              # 마지막 요소 제거
a.pop(0)             # 인덱스 0 제거
a.sort()             # 오름차순 정렬 (원본 변경)
a.reverse()          # 순서 뒤집기
print(a.count(1))    # 1의 개수
print(a.index(4))    # 4의 위치

# 정렬 비교
lst = [3, 1, 4, 1, 5]
lst.sort()                     # 원본 변경
new = sorted(lst)              # 새 리스트 반환
sorted(lst, reverse=True)      # 내림차순

# 참조 vs 복사
a = [1, 2, 3]
b = a              # 참조
b[0] = 99
print(a)           # [99, 2, 3]  ← a도 바뀜!

c = a.copy()       # 복사
c[0] = 0
print(a)           # [99, 2, 3]  ← a는 그대로

# 리스트 컴프리헨션
squares = [x**2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

evens = [x for x in range(10) if x % 2 == 0]
print(evens)     # [0, 2, 4, 6, 8]
```

## 실전 예제: 리스트 중복 제거 (순서 유지)

```python
def remove_duplicates(lst):
    """순서를 유지하면서 중복 제거"""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

lst = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(remove_duplicates(lst))   # [3, 1, 4, 5, 9, 2, 6]
```

# 메타데이터
```json
{
  "category": "자료형",
  "topic": "리스트",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "beginner",
  "language": "python"
}
```
