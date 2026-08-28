# [알고리즘] Deque

## 1. 한 줄 요약

> Deque는 양쪽 끝에서 데이터를 빠르게 넣고 뺄 수 있는 양방향 큐 자료구조입니다.

---

## 2. 선수 지식

- 큐
  - 먼저 들어온 데이터가 먼저 나가는 자료구조입니다.

- 스택
  - 마지막에 들어온 데이터가 먼저 나가는 자료구조입니다.

- 리스트
  - 여러 값을 순서대로 저장하는 자료구조입니다.

- 시간복잡도
  - 자료구조에서 삽입과 삭제가 얼마나 빠른지 판단할 때 필요합니다.

- Python collections 모듈
  - Python에서 `deque`를 사용하려면 `collections` 모듈에서 가져와야 합니다.

---

## 3. 어떤 문제를 해결하기 위해 사용하는가?

Deque는 앞과 뒤 양쪽에서 삽입과 삭제가 모두 필요한 문제에 사용합니다.

### 기존 방식의 문제

- Python 리스트에서 맨 앞 원소를 삭제하면 뒤 원소들을 앞으로 당겨야 합니다.
- 그래서 `pop(0)`을 반복하면 데이터가 많을 때 느려집니다.
- 일반 큐는 한쪽으로 넣고 반대쪽으로 빼는 구조라 양쪽 조작이 필요한 문제에는 불편합니다.

예를 들어 대기열에서 앞사람을 처리하기도 하고, 긴급한 사람을 맨 앞에 넣기도 해야 한다면 일반 리스트보다 Deque가 적합합니다.

### 이 알고리즘을 사용하면

- 앞쪽 삽입과 삭제를 빠르게 처리할 수 있습니다.
- 뒤쪽 삽입과 삭제도 빠르게 처리할 수 있습니다.
- 큐처럼도 쓰고, 스택처럼도 쓸 수 있습니다.
- BFS, 회전 큐, 슬라이딩 윈도우, 작업 대기열 문제에 활용할 수 있습니다.

입력 크기가 커질수록 리스트의 앞쪽 삭제보다 Deque가 훨씬 안정적입니다.

---

## 4. 핵심 아이디어

Deque는 double-ended queue의 줄임말입니다. 이름 그대로 양쪽 끝이 모두 열려 있는 큐입니다.

오른쪽 끝에는 `append`, 왼쪽 끝에는 `appendleft`로 값을 넣습니다. 오른쪽 끝에서는 `pop`, 왼쪽 끝에서는 `popleft`로 값을 뺍니다.

### 쉬운 비유

양쪽 문이 있는 버스를 떠올려봅시다. 앞문으로도 사람이 탈 수 있고, 뒷문으로도 사람이 탈 수 있습니다. 내릴 때도 앞문과 뒷문을 모두 사용할 수 있습니다.

Deque는 이런 버스처럼 양쪽 끝에서 모두 출입이 가능한 자료구조입니다.

### 직관적으로 이해하기

Deque에 `[2, 3]`이 있다고 해봅시다.

- 왼쪽에 `1`을 넣으면 `[1, 2, 3]`이 됩니다.
- 오른쪽에 `4`를 넣으면 `[1, 2, 3, 4]`가 됩니다.
- 왼쪽에서 하나 빼면 `1`이 나가고 `[2, 3, 4]`가 됩니다.
- 오른쪽에서 하나 빼면 `4`가 나가고 `[2, 3]`이 됩니다.

양쪽 끝 조작이 모두 자연스럽게 처리됩니다.

---

## 5. 동작 과정 살펴보기

### 예제 상황

대기열이 있습니다. 일반 손님은 뒤에 추가되고, 긴급 손님은 앞에 추가됩니다. 처리할 때는 항상 앞에서 한 명씩 처리합니다.

### 예제 입력

```text
6
normal Mina
normal Joon
urgent Hana
serve
normal Sol
serve
```

### 예제 출력

```text
Hana
Mina
```

### 단계별 동작

1. 빈 Deque를 만듭니다.
2. `normal Mina`는 오른쪽 뒤에 넣습니다.
3. `normal Joon`도 오른쪽 뒤에 넣습니다.
4. `urgent Hana`는 왼쪽 앞에 넣습니다.
5. `serve`가 나오면 왼쪽 앞에서 한 명을 꺼냅니다.
6. `normal Sol`은 오른쪽 뒤에 넣습니다.
7. 다시 `serve`가 나오면 왼쪽 앞에서 한 명을 꺼냅니다.

