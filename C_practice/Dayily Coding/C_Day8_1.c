/*#include<stdio.h> //  <����> ����ڷκ��� ���� n�� �Է¹޾�, 1���� n������ �� �߿��� �Ҽ�(prime number)�� ����ϰ�, �� �Ҽ����� ������ �յ� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main()
{
    int n, i = 0, j, inP, sum = 0, count = 0;

    printf("������ �Է��ϼ���. :");
    scanf("%d", &n);

    for ( i = 2; i <= n; ++i) {
        inP = 1;
        for (j = 2 ; j*j <= i; ++j)
        if (i % j == 0) {
            inP = 0;
            break;
        }
        if (inP) {
            printf("%d ", i);
            count++;
            sum = sum + i;
        }
    }
    printf("���� : %d\n", count);
    printf("�� : %d", sum);

    return 0;
}
*/

/*#include<stdio.h>// <����> ���� 5���� �Է¹޾� �迭�� ������ ��, �Է��� ���� ��� ����ϰ� �� �߿��� �ִ񰪰� �ּڰ��� ã�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main()
{
    int arr[5];
    int i, max = 0, min = 0;

    printf("���� 5���� �Է��ϼ���. :");
    for (i = 0; i < 5; ++i) {
        scanf("%d", &arr[i]);

    max = arr[0];
    min = arr[0];

    if (arr[i] > max)
        max = arr[i];
    if (arr[i] < min)
        min = arr[i];
    }
    printf("�ִ밪 : %d\n", max);
    printf("�ּҰ� : %d\n", min);
    return 0;
}
*/
