# 시험대비 기초(반복문) 복습
# 1. 0이 입력될 때까지의 숫자를 입력받아 입력받은 숫자의 합과 평균을 출력하는 프로그램을 작성하시오.
# hap = 0
# average = 0
# count = 0
# while True :
#     a = int(input("숫자를 입력하세요(0이 입력되면 종료):"))
#     if a == 0 :
#         break
#     count += 1
#     hap += a
#     average = hap/count
#     print(f"합:{hap} 평균:{average}")
#------------------------------------------------------------------------
# 2. 0이 입력될 때 까지의 숫자를 입력받아 홀수와 짝수로 나누고,
#    각각을 크기순으로 출력 후 각각의 합ㄱ과 평균을 출력하는 프로그램을 작성하시오.
# odd = []
# even = []
# hap = 0
# average = 0
# count = 0
# while True :
#     a = int(input("숫자를 입력하세요(0이 입력되면 종료):"))
#     if a == 0 :
#         break
#     elif a % 2 == 0 :
#         even.append(a)
#     else :
#         odd.append(a)
#     count += 1
#     hap += a
#     average = hap/count
# even.sort()
# odd.sort()
# print(f"짝수 크기순{even} 홀수 크기순{odd}")
# print(f"합 {hap} 평균 {average}")
# --------------------------------------------------------------------
# 3. 몇 개의 숫자를 입력받을 것인지 숫자를 입력받고,
# 입력된 개수의 숫자를 입력받아 크기순으로 출력하는 프로그램을 작성하시오.
# suja = int(input("숫자 개수를 입력하세요:"))
# number = []
# for i in range(suja):
#     num = int(input("숫자를 입력하세요:"))
#     number.append(num)
# a = sorted(number)
# b = sorted(number, reverse=True)
# print(f"오름차순{a}")
# print(f"내림차순{b}")
#----------------------------------------------------------------------
# import random
#
# choice = ["가위", "바위", "보"]
# result_text = ["비겼습니다", "이겼습니다", "졌습니다"]
#
# while True:
#     user = input("가위, 바위, 보 중에 선택하세요: ")
#     ai = random.choice(choice)
#
#     u = choice.index(user)
#     a = choice.index(ai)
#     res_index = (u - a) % 3
#
#     print(f"user: {user}, ai: {ai} -> {result_text[res_index]}")
#
#     if res_index != 0:
#         attacker = ["AI", "USER"][res_index == 1]
#         print(f"공격자는 {attacker} 입니다.")
#         break
#
# while True:
#     user = input("묵(바위), 찌(가위), 빠(보) 중 하나를 입력하세요: ")
#     ai = random.choice(choice)
#
#     u = choice.index(user)
#     a = choice.index(ai)
#     res_index = (u - a) % 3
#
#     print(f"user: {user}, ai: {ai} -> {result_text[res_index]}")
#
#     if user == ai:
#         print(f"{attacker} 승리! 게임 종료!")
#         break
#
#     attacker = ["AI", "USER"][res_index == 1]
#     print(f"공격자가 {attacker}로 바뀝니다!")
#--------------------------------------------------------------------------------
# 5. 컴퓨터와 up/down 게임을 하는 프로그램을 작성하시오
# 컴퓨터는 0~100 사이의 정수를 사용자에게 보이지 않게 정한다.
# 사용자는 컴퓨터의 숫자를 추측하여 입력하고 숫자가 크면 up, 작으면 down을 출력한다.
# 사용자가 숫자를 맞추면 몇 번만에 맞추었는지 출력한다.
# import random
# hap = 0
# computer = random.choice(range(1, 101))
# while True :
#     user = int(input("숫자를 입력하세요:"))
#     hap += 1
#     if user == computer:
#         print(f"{hap}번 만에 맞췄습니다.")
#         break
#     elif user > computer:
#         print("Down")
#     else :
#         print("Up")