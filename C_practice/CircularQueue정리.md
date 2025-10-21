## 웨이팅 프로그램 헤더 파일

```c
Element data[MAX_SIZE];
int front;
int rear;

void error(char* str)
{
    printf("%s\n", str);
    exit(1);
}

void init_queue()
{
    front = rear = 0;
}
int is_empty()
{
    return front == rear;
}
int is_full()
{
    return front == (rear +1) % MAX_SIZE;
}
void enqueue(Element e)
{
    if (is_full())
        error("Overflow Error!");
    rear = (rear +1) % MAX_SIZE;
    data[rear] = e;
}

Element dequeue()
{
    if (is_empty())
        error("Underflow Error!");
    front = (front +1) % MAX_SIZE;
    return data[front];
}

Element peek()
{
    if (is_empty())
        error("Underflow Error!");
    return data[(front +1) % MAX_SIZE];
}

```

---

### 전역 변수

```c
Element data[MAX_SIZE];
int front;
int rear;
```

- data : 큐에 저장될 실제 데이터 배열 (크기 = MAX_SIZE)
- front : 맨 앞 요소 앞 위치 (즉, 꺼낼 위치 바로 앞)
- rear : 마지막 요소 위치
- 초기에는 둘 다 0으로 둬서 “빈 큐” 상태로 설정

---

### 에러 처리 함수

```c
void error(char* str)
{
    printf("%s\n", str);
    exit(1);
}
```

- 문자열 str을 출력하고 프로그램을 강제 종료.
- exit(1)은 비정상 종료 코드.
    - 보통 성공은 exit(0)을 사용.

---

### 초기화 함수

```c
void init_queue()
{
    front = rear = 0;
}
```

- front와 rear를 0으로 설정해 큐를 “비운 상태”로 초기화
- 프로그램 처음 실행 시 꼭 한 번 호출해야 함.

---

### 공백 검사 함수

```c
int is_empty()
{
    return front == rear;
}
```

- front와 rear가 같으면 큐가 비었다는 뜻.
- 리턴값: 1(참) → 비어 있음, 0(거짓) → 비어 있지 않음.

---

### 포화 검사 함수

```c
int is_full()
{
    return front == (rear + 1) % MAX_SIZE;
}
```

- rear가 한 칸 앞으로 가면 front와 같아지는 경우 → 꽉 참.
- % MAX_SIZE로 한 바퀴 돌아도 인덱스가 맞게 유지
- 즉, 원형 큐의 핵심 개념인 모듈러(modulo) 연산 사용.

---

### 삽입 함수(enqueue)

```c
void enqueue(Element e)
{
    if (is_full())
        error("Overflow Error!");
    rear = (rear + 1) % MAX_SIZE;
    data[rear] = e;
}
```

- 큐가 꽉 찼는지 확인 → 꽉 차면 에러 종료.
- 아니면 rear를 한 칸 이동시켜 새 데이터를 넣는다.
- rear는 항상 마지막에 삽입된 위치를 가리킴.

---

### 삭제 함수

```c
Element dequeue()
{
    if (is_empty())
        error("Underflow Error!");
    front = (front + 1) % MAX_SIZE;
    return data[front];
}
```

- 큐가 비어 있으면 에러 종료.
- front를 한 칸 앞으로 옮기고, 그 위치의 데이터를 리턴.
- front는 항상 맨 앞 데이터의 “직전” 위치를 가르킨다.

---

### 맨 앞 값만 보기 (peek)

```c
Element peek()
{
    if (is_empty())
        error("Underflow Error!");
    return data[(front +1) % MAX_SIZE];
}
```

- dequeue()와 다르게 front를 움직이지 않고, 바로 다음 칸의 데이터를 “보기만” 함.