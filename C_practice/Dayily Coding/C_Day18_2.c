// ���� Ȱ�� - ��ȣ �˻� ���α׷�
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
        fprintf(stderr, "���� ��ȭ ����\n");
        return;
    }
    s ->data[++(s->top)] = item;
}
element pop(StackType* s) {
        if (is_empty(s)) {
            fprintf(stderr, "���� ���� ����\n");
            return -1;
        }
        return s->data[(s->top)--];
}

element peek(StackType* s) {
    if (is_empty(s)) {
        fprintf(stderr, "���� ���� ����\n");
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
            printf("%s ��ȣ �˻� ���� \n", str);
        else
            printf("%s ��ȣ �˻� ���� \n", str);
    }
}
