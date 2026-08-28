# 제목
[알고리즘] DFS - 깊이 우선 탐색 (SW검정 알고리즘 강의)

# 링크
<https://wikidocs.net/146571>

# 본문

## DFS 이해하기

DFS를 재귀함수를 사용해서 구성할 수도 있지만, 이번에는 Stack을 활용한 DFS 코드를 작성한다.

0부터 6까지 총 7개의 노드가 존재하고 중간중간 노드를 연결해 주는 간선이 있는 그래프가 있다고 가정하자. 모든 간선을 이용하여 연결된 점을 찾는 로직을 DFS(Stack)로 구현한다.

### DFS 탐색 과정 (Stack 활용)

**step 1**: 시작점을 Stack에 저장한다.

<IMAGE>DFS stack1 - 시작 노드 0을 스택에 삽입</IMAGE>

**step 2**: Stack에서 값을 꺼내어(pop) 꺼낸 값에 연결되어 있는 값들을 다시 Stack에 넣는다.
0번 노드에 연결된 1번, 2번 노드가 차례로 Stack에 쌓인다.

<IMAGE>DFS stack2 - 0을 pop 후 연결된 1, 2를 push</IMAGE>

**step 3**: 가장 위에 있던 값 2가 빠져나간 후 5가 Stack에 저장된다.

<IMAGE>DFS stack3 - 2를 pop 후 연결된 5를 push</IMAGE>

**step 4**: 5가 빠져나오고 6이 추가된다. 6번 노드는 다음으로 연결된 노드가 없으므로 바로 빠져나간다.

<IMAGE>DFS stack4 - 5를 pop 후 6을 push, 6은 연결 노드 없어 바로 pop</IMAGE>

**step 5**: 시작점 이후 가장 먼저 입력되었던 값 1을 대상으로 다시 탐색을 시작한다.

<IMAGE>DFS stack5 - 1번 노드 탐색 시작</IMAGE>

**step 6**: 1과 연결된 3, 4가 Stack에 저장되어 탐색을 마저 수행한다.

<IMAGE>DFS stack6 - 1을 pop 후 연결된 3, 4를 push</IMAGE>

**...(중략)...**

**step 7**: 마지막으로 다시 6번이 Stack으로 입력된다.

<IMAGE>DFS stack7 - 6번 노드 재입력</IMAGE>

**step 8**: Stack이 비어 완전탐색이 끝난다.

<IMAGE>DFS stack8 - 스택 비어 탐색 완료</IMAGE>

## DFS, BFS와 무엇이 다를까

가장 눈에 띄는 차이점은 탐색 방향과 사용하는 자료구조가 다르다는 점이다.

| | BFS | DFS |
|--|--|--|
| 자료구조 | 큐(Queue) - FIFO | 스택(Stack) - LIFO |
| 탐색 방향 | 넓게(너비 우선) | 깊게(깊이 우선) |
| 최단 경로 | 보장됨 | 보장 안 됨 |

BFS에서는 `visited` 배열에 거리(방문 순서)를 누적하여 최단 경로를 보장할 수 있다.
DFS는 단지 방문 여부를 기록할 수는 있지만, 최단 경로를 보장하지 않는다.

DFS는 BFS와 함께 가장 대표적인 완전탐색 유형 중 하나이다. 사용하는 자료구조가 다를 뿐, 구현 과정도 큰 차이가 없다. 둘 중 하나만 완벽하게 이해한다면 다른 하나는 거저 얻어가는 것과 마찬가지이다.

## DFS 구현 (Stack 사용, Java)

```java
import java.util.*;

public class DFS {
    public static void main(String[] args) {
        // 간선 정보 (인접 리스트)
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= 6; i++) adj.add(new ArrayList<>());

        // 노드 연결 정보 입력
        adj.get(0).addAll(Arrays.asList(1, 2));
        adj.get(1).addAll(Arrays.asList(0, 3, 4));
        adj.get(2).addAll(Arrays.asList(0, 5));
        adj.get(5).add(6);

        // 0. 변수 생성
        Stack<Integer> myStack = new Stack<>();
        boolean[] visited = new boolean[7];

        // 1. 시작 노드 입력
        myStack.push(0);

        while (!myStack.isEmpty()) {
            // 2. 스택에서 값 꺼내기 (LIFO)
            int node = myStack.pop();

            // 이미 방문한 노드는 건너뜀
            if (visited[node]) continue;

            // 3. 방문 처리 및 연산 수행
            visited[node] = true;
            System.out.print(node + " ");

            // 4. 인접한 노드 스택에 저장
            for (int next : adj.get(node)) {
                if (!visited[next]) {
                    myStack.push(next);
                }
            }
        }
        // 출력 예시: 0 2 5 6 1 4 3
    }
}
```

## DFS 구현 (재귀 사용, Java)

재귀를 이용한 DFS도 자주 사용된다. 백트래킹 문제에서 주로 이 방식을 사용한다.

```java
import java.util.*;

public class DFSRecursion {
    static List<List<Integer>> adj = new ArrayList<>();
    static boolean[] visited;

    static void dfs(int node) {
        visited[node] = true;
        System.out.print(node + " ");

        for (int next : adj.get(node)) {
            if (!visited[next]) {
                dfs(next); // 재귀 호출
            }
        }
    }

    public static void main(String[] args) {
        for (int i = 0; i <= 6; i++) adj.add(new ArrayList<>());

        adj.get(0).addAll(Arrays.asList(1, 2));
        adj.get(1).addAll(Arrays.asList(0, 3, 4));
        adj.get(2).addAll(Arrays.asList(0, 5));
        adj.get(5).add(6);

        visited = new boolean[7];
        dfs(0); // 출력: 0 1 3 4 2 5 6
    }
}
```

## BFS와 DFS 선택 기준

| 상황 | 추천 |
|------|------|
| 최단 경로가 필요할 때 | BFS |
| 모든 노드를 방문해야 할 때 | DFS 또는 BFS 둘 다 가능 |
| 경우의 수 탐색, 백트래킹 | DFS (재귀) |
| 연결 요소(섬 개수 등) 찾기 | DFS 또는 BFS 둘 다 가능 |
| 스택 깊이 제한이 걱정될 때 | BFS 또는 스택 DFS |

BFS로 풀 수 있는 문제는 DFS로도 풀 수 있고, 그 역도 마찬가지이다(최단 경로 제외). 두 알고리즘은 거의 대부분 상호 대체가 가능하다.

# 메타데이터
```json
{
  "category": "탐색",
  "algorithm": "DFS",
  "source_type": "blog",
  "style": [
    "easy",
    "code"
  ],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "mid",
  "language": "java",
  "source": "wikidocs.net SW검정 알고리즘 강의"
}
```
