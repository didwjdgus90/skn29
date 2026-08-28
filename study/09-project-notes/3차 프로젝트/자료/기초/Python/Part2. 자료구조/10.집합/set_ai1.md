# 제목
[Python 기초] 집합 자료형 (Set Type)

# 본문
중복이 없고 순서가 없는 자료형이다.
수학의 집합 개념을 그대로 구현한 것으로, 교집합·합집합·차집합 연산을 제공한다.

중괄호 `{}` 로 만들지만, 빈 집합은 `set()` 으로 만들어야 한다.
`{}` 단독으로 쓰면 딕셔너리가 된다는 점에 주의한다.

집합의 탐색(`in`)은 해시 기반이라 O(1)로 빠르다.
이 때문에 중복 제거나 멤버십 테스트에 많이 활용된다.

## 집합 연산자

| 연산자 | 메서드 | 설명 |
|--------|--------|------|
| & | intersection() | 교집합 |
| \| | union() | 합집합 |
| - | difference() | 차집합 |
| ^ | symmetric_difference() | 대칭차집합 |

## 언제 집합을 쓸까

리스트에서 중복을 제거하거나, 특정 원소가 존재하는지 O(1)로 빠르게 확인할 때,
또는 두 그룹의 공통/차이 원소를 구할 때 사용한다.

<IMAGE>집합 연산 벤 다이어그램 그림</IMAGE>

## 수도코드(Pseudocode)

```
집합_교집합(A, B):
    결과 = {}
    for each x in A:
        if x in B:
            결과.add(x)
    return 결과

중복제거(lst):
    return set(lst)  → 중복 자동 제거
```

## 구현 코드 (Python)

```python
# 생성
a = {1, 2, 3, 4, 5}
b = set([1, 2, 3, 2, 1])    # 중복 제거됨
print(b)                     # {1, 2, 3}

empty = set()                # 빈 집합 ({} 아님!)

# 집합 연산
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}

print(a & b)    # {3, 4, 5}            교집합
print(a | b)    # {1,2,3,4,5,6,7}      합집합
print(a - b)    # {1, 2}               차집합
print(a ^ b)    # {1,2,6,7}            대칭차집합

# 메서드 방식
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))

# 추가 / 삭제
s = {1, 2, 3}
s.add(4)              # 단일 추가
s.update([5, 6, 7])   # 여러 개 추가
s.remove(1)           # 없으면 KeyError
s.discard(99)         # 없어도 에러 없음
s.pop()               # 임의 제거 후 반환

# 부분집합 확인
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))    # True  (a ⊆ b)
print(b.issuperset(a))  # True  (b ⊇ a)
print(a.isdisjoint({4, 5}))  # True  (교집합 없음)

# 중복 제거 (순서 유지 안 됨)
lst = [3, 1, 4, 1, 5, 9, 2, 6, 5]
unique = list(set(lst))
print(unique)   # 순서 보장 없음
```

## 실전 예제: 두 리스트의 공통 원소 찾기

```python
def common_elements(lst1, lst2):
    """두 리스트에서 공통 원소를 정렬된 리스트로 반환"""
    return sorted(set(lst1) & set(lst2))

a = [1, 2, 3, 4, 5, 3, 2]
b = [3, 4, 5, 6, 7]
print(common_elements(a, b))   # [3, 4, 5]
```

# 메타데이터
```json
{
  "category": "자료형",
  "topic": "집합",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 4,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "beginner",
  "language": "python"
}
```
