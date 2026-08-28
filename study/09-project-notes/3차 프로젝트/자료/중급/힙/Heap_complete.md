# 제목
[알고리즘] 힙(Heap) 완전 정복 — Min/Max Heap, 우선순위 큐, 실전 문제 3선

# 본문

## 한줄 요약

힙은 "항상 가장 크거나 가장 작은 값을 즉시 꺼낼 수 있는 특수한 트리 구조"이며, 우선순위 큐의 엔진 역할을 한다.

---

## 왜 필요한가

병원 응급실을 떠올려 보자. 환자가 도착한 순서대로 진료하는 게 아니라, **증상이 가장 심한 환자부터** 먼저 본다. 일반 배열로 이 로직을 만들면 매번 전체를 훑어야 하므로 환자가 수천 명이면 병목이 생긴다.

힙은 이 문제를 해결한다. 데이터를 넣을 때마다 내부에서 자동으로 정렬 상태를 유지하기 때문에, 가장 급한 데이터를 **O(1)**에 확인하고 **O(log N)**에 꺼낼 수 있다.

배열 정렬(`O(N log N)`)이나 매번 최솟값 탐색(`O(N)`)보다 훨씬 빠르게 "우선순위가 높은 것부터 처리"해야 하는 상황에서 힙이 등장한다.

---

## 핵심 개념

### 1. 완전 이진 트리

힙은 완전 이진 트리(Complete Binary Tree) 형태다. 노드가 위에서 아래로, 왼쪽에서 오른쪽으로 빈틈 없이 채워진다. 이 덕분에 배열 하나로 트리를 표현할 수 있다.

배열 인덱스 관계 (0-base 기준):
- 부모 → `(i - 1) // 2`
- 왼쪽 자식 → `2 * i + 1`
- 오른쪽 자식 → `2 * i + 2`

### 2. Min Heap vs Max Heap

| 구분 | 규칙 | 루트에 위치하는 값 |
|------|------|------------------|
| Min Heap | 부모 ≤ 자식 | 전체 최솟값 |
| Max Heap | 부모 ≥ 자식 | 전체 최댓값 |

주의: 형제 노드 사이에는 크기 관계가 없다. 왼쪽이 오른쪽보다 크든 작든 상관없다.

### 3. 우선순위 큐 (Priority Queue)

우선순위 큐는 **추상 자료형(ADT)**이고, 힙은 그것을 구현하는 **구체적 자료구조**다.

| 일반 큐 | 우선순위 큐 |
|---------|-----------|
| 먼저 들어온 것이 먼저 나감 (FIFO) | 우선순위가 높은 것이 먼저 나감 |
| `O(1)` 삽입/삭제 | `O(log N)` 삽입/삭제 |

### 4. 시간 복잡도

| 연산 | 복잡도 |
|------|--------|
| 최솟값/최댓값 확인 (peek) | O(1) |
| 삽입 (push) | O(log N) |
| 삭제 (pop) | O(log N) |
| N개 원소로 힙 구성 (heapify) | O(N) |

---

## 동작 흐름

### 삽입 (Push) — 위로 올라가며 조정 (sift-up)

1. 새 값을 배열 맨 끝에 추가한다 (트리의 마지막 자리).
2. 부모와 비교해서 힙 조건을 위반하면 부모와 교환한다.
3. 루트에 도달하거나 조건을 만족할 때까지 2를 반복한다.

### 삭제 (Pop) — 아래로 내려가며 조정 (sift-down)

1. 루트(최솟값 또는 최댓값)를 결과로 보관한다.
2. 배열 맨 끝 원소를 루트 자리로 옮긴다.
3. 자식 둘 중 힙 조건에 맞는 쪽과 비교해서 교환한다.
4. 리프에 도달하거나 조건을 만족할 때까지 3을 반복한다.

---

## Text Flow Chart

### Min Heap에 값 삽입: [5, 3, 8] 상태에서 1 삽입

```
상태 0: 현재 힙                삽입할 값: 1
        3
       / \
      5   8

상태 1: 맨 끝에 1 추가
        3
       / \
      5   8
     /
    1

상태 2: 1 < 5 (부모) → 교환
        3
       / \
      1   8
     /
    5

상태 3: 1 < 3 (부모) → 교환
        1
       / \
      3   8
     /
    5

완료: 1이 루트에 도착, 힙 조건 충족
배열: [1, 3, 8, 5]
```

