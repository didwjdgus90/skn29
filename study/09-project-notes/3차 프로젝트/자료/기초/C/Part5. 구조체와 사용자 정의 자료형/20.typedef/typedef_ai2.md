# 제목
[C/Cpp 기초] typedef

# 본문

## 1. 한 줄 요약

`typedef`는 긴 타입 이름에 별명을 붙이는 것이다. "unsigned long long int"를 "UInt64"라고 부르기로 약속하는 것처럼.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

회사에서 "대한민국 서울특별시 강남구에 사는 직원"이라고 매번 쓰는 대신 "강남직원"이라고 약칭을 정하는 것과 같다.

```c
/* 별명 없이 */
struct Point { int x, y; };
struct Point p1;
struct Point p2;
/* 매번 struct Point... */

/* 별명 사용 */
typedef struct { int x, y; } Point;
Point p1;  /* 훨씬 간결 */
Point p2;
```

---

## 3. 핵심 아이디어

### 별명 붙이기

```text
typedef  원본이름  별명;
   ↑         ↑       ↑
"앞으로"  "이것을"  "이렇게 부를게"
```

```c
typedef unsigned int uint;
/* "앞으로 unsigned int를 uint라고 부를게" */

uint a = 100;  /* unsigned int a = 100; 와 동일 */
```

### 구조체 별명 (가장 많이 사용)

```c
/* 전: 학생 봉투를 꺼낼 때마다 "struct" 필요 */
struct Student { char name[20]; int age; };
struct Student s1;  /* struct 키워드 필수! */

/* 후: typedef로 별명 */
typedef struct { char name[20]; int age; } Student;
Student s1;  /* struct 없이 OK */
```

---

## 4. 동작 과정 살펴보기

### typedef vs #define 차이

```text
#define 방식: 텍스트 치환 (복사+붙여넣기)
typedef 방식: 진짜 타입 별명 (완전한 타입 취급)

typedef char* String;
String a, b;  → char *a, char *b  (둘 다 포인터)

#define STRING char*
STRING c, d;  → char *c, d  (c만 포인터, d는 char!)
              ↑ 복붙이라서 d에는 *가 안 붙음!
```

typedef가 더 안전하고 예측 가능하다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

/* 숫자 타입에 의미 있는 이름 붙이기 */
typedef int Age;
typedef float Score;
typedef char Name[20];

/* 구조체에 별명 */
typedef struct {
    Name  name;
    Age   age;
    Score score;
} Student;

/* 함수: 구조체 이름이 훨씬 읽기 좋아짐 */
void describe(Student s) {
    printf("학생: %s, 나이: %d세, 점수: %.1f점\n",
           s.name, s.age, s.score);
}

/* 등급 판정 (함수 포인터 별명) */
typedef char (*Grader)(Score);

char grade_normal(Score s) {
    if (s >= 90) return 'A';
    if (s >= 80) return 'B';
    if (s >= 70) return 'C';
    return 'D';
}

int main() {
    Student s1 = {"홍길동", 20, 87.5f};
    Student s2 = {"이순신", 25, 94.0f};

    describe(s1);
    describe(s2);

    /* 함수 포인터 별명 활용 */
    Grader get_grade = grade_normal;
    printf("\n%s의 등급: %c\n", s1.name, get_grade(s1.score));
    printf("%s의 등급: %c\n", s2.name, get_grade(s2.score));

    return 0;
}
```

---

## 6. 마지막 정리

`typedef`는 타입에 별명을 붙여서 코드를 더 읽기 쉽게 만든다.

구조체와 함께 사용하면 `struct` 키워드를 매번 쓰지 않아도 된다.

`#define`과 달리 진짜 타입이라서 복잡한 선언에서도 안전하게 동작한다.

변수 이름에 의미를 담을 수 있어 (`Age`, `Score` 등) 코드의 의도가 명확해진다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp typedef",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
