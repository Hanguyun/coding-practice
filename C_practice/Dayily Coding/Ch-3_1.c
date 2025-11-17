#include<stdio.h>
#include<stdlib.h>
#include<string.h>

struct Waiting {
    int id;
    int nperson;
    char info[30];
};
typedef struct Waiting Element;
#include "Ch06-3_1.h"

static int reservedid = 1;

void reserve() {
    int su;
    char tel[30];
    Element e;

    printf("인원 수 : ");
    scanf("%d", &su);

    printf("전화번호 : ");
    scanf("%29s", tel);

    e.id = reservedid++;
    e.nperson = su;
    strcpy(e.info, tel);

    append(e);
    printf("대기번호: %d  인원 수: %d  연락처: %s\n",
           e.id, e.nperson, e.info);
}


void findWaitingSu() {
    int nTeam = 0;
    int nPeople = 0;
    int myRld;
    Element e;

    printf("대기번호 :");
    scanf("%d", &myRld);

    for(int pos=0; pos < size(); pos++){
        e = get_entry(pos);
        if(e.id == myRld){
            printf("<확인> 대기번호 %d 앞 대기팀 : %d 대기인원 : %d\n", myRld, nTeam, nPeople);
            return;
        }
        nTeam++;
        nPeople += e.nperson;
    }
}

void printAll() {
    Element e;
    printf("<<대기 팀 목록>>");
    printf("----------------------------\n");
    for(int i=0; i < size(); i++) {
        e = get_entry(i);
        printf("대기 번호: %3d\t대기 인원: %2d\t연락처:%s\n", e.id, e.nperson, e.info);
    }
    printf("----------------------------\n");
}

void deleteReserve() {
    int myRId;
    Element e;

    printf("삭제할 대기번호 :");
    scanf("%d", &myRId);

    for(int pos=0; pos < size(); pos++){
        e = get_entry(pos);
        if(e.id == myRId){
            printf("<확인> 대기번호 %d   앞 대기팀 : %d   대기인원 : %d\n", e.id, e.nperson, e.info);
                delete(pos);
            return;
        }
    }
}

void enter() {
    Element e;
    e = get_entry(0);
    printf("<입장 대상 확인> 대기번호 %d   앞 대기팀 : %d   대기인원 : %d\n", e.id, e.nperson, e.info);
    delete(0);
}

void delay() {
    int delayId;
    Element e;

    printf("연기할 대기번호:");
    scanf("%d", delayId);

    for(int pos=0; pos < size(); pos++){
        e = get_entry(pos);
        if(e.id == delayId){
            printf("<확인> 대기번호 %d   앞 대기팀 : %d   대기인원 : %d\n", e.id, e.nperson, e.info);
            delete(pos);
            insert(pos+1, e);
            printf("대기 번호 %d 팀을 다음 순번으로 조정하였습니다.", delayId);
            return;
        }
    }
}

int main(void) {
    int menu;

    init_list();
    while(1){
        printf("1.대기  2.입장  3.취소  4.순번 연기  5.앞선 대기팀 수 확인  6.전체 대기 명단  7.종료    :");
        scanf("%d", &menu);
        switch(menu){
        case 1: reserve();
                    break;

        case 2: enter();
                    break;

        case 3: deleteReserve();
                    break;

        case 4: delay();
                    break;

        case 5: findWaitingSu();
                    break;

        case 6: printAll();
                    break;

        case 7: printf("프로그램을 종료합니다.\n");
                    exit(0);

        default :
            printf("잘못된 입력입니다.");
        }
    }
}