### Min Heap에서 루트 삭제

```
상태 0: 현재 힙
        1
       / \
      3   8
     /
    5

상태 1: 루트(1) 제거, 마지막 원소(5)를 루트로
        5
       / \
      3   8

상태 2: 5 > 3 (왼쪽 자식) → 교환
        3
       / \
      5   8

완료: 힙 조건 충족
반환값: 1 (최솟값)
배열: [3, 5, 8]
```

---

## 기본 코드 템플릿

### Python — heapq 모듈 활용

```python
import heapq

# === Min Heap (기본) ===
bucket = []
heapq.heappush(bucket, 40)
heapq.heappush(bucket, 10)
heapq.heappush(bucket, 25)

# 가장 작은 값 확인 (제거하지 않음)
print(bucket[0])  # 10

# 가장 작은 값 꺼내기
smallest = heapq.heappop(bucket)
print(smallest)  # 10
print(bucket)    # [25, 40]


# === Max Heap (부호 반전 트릭) ===
# Python heapq는 Min Heap만 지원
# 넣을 때 부호를 뒤집고, 꺼낼 때 다시 뒤집는다
scores = []
for s in [40, 10, 25]:
    heapq.heappush(scores, -s)

biggest = -heapq.heappop(scores)
print(biggest)  # 40
```

**코드 흐름 설명**

1. `heapq`는 리스트를 Min Heap처럼 동작하게 만드는 모듈이다.
2. `heappush`는 값을 넣으면서 자동으로 sift-up을 수행한다.
3. `heappop`은 루트(최솟값)를 꺼내고 sift-down으로 힙을 재정비한다.
4. Max Heap이 필요하면 `-값`을 넣고 꺼낼 때 `-`를 다시 붙인다.

### Java — PriorityQueue 활용

```java
import java.util.PriorityQueue;
import java.util.Collections;

public class HeapBasic {
    public static void main(String[] args) {
        // === Min Heap (기본) ===
        PriorityQueue<Integer> minPQ = new PriorityQueue<>();
        minPQ.offer(40);
        minPQ.offer(10);
        minPQ.offer(25);

        System.out.println(minPQ.peek()); // 10 (확인만)
        System.out.println(minPQ.poll()); // 10 (꺼냄)

        // === Max Heap (역순 Comparator) ===
        PriorityQueue<Integer> maxPQ =
            new PriorityQueue<>(Collections.reverseOrder());
        maxPQ.offer(40);
        maxPQ.offer(10);
        maxPQ.offer(25);

        System.out.println(maxPQ.poll()); // 40 (최댓값 먼저)
    }
}
```

**코드 흐름 설명**

1. `PriorityQueue`는 기본적으로 Min Heap이다.
2. `offer()`로 삽입, `poll()`로 최솟값 추출, `peek()`로 확인만 한다.
3. `Collections.reverseOrder()`를 생성자에 전달하면 Max Heap으로 동작한다.

### C++ — priority_queue 활용

```cpp
#include <iostream>
#include <queue>
#include <vector>
#include <functional>
using namespace std;

int main() {
    // === Max Heap (C++ 기본) ===
    priority_queue<int> maxPQ;
    maxPQ.push(40);
    maxPQ.push(10);
    maxPQ.push(25);
    cout << maxPQ.top() << endl; // 40
    maxPQ.pop();

    // === Min Heap (greater 사용) ===
    priority_queue<int, vector<int>, greater<int>> minPQ;
    minPQ.push(40);
    minPQ.push(10);
    minPQ.push(25);
    cout << minPQ.top() << endl; // 10
    minPQ.pop();

    return 0;
}
```

**코드 흐름 설명**

1. C++ `priority_queue`는 기본이 **Max Heap**이다 (Python, Java와 반대).
2. Min Heap은 세 번째 템플릿 인자로 `greater<int>`를 지정한다.
3. `top()`으로 확인, `pop()`으로 제거 (반환값 없음에 주의).

---

## 실전 문제 풀이

---

### 문제 1: 매운맛 조절 (프로그래머스 "더 맵게" 유형)

#### 핵심 개념

이 문제는 **"반복적으로 가장 작은 값을 꺼내야 하는 상황"**의 전형적 패턴이다.

