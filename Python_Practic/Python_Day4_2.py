# 조건문을 사용하지 않고 가위바위보 프로그램을 작성하시오.
import random

choices = ["가위", "바위", "보"]
player = input("가위, 바위, 보 중 하나를 입력하세요. :")
computer = random.choice(choices)

p = choices.index(player)
c = choices.index(computer)

result = (p - c) % 3

outcomes = ["비겼습니다!", "플레이어 승!", "컴퓨터 승!"]
print(outcomes[result])