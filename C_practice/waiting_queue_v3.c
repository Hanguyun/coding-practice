#include<stdio.h>
#include<stdlib.h>

#define MAX_SIZE 8
struct Waiting{
    int id;
    int nperson;
    char info[32];
};
typedef struct Waiting Element;
#include "CircularQueue.h"
int waiting_id=1;

void inputing(){
        Element *customer;
        customer = (Element *) malloc(sizeof(Element));
        printf("�ο��� : ");
        scanf("%d",&(customer->nperson));
        printf("��ȭ��ȣ : ");
        scanf("%s",customer->info);
        customer->id = waiting_id++;
        printf("��� ��û �Ϸ�....... ����ȣ: %d �ο�:%d  ����:%s\n",customer->id, customer->nperson,customer->info);
        enqueue(*customer);
}

void entering(){
       if( !is_empty()){
            Element temp = dequeue();
            printf(" ����ȣ %d �� ���� �����Դϴ�..(�ο�:%d  ����:%s)\n",temp.id, temp.nperson,temp.info);
       }
       else
            printf("����ϴ� ����� �����ϴ�.");
}

void main(){
    int menu;
    int waiting_id=1;
    init_queue();
    while(1){
         printf("1. ����û   2. ����   3. ���� : ");
        scanf("%d",&menu);
        switch(menu){
            case 1: inputing();
                        break;
            case 2: entering();
                        break;
            case 3: printf("���α׷��� �����մϴ�.");
                        exit(1);
            default: printf("�߸��� �Է��Դϴ�...Ȯ���ϰ� �ٽ� �Է��ϼ���.");
        }
    }
}


