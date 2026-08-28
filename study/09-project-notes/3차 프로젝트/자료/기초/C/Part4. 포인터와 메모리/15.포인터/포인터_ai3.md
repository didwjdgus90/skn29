# 제목
[C/Cpp 기초] 포인터

# 본문

## 1. 한 줄 요약

포인터는 가상 주소 공간의 특정 위치를 타입화된 핸들로 참조하는 객체이며, 역참조를 통해 해당 위치의 데이터를 읽거나 쓸 수 있다.

---

## 2. 어떤 문제를 해결하기 위해 사용하는가?

C는 값 의미론(value semantics)을 기본으로 하므로, 큰 구조체의 복사 비용을 피하거나 호출자의 변수를 수정하려면 참조(포인터)가 필요하다.

또한 동적 메모리 할당(malloc), 함수 포인터, 배열 추상화는 포인터 없이 구현 불가능하다.

---

## 3. 핵심 아이디어

### 타입화된 포인터

```c
int *p;     /* int의 주소를 저장 */
double *d;  /* double의 주소를 저장 */
```

타입 정보는 역참조 시 메모리를 어떻게 해석할지와 포인터 산술의 단위를 결정한다.

```c
int arr[3] = {1, 2, 3};
int *p = arr;
p + 1;  /* &arr[1]: base + 1 * sizeof(int) */
```

### void 포인터

```c
void *vp;  /* 임의 타입 주소 저장 가능 */
```

역참조 불가, 포인터 산술 불가. `malloc`의 반환 타입이 `void *`이다. 사용 전 구체적 타입으로 캐스팅.

### const와 포인터

```c
const int *p;     /* 포인터를 통한 값 수정 불가 */
int * const p;    /* 포인터 자체 변경 불가 */
const int * const p;  /* 둘 다 불가 */
```

---

## 4. 동작 과정 살펴보기

### 포인터와 가상 주소 공간

```text
프로세스 가상 주소 공간 (64비트):
0x0000000000000000 ~ 0x00007FFFFFFFFFFF (user space)

int x = 10;
&x → 스택 영역의 주소 (예: 0x7FFEDC123456)

포인터 변수 p 자체도 스택의 어딘가:
p = 0x7FFEDC123456 (이 8바이트 값이 x의 주소)
```

### 포인터 역참조의 하드웨어 동작

```text
*p:
1. p의 값(주소)을 레지스터에 로드
2. 그 주소의 메모리에서 sizeof(*p) 바이트 읽기
3. 해당 타입으로 해석

*p = val:
1. p의 값(주소)을 레지스터에 로드
2. val을 그 주소에 sizeof(*p) 바이트 씀
```

### 댕글링 포인터 (Dangling Pointer)

이미 해제된 메모리를 가리키는 포인터. 역참조하면 UB이다.

```c
int *p = malloc(sizeof(int));
free(p);
*p = 10;  /* UB: 해제된 메모리 접근 */
p = NULL;  /* 해제 후 NULL 설정 관례 */
```

---

## 5. 구현 코드 및 상세 설명

```c
#include <stdio.h>
#include <stdint.h>

/* const 정확성 */
void print_array(const int *arr, size_t n) {
    /* arr[i] = 0; */  /* 컴파일 오류: const int * */
    for (size_t i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

/* void * 활용 */
void memswap(void *a, void *b, size_t size) {
    unsigned char *pa = (unsigned char *)a;
    unsigned char *pb = (unsigned char *)b;
    for (size_t i = 0; i < size; i++) {
        unsigned char tmp = pa[i];
        pa[i] = pb[i];
        pb[i] = tmp;
    }
}

int main() {
    int x = 10, y = 20;

    /* 포인터 산술 */
    int arr[] = {10, 20, 30, 40, 50};
    int *p = arr;

    for (int i = 0; i < 5; i++) {
        printf("arr[%d] = %d, 주소: %p\n", i, *(p + i), (void *)(p + i));
    }

    /* 포인터 간 차이 */
    ptrdiff_t diff = (p + 4) - p;
    printf("포인터 차이: %td\n", diff);  /* 4 (원소 수) */

    /* 주소 차이 (바이트) */
    printf("주소 차이: %zu바이트\n",
           (size_t)((unsigned char *)(p+4) - (unsigned char *)p));  /* 16 */

    /* const int * 함수 */
    print_array(arr, 5);

    /* void * memswap */
    double a = 3.14, b = 2.71;
    printf("교환 전: a=%.2f, b=%.2f\n", a, b);
    memswap(&a, &b, sizeof(double));
    printf("교환 후: a=%.2f, b=%.2f\n", a, b);

    return 0;
}
```

---

## 6. 마지막 정리

포인터는 가상 주소 공간의 타입화된 참조이며, 타입 정보가 역참조 해석과 포인터 산술 단위를 결정한다.

`const int *`는 읽기 전용 포인터, `int * const`는 고정 주소 포인터이다.

`void *`는 제네릭 포인터로 역참조/산술 없이 주소만 저장한다.

댕글링 포인터와 NULL 역참조는 심각한 UB이므로 해제 후 NULL 할당이 방어적 관례이다.

# 메타데이터

```json
{
  "category": "언어 기초",
  "algorithm": "C/Cpp 포인터",
  "source_type": "generated",
  "style": ["professional", "analytical"],
  "intuition_score": 3,
  "friendliness_score": 3,
  "example_score": 4,
  "target_level": "high",
  "language": "c"
}
```