처리 순서는 긴급 손님이 먼저 반영되어 `Hana`, `Mina`가 됩니다.

---

## 6. Text Flow Chart

```text
[시작]
  ↓
[명령 입력]
  ↓
[명령 종류 확인]
  ├─ 뒤에 추가 → [append 실행]
  ├─ 앞에 추가 → [appendleft 실행]
  ├─ 앞에서 제거 → [popleft 실행]
  └─ 뒤에서 제거 → [pop 실행]
  ↓
[Deque 상태 갱신]
  ↓
[남은 명령이 있는가?]
  ├─ 예 → [다음 명령 입력]
  └─ 아니오 → [종료]
```

---

## 7. 기본 코드 템플릿

```python
from collections import deque


def process_waiting_line(commands):
    waiting_line = deque()
    served_people = []

    for command in commands:
        parts = command.split()
        action = parts[0]

        if action == "normal":
            waiting_line.append(parts[1])
        elif action == "urgent":
            waiting_line.appendleft(parts[1])
        elif action == "serve":
            if waiting_line:
                served_people.append(waiting_line.popleft())

    return served_people


command_count = int(input())
commands = []

for _ in range(command_count):
    commands.append(input().strip())

result = process_waiting_line(commands)

for name in result:
    print(name)
```

### 코드 흐름 설명

* `waiting_line`은 Deque로 만든 대기열입니다.
* 일반 손님은 `append`로 오른쪽 끝에 추가합니다.
* 긴급 손님은 `appendleft`로 왼쪽 끝에 추가합니다.
* 처리 명령이 나오면 `popleft`로 왼쪽 끝 사람을 꺼냅니다.
* `served_people`에는 처리된 사람 이름을 저장합니다.
* `if waiting_line`은 Deque가 비어 있는지 확인합니다.
* Deque를 사용하면 앞쪽 삽입과 삭제가 빠르게 처리됩니다.

---

## 8. 시간복잡도와 공간복잡도

### 시간복잡도

* 평균적인 경우
  - `append`, `appendleft`, `pop`, `popleft`는 보통 `O(1)`입니다.

* 최악의 경우
  - 양쪽 끝 조작은 매우 빠르게 처리됩니다.
  - 중간 삽입이나 중간 삭제는 Deque의 장점이 크지 않습니다.

* 입력 크기가 커졌을 때 부담되는 부분
  - 명령을 하나씩 처리하므로 전체 시간은 명령 수를 `N`이라고 할 때 `O(N)`입니다.
  - 리스트에서 `pop(0)`을 반복하는 것보다 훨씬 유리합니다.

### 공간복잡도

* Deque에 저장되는 데이터 개수만큼 공간을 사용합니다.
* 최대 대기 인원이 `N`명이라면 공간복잡도는 `O(N)`입니다.
* 처리 결과를 따로 저장하면 그만큼 추가 공간이 필요합니다.

---

## 9. 예제로 이해하기

앞에서 사용한 예제와 다른 상황을 보겠습니다.

### 입력 데이터

```text
7
normal A
normal B
urgent C
serve
urgent D
normal E
serve
```

### 처리 과정

- `normal A` → `[A]`
- `normal B` → `[A, B]`
- `urgent C` → `[C, A, B]`
- `serve` → `C` 처리, 남은 상태 `[A, B]`
- `urgent D` → `[D, A, B]`
- `normal E` → `[D, A, B, E]`
- `serve` → `D` 처리, 남은 상태 `[A, B, E]`

### 중간 상태 변화

긴급 손님은 항상 앞쪽으로 들어갑니다. 그래서 뒤에 온 사람이라도 먼저 처리될 수 있습니다.

### 최종 결과

```text
C
D
```

---

## 10. 문제에서 이 알고리즘을 떠올리는 신호

* 앞과 뒤 양쪽에서 삽입 또는 삭제가 필요합니다.
* 리스트의 `pop(0)`을 반복하면 느릴 것 같습니다.
* 큐처럼 앞에서 꺼내고 뒤에 넣어야 합니다.
* 때로는 앞에도 새 값을 넣어야 합니다.
* 원소를 회전시키는 작업이 필요합니다.
* BFS처럼 순서대로 처리하는 구조가 나옵니다.
* 슬라이딩 윈도우에서 양쪽 끝 값을 관리해야 합니다.
* "맨 앞", "맨 뒤", "회전", "양방향" 같은 표현이 나옵니다.

