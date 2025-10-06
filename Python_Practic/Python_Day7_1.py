import random

C = random.sample(range(1, 51), k=10)  # 1~50 중 중복 없이 10개
even = []
odd = []

for x in C:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

even_sum = sum(even)
odd_sum  = sum(odd)
total_sum = sum(C)


same_total = (even_sum + odd_sum == total_sum)


if even_sum > odd_sum:
    bigger = "짝수의 합이 더 큽니다."
elif even_sum < odd_sum:
    bigger = "홀수의 합이 더 큽니다."
else:
    bigger = "짝수의 합과 홀수의 합이 같습니다."


avg = total_sum / len(C)
high = [x for x in C if x > avg]

print("C =", sorted(C))
print("even =", sorted(even), "합 =", even_sum)
print("odd  =", sorted(odd),  "합 =", odd_sum)
print("전체 합과 비교:", same_total)
print(bigger)
print("평균 =", round(avg, 2))
print("평균보다 큰 수 =", sorted(high), "개수 =", len(high))