- 전체 데이터 중 최솟값 2개를 꺼내 합치고, 결과를 다시 넣어야 한다.
- 배열을 매번 정렬하면 O(N log N)이 반복되어 느리다.
- **Min Heap을 사용하면** 꺼내기 O(log N), 넣기 O(log N)으로 매 라운드가 O(log N)이 된다.

핵심 공식:

```
합친 값 = 가장_낮은_값 + (두번째_낮은_값 × 2)
```

종료 조건:
- 루트(최솟값) ≥ 기준값 → 성공, 횟수 반환
- 원소 1개 이하인데 기준 미달 → 불가능, -1 반환

#### 풀이 전략

```
[전체 흐름]

음식 리스트 → Min Heap으로 변환
              ↓
         ┌─ 루트 ≥ 기준? ──→ YES → 횟수 반환
         │       ↓ NO
         │  원소 2개 이상?
         │       ↓ NO → -1 반환
         │       ↓ YES
         │  최솟값 2개 꺼내기
         │       ↓
         │  공식으로 합치기
         │       ↓
         │  결과를 힙에 넣기
         │       ↓
         │  횟수 + 1
         └───────┘ (반복)
```

왜 힙인가?
- 합친 결과가 다시 최솟값이 될 수도 있다 → 정렬 순서가 매번 바뀜
- 매번 정렬 대신 **힙에 push만 하면 O(log N)**에 올바른 위치에 들어간다

#### 소스코드

**Python**

```python
import heapq

def count_blending(spicy_list, threshold):
    """모든 원소가 threshold 이상이 되도록 합치는 최소 횟수"""
    heapq.heapify(spicy_list)          # O(N)으로 힙 구성
    blend_count = 0

    while spicy_list[0] < threshold:   # 루트가 기준 미만인 동안
        if len(spicy_list) < 2:        # 합칠 재료가 부족
            return -1

        weakest = heapq.heappop(spicy_list)       # 1순위 최솟값
        runner_up = heapq.heappop(spicy_list)      # 2순위 최솟값
        combined = weakest + runner_up * 2          # 합치기 공식

        heapq.heappush(spicy_list, combined)        # 결과 재투입
        blend_count += 1

    return blend_count

# --- 실행 ---
print(count_blending([1, 2, 3, 9, 10, 12], 7))  # 2
```

**Java**

```java
import java.util.PriorityQueue;

public class SpicyBlender {
    public static int countBlending(int[] spicyArr, int threshold) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int val : spicyArr) pq.offer(val);

        int blendCount = 0;

        while (pq.peek() < threshold) {
            if (pq.size() < 2) return -1;

            int weakest = pq.poll();
            int runnerUp = pq.poll();
            int combined = weakest + runnerUp * 2;

            pq.offer(combined);
            blendCount++;
        }
        return blendCount;
    }

    public static void main(String[] args) {
        int[] foods = {1, 2, 3, 9, 10, 12};
        System.out.println(countBlending(foods, 7));  // 2
    }
}
```

**코드 흐름 설명**

| 단계 | 힙 상태 | 동작 |
|------|---------|------|
| 초기 | `[1, 2, 3, 9, 10, 12]` | heapify |
| 1회 | pop 1, 2 → 합침 `1+2*2=5` → push | `[3, 5, 9, 10, 12]` |
| 2회 | pop 3, 5 → 합침 `3+5*2=13` → push | `[9, 10, 12, 13]` |
| 종료 | 루트(9) ≥ 7 → 성공 | 반환: 2 |

---

### 문제 2: 작업 스케줄링 (프로그래머스 "디스크 컨트롤러" 유형)

#### 핵심 개념

이 문제의 본질은 **"한 번에 하나만 처리할 수 있을 때, 전체 대기시간을 최소화하는 순서 찾기"**다.

- 핵심 전략: **SJF (Shortest Job First)** — 현재 처리 가능한 작업 중 소요시간이 짧은 것부터 처리
- 왜 SJF가 최적인가? 짧은 작업을 먼저 끝내면 뒤에 대기하는 모든 작업의 대기시간이 줄어든다. 마치 편의점 계산대에서 물건 1개인 사람을 먼저 보내는 것과 같다.

핵심 용어:
- **반환시간 (turnaround)** = 작업 완료 시각 − 요청 시각
- 구해야 하는 것 = 모든 작업 반환시간의 평균

