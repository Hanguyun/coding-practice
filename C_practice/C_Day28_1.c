#include <stdio.h>

int main(void) {
    int arr[5] = {10, 20, 30, 40, 50};
    int *p = arr;  // �迭�� ù ��° ���� �ּ� ����

    for (int i = 0; i < 5; i++) {
        printf("%d ", *(p + i));  // ������ �������� �� ���
    }

    return 0;
}
