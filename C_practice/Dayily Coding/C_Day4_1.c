/*#include<stdio.h>  // <����> ���� 1���� �Է¹޾� Ȧ��/¦�� �Ǻ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int i;

    printf("������ �Է��ϼ���.:");
    scanf("%d", &i);

    if (i % 2 == 0)
        printf("%d�� ¦�� �Դϴ�.\n", i);

    if (i % 2 != 0)
        printf("%d�� Ȧ�� �Դϴ�.\n", i);

        return 0;
}
*/

/*#include<stdio.h> // <����>���� 1���� �Է¹޾� Ȧ��/¦�� �Ǻ� ���α׷��� �ۼ��ϼ���. (else ���)
int main() {
    int i;

    printf("������ �Է��ϼ���.:");
    scanf("%d", &i);

    if (i % 2 == 0)
        printf("%d�� ¦�� �Դϴ�.\n", i);
    else printf("%d�� Ȧ�� �Դϴ�.\n", i);

    return 0;
}
*/

/*#include<stdio.h> // <����>����ڷκ��� ���� N�� �޾� 1~N ������ ���� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int sum = 0, n;

    printf("������ �Է��ϼ���.:");
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i)
    {
        sum = sum + i;
    }
    printf("�� : %d\n", sum);

    return 0;
}*/

/*#include<stdio.h> // <����>����ڷκ��� ���� N�� �Է¹޾� 1~N���� �� �� ¦���� ��� ���� ���� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int i = 1, sum = 0, n;

    printf("������ �Է��ϼ���.:");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if (i % 2 == 0)
            sum = sum + i;
    }
    printf("�� : %d\n", sum);

    return 0;
}*/

/*#include<stdio.h> // <����>����ڷκ��� ���� N�� �Է¹޾� 1~N ���� ������ ���� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int n, i = 1, sum = 0;

    printf("������ �Է��ϼ���.:");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        sum = sum + i * i;
    }
    printf("������ �� : %d", sum);

    return 0;
} */

/*#include<stdio.h>  // ����ڷκ��� ���� N�� �Է¹޾� 1~N�� Ȧ���� ������ ���� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main ()
{
    int n, sum = 0, i = 1;

    printf("������ �Է��ϼ���.:");
    scanf("%d", &n);

    for( ; i <= n; ++i)
    {
        if (i % 2 != 0)
            sum = sum + i * i;
    }
    printf("Ȧ�� ������ �� : %d", sum);

    return 0;
}*/

/*#include<stdio.h> // <����>����ڷκ��� ���� N�� M�� �Է¹޾� 1~N���� �� �߿��� M�� ����� ��� ���� ���� ����ϴ� ���α׷��� �ۼ��ϼ���.
int main()
{
    int n, m, sum = 0, i = 1;
    printf("N�� �Է��ϼ���. :");
    scanf("%d", &n);
    printf("M�� �Է��ϼ���. :");
    scanf("%d", &m);

    for ( ; i <= n; ++i)
    {
        if (i % m == 0)
            sum = sum + i;
    }
    printf("M�� ��� �� : %d", sum);

    return 0;
}*/

