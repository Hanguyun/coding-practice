/*#include<stdio.h> // <복습> 구구단을 출력하는 프로그램을 작성하시오.
int main()
{
    int n, i =1;

    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for( ; i < 10; ++i)
    {
        printf("%d * %d = %d\n", n, i, i * n);
    }
    return 0;
}
*/

/*#include<stdio.h> // <복습> 팩토리얼(n!)을 계산하는 프로그램을 작성하시오.
int main()
{
    int n, pro = 1;

    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for (int i = n; i > 0; --i)
    {
        printf("%d", i);

        if (i > 1)
            printf(" * ");
        else
            printf(" = ");
        pro = pro * i;
    }
    printf("%d", pro);
    return 0;
}*/

/*#include<stdio.h> // 정수 n을 입력 받아 1부터 n까지의 숫자를 차례대로 출력하는 프로그램을 작성하시오.
int main()
{
    int n, i = 1;
    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        printf("%d, ", i);
    }
    return 0;
}
*/
