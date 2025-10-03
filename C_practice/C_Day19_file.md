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