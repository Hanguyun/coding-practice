/*#include<stdio.h> //  <복습> 사용자로부터 정수 n을 입력받아, 1부터 n까지의 수 중에서 소수(prime number)만 출력하고, 그 소수들의 개수와 합도 구하는 프로그램을 작성하시오.
int main()
{
    int n, i = 0, j, inP, sum = 0, count = 0;

    printf("정수를 입력하세요. :");
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
    printf("개수 : %d\n", count);
    printf("합 : %d", sum);

    return 0;
}
*/

/*#include<stdio.h>// <복습> 정수 5개를 입력받아 배열에 저장한 후, 입력한 수를 모두 출력하고 그 중에서 최댓값과 최솟값을 찾아 출력하는 프로그램을 작성하시오.
int main()
{
    int arr[5];
    int i, max = 0, min = 0;

    printf("정수 5개를 입력하세요. :");
    for (i = 0; i < 5; ++i) {
        scanf("%d", &arr[i]);

    max = arr[0];
    min = arr[0];

    if (arr[i] > max)
        max = arr[i];
    if (arr[i] < min)
        min = arr[i];
    }
    printf("최대값 : %d\n", max);
    printf("최소값 : %d\n", min);
    return 0;
}
*/
