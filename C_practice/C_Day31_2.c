#include<stdio.h>
#include<stdlib.h>

typedef int Element;
#include "LinkedStack.h"

void main()
{
    int temp;

    init_stack();
    while(1){
        printf("스택에 저장할 정수값: ");
        scanf("%d", &temp);
        if (temp == 0) {
            printf("더 이상 입력할 값이 없네요..\n");
            break;
        }
        push(temp);
    }

    printf("스택에 저장된 값 목록: ");
    while(!is_empty())
        printf("%3d\n", pop());
    printf("\n");

    destory_stack();
}
