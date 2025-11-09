#include <stdio.h>
#include <stdlib.h>

typedef struct PhoneNumberSave {                // 구조체 정의 저장될 이름과 전화번호.
    char name[30]; // 문자 타입 변수 지정
    char number[30]; // 문자 타입 변수 지정
} Element;

#include "C_PhoneNumberSave.h"                  // 원형 연결 구조 헤더 파일.

int main(void) {
    int count;                      // 밑에 while문에서 빠져나오기 위한 변수 지정.
    int counting = 0;          // 밑에 while문에서 빠져나오기 위한 변수 지정.
    Element temp;

    init_queue();                  // 큐 초기화.

    printf("연락처의 수:");  // 입력.
    scanf("%d", &count);    // 스캔.

    while(1) {          // 무한으로 돌려서 counting이 count랑 같으면 break.
        printf("이름과 휴대폰 번호를 입력하세요 : ");
        scanf("%s %s", temp.name, temp.number); //  문자 타입 변수 스캔
        enqueue(temp);  // temp를 큐에 넣기
        counting++;        // temp를 큐에 넣고 counting +1
            if (count == counting) break; //counting이 count랑 같으면 break.
    }

    printf("========================\n"); // 출력.
    printf("이름\t휴대폰 번호\n"); // \t 일정 간격을 두고 띄어쓰기 후 출력.
    printf("----------------------------------------- \n"); // 출력.

    if (!is_empty()) { // 비어있지 않다면
        Node* p = rear->link; // 맨 앞에서부터 시작

        printf("%s\t%s\n", p->data.name, p->data.number); // 처음 사람 정보 출력하고
        p = p->link; // 다음 사람으로 이동


        for (Node *p = rear->link; p != rear; p = p -> link) { // rear가 가리키는 link는 맨 앞을 가르킴 그래서 p != rear->link면 앞이 아니면이 성립.
            printf("%s\t%s\n", p->data.name, p->data.number); // p가 가르키는 data.name 과 data.number를 출력하고
            p = p->link; // 다음으로 이동
            if (is_empty())
                break;
        }
    }

    return 0;
}

