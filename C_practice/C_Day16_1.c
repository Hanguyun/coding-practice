// 코드 3.5의 과롷 검사 프로그램을 다음과 같이 확장하라.
// 1. 코드 3.5의 check_matching() 함수는 문자열을 입력으로 받아 괄호를 검사한다
//     이 함수가 파일을 처리할 수 있도록 수정하라.
//     함수 원형은 다음과 같은데, 검사할 파일이름을 전달한다.
//     이 함수는 에러 코드(1~3)를 반환하는데, 오류가 없으면 0을 반환한다.
//     int check_matching(char filename[]);

// 2. 3장에서 구현한 소스파일들을 검사해 보라.
//     예를 들어, ArrayStack.h, ArrayStack.c 등의 소스코드를 검사하면 대부분의 경우 문제가 없다고 출력될 것이다.

// 3. [심화문제] 코드 3.5(check_matching.c)를 검사하면 오류가 발견될 것이다.
//     이것은 17행에서 발생하는 것으로, 작은따옴표 처리를 하지 않았기 때문이다.
//     즉, 작은따옴표 안의 괄호는 단순히 하나의 문자일 뿐이므로 괄호 검사에서 무시해야하는데,
//     이를 처리하지 않았기 때문이다. 이 파일에서도 괄호 검사가 성공할 수 있도록 함수를 수정하라.

// 4. [심화문제] 큰따옴표도 같은 문제가 있으므로 이를 처리해라.
//     예를 들어, 소스코드에 다음 문장이 추가되더라도 괄호 매칭에는 문제가 없다고 판단되어야한다.
//     printf(" 왼쪽 괄호 = (((((( ");
//     printf(" 오른쪽 괄호 = }}}}}} ");
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 100
typedef char Element;
#include "ArrayStack.h"

int check_matching(char expr[])
{
    int i = 0, prev;

    init_stack();
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
    }
    if (!is_empty()) return 1;
    else return 0;
}

void main()
{
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
