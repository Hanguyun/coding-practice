## 웨이팅 프로그램

```c
#include<stdio.h>
#include<stdlib.h>

#define MAX_SIZE 8
struct Waiting{
    int id;
    int nperson;
    char info[32];
};
typedef struct Waiting Element;
#include "CircularQueue.h"
int waiting_id=1;

void inputing(){
        Element *customer;
        customer = (Element *) malloc(sizeof(Element));
        printf("인원수 : ");
        scanf("%d",&(customer->nperson));
        printf("전화번호 : ");
        scanf("%s",customer->info);
        customer->id = waiting_id++;
        printf("대기 신청 완료....... 대기번호: %d 인원:%d  연락:%s\n",customer->id, customer->nperson,customer->info);
        enqueue(*customer);
}

void entering(){
       if( !is_empty()){
            Element temp = dequeue();
            printf(" 대기번호 %d 번 입장 차례입니다..(인원:%d  연락:%s)\n",temp.id, temp.nperson,temp.info);
       }
       else
            printf("대기하는 사람이 없습니다.");
}

void main(){
    int menu;
    int waiting_id=1;
    init_queue();
    while(1){
         printf("1. 대기신청   2. 입장   3. 종료 : ");
        scanf("%d",&menu);
        switch(menu){
            case 1: inputing();
                        break;
            case 2: entering();
                        break;
            case 3: printf("프로그램을 종료합니다.");
                        exit(1);
            default: printf("잘못된 입력입니다...확인하고 다시 입력하세요.");
        }
    }
}
```

---

### 헤더와 전처리기

```c
#include<stdio.h>
#include<stdlib.h>
```

- stdio.h : printf, scanf 같은 표준 입출력 함수들이 들어있다.
- stdlib.h : malloc, free, exit 같은 표준 라이브러리가 들어있다.

```c
#define MAX_SIZE 8
```

- 전처리 상수. 컴파일 전에 MAX_SIZE를 8로 바꿔치기한다.
- 아마 원형 큐의 최대 크기로 쓰려고 정한 값.

---

### 구조체 정의 + typedef

```c
struct Waiting{
    int id;         // 대기번호
    int nperson;    // 인원수
    char info[32];  // 연락처(전화번호 등) 문자열
};
typedef struct Waiting Element;
```

- struct Waiting 이라는 사용자 정의 타입을 만들었고,
- typedef로 줄여서 Element라고 부르도록 별칭을 줌.
    - 즉, Element는 struct Waiting과 동일.

---

### 사용자 헤더(큐) 포함

```c
#include "CircularQueue.h"
```

- 사용자 정의 헤더. 여기에는 큐 관련 함수/구조(예: init_queue, enqueue, dequeue, is_empty) 선언이 들어있어야 함.

---

### 전역 변수

```c
int waiting_id=1;
```

- 전역 대기번호 카운터. 새 손님 받을 때마다 waiting_id++ 로 번호 증가.

---

### 대기 신청 함수 : inputing

```c
void inputing(){
        Element *customer;
        customer = (Element *) malloc(sizeof(Element));
```

- Element를 힙 메모리에 동적 할당.
- C에서는 malloc 캐스팅이 꼭 필요하진 않음. (Element *)는 생략 가능

```c
        printf("인원수 : ");
        scanf("%d",&(customer->nperson));
```

- 인원수 입력 받아 nperson에 저장.

```c
        printf("전화번호 : ");
        scanf("%s",customer->info);
```

- 문자열 입력을 info 버퍼에 저장.

```c
        customer->id = waiting_id++;
```

- 전역 waiting_id로 대기번호 부여하고 1 증가.

```c
        printf("대기 신청 완료....... 대기번호: %d 인원:%d  연락:%s\n",
               customer->id, customer->nperson,customer->info);
```

- 잘 들어갔는지 출력

```c
        enqueue(*customer);
}
```

- 포인터가 가리키는 구조체 값 자체를 복사해서 큐에 넣음(값 전달).

---

### 입장 처리 함수: entering

```c
void entering(){
       if( !is_empty()){
            Element temp = dequeue();
            printf(" 대기번호 %d 번 입장 차례입니다..(인원:%d  연락:%s)\n",
                   temp.id, temp.nperson,temp.info);
       }
       else
            printf("대기하는 사람이 없습니다.");
}
```

- 큐가 비어있지 않으면 dequeue()로 맨 앞 손님을 꺼내 temp에 복사.
- 해당 손님 입장 안내 출력.
- 비어있으면 “대기 없음” 출력.

---

### 메인 함수와 메뉴 루프

```c
void main(){
    int menu;
    int waiting_id=1;
    init_queue();
    while(1){
         printf("1. 대기신청   2. 입장   3. 종료 : ");
        scanf("%d",&menu);
        switch(menu){
            case 1: inputing();
                        break;
            case 2: entering();
                        break;
            case 3: printf("프로그램을 종료합니다.");
                        exit(1);
            default: printf("잘못된 입력입니다...확인하고 다시 입력하세요.");
        }
    }
}
```

- 무한루프 돌면서 메뉴 입력 받고 분기.
- case 3에서 메세지 출력하고 exit(1)로 즉시 종료.
    - 관례상 정상 종료는 exit(0)이 더 적절.
- default로 잘못된 입력 처리.

---

### 코드 보안 버전

```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_SIZE 8

typedef struct {
    int id;
    int nperson;
    char info[32];
} Element;

#include "CircularQueue.h"

int waiting_id = 1;  // 전역 카운터 (섀도잉 금지)

void inputing(void) {
    Element customer;  // 지역 변수로 안전하게
    printf("인원수 : ");
    if (scanf("%d", &customer.nperson) != 1) {
        fprintf(stderr, "입력 오류: 인원수\n");
        // 입력 버퍼 비우기 등 추가 처리 가능
        return;
    }

    printf("전화번호 : ");
    if (scanf("%31s", customer.info) != 1) {
        fprintf(stderr, "입력 오류: 전화번호\n");
        return;
    }

    customer.id = waiting_id++;
    printf("대기 신청 완료....... 대기번호: %d 인원:%d  연락:%s\n",
           customer.id, customer.nperson, customer.info);

    if (is_full()) {
        printf("대기열이 가득 찼습니다. (최대 %d명)\n", MAX_SIZE);
        return;
    }
    enqueue(customer); // 값 복사로 큐에 저장
}

void entering(void) {
    if (!is_empty()) {
        Element temp = dequeue();
        printf("대기번호 %d 번 입장 차례입니다.. (인원:%d  연락:%s)\n",
               temp.id, temp.nperson, temp.info);
    } else {
        printf("대기하는 사람이 없습니다.\n");
    }
}

int main(void) {
    int menu;
    init_queue();

    while (1) {
        printf("1. 대기신청   2. 입장   3. 종료 : ");
        if (scanf("%d", &menu) != 1) {
            fprintf(stderr, "입력 오류: 메뉴 번호\n");
            // 입력 버퍼 비우기 등 추가 처리 가능
            continue;
        }

        switch (menu) {
            case 1: inputing();  break;
            case 2: entering();  break;
            case 3:
                printf("프로그램을 종료합니다.\n");
                return 0; // 정상 종료
            default:
                printf("잘못된 입력입니다... 확인하고 다시 입력하세요.\n");
        }
    }
}

```