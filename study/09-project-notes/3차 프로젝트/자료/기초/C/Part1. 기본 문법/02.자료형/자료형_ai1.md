# 제목
[C/Cpp 기초] 자료형

# 본문

## 1. 한 줄 요약

자료형은 변수에 저장할 수 있는 데이터의 종류와 크기를 결정하는 분류 체계이다.

C에서 자료형을 이해하면 정수, 실수, 문자 등 다양한 데이터를 적절한 크기의 메모리에 저장할 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

컴퓨터는 모든 데이터를 0과 1(비트)로 저장한다.

그런데 같은 비트 패턴이라도 어떻게 해석하느냐에 따라 완전히 다른 값이 된다.

```text
비트 패턴: 01000001
  → 정수로 해석: 65
  → 문자로 해석: 'A'
  → 실수로 해석: 완전히 다른 값
```

자료형은 "이 메모리를 어떻게 해석할지"를 컴파일러에게 알려주는 역할을 한다.

또한 자료형에 따라 메모리 사용 크기가 달라지므로, 적절한 자료형을 선택하면 메모리를 효율적으로 사용할 수 있다.

---

## 3. 핵심 아이디어

### 기본 자료형 종류

C의 기본 자료형은 크게 정수형, 실수형, 문자형으로 나뉜다.

**정수형**

| 자료형 | 크기 | 범위 |
|---|---|---|
| `char` | 1바이트 | -128 ~ 127 |
| `short` | 2바이트 | -32,768 ~ 32,767 |
| `int` | 4바이트 | -2,147,483,648 ~ 2,147,483,647 |
| `long` | 4 또는 8바이트 | 플랫폼 의존 |
| `long long` | 8바이트 | 매우 큰 정수 |

**실수형**

| 자료형 | 크기 | 정밀도 |
|---|---|---|
| `float` | 4바이트 | 소수점 약 7자리 |
| `double` | 8바이트 | 소수점 약 15자리 |

**unsigned (부호 없는 정수)**

`unsigned`를 붙이면 음수 범위를 없애고 양수 범위를 두 배로 늘린다.

```c
unsigned int x = 4294967295;  /* 최대값 */
```

---

## 4. 동작 과정 살펴보기

### sizeof로 자료형 크기 확인하기

```c
#include <stdio.h>

int main() {
    printf("char   : %zu바이트\n", sizeof(char));
    printf("short  : %zu바이트\n", sizeof(short));
    printf("int    : %zu바이트\n", sizeof(int));
    printf("long   : %zu바이트\n", sizeof(long));
    printf("float  : %zu바이트\n", sizeof(float));
    printf("double : %zu바이트\n", sizeof(double));
    return 0;
}
```

출력 예시 (64비트 시스템):
```text
char   : 1바이트
short  : 2바이트
int    : 4바이트
long   : 8바이트
float  : 4바이트
double : 8바이트
```

### 정수 오버플로우

자료형의 범위를 초과하면 예상치 못한 값이 된다.

```text
int (4바이트) 최대값: 2,147,483,647
              + 1 →  -2,147,483,648  (오버플로우!)
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>

int main() {
    /* 정수형 변수 */
    int age = 25;
    short temperature = -15;
    long long population = 7800000000LL;  /* LL 접미사: long long 리터럴 */
    unsigned int count = 100;

    /* 실수형 변수 */
    float pi_approx = 3.14f;   /* f 접미사: float 리터럴 */
    double pi_exact = 3.14159265358979;

    /* 문자형 변수 */
    char grade = 'A';

    /* 출력 */
    printf("나이: %d\n", age);
    printf("기온: %d도\n", temperature);
    printf("세계 인구: %lld명\n", population);
    printf("개수: %u\n", count);
    printf("원주율(float): %.2f\n", pi_approx);
    printf("원주율(double): %.14f\n", pi_exact);
    printf("학점: %c\n", grade);

    return 0;
}
```

### 형식 지정자

printf에서 자료형에 맞는 형식 지정자를 사용해야 한다.

| 자료형 | 형식 지정자 |
|---|---|
| `int` | `%d` |
| `unsigned int` | `%u` |
| `long long` | `%lld` |
| `float` | `%f` |
| `double` | `%lf` (scanf), `%f` (printf) |
| `char` | `%c` |

### 오버플로우 확인 예제

```c
#include <stdio.h>

int main() {
    short x = 32767;  /* short 최대값 */
    x = x + 1;
    printf("%d\n", x);  /* -32768 출력 (오버플로우) */
    return 0;
}
```

---

## 6. 마지막 정리

자료형은 메모리를 얼마나 쓸지, 어떻게 해석할지를 결정한다.

정수형: `char` → `short` → `int` → `long` → `long long` 순으로 크기가 커진다.

실수형: `float`(4바이트, 7자리 정밀도), `double`(8바이트, 15자리 정밀도).

`unsigned`를 붙이면 양수 범위만 두 배로 늘어난다.

자료형 범위를 넘으면 오버플로우가 발생하므로 주의해야 한다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 자료형",
  "source_type": "generated",
  "style": ["easy", "code"],
  "intuition_score": 5,
  "friendliness_score": 5,
  "example_score": 5,
  "target_level": "low",
  "language": "c"
}
```
