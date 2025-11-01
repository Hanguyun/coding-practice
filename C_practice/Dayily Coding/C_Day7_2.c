/*#include<stdio.h> //  사용자로부터 정수 n을 입력받아, 1부터 n까지의 수 중에서 소수(prime number)만 출력하고, 그 소수들의 개수와 합도 구하는 프로그램을 작성하시오.
int main()
{
    int n, i, j, isPrime, sum = 0, count = 0;

    printf("정수를 입력하세요. :");
    scanf("%d", &n);
    printf("소수 : ");

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
        printf("개수 = %d      ", count);
        printf("합계 = %d", sum);
        return 0;
}
*/

/*#include<stdio.h>// 정수 5개를 입력받아 배열에 저장한 후, 입력한 수를 모두 출력하고 그 중에서 최댓값과 최솟값을 찾아 출력하는 프로그램을 작성하시오.
int main()
{
    int arr[5]; // 배열을 몇개 받을건지 int로 지정
    int i;  // 최대값, 최소값을 구하기 위한 변수 지정
    int max = 0, min = 0;  // 최대값, 최소값을 출력하기 위한 변수 지정과 초기화

    printf("정수 5개를 입력하세요. :");

    //배열의 모든 정수를 입력받을려면 for문 사용
  for (i = 0; i < 5; i++)
  {
      scanf("%d", &arr[i]);
  }
  // 첫 번째 값을 기준으로 초기화
    max = arr[0];
    min = arr[0];

    // 배열 출력 + 최대/최소 찾기
    printf("입력한 수: ");
    for (i = 0; i < 5; i++) {
        printf("%d ", arr[i]);

        if (arr[i] > max) {
            max = arr[i];
        }
        if (arr[i] < min) {
            min = arr[i];
        }
    }
    // 결과 출력
    printf("\n최대값 = %d\n", max);
    printf("최대값 = %d\n", min);

    return 0;
}
*/
