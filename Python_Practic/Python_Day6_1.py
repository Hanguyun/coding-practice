# 1부터 100까지의 정수 중 랜덤하게 10개를 뽑아서 A 집합을 만들고, 또 다른 랜덤한 10개로 B 집합을 만들어라.
# 그 후 다음을 출력하시오.
# 1. A, B
# 2. 합집합
# 3. 교집합
# 4. 차집합 (A - B, B - A)
# 5. 서로소 여부 (isdisjoint() 사용)

import random

num1 = set(random.sample(range(10,100), k = 10))
num2 = set(random.sample(range(10,100), k = 10))
cha1 = num1.difference(num2)
cha2 = num2.difference(num1)

print ("1.", num1, num2)
print ("2.", num1.union(num2))
print ("3.", num1.intersection(num2))
print ("4.", cha1, cha2)
print ("5-1. num1와 (num1 - num2) 서로소 검사:", num1.isdisjoint(cha1))
print ("5-2. num2와 (num2 - num1) 서로소 검사:", num2.isdisjoint(cha2))
print ("5-3.(num1 -num2)와 (num2 - num1) 서로소 검사:", cha1.isdisjoint(cha2))
