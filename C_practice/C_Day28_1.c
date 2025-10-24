#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    int *p = arr;  // 배열의 첫 번째 원소 주소 저장

    for (int i = 0; i < 5; i++) {
        printf("%d ", *(p + i));  // 포인터 연산으로 값 출력
    }

    return 0;
}
