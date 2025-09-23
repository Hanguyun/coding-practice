/*#include<stdio.h>  // <복습> 정수 1개를 입력받아 홀수/짝수 판별 프로그램을 작성하세요.
int main()
{
    int i;

    printf("정수를 입력하세요.:");
    scanf("%d", &i);

    if (i % 2 == 0)
        printf("%d은 짝수 입니다.\n", i);

    if (i % 2 != 0)
        printf("%d은 홀수 입니다.\n", i);

        return 0;
}
*/

/*#include<stdio.h> // <복습>정수 1개를 입력받아 홀수/짝수 판별 프로그램을 작성하세요. (else 사용)
int main() {
    int i;

    printf("정수를 입력하세요.:");
    scanf("%d", &i);

    if (i % 2 == 0)
        printf("%d은 짝수 입니다.\n", i);
    else printf("%d은 홀수 입니다.\n", i);

    return 0;
}
*/

/*#include<stdio.h> // <복습>사용자로부터 정수 N을 받아 1~N 까지의 합을 출력하는 프로그램을 작성하세요.
int main()
{
    int sum = 0, n;

    printf("정수를 입력하세요.:");
    scanf("%d", &n);

    for (int i = 1; i <= n; ++i)
    {
        sum = sum + i;
    }
    printf("합 : %d\n", sum);

    return 0;
}*/

/*#include<stdio.h> // <복습>사용자로부터 정수 N을 입력받아 1~N까지 수 중 짝수만 모두 더한 값을 출력하는 프로그램을 작성하세요.
int main()
{
    int i = 1, sum = 0, n;

    printf("정수를 입력하세요.:");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        if (i % 2 == 0)
            sum = sum + i;
    }
    printf("합 : %d\n", sum);

    return 0;
}*/

/*#include<stdio.h> // <복습>사용자로부터 정수 N을 입력받아 1~N 까지 제곱의 합을 출력하는 프로그램을 작성하세요.
int main()
{
    int n, i = 1, sum = 0;

    printf("정수를 입력하세요.:");
    scanf("%d", &n);

    for ( ; i <= n; ++i)
    {
        sum = sum + i * i;
    }
    printf("제곱의 합 : %d", sum);

    return 0;
} */

/*#include<stdio.h>  // 사용자로부터 정수 N을 입력받아 1~N의 홀수의 제곱의 합을 출력하는 프로그램을 작성하세요.
int main ()
{
    int n, sum = 0, i = 1;

    printf("정수를 입력하세요.:");
    scanf("%d", &n);

    for( ; i <= n; ++i)
    {
        if (i % 2 != 0)
            sum = sum + i * i;
    }
    printf("홀수 제곱의 합 : %d", sum);

    return 0;
}*/

/*#include<stdio.h> // <복습>사용자로부터 정수 N과 M을 입력받아 1~N까지 수 중에서 M의 배수만 모두 더한 값을 출력하는 프로그램을 작성하세요.
int main()
{
    int n, m, sum = 0, i = 1;
    printf("N을 입력하세요. :");
    scanf("%d", &n);
    printf("M을 입력하세요. :");
    scanf("%d", &m);

    for ( ; i <= n; ++i)
    {
        if (i % m == 0)
            sum = sum + i;
    }
    printf("M의 배수 합 : %d", sum);

    return 0;
}*/

