# 조건문을 사용하여 랜덤 가위바위보 프로그램을 작성하시오.
import random
player = input("가위, 바위, 보 중 하나를 입력하세요. :")

choices = ["가위", "바위", "보"]
computer = random.choice(choices)

if player == computer :
    print("비겼습니다.")
elif (player == "가위" and computer == "보") or \
     (player == "바위" and computer == "가위") or \
     (player == "보" and computer == "바위") :
    print("플레이어", player, "승!. 컴퓨터", computer, "패!")
else :
    print("플레이어", player, "패! 컴퓨터", computer, "승!")