왜 힙인가?
- 매 시점 "지금 도착해 있는 작업 중 소요시간 최소"를 빠르게 꺼내야 한다
- 작업이 시간순으로 계속 추가되므로 **동적으로 최솟값이 바뀌는 상황** → Min Heap

#### 풀이 전략

```
[전체 흐름]

작업을 요청시각 순으로 정렬
              ↓
         현재 시각(clock) 이하 도착 작업을 힙에 투입
              ↓
         ┌─ 힙 비어있나? ──→ YES → clock을 다음 도착시각으로 점프
         │       ↓ NO
         │  소요시간 최소 작업을 pop
         │       ↓
         │  clock += 소요시간
         │  반환시간 누적 += clock - 요청시각
         │       ↓
         └── 모든 작업 완료? ──→ YES → 평균 반환
                   ↓ NO
              (반복)
```

주의 포인트:
- **유휴 시간 처리**: 힙이 비었는데 아직 도착 안 한 작업이 있으면, clock을 강제로 다음 도착 시각으로 옮겨야 한다. 빠뜨리면 무한 루프.
- **힙 키 설정**: `(소요시간, 요청시각)` 순서로 넣어야 소요시간 기준 최소가 먼저 나온다.

#### 소스코드

**Python**

```python
import heapq

def optimal_schedule(task_list):
    """모든 작업의 평균 반환시간을 최소화하는 스케줄링"""
    # 1. 요청시각 기준 정렬
    ordered = sorted(task_list, key=lambda x: x[0])
    total_tasks = len(ordered)

    ready_queue = []       # (소요시간, 요청시각) Min Heap
    clock = 0              # 현재 시각
    pointer = 0            # 다음 확인할 작업 인덱스
    turnaround_sum = 0     # 반환시간 합계
    finished = 0           # 완료 작업 수

    while finished < total_tasks:
        # 2. 현재 시각까지 도착한 작업을 힙에 투입
        while pointer < total_tasks and ordered[pointer][0] <= clock:
            arrive, length = ordered[pointer]
            heapq.heappush(ready_queue, (length, arrive))
            pointer += 1

        # 3. 처리할 작업이 있으면 실행
        if ready_queue:
            length, arrive = heapq.heappop(ready_queue)
            clock += length                      # 작업 수행
            turnaround_sum += (clock - arrive)    # 반환시간 누적
            finished += 1
        else:
            # 4. 유휴 상태: 다음 작업 도착까지 시계 점프
            clock = ordered[pointer][0]

    return turnaround_sum // total_tasks

# --- 실행 ---
jobs = [[0, 3], [1, 9], [2, 6]]
print(optimal_schedule(jobs))  # 9
```

**Java**

```java
import java.util.*;

public class TaskScheduler {
    public static int optimalSchedule(int[][] taskList) {
        // 1. 요청시각 기준 정렬
        Arrays.sort(taskList, (a, b) -> a[0] - b[0]);
        int totalTasks = taskList.length;

        // Min Heap: 소요시간 우선, 같으면 요청시각 우선
        PriorityQueue<int[]> readyQueue =
            new PriorityQueue<>((a, b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        int clock = 0, pointer = 0, finished = 0;
        long turnaroundSum = 0;

        while (finished < totalTasks) {
            // 2. 현재 시각까지 도착한 작업 투입
            while (pointer < totalTasks && taskList[pointer][0] <= clock) {
                // (소요시간, 요청시각) 순서로 저장
                readyQueue.offer(new int[]{taskList[pointer][1], taskList[pointer][0]});
                pointer++;
            }

            // 3. 처리할 작업 실행
            if (!readyQueue.isEmpty()) {
                int[] picked = readyQueue.poll();
                clock += picked[0];                         // 작업 수행
                turnaroundSum += (clock - picked[1]);       // 반환시간 누적
                finished++;
            } else {
                // 4. 유휴: 다음 도착까지 점프
                clock = taskList[pointer][0];
            }
        }
        return (int)(turnaroundSum / totalTasks);
    }

    public static void main(String[] args) {
        int[][] jobs = {{0, 3}, {1, 9}, {2, 6}};
        System.out.println(optimalSchedule(jobs));  // 9
    }
}
```

**코드 흐름 설명 (예시: `[[0,3], [1,9], [2,6]]`)**

