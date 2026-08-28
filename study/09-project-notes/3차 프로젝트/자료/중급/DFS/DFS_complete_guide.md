# 제목
[알고리즘] DFS(깊이 우선 탐색) 완전 정복 — 재귀/스택 탐색, 영역 탐색, 백트래킹

# 본문

## 한줄 요약

DFS는 "한 방향으로 끝까지 파고든 뒤, 막히면 되돌아와 다른 길을 탐색"하는 기법으로, 연결 영역 탐색과 모든 경우의 수 탐색에 핵심이 된다.

---

## 왜 필요한가

미로 속에서 출구를 찾는 상황을 떠올려 보자. 갈림길이 나타나면 **한쪽 길을 끝까지 가본다**. 막다른 골목이면 마지막 갈림길로 돌아와 다른 길을 시도한다. 이것이 DFS의 원리다.

DFS가 빛나는 순간:
- **"연결된 덩어리가 몇 개?"** → 하나의 덩어리를 DFS로 전부 방문 처리한 뒤 카운터+1
- **"가능한 모든 조합/순열을 구하라"** → DFS + 백트래킹으로 경우의 수 탐색
- **"경로가 존재하는가?"** → DFS로 도달 가능 여부 확인

BFS와 달리 **최단 거리를 보장하지 않지만**, 코드가 간결하고 재귀로 자연스럽게 구현되기 때문에 "전부 탐색" 유형에서 자주 사용된다.

---

## 핵심 개념

### 1. 재귀 호출과 콜 스택

DFS의 가장 직관적인 구현은 재귀다. 함수가 자기 자신을 호출하면서 깊이 파고들고, 함수가 종료(return)되면 이전 갈림길로 자동 복귀한다.

```
dfs(A) 호출
  → dfs(B) 호출
    → dfs(D) 호출
      → 미방문 이웃 없음 → return
    → dfs(E) 호출
      → return
  → return
→ dfs(C) 호출
  → return
```

내부적으로 **콜 스택**이 갈림길을 기억해주기 때문에, 별도 스택 자료구조 없이도 DFS가 동작한다.

### 2. 스택 기반 DFS (반복문)

재귀 대신 명시적 스택을 사용해도 동일한 결과를 얻는다. Python 재귀 제한이 걱정되거나 깊이가 극단적으로 깊을 때 유용하다.

```
스택에 시작 노드 push
while 스택이 비어있지 않으면:
    node = 스택에서 pop
    if 미방문이면:
        방문 처리
        이웃 노드들을 스택에 push
```

### 3. DFS vs BFS 핵심 차이

| 항목 | DFS | BFS |
|------|-----|-----|
| 자료구조 | 스택 / 재귀 (LIFO) | 큐 (FIFO) |
| 탐색 방향 | 깊게 (분기 단위) | 넓게 (레벨 단위) |
| 최단 거리 | 보장 X | 보장 O (동일 가중치) |
| 메모리 | 깊은 그래프에서 큼 | 넓은 그래프에서 큼 |
| 주요 용도 | 연결 요소, 백트래킹, 사이클 | 최단 경로, 레벨 순회 |

### 4. 시간 복잡도

| 그래프 표현 | 시간 복잡도 |
|------------|-----------|
| 인접 리스트 | O(V + E) |
| 인접 행렬 | O(V²) |
| N×M 격자 | O(N × M) |

### 5. 방문 표시의 역할

DFS에서 방문 표시를 하지 않으면 그래프에 사이클이 있을 때 무한 루프에 빠진다. 격자에서는 이미 방문한 칸을 다시 방문하면 무한 재귀가 발생한다.

---

## 동작 흐름

### 재귀 DFS

