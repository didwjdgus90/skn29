# 제목
[C/Cpp 기초] 함수

# 본문

## 1. 한 줄 요약

함수는 특정 작업을 수행하는 코드 블록에 이름을 붙인 것이다. 필요할 때마다 이름을 불러 재사용할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

같은 코드를 여러 곳에서 반복해서 쓰면 수정할 때 모든 곳을 바꿔야 한다.

```c
/* 함수 없이 */
int area1 = 5 * 3;
int area2 = 10 * 7;
int area3 = 4 * 8;
```

함수를 만들면 한 번 정의하고 여러 번 호출할 수 있다.

```c
int rectangle_area(int width, int height) {
    return width * height;
}

int a1 = rectangle_area(5, 3);
int a2 = rectangle_area(10, 7);
int a3 = rectangle_area(4, 8);
```

---

## 3. 핵심 아이디어

### 함수의 구성 요소

```c
반환타입 함수이름(매개변수1, 매개변수2, ...) {
    /* 함수 본문 */
    return 반환값;
}
```

```c
int add(int a, int b) {
    return a + b;
}
```

- **반환타입**: 함수가 돌려주는 값의 타입 (`int`, `double`, `void` 등)
- **함수이름**: 호출할 때 사용할 이름
- **매개변수**: 함수에 전달할 값 (없으면 `void` 또는 비워둠)
- **return**: 값을 돌려주고 함수 종료

### void 함수 (반환값 없음)

```c
void say_hello(char *name) {
    printf("Hello, %s!\n", name);
    /* return 없거나 return; */
}
```

### 함수 선언 (프로토타입)

함수를 사용하기 전에 컴파일러에게 미리 알려줄 수 있다.

```c
int add(int a, int b);  /* 선언 (세미콜론으로 끝남) */

int main() {
    int result = add(3, 4);  /* 선언 덕분에 사용 가능 */
    return 0;
}

int add(int a, int b) {  /* 정의 */
    return a + b;
}
```

---

## 4. 동작 과정 살펴보기

### 함수 호출 흐름

```text
main() 실행 중
  ↓
add(3, 4) 호출
  ↓
add 함수로 이동
  a = 3, b = 4
  return 3 + 4 = 7
  ↓
main으로 돌아옴
result = 7
  ↓
계속 실행
```

### 값 전달 (Call by Value)

함수에 전달된 값은 복사된다. 원본은 변하지 않는다.

```c
void double_it(int x) {
    x = x * 2;  /* 복사본만 변경 */
}

int n = 5;
double_it(n);
printf("%d\n", n);  /* 5 (원본 그대로) */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 함수 선언 (프로토타입) */
int add(int a, int b);
double average(int arr[], int n);
int max_of_two(int a, int b);
void print_stars(int count);

int main() {
    /* 함수 호출 */
    printf("3 + 4 = %d\n", add(3, 4));
    printf("10 + 20 = %d\n", add(10, 20));

    int scores[] = {85, 92, 78, 90, 88};
    printf("평균: %.2f\n", average(scores, 5));

    printf("최댓값: %d\n", max_of_two(7, 12));

    print_stars(5);

    return 0;
}

/* 함수 정의 */
int add(int a, int b) {
    return a + b;
}

double average(int arr[], int n) {
    int sum = 0;
    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
    return (double)sum / n;
}

int max_of_two(int a, int b) {
    return (a > b) ? a : b;
}

void print_stars(int count) {
    for (int i = 0; i < count; i++) {
        printf("*");
    }
    printf("\n");
}
```

### 배열을 함수에 전달

```c
/* 배열은 포인터로 전달됨 (크기 정보 따로 전달) */
void fill_zeros(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = 0;  /* 원본 배열 변경됨 */
    }
}

int data[5] = {1, 2, 3, 4, 5};
fill_zeros(data, 5);  /* data가 모두 0이 됨 */
```

---

## 6. 마지막 정리

함수는 재사용 가능한 코드 블록이다.

`반환타입 함수명(매개변수) { ... return 값; }` 형태로 정의한다.

반환값이 없으면 `void`를 사용한다.

함수 선언(프로토타입)으로 정의 전에 사용할 수 있다.

기본 자료형은 값이 복사되어 전달되므로 원본이 변하지 않는다.

배열은 포인터로 전달되므로 함수 내에서 원본이 변경된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 함수",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
