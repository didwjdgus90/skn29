# 제목
트라이 (Trie) 자료구조

# 링크
[GPT 생성자료]

## 1. 한 줄 요약

- 트라이는 **문자열을 글자 단위로 저장하여 검색, 삽입, 접두사(Prefix) 탐색을 매우 빠르게 수행하는 자료구조**이다.

---

## 2. 주요 활용처 및 문제 유형

스마트폰에서 검색어를 입력한다고 생각해보자.

```
입력

"a"
```

그러면

```
apple
app
application
```

같은 추천 검색어가 나온다.

---

또는 인터넷 주소창에서

```
goo
```

만 입력해도

```
google.com
google drive
google maps
```

같은 후보가 나온다.

---

컴퓨터는 어떻게 이렇게 빠르게 찾을 수 있을까?

모든 단어를 하나씩 검사한다면 매우 느릴 것이다.

---

이때 사용하는 대표적인 자료구조가

```
Trie
```

이다.

---

### 코딩 테스트에서 자주 나오는 문제

다음 키워드가 보이면 트라이를 떠올려보자.

- 문자열 검색
- 접두사(Prefix)
- 자동완성
- 사전(Dictionary)
- 전화번호 목록
- 문자열 집합

특히

```
특정 문자열로 시작하는 단어 찾기
```

라는 문장이 나오면 트라이일 가능성이 높다.

---

## 3. 핵심 아이디어

### 비유

사전을 찾는다고 생각해보자.

---

만약

```
apple
app
application
banana
```

가 저장되어 있다.

---

일반적인 방법은

```
apple

app

application

banana
```

를 하나씩 비교해야 한다.

---

하지만 자세히 보면

```
app
```

부분이 공통이다.

---

```
apple

application

app
```

모두

```
a → p → p
```

로 시작한다.

---

트라이는

> 같은 시작 부분은 함께 저장하자
> 

라는 아이디어를 사용한다.

---

즉

```
apple

application

app
```

를 저장하면

```
a
└─ p
   └─ p
```

부분을 공유한다.

---

그래서 검색이 매우 빨라진다.

---

## 4. 알고리즘 동작 과정 (Step-by-Step 시각화)

다음 단어들을 저장해보자.

```
app
apple
bat
```

---

### Step 1. "app" 삽입

```
(root)
  |
  a
  |
  p
  |
  p*
```

- 는 단어의 끝을 의미한다.

---

### Step 2. "apple" 삽입

이미

```
a → p → p
```

가 존재한다.

---

뒤만 추가하면 된다.

```
(root)
  |
  a
  |
  p
  |
  p*
  |
  l
  |
  e*
```

---

### Step 3. "bat" 삽입

```
(root)
├─ a
│  └─ p
│     └─ p*
│        └─ l
│           └─ e*
│
└─ b
   └─ a
      └─ t*
```

---

### Step 4. 검색

검색어

```
apple
```

---

탐색

```
a

↓

p

↓

p

↓

l

↓

e
```

---

마지막 노드가

```
단어 끝
```

이라면 존재한다.

---

### Step 5. 접두사 검색

질문

```
ap 로 시작하는 단어 존재?
```

---

탐색

```
a

↓

p
```

---

여기까지만 도달하면 된다.

---

```
apple

app
```

둘 다

```
ap
```

로 시작한다.

---

그래서

```
YES
```

이다.

---

## 5. 파이썬(Python) 구현 코드

### Trie Node

```
classTrieNode:

def__init__(self):
self.children= {}
self.is_end=False
```

---

설명

```
children
```

현재 문자에서 갈 수 있는 다음 문자들

---

```
is_end
```

단어 끝 여부

---

### Trie 구현

```
classTrie:

def__init__(self):
self.root=TrieNode()

definsert(self,word):

node=self.root

forcharinword:

ifcharnotinnode.children:
node.children[char]=TrieNode()

node=node.children[char]

node.is_end=True

defsearch(self,word):

node=self.root

forcharinword:

ifcharnotinnode.children:
returnFalse

node=node.children[char]

returnnode.is_end

defstarts_with(self,prefix):

node=self.root

forcharinprefix:

ifcharnotinnode.children:
returnFalse

node=node.children[char]

returnTrue
```

---

### 사용 예제

```
trie=Trie()

trie.insert("app")
trie.insert("apple")
trie.insert("bat")

print(trie.search("app"))
print(trie.search("apple"))
print(trie.search("banana"))

print(trie.starts_with("ap"))
```

---

출력

```
True
True
False
True
```

---

### 핵심 코드 설명

---

```
forcharinword:
```

문자를 하나씩 따라 내려간다.

---

예시

```
apple
```

이면

```
a

↓

p

↓

p

↓

l

↓

e
```

순서로 이동한다.

---

```
node.children[char]
```

는

현재 문자에서

다음 문자로 이동하는 의미이다.

---

```
node.is_end=True
```

는

```
여기서 단어가 끝난다
```

를 표시한다.

---

## 6. 핵심 요약 및 주의점

### 트라이의 핵심 아이디어

```
공통 접두사를

공유해서 저장한다.
```

---

### 시각화

```
app
apple
application
```

↓

```
a
└─ p
   └─ p
      ├─ (end)
      └─ l
         └─ ...
```

---

### 장점

### 문자열 검색

```
빠름
```

---

### 접두사 검색

```
매우 강력
```

---

### 자동완성 구현

```
적합
```

---

### 시간 복잡도

문자열 길이를 L이라고 하면

---

삽입

```
O(L)
```

---

검색

```
O(L)
```

---

접두사 검색

```
O(L)
```

---

### 일반 리스트와 비교

단어 목록

```
apple
banana
orange
...
```

---

일반 리스트

```
검색

O(N)
```

---

트라이

```
검색

O(L)
```

---

단어 개수가 많을수록 차이가 커진다.

---

### 자주 하는 실수

### 1. 단어 끝 표시 안 하기

예시

```
app
apple
```

---

만약

```
is_end
```

를 저장하지 않으면

```
app
```

가 실제 단어인지

```
apple의 중간 경로
```

인지 구분할 수 없다.

---

### 2. 검색과 접두사 검색 혼동

```
search("app")
```

↓

```
정확히 app 존재?
```

---

```
starts_with("app")
```

↓

```
app로 시작하는 단어 존재?
```

---

결과가 다를 수 있다.

---

### 해시 테이블(Dictionary)와 차이점

| 항목 | Trie | Dictionary(Set) |
| --- | --- | --- |
| 단어 검색 | O(L) | O(L) |
| 접두사 검색 | 매우 강력 | 비효율적 |
| 자동완성 | 적합 | 어려움 |
| 메모리 사용 | 많음 | 적음 |

---

### 언제 사용할까?

### 단순 문자열 존재 여부

```
Set
```

이 더 간단하다.

---

### 접두사 검색

```
Trie
```

가 훨씬 강력하다.

---

### 자동완성

```
Trie
```

가 사실상 정석이다.

---

### 꼭 기억할 것

```
트라이

=

문자열 전용 트리
```

```
문자를 따라 내려가며 저장
```

```
공통 접두사는 공유
```

---

```
app
apple
application
```

↓

```
a → p → p
```

를 함께 사용한다.

---

한 문장으로 기억하면,

> **트라이는 "같은 시작 부분을 공유해서 저장하는 문자열 전용 트리 자료구조"이다.**
>

# 메타데이터
```
{
"category": "트리",
"algorithm": "Trie",
"source_type": "generated",
"style": [
    "analogy", "code"
],
"intuition_score": 5,
"friendliness_score": 4,
"example_score": 4,
"target_level": "high",
"language": "python"
}
```