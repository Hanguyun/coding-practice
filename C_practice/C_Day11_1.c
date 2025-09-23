/*#include<stdio.h>                                           // 1번 - 두 다항식의 뺄셈을 구하는 함수 sub()를 구현하라. 코드 2.7의 add()를 수정하여 구현할 수도 있지만,
#define MAX_DEGREE 1001                            // 앞의 문제에서와 같이 c = a-b = a+(-b) 관계를 이용해 구현하라.                      // 이를 위해 먼저 negate() 함수를 구현해야 할 것이다.
#define MAX_NEGATE 1001
typedef struct                                               // Polynomial negate( Polynomial p);     // -p를 구해 반환하는 함수
{                                                                      // Polynomial negate sub( Polynomial a, Polynomial b);               // a-b를 구해 반환하는 함수
    int degree;
    float coef[MAX_DEGREE];                        // 2번 - 두 다항식의 곱(c = a * b)을 구하는 함수 mult()를 구현하라.
} Polynomial;                                                   // Polynomial negate smult( Polynomial a, Polynomial b);

typedef struct
{
    int negate;
    float coef2[MAX_NEGATE];
} Polynomial2;

int degree(Polynomial p)                              // 3번 - 다항식의 출력함수 print_poly()를 수정하여 계수가 0인 항은 출력되지 않도록 변경하라
{                                                                     // 또한 계수가 1인 경우에는 1이 출력되지 않도록 변경하라.
    return 0;                                                   // void print_poly( Polynomial p, char str[]);
}

int negate(Polynomial2 p)
{
    return 0;
}
                                                                        // [심화 문제] 다항식의 연산 결과 최고차항의 계수가 0으로 변할 수 있다.
float coefficient(Polynomial p, int i)               // 최고차항의 계수가 0이면 다항식의 차수를 줄여 최고차항이 0이 아닌 계수를 갖도록 다항식을 정리하는 함수 trim()을 구현하라.
{                                                                    // 이 함수의 매개변수로는 반드시 포인터형을 사용해야한다.
    return p.coef[i];                                       // 포인터는 5장에서 자세히 다루는데, 이를 참고해서 포인터를 사용해야하는 이유를 생각해 보라.
}                                                                   // void trim( Polynomial* p );     // p가 가르키는 다항식을 정리하는 함수.
float evaluate(Polynomial p, float x)
{
    float result = p.coef[0];
    float mul = 1;
    for (int i = 1; i <= p.degree; i++) {
        mul *= x;
        result += p.coef[i] * mul;
    }
    return result;

    float evaluate(Polynomial2 p, float x)
{
    float result = p.coef2[0];
    float mul = 1;
    for (int i = 1; i <= p.negate; i++) {
        mul *= x;
        result += p.coef2[i] * mul;
    }
    return result;
}
Polynomial add(Polynomial a, Polynomial b)
{
    Polynomial p;
    p.degree = (a.degree > b.degree) ? a.degree : b.degree;

    for (int i = 0; i <= p.degree; i++)
        p.coef[i] = ((i <= a.degree) ? a.coef[i] : 0)
                      + ((i <= b.degree) ? b.coef[i] : 0);
    return p;
}

Polynomial2 sub(Polynomial2 a, Polynomial2 b)
{
    Polynomial2 p;
    p.negate = (a. > b.negate) ? a.negate : b.negate;

    for (int i = 0; i <= p.negate; i++)
        p.coef[i] = ((i <= a.negate) ? a.coef[i] : 0)
                      - ((i <= b.negate) ? b.coef[i] : 0);
    return p;
}

void print_poly(Polynomial p, char str[])
{
    printf(" %s", str);
    for (int i = p.degree; i > 0; i--)
        printf("%5.1f x^%d + ", p.coef[i], i);
    printf("%4.1f\n", p.coef[0]);
}

void print_poly(Polynomial2 p, char str[])
{
    printf(" %s", str);
    for (int i = p.negate; i > 0; i--)
        printf("%5.1f x^%d + ", p.coef[i], i);
    printf("%4.1f\n", p.coef[0]);
}

void main()
{
    Polynomial a = { 5, { 3, 6, 0, 0, 0, 10} };
    Polynomial b = { 4, { 7, 0, 5, 0, 1} };
    Polynomial c = add(a, b);
    Polynomial2 d = sub(a, b);
    print_poly(a, " A = ");
    print_poly(b, " B = ");
    print_poly(c, "A+B = ");
    print_poly(c, "1 번 문제 : A-B = ");
    printf("A(1)= %f\n", evaluate(a, 1.0f));
    printf("B(2)= %f\n", evaluate(b, 2.0f));
}*/