```
그래프:  0 — 1 — 3
         |   |
         2   4

시작: 0

call dfs(0)  → 방문 {0}
  이웃 [1, 2] 중 미방문 1 선택
  call dfs(1)  → 방문 {0, 1}
    이웃 [0, 3, 4] 중 미방문 3 선택
    call dfs(3)  → 방문 {0, 1, 3}
      이웃 [1] → 전부 방문 완료 → return
    미방문 4 선택
    call dfs(4)  → 방문 {0, 1, 3, 4}
      이웃 [1] → 전부 방문 완료 → return
    1의 이웃 탐색 완료 → return
  미방문 2 선택
  call dfs(2)  → 방문 {0, 1, 2, 3, 4}
    이웃 [0] → 전부 방문 완료 → return
  0의 이웃 탐색 완료

방문 순서: 0 → 1 → 3 → 4 → 2
```

### 스택 DFS

```
스택: [0]              방문: {}
 ↓ pop 0 → 미방문 → 방문 처리 → 이웃 1, 2 push
스택: [2, 1]           방문: {0}
 ↓ pop 1 → 미방문 → 방문 처리 → 이웃 3, 4 push
스택: [2, 4, 3]        방문: {0, 1}
 ↓ pop 3 → 미방문 → 방문 처리
스택: [2, 4]           방문: {0, 1, 3}
 ↓ pop 4 → 미방문 → 방문 처리
스택: [2]              방문: {0, 1, 3, 4}
 ↓ pop 2 → 미방문 → 방문 처리
스택: []               방문: {0, 1, 2, 3, 4}

방문 순서: 0 → 1 → 3 → 4 → 2
```

---

## Text Flow Chart

### DFS 재귀 격자 탐색

```
dfs(row, col) 호출
        ↓
   방문 표시
        ↓
   상하좌우 4방향 반복:
     ├─ 범위 밖? → 건너뜀
     ├─ 벽(0)? → 건너뜀
     ├─ 이미 방문? → 건너뜀
     └─ 통과 → dfs(newRow, newCol) 재귀 호출
        ↓
   4방향 모두 완료 → 자동 복귀 (return)
```

### DFS 백트래킹 패턴

```
dfs(현재 상태)
        ↓
   종료 조건 충족? → YES → 결과 저장/출력, return
        ↓ NO
   가능한 선택지 반복:
     ├─ 선택 (상태 변경)
     ├─ dfs(다음 상태) 재귀 호출
     └─ 선택 취소 (상태 복원) ← 핵심: 백트래킹
        ↓
   모든 선택지 시도 완료 → return
```

---

## 기본 코드 템플릿

### Python — 재귀 DFS

```python
def dfs_traverse(adjacency, node, visited, order):
    """인접 리스트 그래프에서 DFS 순서를 기록한다"""
    visited.add(node)
    order.append(node)

    for neighbor in adjacency[node]:
        if neighbor not in visited:
            dfs_traverse(adjacency, neighbor, visited, order)

# --- 실행 ---
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}
result = []
dfs_traverse(graph, 0, set(), result)
print(result)  # [0, 1, 3, 4, 2]
```

### Python — 스택 DFS (반복문)

```python
def dfs_stack(adjacency, start_node):
    """스택을 이용한 반복문 DFS"""
    visited = set()
    order = []
    stack = [start_node]

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        order.append(node)

        # 역순으로 넣어야 왼쪽 이웃이 먼저 pop됨
        for neighbor in reversed(adjacency[node]):
            if neighbor not in visited:
                stack.append(neighbor)

    return order

# --- 실행 ---
graph = {0: [1, 2], 1: [0, 3, 4], 2: [0], 3: [1], 4: [1]}
print(dfs_stack(graph, 0))  # [0, 1, 3, 4, 2]
```

**코드 흐름 설명**

1. 재귀 DFS: 현재 노드 방문 → 미방문 이웃 발견 시 즉시 재귀 호출 → 자연스럽게 깊이 우선
2. 스택 DFS: pop으로 꺼내서 미방문이면 처리. 이웃을 역순으로 push해야 재귀와 동일한 순서가 된다.
3. 스택 DFS에서는 pop 후 방문 체크를 하므로 중복 push가 발생할 수 있지만, `if node in visited: continue`로 걸러낸다.

### Java — 재귀 DFS

