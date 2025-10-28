#include <stdio.h> // 숫자 맞추기 게임.
#include <stdlib.h>
#include <time.h>

int main(void) {
    int user;
    int random;
    int count = 0;

    srand(time(NULL));              // 랜덤 시드 초기화
    random = rand() % 100 + 1;      // 1~100 사이 난수 생성

    while (1) {
        printf("1~100까지의 숫자를 입력하세요: ");
        scanf("%d", &user);
        count++;

        if (user < random) {
            printf("UP!\n");
        }
        else if (user > random) {
            printf("DOWN!\n");
        }
        else {
            printf("%d번 만에 숫자를 맞췄습니다!\n", count);
            break;
        }
    }

    return 0;
}

