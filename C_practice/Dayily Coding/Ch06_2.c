#include<stdio.h>
#include<stdlib.h>
#define MAX_SIZE 10
typedef int Element;
#include "Ch06-2.h"

void main(){
    int menu;
    int temp;
    int loc;

    while(1){
        printf("1.삽입  2.추가  3.삭제  4.처음부터 찾기  5.특정 위치 이후 찾기  6.인쇄  7.종료    :");
        scanf("%d", &menu);
        switch(menu){
        case 1: printf("삽입할 위치:");
                    scanf("%d", &loc);
                    printf("삽입할 값:");
                    scanf("%d", &temp);
                    insert(loc, temp);
                    printf("값을 삽입하였습니다.\n");
                    break;

        case 2: printf("추가할 값:");
                    scanf("%d", &temp);
                    append(temp);
                    printf("값을 추가하였습니다.\n");
                    break;

        case 3: printf("삭제할 위치:");
                    scanf("%d", &loc);
                    temp = delete(loc);
                    printf("값(%d)을 삭제하였습니다.\n");
                    break;

        case 4:printf("찾는 값:");
                    scanf("%d", &temp);
                    loc = find1(temp);
                    printf("값(%d)는 %d 위치에 있습니다.\n");
                    break;

        case 5:printf("찾는 값:");
                    scanf("%d", &temp);
                    printf("찾는 위치:");
                    scanf("%d", &loc);
                    loc = find2(loc, temp);
                    printf("값(%d)는 %d 위치에 있습니다.\n");
                    break;

        case 6: printf("리스트에 저장된 값 목록: ");
                    for(int i=0; i < size(); i++){
                        printf("%3d", get_entry(i));
                    }
                    printf("\n");
                    break;

        case 7: printf("프로그램을 종료합니다.\n");
                    exit(0);

        default :
            printf("잘못된 입력입니다.");
        }
    }
}