```java
import java.util.*;

public class DFSTemplate {
    public static void dfsTraverse(Map<Integer, List<Integer>> adj,
                                   int node, Set<Integer> visited, List<Integer> order) {
        visited.add(node);
        order.add(node);

        for (int neighbor : adj.get(node)) {
            if (!visited.contains(neighbor)) {
                dfsTraverse(adj, neighbor, visited, order);
            }
        }
    }
}
```

### C++ — 재귀 DFS

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> adj[100];
bool visited[100];

void dfs_traverse(int node) {
    visited[node] = true;
    cout << node << " ";

    for (int nxt : adj[node]) {
        if (!visited[nxt]) {
            dfs_traverse(nxt);
        }
    }
}
```

---

## 실전 문제 풀이

---

### 문제 1: 영역 개수 세기 (Connected Component)

#### 핵심 개념

**"격자에서 1로 연결된 덩어리가 몇 개인지 세기"** — DFS의 대표 유형이다.

왜 DFS인가?
- 하나의 덩어리를 발견하면 **연결된 모든 칸을 한 번에 방문 처리**해야 한다.
- DFS는 연결된 곳을 끝까지 파고드므로, 한 번의 호출로 덩어리 전체를 칠할 수 있다.
- BFS로도 동일하게 풀 수 있지만, DFS 재귀가 코드 3줄로 끝나서 더 자주 사용된다.

핵심 패턴 (Flood Fill):
```
카운터 = 0
모든 칸 순회:
    if 땅(1)이고 미방문:
        DFS로 연결된 모든 땅을 방문 처리
        카운터 += 1
```

엣지 케이스:
- 격자 전체가 0 → 0개
- 격자 전체가 1 → 1개
- 대각선 연결 여부는 문제 조건 확인 (보통 상하좌우만)

#### 풀이 전략

```
[전체 흐름]

region_count = 0
               ↓
모든 (r, c) 순회
    ↓
  grid[r][c] == 1 이고 미방문?
    ↓ NO → 다음 칸
    ↓ YES
  flood(r, c) 호출 → 연결된 모든 1을 방문 처리
    ↓
  region_count += 1
    ↓
순회 종료 → region_count 반환
```

#### 소스코드

**Python**

```python
import sys
sys.setrecursionlimit(100000)

def count_regions(grid):
    """격자에서 1로 연결된 영역의 개수를 반환한다"""
    rows, cols = len(grid), len(grid[0])
    marked = [[False] * cols for _ in range(rows)]

    def flood(r, c):
        """(r,c)에서 시작해 연결된 모든 1을 방문 처리"""
        marked[r][c] = True
        for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1 and not marked[nr][nc]:
                    flood(nr, nc)

    region_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not marked[r][c]:
                flood(r, c)
                region_count += 1

    return region_count

# --- 실행 ---
land = [
    [1, 0, 1, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 0, 0, 0]
]
print(count_regions(land))  # 4
```

**Java**

```java
public class RegionFinder {
    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};
    static int rows, cols;
    static boolean[][] marked;

    public static void flood(int[][] grid, int r, int c) {
        marked[r][c] = true;
        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i], nc = c + dc[i];
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (grid[nr][nc] == 1 && !marked[nr][nc]) {
                flood(grid, nr, nc);
            }
        }
    }

    public static int countRegions(int[][] grid) {
        rows = grid.length;
        cols = grid[0].length;
        marked = new boolean[rows][cols];
        int regionCount = 0;

        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                if (grid[r][c] == 1 && !marked[r][c]) {
                    flood(grid, r, c);
                    regionCount++;
                }
        return regionCount;
    }

    public static void main(String[] args) {
        int[][] land = {
            {1,0,1,0,1},{1,1,0,0,1},{0,0,0,1,1},{0,0,0,1,1},{0,1,0,0,0}
        };
        System.out.println(countRegions(land)); // 4
    }
}
```

**코드 흐름 설명**

```
격자 시각화 (영역 번호 표시):

  A 0 B 0 C       A = 영역1 (3칸: (0,0)(1,0)(1,1))
  A A 0 0 C       B = 영역2 (1칸: (0,2))
  0 0 0 C C       C = 영역3 (6칸: (0,4)(1,4)(2,3)(2,4)(3,3)(3,4))
  0 0 0 C C       D = 영역4 (1칸: (4,1))
  0 D 0 0 0
