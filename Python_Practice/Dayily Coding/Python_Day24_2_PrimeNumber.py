def PrimeNumber(user) :
    for x in range(2, user):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                break
        else:
            print("%d" % x, end=" ")
    return

PrimeNumber(int(input("정수를 입력하세요. :")))
