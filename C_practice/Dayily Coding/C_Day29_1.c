#include <stdio.h> // 1. 포인터로 두 변수 값 출력하기

int main(void) {
  int a = 5, int b = 10;
  int *p1 = &a;
  int *p2 = &b;
  printf("a의 값: %d\n", *p1);
  printf("b의 값: %d\n", *p2);
  printf("a의 주소: %d\n", p1);
  printf("b의 주소: %d\n", p2);
  return 0;
}

// 2. 포인터로 두 값 교환하기(swap)

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main(void) {
    int x = 3, y = 7;

    printf("Before: x = %d, y = %d\n", x, y);  // 따옴표 수정 + 세미콜론 추가
    swap(&x, &y);
    printf("After: x = %d, y = %d\n", x, y);

    return 0;
}