```

| 순회 위치 | 동작 | regionCount |
|-----------|------|-------------|
| (0,0)=1, 미방문 | flood → (0,0),(1,0),(1,1) 칠함 | 1 |
| (0,2)=1, 미방문 | flood → (0,2)만 칠함 | 2 |
| (0,4)=1, 미방문 | flood → 6칸 전부 칠함 | 3 |
| (4,1)=1, 미방문 | flood → (4,1)만 칠함 | 4 |
| 나머지 | 0이거나 이미 방문 | **최종: 4** |

---

### 문제 2: 순열/조합 생성 (백트래킹)

#### 핵심 개념

**"N개 원소에서 R개를 뽑는 모든 순열(또는 조합)을 구하라"** — DFS 백트래킹의 가장 기본 유형이다.

왜 DFS인가?
- 선택의 트리를 그리면, 각 깊이에서 하나를 선택하고 다음 깊이로 내려가는 구조다.
- 깊이 R에 도달하면 하나의 순열이 완성된다 → 결과 저장 후 return.
- return하면 마지막 선택을 **취소(백트래킹)**하고 다른 선택지를 시도한다.

핵심 패턴:
```
dfs(현재 깊이, 현재까지 선택):
    if 깊이 == R:
        결과 저장
        return
    for 후보 in 전체 원소:
        if 후보를 아직 안 썼으면:
            선택 (사용 표시)
            dfs(깊이+1, 현재+후보)
            선택 취소 (사용 해제) ← 백트래킹
```

순열 vs 조합 차이:
- 순열: 순서 O, 모든 후보를 매번 검사
- 조합: 순서 X, 현재 인덱스 이후만 검사 (중복 방지)

#### 풀이 전략

```
[순열 생성 흐름]

dfs(depth, path)
        ↓
  depth == R? → YES → 결과에 path 저장, return
        ↓ NO
  0부터 N-1까지 반복:
    ├─ 이미 사용? → 건너뜀
    └─ 미사용:
       사용 표시 → path에 추가
       dfs(depth+1, path) 호출
       path에서 제거 → 사용 해제   ← 백트래킹
```

#### 소스코드

**Python — 순열**

```python
def generate_perms(elements, pick_count):
    """elements에서 pick_count개를 뽑는 모든 순열을 반환"""
    total = len(elements)
    used = [False] * total
    all_perms = []

    def explore(depth, path):
        if depth == pick_count:
            all_perms.append(path[:])  # 복사해서 저장
            return

        for i in range(total):
            if not used[i]:
                used[i] = True
                path.append(elements[i])
                explore(depth + 1, path)
                path.pop()           # 백트래킹
                used[i] = False      # 사용 해제

    explore(0, [])
    return all_perms

# --- 실행 ---
print(generate_perms([1, 2, 3], 2))
# [[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]
```

**Python — 조합**

```python
def generate_combos(elements, pick_count):
    """elements에서 pick_count개를 뽑는 모든 조합을 반환"""
    total = len(elements)
    all_combos = []

    def explore(start_idx, path):
        if len(path) == pick_count:
            all_combos.append(path[:])
            return

        for i in range(start_idx, total):   # start_idx 이후만 탐색
            path.append(elements[i])
            explore(i + 1, path)             # i+1부터 → 중복 방지
            path.pop()

    explore(0, [])
    return all_combos

# --- 실행 ---
print(generate_combos([1, 2, 3, 4], 2))
# [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
```

**Java — 순열**

```java
import java.util.*;

public class PermGenerator {
    static List<List<Integer>> allPerms = new ArrayList<>();

