# 제목
[C/Cpp 기초] 문자열

# 본문

## 1. 한 줄 요약

C의 문자열은 마지막에 종료 신호(`\0`)가 붙은 문자들의 줄이다. 마치 마지막에 마침표가 있는 문장처럼.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

사람 이름, 인사말, 메시지처럼 글자로 이루어진 데이터가 필요할 때가 있다.

C에는 Java의 String, Python의 str 같은 전용 문자열 타입이 없다.

대신 알파벳 하나하나를 담는 `char` 상자들을 일렬로 세워서 문자열을 만든다.

```text
"Hello"를 저장하는 방법:

[H][e][l][l][o][\0]
                 ↑
             끝 표시 (null 문자)
```

마지막의 `\0`은 "여기서 문자열이 끝났습니다"라는 신호이다.

---

## 3. 핵심 아이디어

### 진주 목걸이 비유

문자열은 진주 목걸이와 같다.

```text
H → e → l → l → o → \0
진주 진주 진주 진주 진주  마지막 고리(끝 신호)
```

각 진주(문자)를 순서대로 꿰어두고, 마지막에 특별한 고리(`\0`)로 묶어두는 것이다.

이 고리가 없으면 목걸이가 어디서 끝나는지 알 수 없다.

### 상자들을 일렬로 (char 배열)

```text
char name[] = "Alice";

name[0] = 'A'
name[1] = 'l'
name[2] = 'i'
name[3] = 'c'
name[4] = 'e'
name[5] = '\0'  ← 끝 표시 (자동으로 추가됨)
```

크기를 직접 정할 때는 null 문자 자리를 포함해야 한다.

```c
char name[6] = "Alice";  /* 5글자 + \0 = 6칸 */
```

---

## 4. 동작 과정 살펴보기

### strlen - 목걸이 진주 개수 세기

`strlen`은 `\0`이 나올 때까지 진주(문자)를 세어 길이를 알려준다.

```text
H → e → l → l → o → \0
↑                    ↑
시작                여기서 멈춤

진주 5개 = 길이 5
```

```c
#include <string.h>
char name[] = "Alice";
printf("%zu\n", strlen(name));  /* 5 출력 */
```

### sizeof와 strlen의 차이

```text
char str[10] = "Hi";

sizeof(str)  → 10  (상자 전체 개수)
strlen(str)  →  2  (실제 문자 수, \0 제외)
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

int main() {
    /* 목걸이 만들기 */
    char greeting[] = "Hello";
    char name[20] = "World";

    printf("인사말: %s\n", greeting);
    printf("이름: %s\n", name);

    /* 두 목걸이 연결하기 (strcat) */
    char message[50] = "Hello, ";
    strcat(message, "World!");
    printf("%s\n", message);

    /* 목걸이 복사하기 (strcpy) */
    char copy[20];
    strcpy(copy, name);
    printf("복사: %s\n", copy);

    /* 두 목걸이 비교하기 (strcmp) */
    /* 같으면 0, 다르면 0이 아닌 값 반환 */
    if (strcmp(greeting, "Hello") == 0) {
        printf("같은 문자열입니다!\n");
    }

    return 0;
}
```

### 문자열 수정 가능/불가능

```text
방법 1: char 배열 → 수정 가능 (내 노트)
  char str[] = "Hello";
  str[0] = 'h';  /* OK */

방법 2: char 포인터 → 수정 불가 (박물관 전시물)
  char *str = "Hello";
  str[0] = 'h';  /* 위험! 프로그램이 멈출 수 있음 */
```

---

## 6. 마지막 정리

C의 문자열은 `\0`(null 문자)로 끝나는 문자들의 줄이다.

`char 배열`로 선언하면 내용을 바꿀 수 있고, `char *`로 리터럴을 가리키면 바꿀 수 없다.

`strlen`은 `\0` 전까지의 문자 수를 세고, `sizeof`는 배열 전체 크기를 반환한다.

`<string.h>`에는 문자열을 다루는 유용한 함수들(strcpy, strcat, strcmp)이 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
