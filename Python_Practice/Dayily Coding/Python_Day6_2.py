# 1부터 50 사이의 랜덤한 정수 10개로 이루어진 집합 C를 만든다.
# 집합 C의 원소 중 짝수만 모아서 even 집합을 만들고, 홀수만 모아서 odd 집합을 만들어라
# 1. even과 odd의 원소 개수
# 2. even과 odd가 서로소인지 검사
# 3. even과 odd의 합집합이 C와 같은지 검사 (== 연산자 활용)

import random

C = random.sample(range(1,51), k = 10)
even = []
odd = []

for i in C :
  if i % 2 == 0 :
    even.append(i)
  else :
    odd.append(i)

print("1-1. 짝수의 개수:", len(even))
print("1-2. 홀수의 개수:", len(odd))
print("2-1. even, odd 서로소 검사:", set(even).isdisjoint(set(odd)))
print("2-2. odd, even 서로소 검사:", set(odd).isdisjoint(set(even)))
print("3. even과 odd의 합집합이 C와 같은지 검사", set(even).union(set(odd)) == set(C))
