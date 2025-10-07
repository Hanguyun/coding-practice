# 집합 응용 --- 최대, 최소, 평균, 조건 검사
# 1~100 사이의 랜덤한 정수 10개로 이루어진 집합 C를 만든다 그 후 다음을 수행하라
# 1. C의 최댓값(max), 최솟값(min), 평균(mean)을 각각 구하고 출력하라.
# 2. 평균보다 큰 수만 모은 집합 high, 평균보다 작은 수만 모은 집합 low를 만들어라.
# 3. high와 low의 원소 개수를 각각 구하라.
# 4. high와 low가 서로소인지 검사하라.
# 5. high와 low의 합집합이 C와 같은지 확인하라.
# 6. high와 low의 평균값 중 어느 쪽이 더 큰지도 출력하라

import random

C = random.sample(range(1,101), k = 10)
max_value = max(C)
min_value = min(C)
mean = sum(C) / len(C)

high = []
low = []
for i in C :
    if mean < i :
        high.append(i)
    else :
        low.append(i)

average_high = sum(high) / len(high)
average_low = sum(low) / len(low)

print("1. 최댓값, 최솟값, 평균 :", max_value, min_value, mean)
print("2.", high, low)
print("3.", len(high), len(low))
print("4.", set(high).isdisjoint(set(low)))
print("5.", set(high).union(set(low)) == set(C))

if average_high < average_low :
    print("6. average_low")
else :
    print("6. average_high")