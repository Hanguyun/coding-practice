/*#include<stdio.h>                                           // 1�� - �� ���׽��� ������ ���ϴ� �Լ� sub()�� �����϶�. �ڵ� 2.7�� add()�� �����Ͽ� ������ ���� ������,
#define MAX_DEGREE 1001                            // ���� ���������� ���� c = a-b = a+(-b) ���踦 �̿��� �����϶�.
#define MAX_NEGATE 1001                           // �̸� ���� ���� negate() �Լ��� �����ؾ� �� ���̴�.
typedef struct                                               // Polynomial negate( Polynomial p);     // -p�� ���� ��ȯ�ϴ� �Լ�
{                                                                      // Polynomial negate sub( Polynomial a, Polynomial b);               // a-b�� ���� ��ȯ�ϴ� �Լ�
    int degree, negate;
    float coef[MAX_DEGREE];
    float coef2[MAX_NEGATE];                          // 2�� - �� ���׽��� ��(c = a * b)�� ���ϴ� �Լ� mult()�� �����϶�.
} Polynomial;                                                   // Polynomial negate smult( Polynomial a, Polynomial b);

int degree(Polynomial p)                              // 3�� - ���׽��� ����Լ� print_poly()�� �����Ͽ� ����� 0�� ���� ��µ��� �ʵ��� �����϶�
{                                                                     // ���� ����� 1�� ��쿡�� 1�� ��µ��� �ʵ��� �����϶�.
    return 0;                                                   // void print_poly( Polynomial p, char str[]);
}
int negate(Polynomial p) // 1��
{
    return 0;
}                                                                    // [��ȭ ����] ���׽��� ���� ��� �ְ������� ����� 0���� ���� �� �ִ�.
float coefficient(Polynomial p, int i)               // �ְ������� ����� 0�̸� ���׽��� ������ �ٿ� �ְ������� 0�� �ƴ� ����� ������ ���׽��� �����ϴ� �Լ� trim()�� �����϶�.
{                                                                    // �� �Լ��� �Ű������δ� �ݵ�� ���������� ����ؾ��Ѵ�.
    return p.coef[i], p.coef2[i];                                       // �����ʹ� 5�忡�� �ڼ��� �ٷ�µ�, �̸� �����ؼ� �����͸� ����ؾ��ϴ� ������ ������ ����.
}                                                                   // void trim( Polynomial* p );     // p�� ����Ű�� ���׽��� �����ϴ� �Լ�.
float evaluate(Polynomial p, float x)
{
    float result = p.coef[0] && p.coef2[0];
    float mul = 1;
    for (int i = 1; i <= p.degree; i++) {
        mul *= x;
        result += p.coef[i] && p.coef2[i] * mul;
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
Polynomial sub(Polynomial a, Polynomial b)  // 1�� �� ���׽Ŀ� ������ ���ϴ� �ڵ�
{
    Polynomial p;
    p.negate = (a.negate > b.negate) ? a.negate : b.negate;

    for (int i = 0; i <= p.negate; i++)
        p.coef2[i] = ((i <= a.negate) ? a.coef2[i] : 0)
                      - ((i <= b.negate) ? b.coef2[i] : 0);
    return p;
}

void print_poly(Polynomial p, char str[])
{
    printf(" %s", str);
    for (int i = p.degree; i > 0; i--)
        printf("%5.1f x^%d + ", p.coef[i], i);
    printf("%4.1f\n", p.coef[0]);
}
void main()
{
    Polynomial a = { 5, { 3, 6, 0, 0, 0, 10} };
    Polynomial b = { 4, { 7, 0, 5, 0, 1} };
    Polynomial c = add(a, b);
    Polynomial d = sub(a, b);
    print_poly(a, " A = ");
    print_poly(b, " B = ");
    print_poly(c, "A+B = ");
    print_poly(d, "A-B = ");
    printf("A(1)= %f\n", evaluate(a, 1.0f));
    printf("B(2)= %f\n", evaluate(b, 2.0f));
}
*/
