/*#include<stdio.h> // 1~n������ ¦���� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int n, i = 1;

    printf("������ �Է��ϼ���. :");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if (i % 2 == 0)
            printf("%d ", i);
    }

    return 0;
}
*/

/*include<stdio.h> // ���� n�� �Է¹޾� 1~n������ �� �� 3�� ����� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int n, i = 1;
    printf("������ �Է��ϼ���. :");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
            if (i % 3 == 0)
                printf("%d\n", i);
    }
    return 0;
}
*/

/*#include<stdio.h> //����ڷκ��� ���� n�� �Է¹޾�, 1���� n������ �� �߿��� 3�� ����� ���� ���ؼ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main()
{
    int n, i = 1, sum = 0;

    printf("������ �Է��ϼ���. : ");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if (i % 3 == 0)
            sum = sum + i;
    }
    printf("1���� %d������ 3�� ��� �� = %d\n", n, sum);
     return 0;
}*/

/*#include<stdio.h> //����ڷκ��� ���� n�� �Է¹޾�, 1���� n������ �� �߿��� 3�� ����̸鼭 ¦���� ���� ����ϰ�, �� ������ �յ� ���ؼ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
int main()
{
    int n, sum = 0, i = 1;

    printf("������ �Է��ϼ���. : ");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if ((i % 3 == 0)&&(i % 2 == 0))
        {
         printf("3�� ����̸鼭 ¦���� �� : %d\n", i);
        sum = sum + i;
        }
    }
    printf("�հ� = %d\n", sum);
    return 0;
}
*/