---

## 11. 비슷한 알고리즘과 헷갈리는 부분

* Deque와 Queue
  - Queue는 보통 한쪽으로 넣고 반대쪽으로 뺍니다.
  - Deque는 양쪽 끝에서 모두 넣고 뺄 수 있습니다.

* Deque와 Stack
  - Stack은 한쪽 끝만 사용하면 됩니다.
  - Deque는 한쪽 끝만 사용하면 스택처럼 쓸 수도 있습니다.

* Deque와 List
  - 리스트는 뒤쪽 삽입과 삭제는 빠르지만 앞쪽 삭제는 느릴 수 있습니다.
  - Deque는 양쪽 끝 삽입과 삭제에 강합니다.

* Deque와 Linked List
  - Deque는 언어마다 내부 구현이 다를 수 있습니다.
  - 알고리즘 문제에서는 양쪽 끝 조작이 빠르다는 특징을 중심으로 이해하면 됩니다.

* Deque와 Priority Queue
  - Deque는 양쪽 끝 순서대로 처리합니다.
  - Priority Queue는 우선순위가 높은 원소를 먼저 꺼냅니다.

---

## 12. 자주 하는 실수

* 리스트에서 `pop(0)`을 반복해 시간초과가 나는 실수
* Deque가 비어 있는데 `popleft`나 `pop`을 호출하는 실수
* `append`와 `appendleft` 방향을 반대로 쓰는 실수
* `pop`과 `popleft`를 헷갈리는 실수
* `extendleft`가 입력 순서를 뒤집어 넣는다는 점을 잊는 실수
* 중간 삽입과 삭제도 항상 빠르다고 착각하는 실수
* 인덱싱과 슬라이싱 용도로 Deque를 남용하는 실수
* 회전 방향을 잘못 이해하는 실수

---

## 13. 힌트 생성용 관점

이 문서는 RAG 기반 AI 튜터의 힌트 생성에도 활용될 수 있습니다.

### 1단계 힌트: 개념 힌트

문제에서 앞과 뒤 양쪽 끝을 모두 다루는지 확인해보세요. 한쪽 끝만 빠르게 처리하는 구조보다 Deque가 필요할 수 있습니다.

### 2단계 힌트: 접근 힌트

명령을 네 가지로 나누어 생각하세요. 앞에 넣기, 뒤에 넣기, 앞에서 빼기, 뒤에서 빼기입니다.

### 3단계 힌트: 구현 힌트

Python에서는 `collections.deque`를 사용하세요. 오른쪽 추가는 `append`, 왼쪽 추가는 `appendleft`, 오른쪽 제거는 `pop`, 왼쪽 제거는 `popleft`입니다.

---

## 14. 언제 사용하면 좋은가

* 입력 조건
  - 데이터가 많고 앞쪽 삭제 또는 앞쪽 삽입이 자주 일어나는 경우

* 문제 유형
  - BFS, 대기열, 카드 회전, 회전 큐, 슬라이딩 윈도우, 양방향 명령 처리

* 자주 등장하는 표현
  - "앞에서 제거", "뒤에 추가", "앞에 추가", "양쪽 끝", "회전"

* 적합한 자료구조
  - Python의 `collections.deque`, C++의 `deque`

* 사용하면 안 되는 경우
  - 중간 인덱스를 자주 탐색하거나 슬라이싱해야 하는 경우
  - 정렬된 상태를 유지해야 하는 경우
  - 우선순위에 따라 꺼내야 하는 경우

---

## 15. 요약 정리

* Deque의 목적
  - 양쪽 끝에서 빠르게 삽입과 삭제를 처리하는 것입니다.

* 핵심 아이디어
  - 앞과 뒤를 모두 입구이자 출구로 사용할 수 있습니다.

* 주요 자료구조
  - Python에서는 `collections.deque`를 사용합니다.

* 시간복잡도
  - 양쪽 끝 삽입과 삭제는 보통 `O(1)`입니다.

* 문제에서 떠올리는 신호
  - 앞뒤 양쪽 조작, 회전, BFS, 대기열 처리가 보이면 떠올릴 수 있습니다.

* 초급자가 주의할 점
  - `append`, `appendleft`, `pop`, `popleft`의 방향을 정확히 구분해야 합니다.

---

## 메타데이터

```json
{
  "category": "큐",
  "algorithm": "Deque",
  "source_type": "generated",
  "style": ["easy", "code", "analogy", "theory"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "python"
}
```
