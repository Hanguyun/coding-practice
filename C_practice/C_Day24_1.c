#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
typedef char Element;
#include "ArrayStack.h"

int check_matching(char filename[]);   //1��
char quotes = '\'';                  //3��?
int quotes2 = 39;

int check_matching(char expr[])
{
    int i = 0, prev;


    init_stack();
    while (expr[i] != '\0') {
        char ch = expr[i++];
        if (ch == quotes2 || ch == 39 || ch == '[' || ch == '(' || ch == '{')
                push(ch);
        else if (ch == quotes2 || ch == ']' || ch == ')' || ch == '}') {
            if (is_empty())
                return 2;

            prev = pop();
            if ((ch == quotes2 && ch == ']' && prev != '[')
                || (ch == ')' && prev != '(')
                || (ch == '}' && prev != '{'))
                    return 3;
        }
    }
    if (!is_empty()) return 1;
    else return 0;
}

int main()
{
    FILE *fp = NULL;                                // 1, 2 ��
    char line[100];
    fp = fopen("C_Day22_check_matching.c", "r");
    if (fp == NULL) {
            printf("������ �� �� �����ϴ�.");
    return 0;
    }
    while (fgets(line, sizeof(line), fp) != NULL) {
        int errCode = check_matching(line);
        if (errCode == 0) printf("%-20s -> ����\n", line);
        else printf("%-20s -> ����(����%d ����)\n", line, errCode);
    }
    fclose(fp);
    printf("\n\n\n");

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
    printf("����ǥ ��� %c\n", quotes);
    printf("����ǥ ��� %c\n", quotes2);
}