| clock | 동작 | 힙 상태 | 반환시간 |
|-------|------|---------|---------|
| 0 | 작업A(0,3) 투입 → pop → 수행 | `[]` | clock=3, 3-0=3 |
| 3 | 작업B(1,9), C(2,6) 투입 → C가 더 짧아 pop | `[(9,1)]` | clock=9, 9-2=7 |
| 9 | 작업B pop → 수행 | `[]` | clock=18, 18-1=17 |
| 합계 | | | 3+7+17=27, 27/3=**9** |

---

### 문제 3: 양방향 우선순위 큐 (프로그래머스 "이중 우선순위 큐" 유형)

#### 핵심 개념

일반 힙은 **한쪽 극값**만 빠르게 꺼낼 수 있다. 이 문제는 **최댓값 삭제와 최솟값 삭제를 모두** 요구한다.

접근법 3가지:

| 방법 | 삽입 | 최대 삭제 | 최소 삭제 | 적합 상황 |
|------|------|----------|----------|----------|
| 정렬 리스트 | O(N) | O(1) | O(1) | 데이터 적을 때 |
| TreeMap(균형BST) | O(log N) | O(log N) | O(log N) | 범용 |
| 이중 힙 + 동기화 | O(log N) | O(log N)* | O(log N)* | 힙 연습용 |

이 문제에서 핵심 함정:
- 빈 큐에 삭제 명령 → **무시** (에러 아님)
- 같은 값이 여러 번 들어올 수 있음 → 중복 처리 필수
- 모든 명령 후 비어있으면 `[0, 0]` 반환

#### 풀이 전략

```
[전체 흐름]

명령어 순회
    ↓
┌─ "I 숫자" → 자료구조에 삽입
│
├─ "D 1"  → 비어있으면 무시, 아니면 최댓값 삭제
│
├─ "D -1" → 비어있으면 무시, 아니면 최솟값 삭제
│
└─ 모든 명령 완료 후
       ↓
   비어있나? → YES → [0, 0]
              NO  → [최댓값, 최솟값]
```

#### 소스코드

**Python (정렬 리스트 방식 — 직관적)**

```python
import bisect

def dual_pq(command_list):
    """이중 우선순위 큐: 최대/최소 양방향 삭제 지원"""
    container = []

    for command in command_list:
        action, number = command.split()
        number = int(number)

        if action == 'I':
            # 정렬 상태를 유지하며 삽입 (이진 탐색으로 위치 결정)
            bisect.insort(container, number)
        elif container:                 # 비어있으면 무시
            if number == 1:
                container.pop()         # 맨 뒤 = 최댓값 제거
            else:
                container.pop(0)        # 맨 앞 = 최솟값 제거

    if container:
        return [container[-1], container[0]]
    return [0, 0]

# --- 실행 ---
cmds1 = ["I 7", "I 5", "I -5", "D -1"]
print(dual_pq(cmds1))  # [7, 5]

cmds2 = ["I 16", "D 1"]
print(dual_pq(cmds2))  # [0, 0]
```

**코드 흐름 설명**

1. `bisect.insort`는 이진 탐색으로 삽입 위치를 찾아 정렬 상태를 유지한다.
2. 정렬된 리스트이므로 `[-1]`이 최대, `[0]`이 최소다.
3. 삽입 O(N), 삭제 O(1)이므로 데이터가 적을 때 적합하다.

**Java (TreeMap 방식 — 효율적)**

```java
import java.util.TreeMap;

public class BiDirectionalPQ {
    public static int[] dualPQ(String[] commands) {
        // TreeMap: key=값, value=등장횟수 (중복 허용)
        TreeMap<Integer, Integer> storage = new TreeMap<>();

        for (String cmd : commands) {
            String[] parts = cmd.split(" ");
            String action = parts[0];
            int number = Integer.parseInt(parts[1]);

            if (action.equals("I")) {
                // 삽입: 기존 카운트 + 1
                storage.merge(number, 1, Integer::sum);
            } else if (!storage.isEmpty()) {
                // 삭제: number=1이면 최댓값, -1이면 최솟값
                int targetKey = (number == 1)
                    ? storage.lastKey()    // 최대
                    : storage.firstKey();  // 최소

                // 카운트 감소, 0이 되면 키 자체 제거
                if (storage.get(targetKey) == 1) {
                    storage.remove(targetKey);
                } else {
                    storage.merge(targetKey, -1, Integer::sum);
                }
            }
        }

        if (storage.isEmpty()) return new int[]{0, 0};
        return new int[]{storage.lastKey(), storage.firstKey()};
    }

    public static void main(String[] args) {
        String[] cmds = {"I 7", "I 5", "I -5", "D -1"};
        int[] result = dualPQ(cmds);
        System.out.println(result[0] + ", " + result[1]);  // 7, 5
    }
}
```

