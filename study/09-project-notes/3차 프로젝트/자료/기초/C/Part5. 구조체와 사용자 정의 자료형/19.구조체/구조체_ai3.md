# 제목
[C/Cpp 기초] 구조체

# 본문

## 1. 한 줄 요약

구조체는 이종(heterogeneous) 데이터를 단일 집성 타입(aggregate type)으로 캡슐화하는 메커니즘으로, 컴파일러가 멤버 간 정렬(alignment)을 위해 패딩을 삽입할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

C는 기본 타입 외에 사용자 정의 복합 타입이 없다. 구조체는 논리적으로 연관된 데이터를 단일 메모리 블록으로 관리하고 타입 시스템을 통한 추상화를 제공한다.

- 관련 데이터의 응집도 향상과 코드 가독성
- 함수 인터페이스 단순화 (여러 인자 → 구조체 포인터)
- 자료구조(링크드 리스트, 트리) 노드 구현의 기반

---

## 3. 핵심 아이디어

### 메모리 레이아웃과 패딩

```c
struct A {
    char c;   /* 1바이트 */
    int i;    /* 4바이트 */
    char d;   /* 1바이트 */
};
```

```text
실제 레이아웃 (x86-64):
offset  0: c    (1바이트)
offset  1: [패딩 3바이트]  ← int 정렬을 위해
offset  4: i    (4바이트)
offset  8: d    (1바이트)
offset  9: [패딩 3바이트]  ← 구조체 크기 = 최대 정렬의 배수
총 크기: 12바이트 (sizeof(A) == 12)
```

```c
struct B {
    int i;    /* 4바이트 */
    char c;   /* 1바이트 */
    char d;   /* 1바이트 */
};
/* 총 8바이트: int(4) + c(1) + d(1) + 패딩(2) */
/* 멤버 순서가 크기에 영향 */
```

### 비트 필드 (Bit Field)

```c
struct Flags {
    unsigned int read    : 1;
    unsigned int write   : 1;
    unsigned int execute : 1;
    unsigned int         : 5;  /* 패딩 비트 */
};
/* 1바이트에 세 플래그 저장 */
```

---

## 4. 동작 과정 살펴보기

### 구조체 포인터와 자기 참조

```c
/* 링크드 리스트 노드 */
struct Node {
    int data;
    struct Node *next;  /* 자기 참조 포인터 */
};
```

### 값 전달 vs 포인터 전달

```c
void by_value(struct Student s) {
    /* s는 복사본 (원본 불변) */
    /* 크기 큰 구조체면 복사 비용 발생 */
}

void by_pointer(struct Student *s) {
    /* s는 원본의 주소 (포인터 크기 8바이트만 복사) */
    /* 읽기 전용이면 const struct Student * */
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* 링크드 리스트로 구조체 응용 */
struct Node {
    int data;
    struct Node *next;
};

struct Node *node_create(int data) {
    struct Node *n = malloc(sizeof(struct Node));
    if (!n) return NULL;
    n->data = data;
    n->next = NULL;
    return n;
}

void list_append(struct Node **head, int data) {
    struct Node *new_node = node_create(data);
    if (!new_node) return;
    if (*head == NULL) { *head = new_node; return; }
    struct Node *cur = *head;
    while (cur->next) cur = cur->next;
    cur->next = new_node;
}

void list_print(const struct Node *head) {
    const struct Node *cur = head;
    while (cur) {
        printf("%d", cur->data);
        if (cur->next) printf(" -> ");
        cur = cur->next;
    }
    printf("\n");
}

void list_free(struct Node *head) {
    while (head) {
        struct Node *next = head->next;
        free(head);
        head = next;
    }
}

int main() {
    /* 구조체 크기와 정렬 확인 */
    struct A { char c; int i; char d; };
    struct B { int i; char c; char d; };
    printf("sizeof(A) = %zu\n", sizeof(struct A));
    printf("sizeof(B) = %zu\n", sizeof(struct B));

    /* 링크드 리스트 */
    struct Node *head = NULL;
    for (int i = 1; i <= 5; i++) list_append(&head, i * 10);
    list_print(head);
    list_free(head);

    /* 비트 필드 */
    struct Flags { unsigned read:1; unsigned write:1; unsigned exec:1; };
    struct Flags f = {1, 1, 0};
    printf("r=%d w=%d x=%d, size=%zu\n", f.read, f.write, f.exec, sizeof(f));

    return 0;
}
```

---

## 6. 마지막 정리

구조체 멤버 배치 순서가 메모리 크기에 영향을 미친다. 큰 타입을 앞에 두면 패딩을 최소화할 수 있다.

`offsetof(struct T, member)` 매크로로 멤버의 오프셋을 확인한다.

함수 인자로 큰 구조체 전달 시 포인터를 사용하고, 읽기 전용이면 `const`를 붙인다.

자기 참조 구조체 포인터로 링크드 리스트, 트리 등 자료구조를 구현한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 구조체",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 5,
  "target_level": "high",
  "language": "c"
}
```
