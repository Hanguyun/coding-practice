#include<stdio.h>
#include<stdlib.h>

typedef int Element;
#include "LinkedStack.h"

void main()
{
    int temp;

    init_stack();
    while(1){
        printf("���ÿ� ������ ������: ");
        scanf("%d", &temp);
        if (temp == 0) {
            printf("�� �̻� �Է��� ���� ���׿�..\n");
            break;
        }
        push(temp);
    }

    printf("���ÿ� ����� �� ���: ");
    while(!is_empty())
        printf("%3d\n", pop());
    printf("\n");

    destory_stack();
}
