/*#include<stdio.h>//정수 5개를 입력받아 배열에 저장한 후, 입력한 순서의 반대 순서(역순)로 출력하는 프로그램을 작성하시오.
int main()
{
    int arr[5];
    int i = 0;

    printf("정수 5개를 입력하세요. :");
    for ( ; i < 5; ++i) {
        scanf("%d", &arr[i]);
    }
    for (i = 4; i >=0; i--) {
        printf("%d\n", arr[i]);
    }

    return 0;
}
*/
/*#include<stdio.h> // 정수 5개를 입력받아 배열에 저장한 후, 입력한 수들의 합과 평균을 구하는 프로그램을 작성하시오.
int main()
{
    int arr[5], i = 0, sum = 0;
    float average = 0;

    printf("정수 5개를 입력하세요. :");
    for ( ; i < 5 ; ++i) {
        scanf("%d", &arr[i]);
    }
    i = 0;
    printf("입력한 수 :");
    for ( ; i < 5; ++i) {
        printf("%d ", arr[i]);
        sum = sum + arr[i];
    }
        average = sum / 5.0;
        printf("\n합계 = %d\n", sum);
        printf("평균 = %.2f\n", average);
        return 0;
}
*/
