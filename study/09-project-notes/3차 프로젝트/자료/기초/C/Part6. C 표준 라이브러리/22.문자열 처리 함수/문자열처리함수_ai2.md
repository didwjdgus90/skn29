# 제목
[C/Cpp 기초] 문자열 처리 함수

# 본문

## 1. 한 줄 요약

문자열 처리 함수들은 문자열이라는 재료를 다루는 주방 도구들이다. 길이 재기, 복사, 붙이기, 비교, 잘라내기 등 각 도구마다 쓸 곳이 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

요리사가 매번 칼을 직접 만들지 않듯, 문자열을 다룰 때마다 처음부터 코드를 짜지 않아도 된다.

```text
표준 라이브러리 = 이미 만들어진 주방 도구 세트

strlen  = 자 (길이 재기)
strcpy  = 복사기 (내용 복사)
strcat  = 풀 (뒤에 붙이기)
strcmp  = 저울 (둘 비교)
strchr  = 찾기 도구 (특정 글자 위치)
strtok  = 가위 (구분자로 자르기)
```

---

## 3. 핵심 아이디어

### 자 (strlen)

```c
char str[] = "Hello";
int len = strlen(str);  /* 5 */

/* \0은 세지 않는다 */
/* H-e-l-l-o = 5글자 */
```

### 복사기 (strcpy)

```c
char src[] = "Hello";
char dst[20];
strcpy(dst, src);
/* dst: "Hello" */
/* 주의: dst가 충분히 커야 함! */
```

### 풀 (strcat)

```c
char buf[20] = "Hello";
strcat(buf, " World");
/* buf: "Hello World" */
/* 뒤에 붙인다 */
```

### 저울 (strcmp)

```c
strcmp("abc", "abc");  /* 0: 같음 */
strcmp("abc", "abd");  /* 음수: abc < abd */
strcmp("b", "a");      /* 양수: b > a */
```

---

## 4. 동작 과정 살펴보기

### 가위 (strtok): 문자열 자르기

```text
원본: "사과,바나나,딸기"
       ↑        ↑
       ','로 자름

1번째 잘린 조각: "사과"
2번째 잘린 조각: "바나나"
3번째 잘린 조각: "딸기"
4번째 호출: NULL (더 없음)
```

주의: 원본 문자열이 변경된다(구분자가 `\0`으로 바뀐다).

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <string.h>

int main() {
    /* 자 사용: 길이 재기 */
    char greeting[] = "안녕하세요";
    printf("바이트 수: %zu\n", strlen(greeting));

    /* 복사기 사용 */
    char original[] = "Hello, C!";
    char copy[20];
    strcpy(copy, original);
    printf("복사본: %s\n", copy);

    /* 안전한 복사기: 크기 제한 */
    char safe_copy[5];
    strncpy(safe_copy, original, 4);
    safe_copy[4] = '\0';  /* 수동으로 종료 문자 추가 */
    printf("안전 복사: %s\n", safe_copy);

    /* 풀 사용: 뒤에 붙이기 */
    char sentence[50] = "오늘은";
    strcat(sentence, " 날씨가");
    strcat(sentence, " 맑다.");
    printf("붙인 결과: %s\n", sentence);

    /* 저울 사용: 비교 */
    const char *words[] = {"banana", "apple", "cherry"};
    /* apple과 banana 비교 */
    if (strcmp(words[0], words[1]) > 0) {
        printf("%s가 %s보다 사전에서 뒤에 있어요\n", words[0], words[1]);
    }

    /* 찾기 도구: 특정 글자 위치 */
    char email[] = "user@example.com";
    char *at = strchr(email, '@');
    if (at) printf("도메인: %s\n", at + 1);  /* @ 이후 */

    /* 가위 사용: CSV 파싱 */
    char data[] = "홍길동,20,서울,컴퓨터공학";
    printf("\n데이터 파싱:\n");
    const char *labels[] = {"이름", "나이", "도시", "전공"};
    int i = 0;
    char *field = strtok(data, ",");
    while (field && i < 4) {
        printf("  %s: %s\n", labels[i++], field);
        field = strtok(NULL, ",");
    }

    return 0;
}
```

---

## 6. 마지막 정리

`strlen`은 `\0` 전까지의 글자 수를 센다.

`strcpy`와 `strcat`은 버퍼가 충분히 큰지 확인 후 사용해야 한다.

`strcmp`는 같으면 0, 작으면 음수, 크면 양수를 돌려준다.

`strtok`는 원본을 수정하므로 필요하면 복사본에 사용한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 문자열 처리 함수",
  "source_type": "generated",
  "style": ["easy", "analogy"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 4,
  "target_level": "low",
  "language": "c"
}
```
