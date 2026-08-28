# 제목
[알고리즘] BFS - 너비 우선 탐색 (SW검정 알고리즘 강의)

# 링크
<https://wikidocs.net/125660>

# 본문

## BFS 이해하기

BFS 알고리즘은 백트래킹보다 조금 더 직관적이고 이해가 쉬운 알고리즘이다.

BFS를 사용하여 탐색하는 과정:

<IMAGE>BFS 탐색 step1 - 시작 노드(6)를 큐에 삽입</IMAGE>

<IMAGE>BFS 탐색 step2 - 6의 인접 노드 2, 5, 7, 10을 큐에 삽입</IMAGE>

<IMAGE>BFS 탐색 step3 - 2를 꺼내 인접 노드 1, 3 삽입 (6은 이미 방문)</IMAGE>

<IMAGE>BFS 탐색 step4 - 계속 진행 (중략)</IMAGE>

<IMAGE>BFS 탐색 step5 - 모든 노드 탐색 완료</IMAGE>

## BFS 알고리즘의 진행 과정

1. 가장 먼저 할 일은 시작점을 큐에 넣는 것이다.
   - 예시에서 시작 노드 번호 6이 큐에 들어간다.
   - 초기 큐의 상태: [6]

2. 큐에서 맨 앞의 값을 꺼내서 필요한 연산을 수행한다.

3. 모든 연산이 끝나면 인접한(연결된) 노드들을 큐에 저장한다.
   - 이전에 방문한 노드는 제외한다.
   - 6의 상하좌우 노드들이 차례로 저장된다.
   - 현재 큐의 상태: [6, 2, 5, 7, 10]

4. `visited`를 사용해 방문한 노드를 표시한다.
   - 큐에 넣는 즉시 표시하는 것이 중요하다.
   - 그래야 방문한 값을 다시 큐에 넣지 않고 루프를 방지할 수 있다.

5. 탐색이 끝난 노드를 버리고 다음 노드를 큐에서 꺼낸다.
   - 큐는 선입선출(FIFO) 자료구조이므로 가장 앞의 2를 기준으로 동일 작업 반복
   - 2의 방문 표시 후 인접 노드 1, 3, 6 확인 → 6은 이미 방문했으므로 제외
   - 현재 큐의 상태: [2, 5, 7, 10, 1, 3]

6. 이렇게 계속 탐색하면 모든 노드들이 큐에 저장되었다가 빠져나가게 된다.

## BFS의 구성 (코드 구현)

BFS 구현 핵심 요소:
- **큐(Queue)**: 탐색할 노드를 순서대로 저장
- **visited 배열**: 방문 여부 또는 거리 기록
- **좌표 처리**: x, y 좌표를 큐에 함께 관리

```java
public static void main(String args[]) {
    // 4x4 배열 생성 (1~16으로 초기화)
    int[][] map = new int[4][4];
    int temp = 1;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++) {
            map[i][j] = temp;
            temp++;
        }

    // 0. 변수 생성
    Queue<Integer> myQ   = new LinkedList<Integer>(); // 노드 값
    Queue<Integer> myQ_x = new LinkedList<Integer>(); // x좌표
    Queue<Integer> myQ_y = new LinkedList<Integer>(); // y좌표
    int[][] visited = new int[4][4];

    // 1. 시작 노드 입력 (6 = 좌표 (1,1))
    myQ.add(6);
    visited[1][1] = 1;
    myQ_x.add(1);
    myQ_y.add(1);

    while (!myQ.isEmpty()) {
        // 2. 큐의 맨 앞 노드 값 저장 (peek = 꺼내지 않고 확인)
        int node = myQ.peek();
        int x = myQ_x.peek();
        int y = myQ_y.peek();

        // 3. 해당 노드에 대한 연산 수행

        // 4. 인접한 노드 저장 (상하좌우)
        // 위쪽 노드
        if (x - 1 >= 0 && visited[x-1][y] != 1) {
            myQ.add(map[x-1][y]);
            visited[x-1][y] = 1;
            myQ_x.add(x-1); myQ_y.add(y);
        }
        // 왼쪽 노드
        if (y - 1 >= 0 && visited[x][y-1] != 1) {
            myQ.add(map[x][y-1]);
            visited[x][y-1] = 1;
            myQ_x.add(x); myQ_y.add(y-1);
        }
        // 아래쪽 노드
        if (x + 1 < 4 && visited[x+1][y] != 1) {
            myQ.add(map[x+1][y]);
            myQ_x.add(x+1); myQ_y.add(y);
        }
        // 오른쪽 노드
        if (y + 1 < 4 && visited[x][y+1] != 1) {
            myQ.add(map[x][y+1]);
            visited[x][y+1] = 1;
            myQ_x.add(x); myQ_y.add(y+1);
        }

        // 5. 연산이 끝난 노드 제거
        myQ.poll();
        myQ_x.poll();
        myQ_y.poll();
        // 큐 상태: [2, 5, 7, 10] → [5, 7, 10, 1, 3] → ...
    }
}
```

### 주의사항

