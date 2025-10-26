#inclued<stdio.h>

int main(void) {
  int arr[] = arr;
  int *p = arr;
  int max = *p;

  for(int i = 0; sizeof(arr)/sizeof(arr[0]); i++) {
      if(*(p + i) > max)
        max = *(p + i);
  }
  printf("최대값 = %d", max);
  return 0;
}
