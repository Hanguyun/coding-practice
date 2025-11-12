# 중첩 for문을 사용한 1~100까지 소수 구하기

for x in range(2, 101):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            break
    else:
        print("%d" % x, end=" ")
