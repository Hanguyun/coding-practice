// 포인터로 변수 값 바꾸기
#include <stdio.h>

int main(void) {
    int num = 10;        //  정수형 변수 num 선언하고 10으로 초기화
    int *p = &num;       //  포인터 p에 num의 주소 저장

    *p = 99;             //  포인터를 통해 num의 값을 99로 변경

    printf("num = %d\n", num);  //  변수 num의 값 출력
    printf("*p = %d\n", *p);    //  포인터 p가 가리키는 값 출력

    return 0; // 반환 값 없음
}

