#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
#define MAX_SIZE 1000
typedef char Element;
#include "ArrayStack.h"


int check_matching(char filename[]);   //1��

int check_matching(char* expr[])
{
    StackType s;
    char ch, open_ch;

    int len = strlen(expr);
    init_stack(&s);

    switch (ch) {
     while (expr[i] != '\0') {
        char ch = expr[i++];
        if (ch == '[' || ch == '(' || ch == '{')
                push(ch);
        else if (ch == ']' || ch == ')' || ch == '}') {
            if (is_empty())
                return 2;

            prev = pop();
            if ((ch == ']' && prev != '[')
                || (ch == ')' && prev != '(')
                || (ch == '}' && prev != '{'))
                    return 3;
}
    if (!is_empty()) return 1;
    else return 0;
}

int main()
{
    FILE *fp = NULL;
    char buf[1000] = { 0 };

    fp = fopen("ArrayStack.h", "rt");
    if (fp == NULL) {
            printf("������ �� �� �����ϴ�.");
    return 0;
    }
    while (!feof(fp)) {
        fscanf(fp, "%s", buf) ;
        if (check_matching(buf) == true)
            printf("��Ī �����Դϴ�.  : ");
        else
            printf("��Ī �����Դϴ�. :");

        printf("%s\n", buf);
    }
    fclose(fp);

    char expr[4][80] = {
        "{A[(i+1)]=0;}",
        "if((i==0) && (j==0)",
        "while(n<8)){n++;}",
        "arr[(i+1]) = 0;" };

    for (int i = 0; i < 4; i++) {
        int errCode = check_matching(expr[i]);
        if (errCode == 0) printf("%-20s -> ����\n", expr[i]);
        else printf("%-20s -> ����(����%d ����)\n", expr[i], errCode);
    }
}
