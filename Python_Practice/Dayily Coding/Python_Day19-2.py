# 시험대비 기초(리스트) 복습

import random

num = random.sample(range(10,101),k=5)
print(f"1. {num}")

num2 = random.sample(range(10,101),k=5)
num3 = random.sample(range(10,101),k=5)
num2_num3 = num2.append(num3)
print(f"2. {num2_num3}")

print(f"3. {num2_num3.sort()}")

print(f"4. {num2_num3.sort(revers=True)}")

del num2_num3[4]
print(f"5. {num2_num3}")

num2_num3.append(10)
print(f"6. {num2_num3}")

print(f"7. {num2_num3.count(20)}")

print(f"8. {random.shuffle(num2_num3)}")