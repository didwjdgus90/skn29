# 제목
[C/Cpp 기초] 입력과 출력

# 본문

## 1. 한 줄 요약

C의 입출력은 `printf`로 화면에 출력하고, `scanf`로 키보드에서 입력받는다.

`<stdio.h>` 헤더를 포함하면 표준 입출력 함수들을 사용할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

프로그램이 사용자와 소통하려면 정보를 화면에 보여주고, 사용자의 입력을 받아야 한다.

```c
printf("이름을 입력하세요: ");  /* 출력 */
scanf("%s", name);              /* 입력 */
printf("안녕하세요, %s!\n", name);  /* 출력 */
```

---

## 3. 핵심 아이디어

### printf - 형식 지정 출력

형식 지정자(format specifier)를 사용해 변수 값을 원하는 형식으로 출력한다.

| 형식 지정자 | 자료형 | 설명 |
|---|---|---|
| `%d` | int | 정수 |
| `%f` | float/double | 실수 |
| `%c` | char | 문자 |
| `%s` | char[] | 문자열 |
| `%lld` | long long | 큰 정수 |
| `%u` | unsigned int | 부호 없는 정수 |
| `%p` | pointer | 주소 |
| `%x` | int | 16진수 |

### 특수 문자 (이스케이프 시퀀스)

| 코드 | 의미 |
|---|---|
| `\n` | 줄바꿈 |
| `\t` | 탭 |
| `\\` | 역슬래시 |
| `\"` | 큰따옴표 |
| `%%` | % 문자 |

### scanf - 키보드 입력

```c
int n;
scanf("%d", &n);  /* &n: 변수의 주소 전달 */
```

`&`(주소 연산자)를 사용하는 이유: scanf가 값을 해당 변수에 직접 저장하기 위해 주소를 알아야 하기 때문.

---

## 4. 동작 과정 살펴보기

### printf 형식 지정 세부 옵션

```c
int n = 42;
double d = 3.14159;

printf("%10d\n", n);     /* 오른쪽 정렬, 너비 10 */
printf("%-10d|\n", n);   /* 왼쪽 정렬, 너비 10 */
printf("%010d\n", n);    /* 0으로 채우기 */
printf("%.2f\n", d);     /* 소수점 2자리 */
printf("%8.2f\n", d);    /* 너비 8, 소수점 2자리 */
```

출력:
```text
        42
42        |
0000000042
3.14
    3.14
```

### scanf 여러 값 입력

```c
int a, b;
scanf("%d %d", &a, &b);  /* 공백으로 구분된 두 정수 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 정수 입력 */
    int age;
    printf("나이를 입력하세요: ");
    scanf("%d", &age);

    /* 실수 입력 */
    double height;
    printf("키(cm)를 입력하세요: ");
    scanf("%lf", &height);  /* double은 %lf */

    /* 문자 입력 */
    char grade;
    printf("학점을 입력하세요 (A/B/C): ");
    scanf(" %c", &grade);  /* 공백 추가: 이전 입력 버퍼의 개행 무시 */

    /* 문자열 입력 */
    char name[50];
    printf("이름을 입력하세요: ");
    scanf("%s", name);  /* name은 배열이므로 & 불필요 */

    /* 결과 출력 */
    printf("\n=== 입력한 정보 ===\n");
    printf("이름: %s\n", name);
    printf("나이: %d세\n", age);
    printf("키: %.1f cm\n", height);
    printf("학점: %c\n", grade);

    return 0;
}
```

### fgets로 공백 포함 문자열 입력

```c
char sentence[100];
printf("문장을 입력하세요: ");
fgets(sentence, sizeof(sentence), stdin);
/* fgets는 공백 포함 한 줄을 읽음 */
/* 마지막에 \n이 포함될 수 있으므로 제거 필요 */
```

### 여러 값 한 줄에 입력

```c
int x, y;
printf("x y를 입력 (예: 3 5): ");
scanf("%d %d", &x, &y);
printf("x=%d, y=%d\n", x, y);
```

---

## 6. 마지막 정리

`printf`는 형식 지정자를 이용해 다양한 자료형을 출력한다.

`scanf`는 형식 지정자와 변수 주소(`&`)를 사용해 입력받는다.

문자열 배열은 이미 주소이므로 `&` 없이 사용한다.

`%lf`는 `double` 입력용, `%f`는 `float` 입력용이다.

공백 포함 문자열은 `fgets`를 사용한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 입력과 출력",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
