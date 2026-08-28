# 제목
[C/Cpp 기초] 문자열과 포인터

# 본문

## 1. 한 줄 요약

C에서 문자열은 포인터로 다루며, `char *`로 문자열 리터럴을 가리키거나 `char[]` 배열을 포인터처럼 다룰 수 있다. 두 방식은 수정 가능 여부가 다르다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

문자열을 함수에 전달하거나 문자 단위로 처리할 때 포인터를 사용한다.

```c
/* 포인터로 문자열 처리 */
void to_upper(char *str) {
    while (*str) {
        if (*str >= 'a' && *str <= 'z') {
            *str -= 32;
        }
        str++;
    }
}
```

---

## 3. 핵심 아이디어

### 두 가지 선언 방식

**방식 1: char 배열 (수정 가능)**

```c
char str[] = "Hello";  /* 스택에 복사, 수정 가능 */
str[0] = 'h';          /* OK */
```

**방식 2: char 포인터 (수정 불가)**

```c
char *p = "Hello";  /* 읽기 전용 영역을 가리킴 */
p[0] = 'h';        /* 위험! 런타임 오류 가능 */
```

### 포인터로 문자열 순회

```c
char str[] = "Hello";
char *p = str;

while (*p != '\0') {
    printf("%c\n", *p);
    p++;
}
```

### 포인터가 가리키는 곳 변경

```c
char *p = "Hello";
p = "World";  /* 다른 문자열로 포인터만 변경 */
printf("%s\n", p);  /* World */
```

---

## 4. 동작 과정 살펴보기

### char 배열 vs char 포인터

```text
char str[] = "Hello";
메모리: [ H ][ e ][ l ][ l ][ o ][\0 ]  ← 스택에 복사
str → str[0]의 주소 (배열 자체가 데이터)

char *p = "Hello";
메모리:
  .rodata: [ H ][ e ][ l ][ l ][ o ][\0 ]  ← 읽기 전용
p → .rodata의 'H' 주소 (포인터만 스택에)
```

### strlen 구현 (포인터 버전)

```c
size_t my_strlen(const char *s) {
    const char *p = s;
    while (*p != '\0') p++;  /* \0 전까지 이동 */
    return p - s;            /* 이동한 거리 = 문자 수 */
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

/* 포인터로 문자열 복사 */
void my_strcpy(char *dest, const char *src) {
    while ((*dest++ = *src++));  /* src를 dest에 복사, \0도 복사되면 루프 종료 */
}

/* 포인터로 문자 찾기 */
char *my_strchr(const char *str, char c) {
    while (*str) {
        if (*str == c) return (char *)str;
        str++;
    }
    return NULL;
}

int main() {
    /* 배열 - 수정 가능 */
    char greeting[] = "Hello, World!";
    greeting[0] = 'h';
    printf("수정된 문자열: %s\n", greeting);

    /* 포인터 - 수정 불가, 가리키는 곳 변경은 가능 */
    const char *msg = "Hello";
    printf("msg: %s\n", msg);
    msg = "Goodbye";  /* 포인터가 다른 곳을 가리킴 */
    printf("msg: %s\n", msg);

    /* 포인터로 문자열 순회 */
    char str[] = "Programming";
    char *p = str;
    int count = 0;
    while (*p) {
        if (*p >= 'a' && *p <= 'z') count++;
        p++;
    }
    printf("소문자 개수: %d\n", count);

    /* 직접 구현한 함수들 */
    char src[] = "Test String";
    char dest[20];
    my_strcpy(dest, src);
    printf("복사 결과: %s\n", dest);

    char *found = my_strchr(str, 'g');
    if (found) {
        printf("'g' 발견: %s\n", found);
    }

    return 0;
}
```

### 문자열 배열

```c
/* 문자열 포인터 배열 */
const char *fruits[] = {"apple", "banana", "cherry"};
int n = 3;

for (int i = 0; i < n; i++) {
    printf("%s\n", fruits[i]);
}
```

---

## 6. 마지막 정리

`char *p = "literal"`은 읽기 전용 메모리를 가리키므로 내용 수정은 UB이다.

`char str[] = "literal"`은 스택에 복사되므로 내용 수정이 가능하다.

포인터로 문자열을 순회할 때 `\0`을 만나면 종료한다.

`const char *`를 사용하면 컴파일러가 수정 시도를 감지할 수 있다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열과 포인터",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
