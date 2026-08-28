# 제목
[Python 기초] 튜플 자료형 (Tuple Type)

# 본문
리스트와 거의 비슷하지만 불변(immutable)인 자료형이다.
한 번 만들면 내부 값을 수정, 추가, 삭제할 수 없다.

소괄호 `()` 로 만들며, 괄호를 생략해도 된다.
요소가 1개일 때는 반드시 쉼표를 붙여야 한다. `(1,)` ← 이렇게.

## 리스트 vs 튜플

| 구분 | 리스트 | 튜플 |
|------|--------|------|
| 기호 | [] | () |
| 변경 | 가능 (mutable) | 불가 (immutable) |
| 속도 | 느림 | 빠름 |
| 딕셔너리 키 | 불가 | 가능 |
| 용도 | 동적 데이터 | 고정 데이터 |

## 튜플 언패킹

튜플의 값을 여러 변수에 한 번에 대입하는 기능이다.
이를 활용하면 두 변수의 값을 임시 변수 없이 스왑할 수 있다.

<IMAGE>튜플 언패킹 동작 원리 그림</IMAGE>

## 언제 쓸까?

함수에서 여러 값을 반환할 때, 딕셔너리의 키로 쓸 때, 변경되면 안 되는 상수 묶음을 표현할 때 주로 사용한다.

## 수도코드(Pseudocode)

```
튜플_언패킹(tuple):
    a, b, c = (1, 2, 3)
    → a=1, b=2, c=3 동시 할당

스왑(x, y):
    x, y = y, x  ← 임시 변수 불필요
```

## 구현 코드 (Python)

```python
# 생성
a = ()              # 빈 튜플
b = (1,)            # 요소 1개 (쉼표 필수!)
c = (1, 2, 3)       # 일반 튜플
d = 1, 2, 3         # 괄호 생략 가능

# 주의: (1)은 정수, (1,)이 튜플
print(type((1)))    # <class 'int'>
print(type((1,)))   # <class 'tuple'>

# 인덱싱 / 슬라이싱
t = (1, 2, 3, 4, 5)
print(t[0])         # 1
print(t[-1])        # 5
print(t[1:3])       # (2, 3)
print(t[::-1])      # (5, 4, 3, 2, 1)

# 연산
a = (1, 2, 3)
b = (4, 5, 6)
print(a + b)        # (1, 2, 3, 4, 5, 6)
print(a * 2)        # (1, 2, 3, 1, 2, 3)
print(len(a))       # 3

# 언패킹
a, b, c = (1, 2, 3)
print(a, b, c)      # 1 2 3

# 스왑 (임시 변수 없이)
x, y = 10, 20
x, y = y, x
print(x, y)         # 20 10

# * 활용 언패킹
first, *rest = (1, 2, 3, 4, 5)
print(first)   # 1
print(rest)    # [2, 3, 4, 5]

# 딕셔너리 키로 사용
d = {(1, 2): "좌표A", (3, 4): "좌표B"}
print(d[(1, 2)])    # 좌표A
```

## 실전 예제: 함수에서 여러 값 반환

```python
def min_max(lst):
    """최솟값과 최댓값을 튜플로 반환"""
    return min(lst), max(lst)

data = [3, 1, 4, 1, 5, 9, 2, 6]
lo, hi = min_max(data)
print(f"최솟값: {lo}, 최댓값: {hi}")   # 최솟값: 1, 최댓값: 9
```

# 메타데이터
```json
{
  "category": "자료형",
  "topic": "튜플",
  "source_type": "generated",
  "style": ["theory", "code"],
  "intuition_score": 4,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "beginner",
  "language": "python"
}
```
