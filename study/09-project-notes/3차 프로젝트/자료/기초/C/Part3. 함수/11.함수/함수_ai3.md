# 제목
[C/Cpp 기초] 함수

# 본문

## 1. 한 줄 요약

C의 함수는 독립적인 번역 단위에서 컴파일되는 서브루틴으로, 호출 규약(calling convention)에 따라 스택 프레임을 할당하고 값 의미론(value semantics)으로 인수를 전달한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

함수는 프로그램을 관심사 분리(Separation of Concerns) 원칙에 따라 모듈화한다.

- **재사용성**: 동일 로직의 중복 제거
- **추상화**: 구현 세부사항 은닉
- **테스트 용이성**: 독립적 단위 테스트 가능
- **스코프 분리**: 지역 변수로 명명 충돌 방지

---

## 3. 핵심 아이디어

### 호출 규약과 스택 프레임

함수 호출 시 스택에 활성화 레코드(activation record)가 생성된다.

```text
함수 호출 시 스택:
┌─────────────────┐  ← 높은 주소
│  caller의 스택   │
├─────────────────┤
│  리턴 주소       │  caller로 돌아갈 주소
│  old frame ptr  │  이전 스택 프레임 포인터
│  지역 변수들     │
│  매개변수들      │
├─────────────────┤  ← 낮은 주소 (스택 성장 방향)
```

x86-64 Linux에서 `cdecl`/`System V AMD64 ABI`는 처음 6개 정수 인수를 레지스터(RDI, RSI, RDX, RCX, R8, R9)로 전달한다.

### 값 의미론 (Pass by Value)

기본 타입은 항상 복사되어 전달된다.

```c
void modify(int x) { x = 100; }  /* 복사본 수정 */

int n = 5;
modify(n);
/* n == 5: 원본 불변 */
```

포인터를 전달하면 주소가 복사되지만, 역참조로 원본 데이터를 수정할 수 있다.

```c
void modify_ptr(int *x) { *x = 100; }

int n = 5;
modify_ptr(&n);
/* n == 100 */
```

### 함수 포인터

함수도 메모리 상의 코드이며, 포인터로 가리킬 수 있다.

```c
int (*operation)(int, int);  /* 함수 포인터 선언 */
operation = add;             /* 함수 주소 대입 */
int result = operation(3, 4); /* 역참조로 호출 */
```

---

## 4. 동작 과정 살펴보기

### 인라인 함수 최적화

컴파일러는 작은 함수를 인라인으로 펼쳐 호출 오버헤드를 제거할 수 있다.

```c
/* 힌트만 제공: 컴파일러가 무시할 수 있음 */
static inline int square(int x) { return x * x; }
```

`-O2` 이상에서 컴파일러가 자동으로 인라인화를 결정한다.

### 재귀와 스택 오버플로우

함수를 재귀 호출할 때마다 스택 프레임이 쌓인다. 기저 조건 없이 재귀하면 스택이 고갈된다.

```c
void infinite_recursion() {
    infinite_recursion();  /* 스택 오버플로우 */
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 함수 포인터를 이용한 전략 패턴 */
typedef int (*BinaryOp)(int, int);

int add(int a, int b) { return a + b; }
int sub(int a, int b) { return a - b; }
int mul(int a, int b) { return a * b; }

void apply(int a, int b, BinaryOp op, const char *name) {
    printf("%d %s %d = %d\n", a, name, b, op(a, b));
}

/* 배열을 함수에 전달: 포인터 decay */
double arr_average(const int *arr, size_t n) {
    long long sum = 0;
    for (size_t i = 0; i < n; i++) sum += arr[i];
    return (double)sum / n;
}

int main() {
    BinaryOp ops[] = {add, sub, mul};
    const char *names[] = {"+", "-", "*"};

    for (int i = 0; i < 3; i++) {
        apply(10, 3, ops[i], names[i]);
    }

    int data[] = {1, 2, 3, 4, 5};
    printf("평균: %.2f\n", arr_average(data, 5));

    /* 함수 주소 출력 */
    printf("add 함수 주소: %p\n", (void *)add);

    return 0;
}
```

### 정적 함수와 링크 지정

```c
/* static: 파일 내부에서만 접근 가능 (internal linkage) */
static int helper(int x) { return x * 2; }

/* extern: 다른 번역 단위에서 접근 가능 (external linkage, 기본) */
extern int public_func(int x);
```

---

## 6. 마지막 정리

함수 호출은 스택 프레임 할당, 인수 복사, 점프, 반환 주소 복귀로 이루어진다.

기본 타입은 값 의미론(복사)으로 전달되며, 포인터를 사용하면 원본에 접근할 수 있다.

함수 포인터로 고차 함수(콜백, 전략 패턴)를 구현할 수 있다.

`static` 함수는 파일 스코프 내부 링크로 모듈 캡슐화에 활용된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 함수",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
