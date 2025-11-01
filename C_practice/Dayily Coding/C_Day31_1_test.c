#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 100

struct Waiting {
    int id;
    int nperson;
    char info[32];
};
typedef struct Waiting Element;
#include "CircularQ.h"
int waiting_id = 1;

void inputing() {
        Element *customer;
        customer = (Element *) malloc(sizeof(Element));
        printf("인원수 :");
        scanf("%d", &(customer->nperson));
        printf("전화번호 :");
        scanf("%s", customer->info);
        customer->id = waiting_id++;
        printf("대기 신청 완료....... 대기번호 : %d 인원:%d 연락:%s\n", customer->id, customer->nperson, customer->info);
        enqueue(*customer);
}

void entering() {
        if (!is_empty()) {
        Element temp = dequeue();
        printf("대기번호 %d 번 입장 차례입니다. (인원:%d 연락: %s\n)", temp.id, temp.nperson, temp.info);
    }
        else
            printf("대기하는 사람이 없습니다.");
}
void waiting_person() {
        Element temp;
        temp = peek();
        int first = temp.id;
        int flag = 0;

        printf("-----------------------------------------------\n");
        printf("대기인원\t연락처\t대기번호\n");
        printf("-----------------------------------------------\n");

        while(1) {
            if(!is_empty()) {
                temp = dequeue();
                if(temp.id == first&&flag == 1)
                    break;
                else
                    flag = 1;
            }
            else
                break;
            Element temp = dequeue();
            printf("%d\t%s\t%d\n", temp.nperson, temp.info, temp.id);
            enqueue(temp);
        }
        printf("-----------------------------------------------\n");
    }


void main()
{
    int menu;
    int waiting_id = 1;
    init_queue();
    while(1){
        printf("1.대기신청 2.대기완료 : 3.대기목록확인 : 4.종료 :");
        scanf("%d",&menu);
       switch(menu) {
       case 1: inputing();
                    break;
       case 2: entering();
                    break;
       case 3: waiting_person();
                    break;
       case 4: printf("프로그램을 종료합니다.");
                    exit(1);

       default : printf("잘못된 입력입니다. 확인하고 다시 입력하세요.");
       }
    }
}

