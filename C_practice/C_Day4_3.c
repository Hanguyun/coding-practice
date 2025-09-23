/*#include<stdio.h> // 1~n까지의 짝수만 출력하는 프로그램을 작성하세요.
int main()
{
    int n, i = 1;

    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if (i % 2 == 0)
            printf("%d ", i);
    }

    return 0;
}
*/

/*include<stdio.h> // 정수 n을 입력받아 1~n까지의 수 중 3의 배수만 출력하는 프로그램을 작성하세요.
int main()
{
    int n, i = 1;
    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
            if (i % 3 == 0)
                printf("%d\n", i);
    }
    return 0;
}
*/

/*#include<stdio.h> //사용자로부터 정수 n을 입력받아, 1부터 n까지의 수 중에서 3의 배수의 합을 구해서 출력하는 프로그램을 작성하시오.
int main()
{
    int n, i = 1, sum = 0;

    printf("정수를 입력하세요. : ");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if (i % 3 == 0)
            sum = sum + i;
    }
    printf("1부터 %d까지의 3의 배수 합 = %d\n", n, sum);
     return 0;
}*/

/*#include<stdio.h> //사용자로부터 정수 n을 입력받아, 1부터 n까지의 수 중에서 3의 배수이면서 짝수인 수를 출력하고, 그 수들의 합도 구해서 출력하는 프로그램을 작성하시오.
int main()
{
    int n, sum = 0, i = 1;

    printf("정수를 입력하세요. : ");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if ((i % 3 == 0)&&(i % 2 == 0))
        {
         printf("3의 배수이면서 짝수인 수 : %d\n", i);
        sum = sum + i;
        }
    }
    printf("합계 = %d\n", sum);
    return 0;
}
*/
