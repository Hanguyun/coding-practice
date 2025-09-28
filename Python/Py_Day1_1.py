#List 연습문제

# 1. 두 자리수 정수 5개로 이루어진 리스트를 만들어라(중복 불가)
import random
num1 = random.sample(range(0,100), 5)
print ("1.", num1)

# 2. 두 자리수 정수 5개로 이루어진 리스트를 2개를 만들고 두 리스트를 연접시켜라(중복 불가)
num2 = random.sample(range(0,100), 5)
num3 = random.sample(range(0,100), 5)
hap = num2 + num3
print ("2. ", hap)

# 3. 2번의 결과를 오름차순으로 정렬하라
hap.sort()
print ("3. ", hap)

# 4. 3번의 결과를 역순으로 정렬하라
hap.sort(reverse = True)
print ("4. ", hap)

# 5. 4번의 결과에서 index 5의 위치에 있는 원소를 삭제하라
del hap [5]
print ("5. ", hap)

# 6. 5번의 결과에 10을 원소로 추가하라
hap.append(10)
print ("6. ", hap)

# 7. 6번의 결과에서 20이 몇 개 있는지 찾아라
print ("7. ", hap, hap.count(20))

# 8. 7번의 결과에서 순서를 랜덤하게 섞어라(shuffle)
random.shuffle(hap)
print ("8. ", hap)
