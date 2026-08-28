# 제목
[C/Cpp 기초] 문자열 처리 함수

# 본문

## 1. 한 줄 요약

`<string.h>`의 문자열 함수들은 대부분 `\0` 종단 바이트에 의존하며, 경계 검사를 수행하지 않는 함수들(`strcpy`, `strcat`, `gets`)은 버퍼 오버플로우의 주요 원인이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

문자열 조작의 표준화와 이식성을 제공한다. 단, C의 문자열 함수들은 역사적으로 보안 취약점의 원인이 되어왔으며, 안전한 대안 함수 사용이 권장된다.

- `strcpy` → `strlcpy`(BSD) 또는 `snprintf`
- `strcat` → `strlcat`(BSD) 또는 `snprintf`
- `gets` → `fgets` (POSIX 2008에서 완전 제거)

---

## 3. 핵심 아이디어

### 문자열 함수의 복잡도

```text
strlen(s)     : O(n)  — \0까지 탐색
strcpy(d, s)  : O(n)  — \0 포함 복사
strcat(d, s)  : O(n+m) — d의 끝 탐색 후 s 복사
strcmp(s1, s2): O(n)  — 첫 불일치 시 종료
strchr(s, c)  : O(n)  — 선형 탐색
strstr(s, sub): O(n*m) — 단순 구현; KMP 등 최적화 가능
```

### `strstr`의 나이브 구현

```c
char *my_strstr(const char *haystack, const char *needle) {
    size_t nlen = strlen(needle);
    if (nlen == 0) return (char *)haystack;
    for (; *haystack; haystack++) {
        if (strncmp(haystack, needle, nlen) == 0)
            return (char *)haystack;
    }
    return NULL;
}
/* O(n*m): needle 길이가 길면 느림 */
```

### `strtok`의 상태 저장 문제

```c
/* strtok는 static 포인터를 사용 → 재진입 불가 (not reentrant) */
char s1[] = "a,b", s2[] = "1:2";
strtok(s1, ",");  /* 내부 상태: s1 위치 저장 */
strtok(s2, ":");  /* 내부 상태 충돌! */

/* 재진입 가능 버전 */
char *saveptr;
strtok_r(s1, ",", &saveptr);  /* POSIX */
```

---

## 4. 동작 과정 살펴보기

### 버퍼 오버플로우 메커니즘

```c
char dst[5];
strcpy(dst, "Hello, World!");  /* 13바이트 → 5바이트 버퍼 */

/* 스택 레이아웃:
   [dst: H e l l o][ , ][ W o r l d ! \0]
                         ↑ 버퍼 경계 침범
                         → 리턴 주소, 다른 변수 덮어씀 */
```

### `memcmp` vs `strcmp`

```c
/* strcmp: \0 만나면 중단 */
char a[] = "abc\0xyz";
char b[] = "abc\0ABC";
strcmp(a, b) == 0;   /* 같다고 판정 (xyz, ABC 무시) */

/* memcmp: 지정한 크기까지 비교 */
memcmp(a, b, 7) != 0;  /* xyz vs ABC: 다름 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* 안전한 문자열 복사 (snprintf 기반) */
size_t safe_strcpy(char *dst, size_t dst_size, const char *src) {
    if (!dst || dst_size == 0) return 0;
    size_t n = snprintf(dst, dst_size, "%s", src);
    return n >= dst_size ? dst_size - 1 : n;
}

/* 문자열 split (strtok_r 기반) */
char **str_split(const char *str, const char *delim, int *count) {
    char *copy = malloc(strlen(str) + 1);
    if (!copy) return NULL;
    strcpy(copy, str);

    /* 개수 파악 */
    int n = 1;
    for (const char *p = str; *p; p++) {
        if (strchr(delim, *p)) n++;
    }

    char **parts = malloc(n * sizeof(char *));
    if (!parts) { free(copy); return NULL; }

    char *saveptr, *token;
    int i = 0;
    token = strtok_r(copy, delim, &saveptr);
    while (token && i < n) {
        parts[i] = malloc(strlen(token) + 1);
        strcpy(parts[i++], token);
        token = strtok_r(NULL, delim, &saveptr);
    }
    *count = i;
    free(copy);
    return parts;
}

int main() {
    /* 안전한 복사 */
    char buf[10];
    size_t written = safe_strcpy(buf, sizeof(buf), "Hello, World!");
    printf("복사된 바이트: %zu, 결과: %s\n", written, buf);

    /* memcmp vs strcmp */
    char a[] = "abc\0xyz";
    char b[] = "abc\0ABC";
    printf("\nstrcmp: %s\n",  strcmp(a, b) == 0  ? "같음" : "다름");
    printf("memcmp: %s\n",  memcmp(a, b, 7) == 0 ? "같음" : "다름");

    /* str_split */
    int count;
    char **tokens = str_split("one:two:three:four", ":", &count);
    printf("\n분리 결과 (%d개):\n", count);
    for (int i = 0; i < count; i++) {
        printf("  [%d] %s\n", i, tokens[i]);
        free(tokens[i]);
    }
    free(tokens);

    return 0;
}
```

---

## 6. 마지막 정리

`strcpy`, `strcat`은 경계 검사 없이 쓰면 버퍼 오버플로우를 유발한다. `snprintf` 또는 `strlcpy`/`strlcat`을 사용한다.

`strtok`는 내부 전역 상태를 사용하므로 멀티스레드 환경에서는 `strtok_r`을 사용한다.

`strcmp`는 `\0` 이후를 무시하므로, 바이너리 데이터 비교에는 `memcmp`를 사용한다.

`strstr`의 나이브 구현은 O(n*m)이다. 고성능이 필요하면 KMP, Boyer-Moore 등을 고려한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열 처리 함수",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 5,
  "target_level": "high",
  "language": "c"
}
```
