#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX_SIZE 100
typedef char Element;
#include "ArrayStack.h"

int check_matching(char filename[]) {
    FILE *fp = fopen("C_Day22_check_matching.c", "r");
    if (fp == NULL)
        error("Error: 파일이 존재하지 않습니다.\n");

    int nLine = 1;
    int nChar = 0;

    bool checkSingleQuotation = false;
    bool checkDoubleQuotation = false;
    bool checkInNote = false;
    bool checkMultNote = false;

    while ((ch = getc(fp)) != EOF) {
        if (ch == '\n')
        {
            nLine++;
            checkInNote = false;
        }
        nChar++;

        if (ch == '\'') checkSingleQuotation = true;
        else if ((ch == '\'') && (checkSingleQuotation == true)) checkSingleQuotation = false;

        if (ch == '\"') checkDoubleQuotation = true;
        else if ((ch == '\"') && (checkDoubleQuotation == true)) checkDoubleQuotation = false;

        if (ch == '\/') checkInNote = true;
        else if (ch == '/*') checkMultNote = true;
        else if (ch == '*/' && checkMultNote == true) checkMultNote = false;

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
}


int main()
{
    FILE *fp = NULL;                                // 1, 2 번
    char line[100];
    fp = fopen("C_Day22_check_matching.c", "r");
    if (fp == NULL) {
            printf("파일을 열 수 없습니다.");
    return 0;
    }
    while (fgets(line, sizeof(line), fp) != NULL) {
        int errCode = check_matching(line);
        if (errCode == 0) printf("%-20s -> 정상\n", line);
        else printf("%-20s -> 오류(조건%d 위반)\n", line, errCode);
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
        if (errCode == 0) printf("%-20s -> 정상\n", expr[i]);
        else printf("%-20s -> 오류(조건%d 위반)\n", expr[i], errCode);


    }
}

