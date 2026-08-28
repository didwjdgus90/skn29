# 제목
[C/Cpp 기초] 문자열과 포인터

# 본문

## 1. 한 줄 요약

문자열 리터럴은 박물관 전시물(수정 불가), char 배열은 내 노트(수정 가능)이다. 포인터는 어느 쪽이든 가리킬 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

같은 `char *`처럼 보이는 두 문자열이 있다.

```c
char *p1 = "Hello";    /* 박물관 전시물 */
char arr[] = "Hello";  /* 내 노트 */
```

전시물을 수정하려 하면 경비원(운영체제)이 막는다!

```c
p1[0] = 'h';   /* 위험! 프로그램 종료 가능 */
arr[0] = 'h';  /* OK: 내 노트는 수정 가능 */
```

이 차이를 모르면 예상치 못한 버그가 생긴다.

---

## 3. 핵심 아이디어

### 두 종류의 문자열 저장소

```text
char *p = "Hello";

[박물관 전시실 - 읽기 전용]
H  e  l  l  o  \0
↑
p가 여기를 가리킴 (전시물의 주소 저장)

p[0] = 'h' → 전시물 수정 시도 → 경비원 차단!
```

```text
char str[] = "Hello";

[내 노트 - 스택]
H  e  l  l  o  \0
↑
str은 이 노트 자체

str[0] = 'h' → 내 노트 수정 → OK!
```

### 포인터로 문자열 읽기

```c
const char *p = "Hello";
while (*p) {          /* \0이 아닌 동안 */
    printf("%c", *p);
    p++;              /* 다음 문자로 이동 */
}
```

---

## 4. 동작 과정 살펴보기

### 포인터 이동 = 책 페이지 넘기기

```text
"Hello\0" 읽기:

시작: p → H
  출력 'H', p++ → e
  출력 'e', p++ → l
  출력 'l', p++ → l
  출력 'l', p++ → o
  출력 'o', p++ → \0
  *p == '\0' → 종료
```

### 포인터 위치 바꾸기

```text
const char *p = "Hello";  ← p가 "Hello" 전시물을 가리킴
p = "World";              ← p가 "World" 전시물로 이동

전시물 자체는 변함없음, 가리키는 곳만 바뀜
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 박물관 전시물 (수정 불가) */
    const char *exhibit = "Hello";
    printf("전시물: %s\n", exhibit);

    /* 가리키는 전시물은 바꿀 수 있음 */
    exhibit = "World";
    printf("다른 전시물: %s\n", exhibit);

    /* 내 노트 (수정 가능) */
    char notebook[] = "Hello";
    notebook[0] = 'h';  /* 내 노트 수정 OK */
    printf("수정된 노트: %s\n", notebook);

    /* 포인터로 문자열 읽기 */
    const char *sentence = "I love C";
    int word_count = 0;
    const char *p = sentence;

    printf("\n글자별 출력:\n");
    while (*p) {
        printf("%c", *p);
        if (*p == ' ' || *(p+1) == '\0') word_count++;
        p++;
    }
    printf("\n단어 수: %d\n", word_count);

    /* 문자열 포인터 배열 */
    const char *days[] = {"월", "화", "수", "목", "금", "토", "일"};
    int today = 2;  /* 수요일 */
    printf("\n오늘은 %s요일입니다.\n", days[today]);

    return 0;
}
```

### 문자열 함수들은 포인터를 사용한다

```text
strlen(str):  str → 끝(\0)까지 이동 → 거리 반환
strcpy(d, s): s의 각 문자를 d에 복사, \0 포함
strcmp(s1,s2): 두 포인터를 동시에 이동하며 문자 비교
```

---

## 6. 마지막 정리

문자열 리터럴(`"Hello"`)은 읽기 전용 박물관 전시물이다. 수정하면 프로그램이 죽는다.

`char arr[] = "Hello"`는 내 노트이다. 자유롭게 수정 가능.

포인터로 전시물의 내용은 못 바꾸지만, 다른 전시물을 가리키는 것은 가능하다.

`const char *`를 쓰면 컴파일러가 전시물 수정 시도를 사전에 차단해 준다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열과 포인터",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
