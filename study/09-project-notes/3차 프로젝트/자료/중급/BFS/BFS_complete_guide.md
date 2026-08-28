# 제목
[알고리즘] BFS(너비 우선 탐색) 완전 정복 — 큐 기반 탐색, 최단 거리, 동시 확산

# 본문

## 한줄 요약

BFS는 "시작점에서 가까운 노드부터 넓게 퍼지며 탐색"하는 기법으로, 동일 가중치 그래프에서 최단 거리를 보장한다.

---

## 왜 필요한가

지하철 노선도에서 A역에서 B역까지 **최소 환승 경로**를 찾는다고 생각해 보자. 한 정거장씩 갈 수 있는 모든 역을 먼저 확인하고, 다음에 두 정거장 거리인 역들을 확인하면 B역에 처음 도달한 순간이 곧 최소 환승이다.

이것이 BFS의 원리다. **거리 1인 곳을 전부 처리 → 거리 2인 곳을 전부 처리 → ...** 이렇게 레벨 단위로 확장하므로, 어떤 노드에 **처음 도달한 거리 = 최단 거리**가 된다.

배열을 매번 정렬하거나 모든 경로를 일일이 비교하는 것보다 훨씬 효율적이다.

---

## 핵심 개념

### 1. 큐(Queue)와 FIFO

BFS의 엔진은 **큐(Queue)**다. 먼저 넣은 것을 먼저 꺼내는 FIFO(First-In First-Out) 구조 덕분에, 가까운 노드가 항상 먼저 처리된다.

- Python: `collections.deque` (popleft O(1))
- Java: `LinkedList` 또는 `ArrayDeque`
- C++: `queue<int>`

주의: Python 리스트의 `pop(0)`은 O(N)이므로 반드시 `deque`를 쓴다.

### 2. 방문 표시 시점

큐에 **넣는 즉시** 방문 표시해야 한다. 꺼낼 때 표시하면 같은 노드가 큐에 여러 번 들어가서 메모리 낭비와 오답이 발생한다.

```
# ❌ 잘못됨
node = queue.popleft()
visited[node] = True     # 이미 큐에 중복 삽입됐을 수 있음

# ✅ 올바름
visited[neighbor] = True  # 넣기 직전
queue.append(neighbor)
```

### 3. 격자 탐색에서의 방향 벡터

격자 문제에서 상하좌우 이동을 배열로 미리 정의하면 코드가 깔끔해진다.

```
dr = [-1, 1, 0, 0]   # 행 변화: 위, 아래
dc = [0, 0, -1, 1]   # 열 변화: 왼, 오
```

### 4. 시간 복잡도

| 그래프 표현 | 시간 복잡도 |
|------------|-----------|
| 인접 리스트 | O(V + E) |
| 인접 행렬 | O(V²) |
| N×M 격자 | O(N × M) |

V = 노드 수, E = 간선 수

---

## 동작 흐름

```
그래프:  0 — 1 — 3
         |   |
         2   4

시작: 0

큐: [0]              방문: {0}
 ↓ pop 0 → 이웃 1, 2를 push
큐: [1, 2]           방문: {0, 1, 2}
 ↓ pop 1 → 이웃 3, 4를 push (0은 방문 완료)
큐: [2, 3, 4]        방문: {0, 1, 2, 3, 4}
 ↓ pop 2 → 미방문 이웃 없음
큐: [3, 4]
 ↓ pop 3 → pop 4
큐: []               탐색 완료

방문 순서: 0 → 1 → 2 → 3 → 4
거리:       0   1   1   2   2
```

핵심: 거리 1인 노드(1, 2)가 거리 2인 노드(3, 4)보다 항상 먼저 처리된다.

---

## Text Flow Chart

### BFS 격자 탐색

```
시작 좌표를 큐에 넣고 방문 표시
        ↓
   ┌─ 큐 비었나? ──→ YES → 탐색 종료
   │       ↓ NO
   │  큐에서 (row, col) 꺼냄
   │       ↓
   │  상하좌우 4방향 반복:
   │    ├─ 범위 밖? → 건너뜀
   │    ├─ 벽(0)? → 건너뜀
   │    ├─ 이미 방문? → 건너뜀
   │    └─ 통과 → 큐에 넣고 방문 표시
   │       ↓
   └───────┘ (반복)
```

---

## 기본 코드 템플릿

### Python

