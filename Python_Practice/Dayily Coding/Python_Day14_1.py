# 가위 바위 보 게임
# 가위, 바위, 보를 문자로 입력받는다.
# if문 없이 프로그램을 작성하라.
import random

choice = ["가위", "바위", "보"]
user = input("가위, 바위, 보를 선택하세요:")
computer = random.choice(choice)

p = choice.index(user)
c = choice.index(computer)

result = (p-c)%3

match = ["비겼습니다.", "이겼습니다.", "졌습니다."]
print(match[result])
