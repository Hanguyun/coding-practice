#include<stdio.h>                                           // 1�� - �� ���׽��� ������ ���ϴ� �Լ� sub()�� �����϶�. �ڵ� 2.7�� add()�� �����Ͽ� ������ ���� ������,
#define MAX_DEGREE 1001                            // ���� ���������� ���� c = a-b = a+(-b) ���踦 �̿��� �����϶�.  // �̸� ���� ���� negate() �Լ��� �����ؾ� �� ���̴�.
typedef struct                                               // Polynomial negate( Polynomial p);     // -p�� ���� ��ȯ�ϴ� �Լ�
{                                                                      // Polynomial negate sub( Polynomial a, Polynomial b);               // a-b�� ���� ��ȯ�ϴ� �Լ�
    int degree;
    float coef[MAX_DEGREE];                            // 2�� - �� ���׽��� ��(c = a * b)�� ���ϴ� �Լ� mult()�� �����϶�.
} Polynomial;                                                   // Polynomial negate smult( Polynomial a, Polynomial b);

int degree(Polynomial p)                              // 3�� - ���׽��� ����Լ� print_poly()�� �����Ͽ� ����� 0�� ���� ��µ��� �ʵ��� �����϶�
{                                                                     // ���� ����� 1�� ��쿡�� 1�� ��µ��� �ʵ��� �����϶�.
    return 0;                                                   // void print_poly( Polynomial p, char str[]);
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
Polynomial negate(Polynomial p)                  // 1��
{
    Polynomial j = p;
     j.degree = p.degree;
     for (int i = 0; i <= p.degree; i++) {
        j.coef[i] = -p.coef[i];
    }
    return j;
}
Polynomial sub(Polynomial a, Polynomial b) {                //1��
    Polynomial nb = negate(b);
    return add(a, nb);
}
Polynomial mult(Polynomial a, Polynomial b)                                      // 2�� //3��
{
    Polynomial p = {0};                    // p�ʱ�ȭ ���� �ʾƼ� ������ ���� ����.
    int i, j;

    for (i = 0; i < a.degree + b.degree + 1; i++) {
        p.degree = a.degree + b.degree;
    }
    for (i = 0; i < a.degree + 1; i++) {
        for (j = 0; j < b.degree + 1; j++) {
            p.coef[i + j] += a.coef[i] * b.coef[j];
        }
    }
    return p;
}

//Polynomial trim(Polynomial a, Polynomial b) {
//    int i = p->degree;
//
//    while (i > 0)
//
//}


void print_poly(Polynomial p, char str[])
{
    printf(" %s", str);
    for (int i = p.degree; i > 0; i--)
        printf("%5.1f x^%d + ", p.coef[i], i);
    printf("%4.1f\n", p.coef[0]);
}

void print_poly2(Polynomial p, char str[])           //1��
{
    printf(" %s", str);
    for (int i = p.degree; i > 0; i--)
        printf("%5.1f x^%d + ", p.coef[i], i);
    printf("%4.1f\n", p.coef[0]);
}

void print_poly3(Polynomial p, char str[])
{
    printf(" %s", str);
    for (int i = p.degree; i > 0; i--)
         if(p.coef[i] != 0)
        printf("%5.1f x^%d + ", p.coef[i], i);
    printf("%4.1f\n", p.coef[0]);

}

void main()
{
    Polynomial a = { 5, { 3, 6, 0, 0, 0, 10} };
    Polynomial b = { 4, { 7, 0, 5, 0, 1} };
    Polynomial c = add(a, b);
    Polynomial d = sub(a, b);
    Polynomial e = mult(a, b);
    //Polynomial f = trim(a, b);
    print_poly(a, " A = ");
    print_poly(b, " B = ");
    print_poly(c, "A+B = ");
    print_poly2(d, "1�� ���� A-B = ");
    print_poly3(e, "2, 3�� ���� A*B = ");
    //print_poly(f, "4�� �ְ����� ���� �� E =")
    //print_poly(f, "4�� �ְ����� ���� �� E =")
    printf("A(1)= %f\n", evaluate(a, 1.0f));
    printf("B(2)= %f\n", evaluate(b, 2.0f));
}


