# 제목
[C/Cpp 기초] 입력과 출력

# 본문

## 1. 한 줄 요약

C의 표준 입출력은 스트림(stream) 기반이며, `stdio.h`가 제공하는 버퍼링된 I/O 추상화를 통해 `stdin`/`stdout`/`stderr` 스트림과 통신한다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

운영체제의 파일 시스템과 하드웨어 I/O는 저수준이며 플랫폼 의존적이다.

`<stdio.h>`는 ANSI C 표준 입출력 라이브러리로, 버퍼링과 형식 변환을 추상화하여 이식성 있는 I/O를 제공한다.

세 가지 기본 스트림이 자동으로 열린다.
- `stdin`: 표준 입력 (기본: 키보드)
- `stdout`: 표준 출력 (기본: 터미널)
- `stderr`: 표준 오류 (기본: 터미널, 버퍼링 없음)

---

## 3. 핵심 아이디어

### 버퍼링 동작 원리

`stdout`은 기본적으로 라인 버퍼링(line-buffered, 터미널 연결 시) 또는 완전 버퍼링(파이프/파일 리다이렉션 시)된다.

```c
printf("loading...");
/* 버퍼에 있어서 즉시 출력 안 될 수 있음 */

fflush(stdout);  /* 버퍼 즉시 플러시 */
/* 또는 */
printf("loading...\n");  /* \n이 라인 버퍼 플러시 트리거 */
```

### printf의 형식 지정자 규격

```text
%[flags][width][.precision][length]type

flags:   -(왼쪽 정렬), +(부호 항상), 0(0 패딩), ' '(공백)
width:   최소 출력 너비
precision: 소수점 자릿수 또는 문자열 최대 길이
length:  hh, h, l, ll, L (타입 수정자)
type:    d, i, u, f, e, g, s, c, p, x, o ...
```

### scanf의 보안 취약점

`scanf("%s", buf)`는 버퍼 크기를 검사하지 않는다. 길이 제한 필수.

```c
/* 위험 */
char buf[10];
scanf("%s", buf);  /* 10자 초과 입력 시 스택 오버플로우 */

/* 안전 */
scanf("%9s", buf);  /* 최대 9자 + null */
```

---

## 4. 동작 과정 살펴보기

### scanf의 반환값 활용

`scanf`는 성공적으로 읽은 항목 수를 반환한다.

```c
int a, b;
int result = scanf("%d %d", &a, &b);
if (result != 2) {
    fprintf(stderr, "입력 오류: %d개만 읽힘\n", result);
    return 1;
}
```

### 입력 버퍼 비우기

`scanf`로 정수를 읽은 후 문자/문자열을 읽으면 이전 입력의 `\n`이 남아있어 문제가 생긴다.

```c
int n;
char c;
scanf("%d", &n);
scanf(" %c", &c);  /* 공백으로 앞의 공백/개행 소비 */
```

또는 `getchar()`로 명시적으로 비운다.

```c
scanf("%d", &n);
while (getchar() != '\n');  /* 버퍼 비우기 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    /* 형식 지정자 정밀 제어 */
    int   i = 255;
    double d = 3.14159265358979;

    printf("10진수: %d\n", i);
    printf("16진수: %x (대: %X)\n", i, i);
    printf("8진수:  %o\n", i);
    printf("고정 소수점: %.6f\n", d);
    printf("지수 표기:   %e\n", d);
    printf("자동 선택:   %g\n", d);

    /* 너비와 정렬 */
    printf("|%10d|\n", 42);    /* |        42| */
    printf("|%-10d|\n", 42);   /* |42        | */
    printf("|%010d|\n", 42);   /* |0000000042| */

    /* 안전한 입력 처리 */
    char name[20];
    int age;

    printf("이름 (최대 19자): ");
    if (scanf("%19s", name) != 1) {
        fprintf(stderr, "입력 오류\n");
        return 1;
    }

    printf("나이: ");
    if (scanf("%d", &age) != 1 || age < 0 || age > 150) {
        fprintf(stderr, "유효하지 않은 나이\n");
        return 1;
    }

    printf("이름: %s, 나이: %d\n", name, age);

    /* stderr로 에러 메시지 */
    if (age < 18) {
        fprintf(stderr, "경고: 미성년자\n");
    }

    return 0;
}
```

### sprintf/sscanf: 문자열 기반 I/O

```c
char buf[100];
/* 메모리로 출력 */
sprintf(buf, "이름: %s, 점수: %d", name, score);

int x, y;
/* 문자열에서 파싱 */
sscanf("10 20", "%d %d", &x, &y);
```

---

## 6. 마지막 정리

C I/O는 스트림 기반 버퍼링 추상화이며, `stdout`의 버퍼링 방식을 이해해야 실시간 출력을 보장할 수 있다.

`printf`의 형식 지정자는 `%[flags][width][.precision][length]type` 규격이다.

`scanf`에서 버퍼 크기 제한(`%9s`)은 필수이며, 반환값으로 입력 성공 여부를 확인해야 한다.

오류 메시지는 `fprintf(stderr, ...)`로 `stderr`에 출력하는 것이 좋다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 입력과 출력",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
