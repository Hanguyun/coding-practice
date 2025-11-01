#include<stdion.h> // 포인터로 배열의 합 구하기

int main(void)
{
  int arr[] = {1,2,3,4,5};
  int *p = 0;
  int sum = 0;

  for(int i = 0; i < sizeof(arr) / sizeof(int); i++)
    {
      sum += arr[i];
    }
  printf("배열의 합 = %d", sum);
  printf("p가 가르키는 주소 = %p", p);
  printf("p 자신의 주소 = %p", &p);

  return 0;
}
  