1. **좌표 관리**: 노드의 상하좌우를 파악하려면 좌표값이 필요하다. `myQ_x`, `myQ_y`를 별도로 관리하거나, x와 y를 하나의 큐에 교대로 넣는 방법도 있다.

2. **인덱스 범위 확인**: 배열 호출 전 항상 인덱스 범위를 먼저 확인해야 한다. 범위를 벗어나면 `ArrayIndexOutOfBoundsException`이 발생한다.

3. **peek()과 poll()의 차이**:
   - `peek()`: 맨 앞의 값을 확인만 함 (제거 X)
   - `poll()`: 맨 앞의 값을 꺼냄 (제거 O)
   - 실제 문제 풀이 시에는 바로 `poll()`을 사용하는 것이 코딩량이 줄어든다.

## BFS 구현하기(1) - 미로 탈출

### 문제

아래와 같이 생긴 미로가 있다.
- S: 시작점
- G: 도착점
- W: 벽
- 0: 이동 가능한 칸

도착점까지 최소한으로 이동하기 위해서는 몇 칸을 가야 할지 구하라.

<IMAGE>미로 지도 그림 (7x7, S→G, W=벽)</IMAGE>

### 핵심 아이디어: visited 배열에 거리 기록

기존 방문 여부(`1`)만 기록하는 대신, **현재 탐색 위치의 값 + 1**을 기록한다.
이렇게 하면 각 위치에 몇 번째 순서로 방문하는지가 `visited` 배열에 기록된다.

```java
String[][] map = {
    { "S", "0", "0", "0", "W", "0", "W" },
    { "W", "0", "W", "0", "0", "0", "0" },
    { "0", "0", "0", "W", "0", "W", "0" },
    { "0", "W", "W", "0", "0", "0", "0" },
    { "0", "0", "W", "W", "0", "W", "W" },
    { "W", "0", "W", "0", "0", "0", "0" },
    { "0", "0", "0", "W", "0", "0", "G" }
};

// 0. 변수 생성
Queue<Integer> myQ = new LinkedList<Integer>(); // x, y 좌표를 번갈아 저장
int[][] visited = new int[7][7];
int answer = 0;

// 1. 시작 노드 입력 ("S" = (0,0))
myQ.add(0); // x좌표
myQ.add(0); // y좌표
visited[0][0] = 1;

while (!myQ.isEmpty()) {
    // 2. 즉시 poll (x, y 번갈아 저장했으므로 peek 두 번이 의미없음)
    int x = myQ.poll();
    int y = myQ.poll();

    // 4. 인접한 노드 저장 (상하좌우)
    // 위쪽
    if (x-1 >= 0 && visited[x-1][y] == 0 && !"W".equals(map[x-1][y])) {
        myQ.add(x-1); myQ.add(y);
        visited[x-1][y] = visited[x][y] + 1; // 거리 누적
    }
    // 아래쪽
    if (x+1 < 7 && visited[x+1][y] == 0 && !"W".equals(map[x+1][y])) {
        myQ.add(x+1); myQ.add(y);
        visited[x+1][y] = visited[x][y] + 1;
    }
    // 왼쪽
    if (y-1 >= 0 && visited[x][y-1] == 0 && !"W".equals(map[x][y-1])) {
        myQ.add(x); myQ.add(y-1);
        visited[x][y-1] = visited[x][y] + 1;
    }
    // 오른쪽
    if (y+1 < 7 && visited[x][y+1] == 0 && !"W".equals(map[x][y+1])) {
        myQ.add(x); myQ.add(y+1);
        visited[x][y+1] = visited[x][y] + 1;
    }
}
answer = visited[6][6];
System.out.println(answer); // 13
```

<IMAGE>visited 배열 결과 그림 (S=1에서 G=13까지 각 칸의 거리값)</IMAGE>

갈 수 없는 부분(W)을 제외하고는 모두 숫자로 채워져 있다. 각 숫자는 시작점(S=1)에서 얼마나 떨어져 있는지를 의미한다. 도착점(G)는 13 → 13번 이동해야 도착 가능.

### 최적 경로 보장하기

BFS에서 visited 배열이 최적 경로를 보장하는 이유:
- 시작점의 visited에는 1을 표기
- 두 번째로 갈 수 있는 모든 경로에 2가, 세 번 만에 도달 가능한 곳에 3이 표기된다.
- 즉, 내가 이번에 발견한 노드가 이미 방문한 노드라면, 기존에 채워진 값은 새로 채우려는 값보다 **항상 작거나 같다.**
- 따라서 방문 여부(`if(visited[i][j]==0)`)만 확인해도 항상 최적 경로가 보장된다.

## BFS vs DFS 핵심 비교

| | BFS | DFS |
|--|--|--|
| 자료구조 | 큐(Queue) - FIFO | 스택(Stack) - LIFO |
| 탐색 방향 | 넓게(가까운 곳 먼저) | 깊게(한 방향 끝까지) |
| 최단 경로 | 보장됨 | 보장 안 됨 |
| visited 거리 누적 | 가능 | 불가 |

# 메타데이터
```json
{
  "category": "탐색",
  "algorithm": "BFS",
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
