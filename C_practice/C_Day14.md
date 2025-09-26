# 2025-09-24 (다항식의 곱셈)

## 다항식 곱셈 코드 정리

```c
#include <stdio.h>
#define MAX_DEGREE 7

typedef struct {
    int degree;
    double coef[MAX_DEGREE];
} polynomial;

polynomial mult(polynomial A, polynomial B) {
    polynomial C = { A.degree + B.degree, {0} };

    // 안전: 경계 체크 (필요시)
    // if (C.degree >= MAX_DEGREE) { /* 오류 처리 */ }

    for (int i = 0; i <= A.degree; i++)
        for (int j = 0; j <= B.degree; j++)
            C.coef[i + j] += A.coef[i] * B.coef[j];

    return C;
}

int main(void) {
    polynomial a = { 4, {0,0,2,2,3,0,0} };
    polynomial b = { 2, {7,3,4,0,0,0,0} };

    polynomial c = mult(a, b);

    printf("%d차 ", c.degree);
    for (int i = 0; i <= c.degree; i++)
        printf("%.0f ", c.coef[i]);   // 정수처럼 출력

    return 0;
}

```

---

### 1. 헤더 파일 포함

```c
#include <stdio.h>
```

- printf, scanf 같은 입출력 함수를 쓰려면 C 표준 입출력 라이브러리 <stdio.h>를 포함해야함.
- 뜻 : 화면에 출력하거나 입력 받는 기능이 필요하니 준비해라

### 2. 상수 정의

```c
#define MAX_DEGREE 7
```

- 다항식을 배열로 저장할 때, 배열 크기를 미리 정해줘야 함. (C는 가변 배열 불가)
- 뜻 : 우리 다항식은 최대 6차(=7칸)까지 다룰 거다. coef 배열은 칸 7개짜리다.

### 3. 구조체 정의

```c
typedef struct
{
    int degree;              // degree: 다항식의 최고 차수
    float coef[MAX_DEGREE];  // coef: 다항식의 계수들을 넣어두는 배열
} Polynomial;            // typedef: 이제 Polynomial 이라는 이름으로 자료형을 부를 수 있음
```

- 다항식을 저장할 때, 차수와 계수를 한 덩어리로 다룬다
- 다항식 = 박스
    - degree = 이 박스에 들어있는 탑의 높이
    - coef = 각 층마다 있는 블록의 개수

### 4. 함수 원형 선언

```c
polynomial mult(polynomial A, polynomial B);
```

- main에서 mult() 함수를 호출할 건데, C는 앞에서 정의하지 않으면 모른다. 그래서 미리 함수가 있다고 선언
- 뜻 : 나중에 mult라는 함수가 있는데, 다항식 두 개(a, b)를 받아서 새로운 다항식(p)를 돌려줄 거야.

### 5. main 함수 시작과 다항식 a, b 초기화

```c
int main() {
 polynomial a = { 4, {0, 0, 2, 2, 3, 0, 0} };
 polynomial b = { 2, {7, 3, 4, 0, 0, 0, 0} };
 }
```

- A(x) = 3x⁴ + 2x³ + 2x²
- B(x) = 4x² + 3x + 7
    - 이런 다항식을 코드에 저장
- `a.degree = 4`, `a.coef = [0,0,2,2,3,0,0]`
    
    → 즉 `a₂=2, a₃=2, a₄=3`
    
- `b.degree = 2`, `b.coef = [7,3,4,0,0,0,0]`
    
    → 즉 `b₀=7, b₁=3, b₂=4`
    

### 6. 다항식 곱하기 실행

```c
c = mult(a, b);
```

- A(x)*B(x)를 계산해서 결과를 C에 저장.
- 뜻 : a랑 b를 곱해서 새로운 다항식 c를 만들어라.

### 7. 결과 출력

```c
    printf("%d차 ", c.degree);
    for (i = 0; i < c.degree + 1; i++)
        printf("%d ", int(c.coef[i]));

    return 0;
}
```

- 결과 다항식이 몇 차인지, 계수들이 뭔지 확인하려고
- `printf("%d차 ", c.degree);`
    
    → “결과 다항식은 몇 차 다항식인지 보여줘.”
    
- `for (i=0; i < c.degree+1; i++)`
    
    → 계수들을 0차부터 최고차수까지 순서대로 출력.
    
- `printf("%d ", int(c.coef[i]));`
    
    → 계수가 실수(float)인데 정수(int)로 바꿔서 출력.
    
    (C에서는 `(int)c.coef[i]` 라고 써야 맞음.)
    

### 8. mult 함수 정의

```c
polynomial mult(polynomial A, polynomial B)
{
    polynomial C;
    int i, j;

    for (i = 0; i < A.degree + B.degree + 1; i++)
        C.coef[i] = 0;

    C.degree = A.degree + B.degree;

    for (i = 0; i < A.degree + 1; i++)
        for (j = 0; j < B.degree + 1; j++)
            C.coef[i + j] += A.coef[i] * B.coef[j];

    return C;
}
```

### (1) 배열 초기화

```c
for (i = 0; i < A.degree + B.degree + 1; i++)
    C.coef[i] = 0;
```

- 곱셈하면서 계수를 더할 거라서, 미리 0으로 초기화
- 뜻 : 결과 배열 C의 모든 칸을 0으로 비워라.

### (2) 결과 차수

```c
C.degree = A.degree + B.degree;
```

- 다항식 곱하면 차수가 합쳐짐. (ex : 4차 x 2차 = 6차)
- 뜻 : 결과 다항식은 A 차수 + B 차수다

### (3) 곱셈 로직 (중첩 반복)

```c
for (i = 0; i < A.degree + 1; i++)
    for (j = 0; j < B.degree + 1; j++)
        C.coef[i + j] += A.coef[i] * B.coef[j];
```

- 모든 항을 하나씩 곱해서 결과에 더해야 함.
- 뜻 :
    - `A`의 i번째 항 × `B`의 j번째 항 → 결과는 **(i+j)번째 항**에 더한다.
    - 예: A의 `a₂x²` × B의 `b₁x¹` = `(a₂·b₁)x³`
        
        → 결과 C의 coef[3]에 더한다.
        
- 비유하자면 두 탑(다항식)을 곱하면 층수(i+j)에 블록이 쌓이는 것. 층수에 맞는 칸(C.coef[i+j])에 블록 개수를 더해준다.

### 9. 최종 결과

실제로 A(x)*B(x)를 하면

```c
C(x) = 12x^6 + 17x^5 + 35x^4 + 20x^3 + 14x^2
```

배열 형태로 :

```c
c.degree = 6
c.coef = [0, 0, 14, 20, 35, 17, 12]
```

출력 :
'''c
6차 0 0 14 20 35 17 12
'''