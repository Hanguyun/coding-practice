# 집합 응용 --- 짝수, 홀수 의 합 비교
# 1~50 사이의 랜덤한 정수 10개로 이루어진 집합 C를 만든다.
# 집합 C의 원소 중 각각 짝수, 홀수만 모아 even, odd 집합을 만든다.
# 1. even, odd 각각의 합을 구하고 출력하라.
# 2. even의 합 + odd의 합이 C의 모든 원소의 합과 같은지 검사하라.
# 3. even과 odd 중 어느 쪽 합이 더 큰지도 출력하라
# 4. C의 평균보다 큰 수들만 모아 새 집합 high를 만들어라.
# 5. high 원소 개수와 내용을 출력하라.

import random

C = set(random.sample(1,51), k = 10)
even = []
odd = []

for i in C :
	if i % 2 == 0 :
		even.append(i)
	else :
		odd.append(i)

print ("1.", even.append.(odd))
