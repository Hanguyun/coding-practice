# set 연습문제
import random

# 1. 두 자리수 정수 5개로 이루어진 set를 만들어라(중복 허용)
num1 = set(random.choices(range(10,100), k=5))
print("1.", num1)

# 2. 두 자리수 정수 5개로 이루어진 set를 2개를 만들고 합집합을 구하라
num2 = set(random.choices(range(10,100), k=5))
num3 = set(random.choices(range(10,100), k=5))
hap = num2 | num3
print("2.", hap)                 # 합집합 |

# 3. 2번의 결과를 원소의 개수를 구하라
print("3.", len(hap))

# 4. 2번의 결과에 10을 원소로 추가하라
hap.add(10)
print("4.", hap)

# 5. 두 자리수 정수 5개로 이루어진 set를 2개 만들고 교집합을 구하라
num4 = set(random.choices(range(10,100), k=5))
num5 = set(random.choices(range(10,100), k=5))
print("5.", num4 & num5)         # 교집합 &

# 6. 두 자리수 정수 5개로 이루어진 set를 2개 만들고 상대 set를 뺀 차집합을 구하라
num6 = set(random.choices(range(10,100), k=5))
num7 = set(random.choices(range(10,100), k=5))
a_b = num6 - num7                 # 차집합 -
b_a = num7 - num6
print("6. num6 - num7", a_b)
print("6. num7 - num6", b_a)

# 7. 서로소 검사
print("7-1. num6 과 (num7 - num6) 서로소 검사:", num6.isdisjoint(b_a))
print("7-2. num7 과 (num6 - num7) 서로소 검사:", num7.isdisjoint(a_b))
print("7-3. (num6 - num7) 과 (num7 - num6) 서로소 검사:", a_b.isdisjoint(b_a))
