/*#include<stdio.h> //  ����ڷκ��� ���� n�� �Է¹޾�, 1���� n������ �� �߿��� �Ҽ�(prime number)�� ����ϰ�, �� �Ҽ����� ������ �յ� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main()
{
    int n, i, j, isPrime, sum = 0, count = 0;

    printf("������ �Է��ϼ���. :");
    scanf("%d", &n);
    printf("�Ҽ� : ");

    for (i = 2 ;i <= n; ++i)
       {
        isPrime = 1;
            for (j =2; j * j <= i; j++)
            {
                if (i % j == 0) {
                    isPrime = 0;
                    break;
                }
            }
        if (isPrime) {
            printf("%d ", i);
            count++;
            sum += i;
        }
        }
        printf("���� = %d      ", count);
        printf("�հ� = %d", sum);
        return 0;
}
*/

/*#include<stdio.h>// ���� 5���� �Է¹޾� �迭�� ������ ��, �Է��� ���� ��� ����ϰ� �� �߿��� �ִ񰪰� �ּڰ��� ã�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main()
{
    int arr[5]; // �迭�� � �������� int�� ����
    int i;  // �ִ밪, �ּҰ��� ���ϱ� ���� ���� ����
    int max = 0, min = 0;  // �ִ밪, �ּҰ��� ����ϱ� ���� ���� ������ �ʱ�ȭ

    printf("���� 5���� �Է��ϼ���. :");

    //�迭�� ��� ������ �Է¹������� for�� ���
  for (i = 0; i < 5; i++)
  {
      scanf("%d", &arr[i]);
  }
  // ù ��° ���� �������� �ʱ�ȭ
    max = arr[0];
    min = arr[0];

    // �迭 ��� + �ִ�/�ּ� ã��
    printf("�Է��� ��: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr[i]);

        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    // ��� ���
    printf("\n�ִ밪 = %d\n", max);
    printf("�ִ밪 = %d\n", min);

    return 0;
}
*/
