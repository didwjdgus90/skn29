# 제목
[C/Cpp 기초] 시간 복잡도

# 본문

## 1. 한 줄 요약

시간 복잡도는 일이 많아질수록 얼마나 더 힘들어지는지를 나타내는 지표다. O(n²)은 사람이 2배 늘면 4배 힘들어지는 것이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

파티에서 모든 사람이 악수를 한 번씩 해야 한다.

10명이면 몇 번 악수? 10명이면 45번.
100명이면 4,950번.
1,000명이면 499,500번!

사람이 10배 늘면 악수가 100배 늘어난다. 이것이 O(n²)이다.

```text
악수 횟수 = n(n-1)/2 ≈ n² → O(n²)
```

---

## 3. 핵심 아이디어

### 여행 비유

```text
O(1)      = GPS 내비게이션
            → 목적지가 어디든 즉시 경로 알려줌

O(log n)  = 두꺼운 전화번호부에서 이름 찾기
            → 반씩 펼쳐서 빠르게 찾기 (이진 탐색)

O(n)      = 버스 정류장 순서대로 걸어가기
            → 목적지까지 모든 정류장 통과

O(n²)     = 미로에서 모든 길 다 가보기
            → 갈 길이 n배 늘면 탐색은 n² 배 증가

O(2ⁿ)    = 자물쇠 암호 조합 다 시도
            → 자릿수 하나 늘면 경우의 수 2배!
```

---

## 4. 동작 과정 살펴보기

### 1000명의 학교 비유

```text
출석 확인 방법 1 (O(n)):
  선생님이 이름 하나씩 부름
  1000명 → 1000번 호출

출석 확인 방법 2 (O(n²)):
  각 학생이 다른 모든 학생에게 인사
  1000명 → 1,000,000번 인사

전화번호부 검색 (O(log n)):
  책을 반씩 펼쳐서 찾기
  1000명 → 약 10번만 펼치면 찾음!
  (2^10 = 1024)
```

### O(1) = 냉장고에서 바로 꺼내기

```text
배열 arr[5] 접근:
  arr[0], arr[3], arr[999] 모두 같은 속도!
  메모리 주소 계산 = 한 번의 덧셈
  → O(1): 배열 크기와 무관하게 일정
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* O(1): 냉장고에서 꺼내기 */
int get_item(int *arr, int index) {
    return arr[index];  /* 바로 접근 */
}

/* O(n): 줄 서서 기다리기 */
int find_item(int *arr, int n, int target) {
    for (int i = 0; i < n; i++) {     /* n번 확인 */
        if (arr[i] == target) return i;
    }
    return -1;
}

/* O(log n): 전화번호부 찾기 */
int fast_find(int *arr, int n, int target) {
    int left = 0, right = n - 1;
    while (left <= right) {            /* log₂(n)번 반복 */
        int mid = (left + right) / 2;
        if (arr[mid] == target) return mid;
        if (arr[mid] < target) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}

/* O(n²): 모든 쌍 악수 */
void handshake(int n) {
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i+1; j < n; j++) {  /* 중첩 반복 */
            count++;
        }
    }
    printf("%d명 악수 횟수: %d\n", n, count);
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11, 13, 15};
    int n = 8;

    /* O(1) */
    printf("arr[3] = %d (O(1): 즉시 접근)\n", get_item(arr, 3));

    /* O(n) vs O(log n) 비교 */
    printf("\n13을 찾아라:\n");
    printf("O(n)  선형 탐색: 인덱스 %d\n", find_item(arr, n, 13));
    printf("O(log n) 이진 탐색: 인덱스 %d\n", fast_find(arr, n, 13));

    /* O(n²) */
    printf("\n악수 횟수:\n");
    handshake(5);
    handshake(10);
    handshake(100);

    /* 실감 나는 비교 */
    printf("\nn=1,000,000일 때 연산 횟수:\n");
    printf("O(1)    = 1\n");
    printf("O(log n)= 약 20\n");
    printf("O(n)    = 1,000,000\n");
    printf("O(n²)   = 1,000,000,000,000 (1조)\n");

    return 0;
}
```

---

## 6. 마지막 정리

O(1)은 입력과 상관없이 항상 같은 시간, O(n)은 n에 비례, O(n²)은 n 제곱에 비례한다.

이진 탐색이 O(log n)인 이유는 매번 절반으로 줄이기 때문이다.

n이 클수록 O(n²)과 O(n)의 차이가 엄청나게 벌어진다.

알고리즘을 선택할 때 "n이 커지면 어떻게 되는가"를 먼저 생각한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 시간 복잡도",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
