// �����ͷ� ���� �� �ٲٱ�
#include <stdio.h>

int main(void) {
    int num = 10;        //  ������ ���� num �����ϰ� 10���� �ʱ�ȭ
    int *p = &num;       //  ������ p�� num�� �ּ� ����

    *p = 99;             //  �����͸� ���� num�� ���� 99�� ����

    printf("num = %d\n", num);  //  ���� num�� �� ���
    printf("*p = %d\n", *p);    //  ������ p�� ����Ű�� �� ���

    return 0; // ��ȯ �� ����
}

