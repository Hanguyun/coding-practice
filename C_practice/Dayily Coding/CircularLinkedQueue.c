#include <stdio.h>
#include <stdlib.h>

typedef int Element;
#include "CircularLinkedQueue.h"

int main(void) {
    int temp;

    init_queue();

    while (1) {
        printf("삽입할 데이터: ");
        scanf("%d", &temp);
        if (temp < 0) break;
        enqueue(temp);
    }

    printf("큐에 저장된 값 목록: ");
    Node* p = rear -> link;
    for (int i = 1; i <= size(); i++) {
        printf("%3d", p->data);
        p = p -> link;
    }
    printf("\n");

    return 0;
}
