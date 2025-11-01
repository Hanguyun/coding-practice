/*#include<stdio.h>                                           // 1�� - �� ���׽��� ������ ���ϴ� �Լ� sub()�� �����϶�. �ڵ� 2.7�� add()�� �����Ͽ� ������ ���� ������,
#define MAX_DEGREE 1001                            // ���� ���������� ���� c = a-b = a+(-b) ���踦 �̿��� �����϶�.                      // �̸� ���� ���� negate() �Լ��� �����ؾ� �� ���̴�.
#define MAX_NEGATE 1001
typedef struct                                               // Polynomial negate( Polynomial p);     // -p�� ���� ��ȯ�ϴ� �Լ�
{                                                                      // Polynomial negate sub( Polynomial a, Polynomial b);               // a-b�� ���� ��ȯ�ϴ� �Լ�
    int degree;
    float coef[MAX_DEGREE];                        // 2�� - �� ���׽��� ��(c = a * b)�� ���ϴ� �Լ� mult()�� �����϶�.
} Polynomial;                                                   // Polynomial negate smult( Polynomial a, Polynomial b);

typedef struct
{
    int negate;
    float coef2[MAX_NEGATE];
} Polynomial2;

int degree(Polynomial p)                              // 3�� - ���׽��� ����Լ� print_poly()�� �����Ͽ� ����� 0�� ���� ��µ��� �ʵ��� �����϶�
{                                                                     // ���� ����� 1�� ��쿡�� 1�� ��µ��� �ʵ��� �����϶�.
    return 0;                                                   // void print_poly( Polynomial p, char str[]);
}

int negate(Polynomial2 p)
{
    return 0;
}
                                                                        // [��ȭ ����] ���׽��� ���� ��� �ְ������� ����� 0���� ���� �� �ִ�.
float coefficient(Polynomial p, int i)               // �ְ������� ����� 0�̸� ���׽��� ������ �ٿ� �ְ������� 0�� �ƴ� ����� ������ ���׽��� �����ϴ� �Լ� trim()�� �����϶�.
{                                                                    // �� �Լ��� �Ű������δ� �ݵ�� ���������� ����ؾ��Ѵ�.
    return p.coef[i];                                       // �����ʹ� 5�忡�� �ڼ��� �ٷ�µ�, �̸� �����ؼ� �����͸� ����ؾ��ϴ� ������ ������ ����.
}                                                                   // void trim( Polynomial* p );     // p�� ����Ű�� ���׽��� �����ϴ� �Լ�.
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
    print_poly(c, "1 �� ���� : A-B = ");
    printf("A(1)= %f\n", evaluate(a, 1.0f));
    printf("B(2)= %f\n", evaluate(b, 2.0f));
}*/
