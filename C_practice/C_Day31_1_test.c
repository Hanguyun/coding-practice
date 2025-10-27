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
        printf("�ο��� :");
        scanf("%d", &(customer->nperson));
        printf("��ȭ��ȣ :");
        scanf("%s", customer->info);
        customer->id = waiting_id++;
        printf("��� ��û �Ϸ�....... ����ȣ : %d �ο�:%d ����:%s\n", customer->id, customer->nperson, customer->info);
        enqueue(*customer);
}

void entering() {
        if (!is_empty()) {
        Element temp = dequeue();
        printf("����ȣ %d �� ���� �����Դϴ�. (�ο�:%d ����: %s\n)", temp.id, temp.nperson, temp.info);
    }
        else
            printf("����ϴ� ����� �����ϴ�.");
}
void waiting_person() {
        Element temp;
        temp = peek();
        int first = temp.id;
        int flag = 0;

        printf("-----------------------------------------------\n");
        printf("����ο�\t����ó\t����ȣ\n");
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
        printf("1.����û 2.���Ϸ� : 3.�����Ȯ�� : 4.���� :");
        scanf("%d",&menu);
       switch(menu) {
       case 1: inputing();
                    break;
       case 2: entering();
                    break;
       case 3: waiting_person();
                    break;
       case 4: printf("���α׷��� �����մϴ�.");
                    exit(1);

       default : printf("�߸��� �Է��Դϴ�. Ȯ���ϰ� �ٽ� �Է��ϼ���.");
       }
    }
}