```python
from collections import deque

def bfs_traverse(adjacency, start_node):
    """인접 리스트 그래프에서 BFS 순서를 반환한다"""
    checked = set([start_node])
    order = []
    queue = deque([start_node])

    while queue:
        current = queue.popleft()
        order.append(current)

        for neighbor in adjacency[current]:
            if neighbor not in checked:
                checked.add(neighbor)
                queue.append(neighbor)

    return order

# --- 실행 ---
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}
print(bfs_traverse(graph, 0))  # [0, 1, 2, 3, 4]
```

**코드 흐름 설명**

1. 시작 노드를 큐에 넣고 방문 집합에 추가한다.
2. `popleft()`로 큐 앞에서 꺼내 처리한다.
3. 이웃 중 미방문 노드를 발견하면 **즉시** 방문 표시 후 큐에 추가한다.
4. 큐가 빌 때까지 반복하면 모든 연결 노드를 방문한다.

### Java

```java
import java.util.*;

public class BFSTemplate {
    public static List<Integer> bfsTraverse(Map<Integer, List<Integer>> adj, int startNode) {
        List<Integer> order = new ArrayList<>();
        Set<Integer> checked = new HashSet<>();
        Queue<Integer> queue = new LinkedList<>();

        queue.offer(startNode);
        checked.add(startNode);

        while (!queue.isEmpty()) {
            int current = queue.poll();
            order.add(current);

            for (int neighbor : adj.get(current)) {
                if (!checked.contains(neighbor)) {
                    checked.add(neighbor);
                    queue.offer(neighbor);
                }
            }
        }
        return order;
    }
}
```

### C++

```cpp
#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<int> adj[100];
bool checked[100];

void bfs_traverse(int start) {
    queue<int> q;
    q.push(start);
    checked[start] = true;

    while (!q.empty()) {
        int cur = q.front(); q.pop();
        cout << cur << " ";

        for (int nxt : adj[cur]) {
            if (!checked[nxt]) {
                checked[nxt] = true;
                q.push(nxt);
            }
        }
    }
}
```

---

## 실전 문제 풀이

---

### 문제 1: 격자 미로 최단 거리

#### 핵심 개념

**"1과 0으로 이루어진 격자에서 출발점→도착점 최소 이동 횟수를 구하라"**

왜 BFS인가?
- 모든 칸 사이의 이동 비용이 1로 동일하다.
- BFS는 거리 1인 칸 → 거리 2인 칸 순서로 탐색하므로, **도착점에 처음 도달한 거리 = 최단 거리**다.
- DFS로 풀면 한 경로를 끝까지 탐색한 뒤 돌아오기 때문에 최단 보장이 안 된다.

핵심 기법: **dist 배열에 거리 누적**
- `dist[r][c] = 0` → 미방문
- `dist[r][c] = k` → 시작점에서 k칸 거리
- 시작점의 dist를 1로 설정하면, 0과 구분하여 "미방문" 판별이 가능하다.

종료 조건:
- 도착점 방문 시 → `dist[도착] - 1` 반환
- 큐가 비었는데 도착점 미방문 → -1 (경로 없음)

#### 풀이 전략

```
[전체 흐름]

시작점을 큐에 넣고 dist[sr][sc] = 1
           ↓
      ┌─ 큐 비었나? ──→ YES → -1 (경로 없음)
      │       ↓ NO
      │  (r, c) 꺼냄
      │       ↓
      │  도착점인가? → YES → dist[r][c] - 1 반환
      │       ↓ NO
      │  상하좌우 4방향:
      │    범위 내 & 길(1) & dist==0?
      │      → dist[nr][nc] = dist[r][c] + 1
      │      → 큐에 추가
      └───────┘ (반복)
```

왜 dist 시작값이 1인가?
- 0은 "미방문"을 의미하도록 쓰기 위해서다.
- 실제 거리는 `dist값 - 1`로 환산한다.

#### 소스코드

**Python**

```python
from collections import deque

def maze_shortest(grid, sr, sc, gr, gc):
    """격자 미로에서 (sr,sc)→(gr,gc) 최소 이동 횟수, 불가능하면 -1"""
    rows, cols = len(grid), len(grid[0])
    dist = [[0] * cols for _ in range(rows)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque([(sr, sc)])
    dist[sr][sc] = 1

    while queue:
        r, c = queue.popleft()

        if r == gr and c == gc:
            return dist[r][c] - 1

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1 and dist[nr][nc] == 0:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return -1

# --- 실행 ---
maze = [
    [1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1],
    [0, 0, 1, 1, 1]
]
print(maze_shortest(maze, 0, 0, 4, 4))  # 8
```

**Java**