**코드 흐름 설명**

1. `TreeMap`은 Red-Black Tree 기반이라 삽입/삭제/최대/최소 모두 O(log N)이다.
2. `merge(key, 1, Integer::sum)`으로 중복 값의 카운트를 관리한다.
3. `lastKey()`가 최댓값, `firstKey()`가 최솟값이다.
4. 삭제 시 카운트가 0이 되면 키를 완전히 제거해야 빈 큐 판정이 올바르게 된다.

**흐름 추적 (예시: `["I 7", "I 5", "I -5", "D -1"]`)**

| 명령 | 동작 | 저장 상태 |
|------|------|----------|
| I 7 | 7 삽입 | `{7:1}` |
| I 5 | 5 삽입 | `{5:1, 7:1}` |
| I -5 | -5 삽입 | `{-5:1, 5:1, 7:1}` |
| D -1 | 최솟값(-5) 삭제 | `{5:1, 7:1}` |
| 결과 | 최대=7, 최소=5 | **[7, 5]** |

---

## 자주 하는 실수

### 1. Python heapq가 Min Heap이라는 사실을 잊는다

C++은 기본이 Max Heap, Python/Java는 Min Heap이다. 최댓값을 원하면 Python은 **부호 반전**, Java는 `reverseOrder()`, C++은 기본이 이미 Max다.

### 2. 힙 원소 부족 상태에서 pop 시도

"더 맵게"처럼 2개를 꺼내야 할 때 1개만 남아 있으면 런타임 에러. **항상 크기 체크 먼저**.

### 3. 정렬된 배열과 힙을 혼동

`[1, 5, 3, 8, 7]`도 유효한 Min Heap이다. 전체가 오름차순일 필요 없다. 보장은 **루트=최솟값** 뿐.

### 4. 디스크 컨트롤러 유휴 시간 미처리

힙이 비었는데 미도착 작업이 있으면 clock을 강제 점프해야 한다. 안 하면 무한 루프.

### 5. 이중 우선순위 큐 빈 큐 삭제

빈 상태에서 D 명령 → 에러가 아니라 **무시**다.

---

## 언제 사용하면 좋은가

| 신호 | 예시 |
|------|------|
| "가장 작은(큰) K개" | 매출 상위 K개 구하기 |
| "매번 최소/최대를 꺼내야" | 작업 스케줄링, 허프만 코딩 |
| "합치기를 반복" | 돌 합치기, 음식 섞기 |
| "실시간으로 중앙값" | 이중 힙 (Max Heap + Min Heap) |
| "다익스트라 최단 경로" | 그래프 가중치 탐색 |
| "시뮬레이션에서 이벤트 순서" | 가장 빠른 이벤트부터 처리 |

---

## 요약 정리

| 항목 | 내용 |
|------|------|
| 자료구조 | 완전 이진 트리 (배열로 구현) |
| 핵심 연산 | push O(log N), pop O(log N), peek O(1) |
| Min Heap | 부모 ≤ 자식 → 루트 = 최솟값 |
| Max Heap | 부모 ≥ 자식 → 루트 = 최댓값 |
| Python 기본 | `heapq` → Min Heap (Max는 부호 반전) |
| Java 기본 | `PriorityQueue` → Min Heap (Max는 reverseOrder) |
| C++ 기본 | `priority_queue` → **Max Heap** (Min은 greater) |
| 더 맵게 | Min Heap으로 최솟값 2개 반복 추출 |
| 디스크 컨트롤러 | Min Heap(소요시간 기준) + SJF 전략 |
| 이중 우선순위 큐 | TreeMap 또는 정렬 리스트로 양방향 삭제 |

---

# 메타데이터
```json
{
  "category": "[자료구조] 힙과 우선순위 큐",
  "algorithm": "힙",
  "source_type": "generated",
  "style": ["easy", "code", "analogy", "theory"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "java"
}
```

---

