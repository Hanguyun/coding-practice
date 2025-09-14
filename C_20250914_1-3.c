/*#include<stdio.h> // 사용자로부터 정수 N을 받아 1~N 까지의 합을 출력하는 프로그램을 작성하세요.
int main() {
    int n, sum = 0, i = 1;

     printf("정수를 입력하세요. :");
     scanf("%d", &n);
    for( ; i <= n; ++i)
    {
        sum = sum + i;
    }
        printf("합 : %d\n", sum);

    return 0;
} */

/*#include<stdio.h> // 사용자로부터 정수 N을 입력받아 1~N까지 수 중 짝수만 모두 더한 값을 출력하는 프로그램을 작성하세요.
int main() {
    int n, sum = 0, i = 1;

    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for( ; i <= n; ++i)
    {
        if (i % 2 == 0)
        sum = sum + i;
    }
    printf("짝수의 합 : %d\n", sum);

    return 0;
} */

/*#include<stdio.h> //사용자로부터 정수 N을 입력받아 1~N 까지 제곱의 합을 출력하는 프로그램을 작성하세요.
int main() {
    int sum = 0, i = 1, n;
    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for( ; i <= n; ++i)
    {
        sum = sum + i * i;
    }
    printf("제곱의 합 : %d\n", sum);

    return 0;
}*/

/*#include<stdio.h> // 사용자로부터 정수 N을 입력받아 1~N의 홀수의 제곱의 합을 출력하는 프로그램을 작성하세요.
int main() {
    int n, sum = 0, i = 1;

    printf("정수를 입력하세요. :");
    scanf("%d", &n);

    for( ; i <=n; ++i)
    {
        if(i % 2 != 0)
            sum = sum + i * i;
    }
    printf("홀수의 제곱의 합 : %d\n", sum);

    return 0;
} */

/*#include<stdio.h> // 사용자로부터 정수 N과 M을 입력받아 1~N까지 수 중에서 M의 배수만 모두 더한 값을 출력하는 프로그램을 작성하세요.
int main() {
    int n, m, i, sum = 0;  // int 에서 i를 지정하는것 보다 for문에서 지정하는게 더 좋다.

    printf("N를 입력하세요. :");
    scanf("%d", &n);
    printf("M를 입력하세요. :");
    scanf("%d", &m);

    for(i = 1 ; i <= n; ++i) // for(i = 1; i <=n; ++i) -> 이렇게 지정
    {
        if(i % m == 0)
            sum = sum + i;
    }
    printf("%d의 배수의 합 : %d\n", m, sum);

    return 0;
} */