```java
import java.util.*;

public class MazeSolver {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static int mazeShortest(int[][] grid, int sr, int sc, int gr, int gc) {
        int rows = grid.length, cols = grid[0].length;
        int[][] dist = new int[rows][cols];

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{sr, sc});
        dist[sr][sc] = 1;

        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int r = pos[0], c = pos[1];

            if (r == gr && c == gc) return dist[r][c] - 1;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                if (grid[nr][nc] == 1 && dist[nr][nc] == 0) {
                    dist[nr][nc] = dist[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[][] maze = {
            {1,0,1,0,1},{1,1,1,0,1},{0,0,1,1,1},{0,0,1,1,1},{0,0,1,1,1}
        };
        System.out.println(mazeShortest(maze, 0, 0, 4, 4)); // 8
    }
}
```

**코드 흐름 설명**

| 단계 | pop 좌표 | dist 갱신 대상 | 설명 |
|------|---------|--------------|------|
| 초기 | - | dist[0][0]=1 | 시작점 투입 |
| 1 | (0,0) | (1,0)=2 | 아래로 1칸 |
| 2 | (1,0) | (1,1)=3 | 오른쪽 1칸 |
| 3 | (1,1) | (1,2)=4 | 오른쪽 1칸 |
| ... | ... | 거리 순으로 확장 | ... |
| 마지막 | (4,4) 도달 | dist=9 | 답: 9-1=**8** |

---

### 문제 2: 동시 확산 시뮬레이션 (Multi-Source BFS — "토마토" 유형)

#### 핵심 개념

**"여러 시작점에서 동시에 퍼져나가 모든 칸을 채우는 데 걸리는 최소 일수"**

왜 Multi-Source BFS인가?
- 시작점이 여러 개다. 각각 BFS를 따로 돌리면 O(시작점수 × N × M)이 된다.
- 모든 시작점을 **처음부터 큐에 한꺼번에 넣으면**, 물에 돌 여러 개를 동시에 던진 것처럼 파문이 동시에 퍼진다 → O(N × M) 한 번으로 끝난다.

일반 BFS와 차이:

| | 일반 BFS | Multi-Source BFS |
|--|---------|-----------------|
| 초기 큐 | 시작점 1개 | 시작점 전부 투입 |
| 나머지 | 동일 | 동일 |

문제 설정:
- 격자에 익은 토마토(1), 안 익은 토마토(0), 빈 칸(-1)
- 익은 토마토는 매일 상하좌우로 인접한 안 익은 토마토를 익힌다
- 모든 토마토가 익는 최소 일수, 불가능하면 -1

#### 풀이 전략

```
[전체 흐름]

1. 격자 전체 탐색 → 익은 토마토(1) 좌표를 모두 큐에 투입 (day=0)
              ↓
2. BFS 시작 (일반 BFS와 동일한 반복문)
   큐에서 꺼내기 → 4방향 → 0인 칸에 day+1 기록 후 큐 추가
              ↓
3. BFS 종료 후:
   격자에 0이 남아있으면 → -1
   0이 없으면 → day 배열 최댓값이 정답
```

주의:
- 빈 칸(-1)은 장애물. 방문 대상 아님.
- 처음부터 모든 토마토가 익어있으면 답은 0.

#### 소스코드

**Python**

```python
from collections import deque

def ripen_days(box):
    """모든 토마토가 익는 최소 일수, 불가능하면 -1"""
    rows, cols = len(box), len(box[0])
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = deque()
    elapsed = [[0] * cols for _ in range(rows)]

    # 1단계: 모든 익은 토마토를 큐에 한꺼번에 투입
    for r in range(rows):
        for c in range(cols):
            if box[r][c] == 1:
                queue.append((r, c))

    # 2단계: Multi-Source BFS
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < rows and 0 <= nc < cols:
                if box[nr][nc] == 0:
                    box[nr][nc] = 1
                    elapsed[nr][nc] = elapsed[r][c] + 1
                    queue.append((nr, nc))

    # 3단계: 결과 판정
    longest = 0
    for r in range(rows):
        for c in range(cols):
            if box[r][c] == 0:
                return -1
            longest = max(longest, elapsed[r][c])

    return longest

# --- 실행 ---
tomato = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1]
]
print(ripen_days(tomato))  # 8
```

**Java**

