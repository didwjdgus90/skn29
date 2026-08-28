# 제목
[C/Cpp 기초] 문자열

# 본문

## 1. 한 줄 요약

C의 문자열은 null 종단 문자(`\0`, 값 0x00)로 끝나는 `char` 배열이며, 언어 수준의 타입이 아닌 관례적 표현이다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

고수준 언어와 달리 C는 문자열을 일급 타입으로 지원하지 않는다.

대신 C 표준은 문자 배열의 마지막 원소가 null 문자(`\0`, 정수 0)인 경우를 "문자열"로 간주하는 관례를 정의하고, 이를 기반으로 `<string.h>` 라이브러리를 제공한다.

이 설계는 저수준 메모리 직접 접근과 높은 성능을 가능케 하지만, 버퍼 오버플로우 취약점의 주요 원인이기도 하다.

---

## 3. 핵심 아이디어

### 메모리 레이아웃

```c
char str[] = "Hello";
```

```text
주소    값(hex)  문자
0x100   0x48    'H'
0x101   0x65    'e'
0x102   0x6C    'l'
0x103   0x6C    'l'
0x104   0x6F    'o'
0x105   0x00    '\0'  ← null terminator
```

컴파일러는 문자열 리터럴 뒤에 자동으로 `\0`을 추가한다.

### char 배열 vs char 포인터

```c
char arr[] = "Hello";   /* 스택에 6바이트 복사 */
char *ptr  = "Hello";   /* .rodata 세그먼트의 리터럴을 가리킴 */
```

| | `char arr[]` | `char *ptr` |
|---|---|---|
| 메모리 위치 | 스택 | .rodata (읽기 전용) |
| 수정 가능 | 가능 | Undefined Behavior |
| sizeof 결과 | 배열 크기 | 포인터 크기 |

### strlen의 동작

```c
size_t strlen(const char *s) {
    size_t n = 0;
    while (s[n] != '\0') n++;
    return n;
}
```

O(n) 시간 복잡도이다. 루프 안에서 반복 호출하면 성능 저하가 발생한다.

---

## 4. 동작 과정 살펴보기

### 버퍼 오버플로우 위험

```c
char buf[5];
strcpy(buf, "Hello, World!");  /* 위험! 버퍼 초과 */
```

`strcpy`는 목적지 버퍼 크기를 검사하지 않는다. 초과 쓰기는 인접 메모리를 덮어 스택 스매싱, 리턴 주소 오염 등 심각한 취약점을 유발한다.

### 안전한 대안 함수

```c
/* strncpy: 최대 n-1개 복사, null 보장 안 됨 */
strncpy(buf, src, sizeof(buf) - 1);
buf[sizeof(buf) - 1] = '\0';

/* snprintf: 가장 안전 */
snprintf(buf, sizeof(buf), "%s", src);
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello, World!";
    char dst[20];

    /* 안전한 복사 */
    snprintf(dst, sizeof(dst), "%s", src);

    /* 포인터를 이용한 순회 */
    const char *p = src;
    size_t len = 0;
    while (*p++ != '\0') len++;
    printf("수동 계산 길이: %zu\n", len);
    printf("strlen 결과: %zu\n", strlen(src));

    /* 문자 비교: ASCII 값 기반 */
    printf("strcmp 결과: %d\n", strcmp("abc", "abd"));
    /* 'c'(99) - 'd'(100) = -1 (음수: 첫 번째 인자가 작음) */

    /* 부분 문자열 탐색 */
    char *found = strstr(src, "World");
    if (found) {
        printf("'World' 발견 위치: %td\n", found - src);
    }

    return 0;
}
```

### 멀티바이트 문자(UTF-8) 주의

C의 `char`는 1바이트이므로, 한글 등 멀티바이트 문자는 `strlen`으로 정확한 문자 수를 셀 수 없다.

```c
char korean[] = "안녕";  /* UTF-8에서 각 한글은 3바이트 */
printf("%zu\n", strlen(korean));  /* 6 (바이트 수) */
```

와이드 문자(`wchar_t`, `<wchar.h>`) 또는 ICU 라이브러리 사용을 고려해야 한다.

---

## 6. 마지막 정리

C 문자열은 null 종단 `char` 배열이라는 관례이며, 언어 내장 타입이 아니다.

`char arr[]`는 스택 복사, `char *ptr`은 .rodata 포인터이며 수정하면 UB이다.

`strcpy`/`strcat` 등은 경계 검사가 없으므로 `snprintf`, `strncat` 같은 크기 제한 함수를 사용해야 한다.

멀티바이트(한글, 한자 등) 처리는 `strlen`이 바이트 수를 반환하므로 별도 처리가 필요하다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