    public static void explore(int[] elements, boolean[] used,
                               List<Integer> path, int pickCount) {
        if (path.size() == pickCount) {
            allPerms.add(new ArrayList<>(path));
            return;
        }
        for (int i = 0; i < elements.length; i++) {
            if (!used[i]) {
                used[i] = true;
                path.add(elements[i]);
                explore(elements, used, path, pickCount);
                path.remove(path.size() - 1);  // 백트래킹
                used[i] = false;
            }
        }
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        explore(nums, new boolean[nums.length], new ArrayList<>(), 2);
        System.out.println(allPerms);
        // [[1,2],[1,3],[2,1],[2,3],[3,1],[3,2]]
    }
}
```

**코드 흐름 설명 (순열 [1,2,3]에서 2개)**

```
탐색 트리:

          (시작)
        /   |   \
      1     2     3
     / \   / \   / \
    2   3 1   3 1   2

리프 = 순열 결과
```

| 깊이 | path | 동작 |
|------|------|------|
| 0 | [] | 1 선택 |
| 1 | [1] | 2 선택 |
| 2 | [1,2] | ✅ 저장 → return → pop 2 |
| 1 | [1] | 3 선택 |
| 2 | [1,3] | ✅ 저장 → return → pop 3 → pop 1 |
| 0 | [] | 2 선택 |
| ... | ... | (이하 동일 패턴) |

---

## 자주 하는 실수

### 1. Python 재귀 깊이 제한

Python 기본 재귀 제한은 1000이다. 격자가 100×100이면 최대 10000 깊이가 필요하므로 반드시 설정해야 한다.

```python
import sys
sys.setrecursionlimit(100000)
```

### 2. 방문 표시를 빼먹는다

방문 표시 없이 DFS를 돌리면 그래프에 사이클이 있을 때 **무한 재귀**에 빠진다. 격자에서도 이전 칸을 다시 방문해 StackOverflow가 발생한다.

### 3. 백트래킹에서 상태 복원을 잊는다

`path.append()` 후 재귀를 호출했으면, 재귀 복귀 후 반드시 `path.pop()`으로 되돌려야 한다. 복원하지 않으면 다른 분기에서 잘못된 상태로 탐색하게 된다.

```python
# ❌ pop 빼먹음
path.append(elements[i])
explore(depth + 1, path)
# path에 elements[i]가 남아있는 채로 다음 i 진행

# ✅ 올바름
path.append(elements[i])
explore(depth + 1, path)
path.pop()  # 반드시 복원
```

### 4. 방향 벡터 인덱스 꼬임

`dr`과 `dc`가 엇갈리면 대각선 이동이 되거나 같은 방향을 두 번 검사한다. 항상 한 쌍씩 확인하자.

### 5. 조합에서 start_idx를 안 쓴다

조합 문제인데 모든 인덱스를 매번 탐색하면 **순열이 나온다**. 조합은 반드시 `i + 1`부터 탐색해야 중복 없는 결과가 나온다.

---

## 언제 사용하면 좋은가

| 신호 | 예시 |
|------|------|
| "연결된 영역 개수" | 섬 개수, 그림 색칠 영역 |
| "모든 경우의 수" / "순열/조합" | N개에서 R개 뽑기, 주사위 던지기 |
| "경로가 존재하는가" | A에서 B로 갈 수 있는가 |
| "조건을 만족하는 배치" | N-Queen, 스도쿠 |
| "사이클 검출" | 그래프에 순환이 있는가 |
| "트리 순회" | 전위/중위/후위 순회 |
| "백트래킹" | 제한 조건 내 최적 탐색 |

한 줄 판별: **"전부 탐색" 또는 "모든 경우"가 보이면 → DFS + 백트래킹**

---

## 요약 정리

| 항목 | 내용 |
|------|------|
| 자료구조 | 재귀 (콜 스택) 또는 명시적 스택 |
| 탐색 순서 | 한 방향 끝까지 → 되돌아와 다른 방향 |
| 최단 거리 보장 | X |
| 시간복잡도 | O(V + E) / 격자: O(N × M) |
| 영역 세기 | ✅ flood fill 패턴 |
| 순열/조합 | ✅ 백트래킹 패턴 |
| Python 주의 | `sys.setrecursionlimit` 필수 |
| 백트래킹 핵심 | 선택 → 재귀 → **선택 취소** |

---

# 메타데이터
```json
{
  "category": "[기초 알고리즘] 그래프 탐색",
  "algorithm": "DFS",
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
