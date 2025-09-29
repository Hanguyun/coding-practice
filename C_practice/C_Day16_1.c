// �ڵ� 3.5�� ���� �˻� ���α׷��� ������ ���� Ȯ���϶�.
// 1. �ڵ� 3.5�� check_matching() �Լ��� ���ڿ��� �Է����� �޾� ��ȣ�� �˻��Ѵ�
//     �� �Լ��� ������ ó���� �� �ֵ��� �����϶�.
//     �Լ� ������ ������ ������, �˻��� �����̸��� �����Ѵ�.
//     �� �Լ��� ���� �ڵ�(1~3)�� ��ȯ�ϴµ�, ������ ������ 0�� ��ȯ�Ѵ�.
//     int check_matching(char filename[]);

// 2. 3�忡�� ������ �ҽ����ϵ��� �˻��� ����.
//     ���� ���, ArrayStack.h, ArrayStack.c ���� �ҽ��ڵ带 �˻��ϸ� ��κ��� ��� ������ ���ٰ� ��µ� ���̴�.

// 3. [��ȭ����] �ڵ� 3.5(check_matching.c)�� �˻��ϸ� ������ �߰ߵ� ���̴�.
//     �̰��� 17�࿡�� �߻��ϴ� ������, ��������ǥ ó���� ���� �ʾұ� �����̴�.
//     ��, ��������ǥ ���� ��ȣ�� �ܼ��� �ϳ��� ������ ���̹Ƿ� ��ȣ �˻翡�� �����ؾ��ϴµ�,
//     �̸� ó������ �ʾұ� �����̴�. �� ���Ͽ����� ��ȣ �˻簡 ������ �� �ֵ��� �Լ��� �����϶�.

// 4. [��ȭ����] ū����ǥ�� ���� ������ �����Ƿ� �̸� ó���ض�.
//     ���� ���, �ҽ��ڵ忡 ���� ������ �߰��Ǵ��� ��ȣ ��Ī���� ������ ���ٰ� �ǴܵǾ���Ѵ�.
//     printf(" ���� ��ȣ = (((((( ");
//     printf(" ������ ��ȣ = }}}}}} ");
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
        if (errCode == 0) printf("%-20s -> ����\n", expr[i]);
        else printf("%-20s -> ����(����%d ����)\n", expr[i], errCode);
    }
}
