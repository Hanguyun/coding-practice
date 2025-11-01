1. 함수(Function)

함수란?

요술 상자: 입력(인수, argument)을 넣으면 결과(반환값, return value)를 돌려줌

main 함수도 함수다 → 실행의 시작점


함수 만드는 법

반환타입 함수이름(매개변수들) {
    실행문;
    return 값; // 반환타입과 같은 자료형
}

반환값이 없으면 void

매개변수(parameter)는 호출 시 넘겨주는 값(argument)을 받는 변수

매개변수 여러 개 → 콤마(,)로 구분

전달하는 값의 개수와 자료형이 반드시 일치해야 함


함수 선언(원형)

함수 정의를 main 뒤에 쓰고 싶을 땐, 앞에 원형(prototype) 선언 필요


#include <stdio.h>

// 함수 원형 선언
int add(int a, int b);

int main(void) {
    printf("%d\n", add(3, 4)); // 7
    return 0;
}

int add(int a, int b) {
    return a+b;
}

return의 의미

return 값; → 함수를 즉시 종료하고 호출한 곳으로 값 반환

return; (반환타입이 void일 경우) → 단순히 함수 종료



---

2. 기억 클래스(Storage Class)

지역 변수

함수 내부에서 선언

stack 영역에 저장

자동 초기화 안 됨 → 반드시 직접 초기화 필요


void test() {
    int x;        // 쓰레기 값
    int y=0;      // 초기화 권장
}

전역 변수

함수 밖에서 선언

프로그램 어디서든 사용 가능

data 영역(BSS/데이터 영역)에 저장

자동 초기화 → 정수는 0, 실수는 0.0, 포인터는 NULL


static 변수

static 지역 변수 → 함수가 끝나도 삭제되지 않고 값 유지

프로그램이 끝날 때까지 메모리에 남음


#include <stdio.h>

void counter() {
    static int cnt = 0; // 딱 한 번 초기화
    cnt++;
    printf("%d\n", cnt);
}

int main(void) {
    counter(); // 1
    counter(); // 2
    counter(); // 3
    return 0;
}

메모리 영역 요약

Stack: 지역 변수, 매개변수 (함수 호출 시 쌓이고 끝나면 해제)

Heap: 동적 할당 영역 (malloc 등)

Data: 전역, static

Code(Text): 프로그램 코드



---

3. 포인터(Pointer)

포인터란?

메모리 주소를 저장하는 변수

포인터를 통해 변수에 간접 접근 가능


& (주소 연산자)

&변수 → 변수의 주소 반환


* (간접 참조 연산자)

포인터가 가리키는 주소에 접근


#include <stdio.h>

int main(void) {
    int i = 100;
    int *p = &i;   // p에 i의 주소 저장

    printf("i의 값: %d\n", i);
    printf("i의 주소: %p\n", (void*)&i);
    printf("p의 값(=i의 주소): %p\n", (void*)p);
    printf("p가 가리키는 값: %d\n", *p);

    *p = 200;  // 포인터를 통해 i 수정
    printf("i의 새로운 값: %d\n", i);
    return 0;
}

출력 예시:

i의 값: 100
i의 주소: 0x7ffc3c...
p의 값: 0x7ffc3c...
p가 가리키는 값: 100
i의 새로운 값: 200


---

4. 포인터와 배열

배열 이름은 배열 첫 번째 원소의 주소

배열이름 == &배열[0]


#include <stdio.h>

int main(void) {
    int arr[3] = {10,20,30};
    int *p = arr; // == &arr[0]

    printf("%d\n", arr[0]); // 10
    printf("%d\n", *p);     // 10
    printf("%d\n", *(p+1)); // 20
    printf("%d\n", arr[1]); // 20
    return 0;
}

- int는 4바이트라서 p+1 → 메모리 주소가 4 증가


---

5. Side Effect (부작용)

연산 결과 외에 변수의 상태가 바뀌는 효과

예: i++, --i, 함수 호출 시 전역 변수 변경 등


int i=1;
int x = i++ + 5; // i의 값도 바뀜 → side effect

주의: 같은 변수를 한 식에서 여러 번 side effect 하면 UB(정의되지 않은 동작) 발생


---

6. 문자열(String)

문자 vs 문자열

문자: 'A' → char 1개

문자열: "ABC" → 문자 배열 + 널 문자 \0 포함

"ABC" 실제 저장: {'A','B','C','\0'}



주의

항상 널문자(\0) 공간 확보 필요

한글: 보통 2바이트(UTF-8에서는 3바이트 이상)


문자열 입출력 함수

puts

문자열 출력 후 자동 줄바꿈


puts("Hello");  // Hello\n

fputs

문자열 출력 (줄바꿈 없음)

첫 번째 인자: 문자열, 두 번째 인자: 스트림(파일/출력)


fputs("Hello", stdout); // Hello

예시

#include <stdio.h>

int main(void) {
    char str[] = "Hello";
    puts(str);               // Hello + 줄바꿈
    fputs(str, stdout);      // Hello (줄바꿈 없음)
    return 0;
}