```java
import java.util.*;

public class TomatoSolver {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};

    public static int ripenDays(int[][] box) {
        int rows = box.length, cols = box[0].length;
        int[][] elapsed = new int[rows][cols];
        Queue<int[]> queue = new LinkedList<>();

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (box[r][c] == 1)
                    queue.offer(new int[]{r, c});

        while (!queue.isEmpty()) {
            int[] pos = queue.poll();
            int r = pos[0], c = pos[1];
            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i], nc = c + dc[i];
                if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
                if (box[nr][nc] == 0) {
                    box[nr][nc] = 1;
                    elapsed[nr][nc] = elapsed[r][c] + 1;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }

        int longest = 0;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++) {
                if (box[r][c] == 0) return -1;
                longest = Math.max(longest, elapsed[r][c]);
            }
        return longest;
    }

    public static void main(String[] args) {
        int[][] box = {
            {0,0,0,0,0,0},{0,0,0,0,0,0},{0,0,0,0,0,0},{0,0,0,0,0,1}
        };
        System.out.println(ripenDays(box)); // 8
    }
}
```

**코드 흐름 설명**

```
초기 (4×6):             elapsed 결과:
0 0 0 0 0 0             8 7 6 5 4 3
0 0 0 0 0 0             7 6 5 4 3 2
0 0 0 0 0 0             6 5 4 3 2 1
0 0 0 0 0 1             5 4 3 2 1 0
                                 ↑ 시작점
```

| 일차 | 새로 익는 칸 | 큐 크기 |
|------|------------|---------|
| 0 | (3,5) 초기 | 1 |
| 1 | (2,5), (3,4) | 2 |
| 2 | (1,5), (2,4), (3,3) | 3 |
| ... | 왼쪽·위로 파문 확산 | ... |
| 8 | (0,0) 마지막 | **최종: 8** |

---

## 자주 하는 실수

### 1. 방문 표시를 꺼낼 때 한다

큐에 넣는 즉시 표시하지 않으면 같은 노드가 여러 번 큐에 들어간다. 메모리 초과와 시간 초과의 주범이다.

### 2. Python에서 리스트를 큐로 사용한다

`list.pop(0)`은 O(N)이다. N이 10만이면 BFS 전체가 O(N²)로 느려진다. 반드시 `deque`를 쓰자.

### 3. 격자 범위를 체크하지 않는다

`grid[nr][nc]` 접근 전에 반드시 `0 ≤ nr < rows`, `0 ≤ nc < cols`를 확인해야 한다.

### 4. Multi-Source BFS를 시작점마다 따로 돌린다

시작점 K개를 각각 BFS 돌리면 O(K × N × M). 전부 큐에 넣고 한 번만 돌리면 O(N × M).

### 5. dist 배열 초기값과 방문 판별을 혼동한다

dist[r][c]=0을 "거리 0"과 "미방문" 두 가지 의미로 쓰면 충돌한다. 시작점 dist를 1로 설정하거나 별도 visited 배열을 사용하자.

---

## 언제 사용하면 좋은가

| 신호 | 예시 |
|------|------|
| "최단 거리" / "최소 횟수" | 미로 탈출, 단어 변환 |
| "가장 가까운 ~" | 가장 가까운 출구까지 거리 |
| "동시에 퍼짐" / "전염" | 토마토 익히기, 불 확산, 바이러스 전파 |
| "레벨 단위 탐색" | 트리 레벨 순회 |
| "가중치 1인 그래프" | 모든 간선 비용 동일 |

한 줄 판별: **"최단" 또는 "최소"가 보이고, 가중치가 동일하면 → BFS**

---

## 요약 정리

| 항목 | 내용 |
|------|------|
| 자료구조 | 큐 (deque / LinkedList / queue) |
| 탐색 순서 | 가까운 곳 → 먼 곳 (레벨 단위) |
| 최단 거리 보장 | O (동일 가중치 한정) |
| 시간복잡도 | O(V + E) / 격자: O(N × M) |
| 핵심 기법 | dist 배열 거리 누적 |
| Multi-Source | 시작점 전부 초기 큐에 투입 |
| Python 주의 | deque 필수, list.pop(0) 금지 |
| 방문 표시 | 큐에 넣는 즉시 (꺼낼 때 아님) |

---

# 메타데이터
```json
{
  "category": "[기초 알고리즘] 그래프 탐색",
  "algorithm": "BFS",
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

```
변환 검수
- 원문 문장을 그대로 사용하지 않았는가: 예
- 원문 목차 구조를 그대로 따르지 않았는가: 예
- 원문 비유를 그대로 사용하지 않았는가: 예
- 원문 코드의 변수명과 주석을 그대로 사용하지 않았는가: 예
- 원문 이미지를 재사용하지 않았는가: 예
- 개념 설명의 정확성을 유지했는가: 예
- 초급자가 이해할 수 있는 흐름으로 재작성했는가: 예
```
