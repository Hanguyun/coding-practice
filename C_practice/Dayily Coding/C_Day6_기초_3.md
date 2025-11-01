## 1. 조건 연산자 (삼항 연산자)

- 조건 ? 값1 : 값2
- if문을 간단하게 표현 가능

### 예시 1: if문

```c
#include <stdio.h>

int main(void) {
    int i;
    if(3 > 4)
        i = 100;
    else
        i = 200;
    printf("%d\n", i); // 200
    return 0;
}

```

### 예시 2: 조건 연산자

```c
#include <stdio.h>

int main(void) {
    int i;
    i = (3 > 4) ? 100 : 200;
    printf("%d\n", i); // 200
    return 0;
}

```

---

## 2. sizeof (메모리 공간 크기)

- 변수나 자료형이 차지하는 **메모리 크기(바이트)** 반환
- 반환 타입: size_t (→ printf에서는 %zu사용 권장)

```c
#include <stdio.h>

int main(void) {
    int i;
    printf("%zu\n", sizeof(i));     // 변수 i 크기
    printf("%zu\n", sizeof(int));   // int 크기
    printf("%zu\n", sizeof(int*));  // int 포인터 크기
    return 0;
}
```

---

## 3. 형 변환 연산자

- (타입) 값: 값을 특정 타입으로 강제 변환

```c
int i = (int)3.14;   // i=3
float f = (float)10; // f=10.0
```

---

## 4. 제어문

### 4-1. if / else

```c
if (조건) {
    // 조건 참일 때 실행
} else {
    // 조건 거짓일 때 실행
}

```

### 4-2. 다중 if문

```c
if (조건1) {
    // 조건1이 참일 때
} else if (조건2) {
    // 조건2가 참일 때
} else {
    // 둘 다 거짓일 때
}

```

### 4-3. switch문

- switch는 정수, 문자형 가능 (실수/문자열 불가)
- break가 없으면 아래 case 계속 실행 (**fall-through**)

```c
#include <stdio.h>

int main(void) {
    int i = 100;
    switch (i/10) {
        case 10:
        case 9: printf("A"); break;
        case 8: printf("B"); break;
        case 7: printf("C"); break;
        default: printf("F");
    }
    return 0;
}

```

---

## 5. 반복문

### 5-1. for문

```c
for(초기화; 조건; 증감) {
    // 실행문
}

```

- for문 내부에서 선언한 변수는 **for문 안에서만 사용 가능**

### 예시: 구구단

```c
#include <stdio.h>

int main(void) {
    for (int dan=1; dan<=9; dan++) {
        for (int i=1; i<=9; i++) {
            printf("%d * %d = %d\n", dan, i, dan*i);
        }
    }
    return 0;
}

```

### 예시: 3단씩 묶어서 출력

```c
#include <stdio.h>

int main(void) {
    for (int dan=1; dan<=9; dan+=3) {
        for (int i=1; i<=9; i++) {
            printf("%d*%d=%d\t", dan,   i, dan*i);
            printf("%d*%d=%d\t", dan+1, i, (dan+1)*i);
            printf("%d*%d=%d\n", dan+2, i, (dan+2)*i);
        }
    }
    return 0;
}

```

---

### 5-2. while문

- 조건이 참일 때 반복
- 조건이 처음부터 거짓이면 한 번도 실행 안 함

```c
int i=0;
while(i < 5) {
    printf("%d\n", i);
    i++;
}

```

---

### 5-3. do~while문

- 무조건 한 번 실행 후 조건 검사

```c
int i=0;
do {
    printf("%d\n", i);
    i++;
} while(i < 5);

```

---

### 5-4. 기타 제어문

- break: 반복 즉시 종료
- continue: 다음 반복으로 건너뜀
- goto: label로 이동 (비추천)

---

## 6. 배열(Array)

- 같은 타입 변수를 연속적으로 저장하는 구조
- 선언: 타입 배열이름[크기];

### 예시

```c
int s[3] = {100, 200, 300};
int s2[] = {100, 200, 300}; // 크기 생략 → 초기값 개수만큼
int s3[3] = {10, 20};       // {10,20,0} 으로 자동 초기화

```

### 배열 주소 & 값 출력

```c
#include <stdio.h>

int main(void) {
    int score[] = {10,20,30,40};

    printf("%p\n", (void*)&score[0]); // 첫 번째 요소 주소
    printf("%p\n", (void*)score);     // 배열 이름 = 첫 번째 주소
    printf("%d\n", score[0]);         // 첫 번째 값
    printf("%p\n", (void*)&score[1]); // 두 번째 요소 주소
    printf("%d\n", score[1]);         // 두 번째 값

    printf("배열 전체 크기: %zu바이트\n", sizeof(score));
    printf("요소 개수: %zu개\n", sizeof(score)/sizeof(int));

    return 0;
}

```

int는 보통 4바이트 → 주소가 4씩 증가

---

## 7. 함수(Function)

- 프로그램을 기능별로 나누어 재사용/관리 용이
- 구조: 반환형 함수이름(매개변수) { … return 값; }
- 반환형 없으면 void

### 함수 선언/호출

```c
#include <stdio.h>

int incre(int a) {
    return ++a;
}

int main(void) {
    printf("%d\n", incre(100)); // 101
    return 0;
}

```

### 실수형 버전

```c
#include <stdio.h>

float incre(float a) {
    a += 1;
    return a;
}

int main(void) {
    printf("%f\n", incre(3.14)); // 4.140000
    return 0;
}

```

### 함수 선언 위치

- 함수 정의는 main 위에 있거나
- main 앞에서 **선언(prototype)** 필요

```c
#include <stdio.h>

float incre(float a); // 함수 원형 선언

int main(void) {
    printf("%f\n", incre(3.14));
    return 0;
}

float incre(float a) {
    return a+1;
}

```

---

## 8. 변수의 유효범위(scope) & 기억 클래스(storage class)

- **전역 변수**: 함수 밖에서 선언, 프로그램 전체에서 사용 가능 (자동 0 초기화)
- **지역 변수**: 함수 안에서만 사용 가능 (자동 초기화 안 됨)
- static: 정적 지역 변수 → 함수가 끝나도 값 유지

### 예시 1: 전역/지역

```c
#include <stdio.h>

int age = 10; // 전역변수

void incre(int a) {
    a += 1;             // 지역변수 a
    printf("%d\n", a);  // 지역
    printf("%d\n", age);// 전역
}

int main(void) {
    int i = 100; // 지역변수
    incre(i);
    printf("%d\n", i);   // 지역 i
    printf("%d\n", age); // 전역 age
    return 0;
}

```

### 예시 2: 전역 변수 수정

```c
#include <stdio.h>

int age = 10;

void incre(int a) {
    printf("%d\n", age);
    age++;
    printf("%d\n", age);
}

int main(void) {
    printf("%d\n", age);
    incre(100);
    printf("%d\n", age);
    return 0;
}

```

---

## 9. Call by Value vs Call by Reference

- **Call by Value**: 값 복사 전달 (원본 영향 없음)
- **Call by Reference**: 주소 전달 (원본 값 직접 변경)

### 예시: Call by Reference