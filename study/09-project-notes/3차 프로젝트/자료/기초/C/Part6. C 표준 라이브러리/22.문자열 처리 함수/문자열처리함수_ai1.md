# 제목
[C/Cpp 기초] 문자열 처리 함수

# 본문

## 1. 한 줄 요약

`<string.h>`에서 제공하는 문자열 처리 함수들은 문자열 길이, 복사, 연결, 비교, 검색 등 문자열 조작의 기본 도구이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

C 문자열은 `char` 배열로 이루어져 있어 직접 조작이 불편하다. `string.h`의 함수들이 이를 편리하게 처리한다.

```c
/* string.h 없이 길이 구하기 */
int len = 0;
while (str[len] != '\0') len++;

/* strlen 사용 */
int len = strlen(str);
```

---

## 3. 핵심 아이디어

### 주요 함수들

| 함수 | 설명 |
|---|---|
| `strlen(s)` | 문자열 길이 반환 (\0 제외) |
| `strcpy(dst, src)` | src를 dst에 복사 |
| `strncpy(dst, src, n)` | 최대 n개 문자 복사 |
| `strcat(dst, src)` | dst 뒤에 src 연결 |
| `strncat(dst, src, n)` | 최대 n개 문자 연결 |
| `strcmp(s1, s2)` | 문자열 비교 |
| `strncmp(s1, s2, n)` | 최대 n개 문자 비교 |
| `strchr(s, c)` | 첫 번째 c 위치 포인터 반환 |
| `strstr(s, sub)` | 부분 문자열 검색 |
| `strtok(s, delim)` | 구분자로 토큰화 |

### 비교 결과

```c
strcmp(s1, s2)
 < 0: s1이 s2보다 앞 (사전순)
 = 0: 같음
 > 0: s1이 s2보다 뒤 (사전순)
```

---

## 4. 동작 과정 살펴보기

### strcpy와 strcat 동작

```text
strcpy(dst, "Hello"):
  dst: [H][e][l][l][o][\0]

strcat(dst, " World"):
  dst: [H][e][l][l][o][ ][W][o][r][l][d][\0]
       ↑ 기존 \0 위치부터 덮어쓰기
```

### strtok 동작

```text
strtok("a,b,c", ","):
  1번 호출: "a" 반환, 내부 포인터가 "b,c" 위치
  2번 호출 strtok(NULL, ","): "b" 반환
  3번 호출 strtok(NULL, ","): "c" 반환
  4번 호출 strtok(NULL, ","): NULL 반환 (끝)
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

int main() {
    char s1[] = "Hello";
    char s2[] = "World";
    char buf[100];

    /* strlen */
    printf("길이: %zu\n", strlen(s1));

    /* strcpy */
    strcpy(buf, s1);
    printf("복사: %s\n", buf);

    /* strcat */
    strcat(buf, " ");
    strcat(buf, s2);
    printf("연결: %s\n", buf);

    /* strcmp */
    int cmp = strcmp(s1, s2);
    if      (cmp < 0) printf("%s < %s\n", s1, s2);
    else if (cmp > 0) printf("%s > %s\n", s1, s2);
    else              printf("%s == %s\n", s1, s2);

    /* strchr */
    char sentence[] = "Hello, World!";
    char *pos = strchr(sentence, 'W');
    if (pos) printf("'W' 위치: %td번째\n", pos - sentence);

    /* strstr */
    char *sub = strstr(sentence, "World");
    if (sub) printf("'World' 발견: %s\n", sub);

    /* strtok */
    char csv[] = "apple,banana,cherry";
    char *token = strtok(csv, ",");
    printf("\nCSV 파싱:\n");
    while (token != NULL) {
        printf("  - %s\n", token);
        token = strtok(NULL, ",");
    }

    /* snprintf: 안전한 포맷 출력 */
    char result[50];
    snprintf(result, sizeof(result), "Score: %d / %d", 85, 100);
    printf("\n%s\n", result);

    /* 대소문자 변환 (ctype.h 필요) */
    #include <ctype.h>
    char word[] = "Hello World";
    for (int i = 0; word[i]; i++) {
        word[i] = tolower(word[i]);
    }
    printf("소문자: %s\n", word);

    return 0;
}
```

> 참고: tolower/toupper는 `<ctype.h>` 포함 필요.

---

## 6. 마지막 정리

`strlen`은 `\0` 제외 길이를 반환한다. 배열 크기와 혼동하지 말 것.

`strcpy`/`strcat`은 버퍼 크기를 확인하지 않으므로 오버플로우 위험이 있다. `strncpy`/`strncat`으로 크기를 제한한다.

`strcmp`는 0이면 같음, 다르면 음수/양수를 반환한다.

`strtok`는 원본 문자열을 수정(구분자를 `\0`으로 교체)하므로 원본 보존이 필요하면 복사 후 사용한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열 처리 함수",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 4,
  "friendliness_score": 4,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
