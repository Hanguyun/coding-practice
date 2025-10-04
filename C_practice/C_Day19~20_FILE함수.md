## 스택을 활용하여 괄호 검사 프로그램을 작성하라.

```c
#include<stdio.h>
#include<string.h>

#define MAX_STACK_SIZE 100
typedef char element;
typedef struct{
    element data[MAX_STACK_SIZE];
    int top;
}StackType;

void init_stack(StackType* s) {
    s -> top = -1;
}

int is_empty(StackType* s) {
        return (s->top == -1);
}

int is_full(StackType* s) {
    return (s->top == (MAX_STACK_SIZE -1));
}

void push(StackType* s, element item) {
    if (is_full(s)){
        fprintf(stderr, "스택 포화 에러\n");
        return;
    }
    s ->data[++(s->top)] = item;
}
element pop(StackType* s) {
        if (is_empty(s)) {
            fprintf(stderr, "스택 공백 에러\n");
            return -1;
        }
        return s->data[(s->top)--];
}

element peek(StackType* s) {
    if (is_empty(s)) {
        fprintf(stderr, "스택 공백 에러\n");
        return -1;
    }
    return s->data[s->top];
}

int bracket_checker(char* exp) {
    StackType s;
    char ch, open_ch;

    int len = strlen(exp);
    init_stack(&s);

    for (int i = 0; i < len; i++) {
        ch = exp[i];

    switch (ch) {
    case '(' : case '[' : case '{' :
        push(&s, ch);
        break;

    case ')' : case ']' : case '}' :
        if (is_empty(&s)) return 0;
        else {
              open_ch = pop(&s);
              if ((open_ch == '(' && ch != ')') || (open_ch == '[' && ch != ']') || (open_ch == '{' && ch != '}'))
                    return 0;
                    break;
            }
        }
    }
    if (!is_empty(&s)) return 0;
    return 1;
}

int main() {
    FILE* fp;
    char str[1024] = { 0 };

    fp = fopen("C_Day18_2_test_data.txt", "rt");
    while (!feof(fp)) {
        fscanf(fp, "%s", str);

        if (bracket_checker(str))
            printf("%s 괄호 검사 성공 \n", str);
        else
            printf("%s 괄호 검사 실패 \n", str);
    }
}
```

---

### 1. 라이브러리 헤더

```c
#include<stdio.h>
#include<string.h>
```

- <stdio.h> 표준입출력관련 함수를 사용하기 위해 선언
- <string.h> 문자열 함수를 사용하기 위해 선언

---

### 2. 전처리기 매크로(Macro) 정의

```c
#define MAX_STACK_SIZE 100
```

- #define → 지시자
    - “앞에 있는 이름을 뒤의 값으로 바꿔라” 라는 뜻
- MAX_STACK_SIZE → 매크로
    - 이름(매크로 이름, 심볼릭 상수처럼 사용)
- 100 → 매크로 몸
    - 값

즉, 프로그램에서 MAX_STACK_SIZE 라는 단어가 나오면 전처리기가 전부 100으로 바꾼다

---

### 3. typedef

```c
typedef char element;
```

- typedef → 새로운 이름(별명)을 만든다
- char → 타입을 앞으로 element라는 이름으로 쓰겠다는 뜻

즉, element는 char와 같은 자료형이다.

나중에 element data[MAX_STACK_SIZE]; 이렇게 쓰면 char data[MAX_STACK_SIZE] 와 같음

---

### 4. 구조체

```c
typedef struct{
	element data[MAX_STACK_SIZE];
	int top;
} StackType;
```

- 구조체 struct { … }을 정의하고 typedef 로 그 구조체의 이름을 StackType으로 붙인다.
- element data[MAX_STACK_SIZE];
    - 크기가 MAX_STACK_SIZE인 배열, 즉 스택에 저장할 데이터 공간
- int top;
    - 스택의 맨 위 원소 위치를 가리키는 인덱스
- 이 코드는 “문자를 저장하는 스택”을 만들기 위해 구조체를 정의한 것

---

### 5-1. 스택 초기화 함수

```jsx
void init_stack(StackType* s) {
	s->top = -1;
}
```

> 이 함수는 스택 구조체 변수를 받아서 top을 -1로 설정 → “스택이 비어 있다”라고 초기화하는 역할.
> 
- 반환형이 void → 이 함수는 값을 돌려주지 않음.
- init_stack → 함수 이름(스택을 초기화한다는 뜻)
- 매개변수 (StackType* s) → StackType 구조체의 주소를 바음.
    - StackType은 아까 정의한 구조체(스택)
    - * s는 포인터 → 스택 변수의 “주소”를 전달받아 직접 수정할 수 있게 함

- s -> top = -1 → s는 포인터니까 . 대신 - > 연산자를 사용해야 구조체 멤버에 접근 가능.
- top = -1로 설정
    - 스택이 비어있음을 나타냄.
    - 보통 스택의 맨 위 인덱스는 0부터 시작하기 때문에, -1이면 “아무것도 없음”을 의미

---

### 5-2. 스택을 반환하는 함수

```jsx
int is_empty(StackType* s) {
	return (s->top == -1);
}
```

> 스택이 비어 있으면 1, 아니면 0을 반환하는 함수.
> 
- 반환형이 int → 이 함수는 정수값을 돌려준다.
- is_empty → 함수 이름(”비어있나?” 검사하는 함수)
- (StackType* s) → 스택 구조체의 주소를 받아옴.
    - s는 StackType을 가리키는 포인터.

