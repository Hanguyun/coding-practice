# 1. 0이 입력될 때 까지의 숫자를 입력받아 입력받은 숫자의 합과 평균을 출력하는 프로그램을 작성하시오.
# hap = 0
# average = 0
# i = 0
# while True :
#     user = int(input("숫자를 입력하세요:"))
#     if user == 0 :
#         break
#     else :
#         i += 1
#         hap += user
#         average = user/i
#     print(f"합:{hap} 평균:{average}")

# 2. 0이 입력될 때 까지의 숫자를 입력받아 홀수와 짝수로 나누고,
# 각각을 크기순으로 출력 후 각각의 합과 평균을 출력하는 프로그램을 작성하시오.
# odd = []
# even = []
# hap = 0
# average = 0
# i = 0
# while True :
#     user = int(input("숫자를 입력하세요:"))
#     i += 1
#     hap += user
#     average = user/i
#     if user == 0 :
#         break
#     elif user % 2 == 0 :
#         even.append(user)
#     else :
#         odd.append(user)
#     print(f"합:{hap} 평균:{average} 홀수:{odd} 짝수{even}")

# 3. 몇 개의 숫자를 입력받을 것인지 숫자를 입력받고,
# 입력된 개수의 숫자를 입력받아 크기순으로 출력하는 프로그램을 작성하시오.
# suja = int(input("숫자 개수를 입력하세요:"))
# number = []
# for i in range(suja):
#     num = int(input("숫자를 입력하세요:"))
#     number.append(num)
# a = sorted(number)
# b = sorted(number, reverse=True)
# print(f"내림차순{a}")
# print(f"오름차순{b}")

# 4. 컴퓨터와 묵찌빠를 하는 프로그램을 작성하시오.
# import random
# user = input("묵, 찌, 빠를 선택하세요:")
# choice = ["묵", "찌", "빠"]
# win = 0
# lose = 0
# while True :
#     computer = random.choice(choice)
#     if user == computer:
#         print("첫 판이 비겼습니다!")
#     elif (user == "찌" and computer == "빠") or \
#          (user == "묵" and computer == "찌") or \
#          (user == "빠" and computer == "묵") :
#         if (user == "찌" and computer == "빠") or \
#             (user == "묵" and computer == "찌") or \
#             (user == "빠" and computer == "묵") :
#             print("player가 이겼습니다.")
#             win += 1
#             break
#     elif win == 1 :
#         break
#
#     elif (computer == "찌" and user == "빠") or \
#          (computer == "묵" and user == "찌") or \
#          (computer == "빠" and user == "묵") :
#         if (computer == "찌" and user == "빠") or \
#          (computer == "묵" and user == "찌") or \
#          (computer == "빠" and user == "묵") :
#             print("Player가 졌습니다.")
#             lose += 1
#             break
#     elif lose == 1 :
#         break

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

# 6. 8X8 체스판 위에 queen이 서로를 죽일 수 없는 자리에 위치하도록 하는 프로그램을 작성하여라.
# 2차원 리스트를 사용