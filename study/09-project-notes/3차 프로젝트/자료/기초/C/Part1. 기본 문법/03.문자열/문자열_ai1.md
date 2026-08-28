# 제목
[C/Cpp 기초] 문자열

# 본문

## 1. 한 줄 요약

C에는 별도의 문자열 타입이 없으며, 문자열은 null 문자(`\0`)로 끝나는 `char` 배열로 표현된다.

C에서 문자열을 이해하면 텍스트 데이터를 저장하고 출력하며 조작할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램에서 이름, 메시지, 경로 등 텍스트 데이터를 다뤄야 하는 경우가 많다.

Java나 Python과 달리 C에는 `String` 타입이 존재하지 않는다.

C에서는 `char` 배열을 이용해 문자열을 직접 표현한다.

```c
char name[10] = "Alice";
```

이때 중요한 것은 문자열의 끝을 나타내는 null 문자(`\0`)이다.

---

## 3. 핵심 아이디어

### null 종단 문자열

C 문자열은 문자들의 배열이며, 마지막에 반드시 `\0`(null 문자, 값은 0)이 붙는다.

```text
"Hello" 를 메모리에 저장하면:

인덱스:  [0]  [1]  [2]  [3]  [4]  [5]
문자:     H    e    l    l    o   \0
값(ASCII): 72   101  108  108  111   0
```

배열 크기는 문자 수 + 1(null 문자 자리)이어야 한다.

```c
char str[6] = "Hello";  /* 5개 문자 + \0 = 6바이트 */
```

### 선언 방법 두 가지

**방법 1: char 배열**

```c
char str1[] = "Hello";        /* 크기 자동 계산 (6) */
char str2[10] = "Hello";      /* 크기 직접 지정 */
char str3[10];                /* 선언만, 이후 값 입력 */
```

**방법 2: char 포인터 (문자열 리터럴)**

```c
char *str4 = "Hello";         /* 수정 불가! */
```

---

## 4. 동작 과정 살펴보기

### 문자열 길이와 배열 크기

```c
char str[] = "Hello";

/* 배열 크기: 6 (H, e, l, l, o, \0) */
printf("배열 크기: %zu\n", sizeof(str));   /* 6 */

/* 문자열 길이: 5 (\0 제외) */
#include <string.h>
printf("문자열 길이: %zu\n", strlen(str));  /* 5 */
```

### 문자 하나씩 접근하기

```c
char str[] = "Hello";
int i = 0;
while (str[i] != '\0') {
    printf("%c\n", str[i]);
    i++;
}
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

int main() {
    /* 문자열 배열 선언 */
    char name[20] = "Alice";
    char greeting[50];

    /* 문자열 길이 */
    printf("이름: %s\n", name);
    printf("이름 길이: %zu\n", strlen(name));

    /* 문자열 복사 */
    char copy[20];
    strcpy(copy, name);
    printf("복사본: %s\n", copy);

    /* 문자열 연결 */
    strcpy(greeting, "Hello, ");
    strcat(greeting, name);
    printf("%s!\n", greeting);

    /* 문자열 비교 */
    if (strcmp(name, "Alice") == 0) {
        printf("이름이 Alice입니다.\n");
    }

    /* 개별 문자 접근 */
    printf("첫 글자: %c\n", name[0]);
    printf("두 번째 글자: %c\n", name[1]);

    return 0;
}
```

### scanf로 문자열 입력

```c
#include <stdio.h>

int main() {
    char name[50];
    printf("이름을 입력하세요: ");
    scanf("%s", name);  /* 공백 전까지 읽음 */
    printf("안녕하세요, %s!\n", name);
    return 0;
}
```

공백이 포함된 문자열을 읽으려면 `fgets`를 사용한다.

```c
fgets(name, sizeof(name), stdin);  /* 한 줄 전체 읽기 */
```

---

## 6. 마지막 정리

C에서 문자열은 `\0`으로 끝나는 `char` 배열이다.

배열 크기는 문자 수보다 1 크게 선언해야 null 문자 자리가 생긴다.

`strlen`은 문자열 길이(null 제외), `sizeof`는 배열 전체 크기를 반환한다.

문자열 처리에는 `<string.h>`의 함수들(strcpy, strcat, strcmp 등)을 활용한다.

`char *str = "literal"`로 선언된 문자열은 수정하면 안 된다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
