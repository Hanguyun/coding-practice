# 시험대비 기초(세트) 복습

import random
num = set(random.choices(range(10,101),k=5))
print(f"문제 1번 {num}")

num2 = set(random.choices(range(10,101),k=5))
num3 = set(random.choices(range(10,101),k=5))
hap = num2 | num3
print(f"문제 2번 {hap}")

print(f"문제 3번 {len(hap)}")

hap.add(10)
print(f"문제 4번 {hap}")

num4 = random.choices(range(10,101),k=5)
num5 = random.choices(range(10,101),k=5)
Inter = num4 & num5
print(f"문제 5번 {Inter}")

num6 = random.choices(range(10,101),k=5)
num7 = random.choices(range(10,101),k=5)
Diff = num6 - num7
Diff2 = num7 - num6
print(f"문제 6번 {Diff} {Diff2}")

print(f"문제 7번 {Diff.isdisjoint(Diff2)}, {Diff2.isdisjoint(Diff)}")