- s ->top : 스택의 top 값(맨 위 인덱스)을 확인
- (s -> top == -1) : top이 -1인지 비교
    - top이 -1 → 스택에 아무것도 없음 → 조건식 결과는 참 (C에서는 1)
    - top이 -1이 아님 → 스택에 뭔가 들어있음 → 조건식 결과는 거짓 (C에서는 0)
- 스택이 비었으면 1 반환
- 스택이 차 있으면 0 반환

---

### 5-3. 스택이 꽉 찼는지 확인하는 함수

```jsx
int is_full(StackType* s) {
	return (s->top == (MAX_STACK_SIZE -1));
}
```

> is_full() 은 스택이 가득 차면 1, 아니면 0을 반환
> 

> 스택이 꽉 찼는지 검사할 때 쓰는수
> 
- 반환형 int → 결과를 정수(1 또는 0)로 돌려줌
- 함수 이름 is_full → “꽉 찼는지?” 검사하는 함수
- 매개변수 (StackType* s) → 스택 구조체를 가리키는 포인터

- s->top : 스택의 맨 위 인덱스
- MAX_STACK_SIZE -1 : 배열의 마지막 인덱스
    - ex) #define MAX_STACK_SIZE 100 이면 배열 크기는 100, 마지막 인덱스는 99
- (s->top == (MAX_STACK_SIZE -1))
    - top이 마지막 인덱스라면 → 스택 꽉 참 → 참(1)
    - 아니면 아직 여유 있음 → 거짓(0)

---

### 5-4. PUSH 함수

```jsx
void push(StackType* s, element item) {
	if (is_full(s)) {
		fprintf(stderr, "스택 포화 에러\n");
		return;
		}
		s->data[++(s->top)] = item;
	}
```

> push() 함수
> 
1. 스택이 꽉 찼는지 검사 → 꽉 찼으면 에러 출력 후 종료
2. 아니라면 top을 1 증가시키고, 그 위치에 데이터를 저장

- 반환형 void → 값을 돌려주지 않는 함수.
- push → 스택에 원소를 넣는 함수 이름
- 매개변수
    - StackType* s : 스택 구조체의 주소 (스택 자체를 가리킴)
    - element item : 스택에 넣을 데이터 (앞에서 typedef char elemeat; 했으니깐 사실상 char item)

- 먼저 is_full(s)를 호출해서 스택이 꽉 찼는지 확인.
- 만약 스택이 가득 차 있으면
    - fprintf(stderr, “스택 포화 에러\n\”);
        - 표준 오류 출력(stderr)으로 에러 메세지를 보여줌.
    - return;
        - 함수 종료(push 동작을 하지 않음)

- (s->top) : 스택 맨 위 인덱스
- ++(s ->top) : top 값을 먼저 1 증가시킴 (비어있을 때는 -1 → 0으로 바뀜)
- s -> data[…] = item; : 증가된 top 위치에 새로운 데이터를 저장

---

### 5-5. POP 함수

```jsx
element pop(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "스택 공백 에러\n");
		return -1;
		}
		return s-> data[(s- > top)--];
}
```

> pop() 함수는
> 
> 1. 스택이 비었는지 검사 → 비었으면 에러 출력 후 -1 반환
> 2. 아니면 top 위치 데이터를 반환하고, top 값을 줄여서 스택에서 제거
- 반환형 : element (앞에서 typedef char element; 했으니 사실 char)
    - 스택에서 꺼낸 데이터를 반환해야 하니까 void가 아니라 element 타입.
- 매개변수 : StackType* s →  스택 구조체 주소를 전달받음.

- 먼저 is_empty(s)로 스택이 비었는지 확인.
- 비어 있으면 :
    - fprintf(stderr, “스택 포화 에러\n\”); 표준 오류 출력(stderr)로 출력.
    - return -1; → 잘못된 값 반환 (문자형으로는 사실상 EOF 비슷하게 “실패”를 나타내는 약속).

- (s->top)-- → 현재 top 위치를 사용한 뒤에 top을 1 감소 시킴.
    - ex) top=3이면 data[3]을 반환하고, top은 2로 줄어듦.
- s-> data[…] → 그 위치에 있던 데이터를 꺼내서 반환.
    - 즉, 맨 위에 있는 데이터를 꺼내고, top을 한 칸 내려준다.

---

### 5-6. peek 함수

```c
element peek(StackType* s) {
	if (is_empty(s)) {
		fprintf(stderr, "스택 공백 에러\n");
		return -1;
		}
		return s->data[s->top];
}
```

> peek() 함수 = 스택 맨 위 데이터를 꺼내지 않고 확인만 하는 함수
> 
> 1. 스택이 비면 에러 출력 후 -1 반환
> 2. 스택이 차 있으면 data[top]을 그대로 반환

- 반환형 : element (앞에서 typedef char element; 했으니 사실 char)
- 함수 이름: peek → “슬쩍 보다”라는 뜻. 스택에서 꺼내지 않고 맨 위 값만 확인하는 기능.
- 매개변수: StackType* s → 스택 구조체를 가리키는 포인터

- 먼저 is_empty(s)로 스택이 비었는지 확인.
- 비어 있으면:
    - fprintf(stderr, “스택 포화 에러\n\”); 표준 오류 출력(stderr)로 출력.
    - return -1; → 실패 표시로 -1 반환.

- 스택이 비어있지 않다면, s->top 인덱스 위치의 데이터를 반환.
- 차이점: pop()과 달리 top 값을 줄이지 않음 → 즉, 스택에서 꺼내지 않고 그냥 확인만 함.

---