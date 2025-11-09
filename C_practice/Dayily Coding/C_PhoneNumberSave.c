#include <stdio.h>
#include <stdlib.h>

typedef int Element;
#include <stdio.h>
#include <stdlib.h>

typedef int Element;
#include "CircularLinkedQueue.h"

int main(void) {
    int temp;
    int count;
    int counting = 1;
    init_queue();

    printf("연락처의 수:");
    scanf("%d", count);

    while (1) {
        printf("이름과 휴대폰 번호를 입력하세요 : ");
        scanf("%d", &temp);
        counting++;
        if (count == counting) break;
        enqueue(temp);
    }

    printf("========================\n");
    printf("         이름          휴대폰 번호               \n");
    printf("----------------------------------------- \n");
    Node* p = rear -> link;
    while (p != rear->link) {
        printf("%3d", p->data);
        p = p -> link;
    }
    printf("\n");

    return 0;
}
