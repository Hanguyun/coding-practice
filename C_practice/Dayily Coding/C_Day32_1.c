#include <stdio.h> // ���� ���߱� ����.
#include <stdlib.h>
#include <time.h>

int main(void) {
    int user;
    int random;
    int count = 0;

    srand(time(NULL));              // ���� �õ� �ʱ�ȭ
    random = rand() % 100 + 1;      // 1~100 ���� ���� ����

    while (1) {
        printf("1~100������ ���ڸ� �Է��ϼ���: ");
        scanf("%d", &user);
        count++;

        if (user < random) {
            printf("UP!\n");
        }
        else if (user > random) {
            printf("DOWN!\n");
        }
        else {
            printf("%d�� ���� ���ڸ� ������ϴ�!\n", count);
            break;
        }
    }

    return 0;
}

