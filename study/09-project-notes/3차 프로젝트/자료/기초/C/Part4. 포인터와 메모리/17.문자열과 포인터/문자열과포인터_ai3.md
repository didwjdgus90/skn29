# 제목
[C/Cpp 기초] 문자열과 포인터

# 본문

## 1. 한 줄 요약

C 문자열 리터럴은 `.rodata` 세그먼트에 배치된 읽기 전용 데이터로, `char *`로 가리키면 수정 시 UB이며, `char []`로 초기화하면 스택에 복사되어 수정 가능하다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

문자열 처리는 포인터 의미론을 깊이 이해해야 하는 영역이다.

함수 간 문자열 전달, 동적 문자열 조작, 경계 검사, 버퍼 오버플로우 방지 모두 포인터와 메모리 레이아웃 이해가 전제된다.

잘못된 문자열 조작은 역사적으로 가장 많은 보안 취약점을 유발했다.

---

## 3. 핵심 아이디어

### 메모리 배치

```c
char *p = "Hello";    /* 방식 1 */
char arr[] = "Hello"; /* 방식 2 */
```

```text
방식 1:
  .rodata: H e l l o \0  ← 읽기 전용 (mmap 보호 플래그: PROT_READ)
  stack:   p (주소 저장)

방식 2:
  stack:   H e l l o \0  ← 읽기/쓰기 가능

방식 1에서 p[0] = 'h' → SIGSEGV (segmentation fault)
방식 2에서 arr[0] = 'h' → 정상 동작
```

### const 정확성

```c
char *p = "Hello";       /* 경고: const char * 권장 */
const char *p = "Hello"; /* 올바름: 수정 불가 명시 */
```

`const char *`는 컴파일러가 수정 시도를 컴파일 오류로 잡아준다.

### 문자열 함수의 포인터 반환

많은 표준 문자열 함수는 포인터를 반환하여 체이닝을 가능케 한다.

```c
char *result = strcat(strcpy(buf, "Hello"), " World");
```

---

## 4. 동작 과정 살펴보기

### strcpy의 내부 구현

```c
char *strcpy(char *dest, const char *src) {
    char *d = dest;
    while ((*d++ = *src++));
    /* *src를 *d에 대입, 대입값이 0(\0)이면 루프 종료 */
    return dest;
}
```

후위 증감 연산자와 대입을 단일 표현식으로 처리하는 관용 코드.

### 버퍼 오버플로우

```c
char buf[5];
char *input = "Hello, World!";  /* 13바이트 */
strcpy(buf, input);  /* buf는 5바이트 → 스택 손상! */
```

스택 기반 버퍼 오버플로우는 리턴 주소를 덮어 임의 코드 실행으로 이어질 수 있다.

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/* 안전한 문자열 복사 */
int safe_copy(char *dest, size_t dest_size, const char *src) {
    if (!dest || !src || dest_size == 0) return -1;
    snprintf(dest, dest_size, "%s", src);
    return 0;
}

/* 동적 문자열 복제 */
char *str_dup(const char *src) {
    if (!src) return NULL;
    size_t len = strlen(src) + 1;
    char *dup = malloc(len);
    if (dup) memcpy(dup, src, len);
    return dup;
}

/* 문자열 역전 (in-place) */
void str_reverse(char *str) {
    char *left = str;
    char *right = str + strlen(str) - 1;
    while (left < right) {
        char tmp = *left;
        *left++ = *right;
        *right-- = tmp;
    }
}

int main() {
    /* 리터럴 포인터와 배열 비교 */
    const char *lit = "Hello";
    char arr[] = "Hello";

    printf("리터럴 주소: %p\n", (void *)lit);
    printf("배열 주소:   %p\n", (void *)arr);
    /* 서로 다른 메모리 영역 */

    /* 안전한 복사 */
    char buf[10];
    safe_copy(buf, sizeof(buf), "Test");
    printf("안전 복사: %s\n", buf);

    /* 동적 복제 */
    char *dup = str_dup("Dynamic");
    if (dup) {
        printf("동적 복제: %s\n", dup);
        str_reverse(dup);
        printf("역전: %s\n", dup);
        free(dup);  /* 반드시 해제 */
    }

    /* 부분 문자열 (포인터로) */
    const char *full = "Hello, World!";
    const char *sub = full + 7;  /* "World!" */
    printf("부분 문자열: %s\n", sub);

    /* 포인터 배열: 문자열 테이블 */
    const char *errors[] = {
        "성공",
        "파일 없음",
        "권한 없음",
        "메모리 부족"
    };
    int code = 2;
    printf("오류: %s\n", errors[code]);

    return 0;
}
```

---

## 6. 마지막 정리

문자열 리터럴은 `.rodata`의 읽기 전용 데이터이다. `char *`로 가리키면 타입 시스템 위반이며 수정 시 SIGSEGV.

`const char *`를 사용하면 컴파일러가 수정 시도를 거부한다.

`strcpy`/`strcat`은 경계 검사가 없으므로 `snprintf`, `strncat` 등 크기 제한 함수를 사용해야 한다.

동적 문자열은 `malloc` + `free` 쌍으로 수명을 관리한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열과 포인터",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
