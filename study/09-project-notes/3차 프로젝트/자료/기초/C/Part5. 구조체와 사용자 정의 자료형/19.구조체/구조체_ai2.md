# 제목
[C/Cpp 기초] 구조체

# 본문

## 1. 한 줄 요약

구조체는 여러 정보를 하나의 봉투에 담는 것이다. 이름, 나이, 점수를 각각 들고 다니지 않고 한 봉투에 넣어 처리한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

택배를 보낼 때 이름, 주소, 전화번호를 따로따로 들고 다니면 불편하다.

송장 하나에 모두 적어두면 편리하다.

```text
구조체 없이:
  char name[20];    ← 이름
  char address[50]; ← 주소  
  char phone[15];   ← 전화번호
  → 세 변수를 항상 같이 챙겨야 함

구조체 사용:
  struct Recipient {  ← 수신자 봉투
      char name[20];
      char address[50];
      char phone[15];
  };
  → 봉투 하나만 챙기면 OK
```

---

## 3. 핵심 아이디어

### 봉투 설계도 만들기

```c
struct 봉투이름 {
    자료형 항목1;
    자료형 항목2;
    /* ... */
};
```

```c
struct Student {  /* 학생 봉투 설계도 */
    char name[20];
    int age;
    float score;
};
```

### 봉투 만들기

```c
struct Student s1;  /* 학생 봉투 하나 */
```

### 봉투 열어서 꺼내기

```c
/* 점(.) = 봉투의 특정 칸 열기 */
s1.age = 20;
printf("%s\n", s1.name);
```

---

## 4. 동작 과정 살펴보기

### 점(.) vs 화살표(->) 연산자

```text
직접 들고 있을 때 → 점(.) 사용
  struct Student s;
  s.age = 20;        ← "봉투의 나이 칸"

대리인이 들고 있을 때 → 화살표(->) 사용
  struct Student *p = &s;
  p->age = 20;       ← "대리인이 가진 봉투의 나이 칸"
```

### 구조체 배열 = 봉투 묶음

```text
struct Student class[30];
              ↑
          30개 봉투 묶음

class[0] = 1번 학생 봉투
class[1] = 2번 학생 봉투
...
class[29] = 30번 학생 봉투
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

/* 학생 봉투 설계도 */
struct Student {
    char name[20];
    int age;
    float score;
};

/* 봉투를 화면에 출력 */
void print_student(struct Student s) {
    printf("[%s] 나이: %d, 점수: %.1f\n", s.name, s.age, s.score);
}

/* 봉투 내용 수정 (포인터로 직접 수정) */
void give_bonus(struct Student *s, float bonus) {
    s->score += bonus;
    printf("%s에게 보너스 점수 +%.1f 지급!\n", s->name, bonus);
}

int main() {
    /* 봉투 만들기 */
    struct Student alice;
    strcpy(alice.name, "Alice");
    alice.age = 20;
    alice.score = 80.0f;

    struct Student bob = {"Bob", 22, 75.5f};

    print_student(alice);
    print_student(bob);

    /* 봉투 내용 수정 */
    give_bonus(&alice, 5.0f);
    print_student(alice);

    /* 봉투 30개 묶음 (반 전체) */
    struct Student class[3] = {
        {"Charlie", 21, 88.0f},
        {"Diana", 20, 92.5f},
        {"Eve", 23, 70.0f}
    };

    printf("\n반 전체:\n");
    float total = 0;
    for (int i = 0; i < 3; i++) {
        print_student(class[i]);
        total += class[i].score;
    }
    printf("평균 점수: %.1f\n", total / 3);

    /* 봉투 안에 봉투 */
    struct Address {
        char city[20];
        char street[50];
    };

    struct Person {
        char name[20];
        struct Address home;  /* 주소 봉투 */
    };

    struct Person p = {"홍길동", {"서울", "강남구"}};
    printf("\n%s의 주소: %s %s\n", p.name, p.home.city, p.home.street);

    return 0;
}
```

---

## 6. 마지막 정리

구조체는 관련 정보를 하나의 봉투에 담는 방법이다.

`struct 이름 {}` 으로 설계도를 만들고, `struct 이름 변수명`으로 봉투를 만든다.

직접 접근은 점(`.`), 포인터로 접근은 화살표(`->`).

구조체 배열로 같은 종류의 봉투를 여러 개 관리할 수 있다.

구조체 안에 구조체를 넣어서 계층적으로 정보를 조직할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 구조체",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
