# 제목
[C/Cpp 기초] 구조체

# 본문

## 1. 한 줄 요약

구조체(struct)는 서로 다른 자료형의 변수들을 하나의 이름으로 묶어 새로운 자료형을 만드는 방법이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

학생 정보(이름, 나이, 점수)를 관리할 때 변수를 따로 선언하면 불편하다.

```c
/* 불편한 방법 */
char name[20];
int age;
float score;

/* 구조체로 묶기 */
struct Student {
    char name[20];
    int age;
    float score;
};

struct Student s;  /* 학생 1명의 정보 */
```

---

## 3. 핵심 아이디어

### 구조체 정의와 선언

```c
/* 구조체 타입 정의 */
struct Point {
    int x;
    int y;
};

/* 구조체 변수 선언 */
struct Point p1;
struct Point p2 = {3, 5};  /* 초기화 */
```

### 멤버 접근

```c
/* 점 연산자로 접근 */
p1.x = 10;
p1.y = 20;

printf("(%d, %d)\n", p1.x, p1.y);
```

### 포인터로 구조체 접근

```c
struct Point *ptr = &p1;

/* 두 방법 모두 동일 */
(*ptr).x = 100;  /* 방법 1 */
ptr->x = 100;    /* 방법 2: 화살표 연산자 */
```

---

## 4. 동작 과정 살펴보기

### 구조체 메모리 레이아웃

```text
struct Student {
    char name[20];  /* 20바이트 */
    int age;        /*  4바이트 */
    float score;    /*  4바이트 */
};
/* 총 28바이트 (패딩 없을 때) */

메모리: [name(20)] [age(4)] [score(4)]
         0         20       24
```

### 구조체 배열

```c
struct Student class[30];  /* 학생 30명 배열 */
class[0].age = 20;
class[1].score = 95.5f;
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

struct Student {
    char name[20];
    int age;
    float score;
};

/* 구조체를 출력하는 함수 */
void print_student(struct Student s) {
    printf("이름: %s, 나이: %d, 점수: %.1f\n", s.name, s.age, s.score);
}

/* 포인터로 받으면 복사 없음 (효율적) */
void update_score(struct Student *s, float new_score) {
    s->score = new_score;
}

int main() {
    /* 구조체 변수 선언 및 초기화 */
    struct Student s1;
    strcpy(s1.name, "홍길동");
    s1.age = 20;
    s1.score = 85.5f;

    /* 지정 초기화 (C99) */
    struct Student s2 = {.name = "이순신", .age = 25, .score = 92.0f};

    print_student(s1);
    print_student(s2);

    /* 포인터로 수정 */
    update_score(&s1, 90.0f);
    printf("수정 후: ");
    print_student(s1);

    /* 구조체 배열 */
    struct Student class[3] = {
        {"김철수", 21, 88.0f},
        {"박영희", 22, 76.5f},
        {"최민수", 20, 95.0f}
    };

    printf("\n반 전체 학생:\n");
    for (int i = 0; i < 3; i++) {
        print_student(class[i]);
    }

    /* 구조체 안의 구조체 */
    struct Date {
        int year, month, day;
    };

    struct Person {
        char name[20];
        struct Date birthday;
    };

    struct Person p = {"홍길동", {1990, 5, 15}};
    printf("\n%s의 생일: %d년 %d월 %d일\n",
           p.name, p.birthday.year, p.birthday.month, p.birthday.day);

    return 0;
}
```

---

## 6. 마지막 정리

`struct` 키워드로 여러 자료형을 하나의 타입으로 묶을 수 있다.

멤버 접근은 변수면 `.`, 포인터면 `->` 연산자를 사용한다.

함수에 구조체를 전달할 때 포인터로 넘기면 복사 비용이 없다.

구조체 안에 구조체를 포함할 수 있다(중첩 구조체).

구조체 배열로 동일한 타입의 여러 객체를 관리한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 구조체",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
