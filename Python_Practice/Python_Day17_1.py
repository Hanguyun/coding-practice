# 묵찌빠 프로그램을 작성하시오.
import random
choice = ["가위","바위","보"]
result = ["비겼습니다", "이겼습니다", "졌습니다"]
while True :
    user = input("가위,바위,보 중에 선택하세요:")
    ai = random.choices(choice)

    u = choice.index(user)
    a = choice.index(ai)
    result = (u - a)%3

    print(f"user : {user}, Ai: {ai} -> {result[result]}")
    if result != 0 :
        attacker = ["AI", "USER"][result == 1]
        print(f"공격자는 {attacker} 입니다.")
        break

    while True :
        user = input("묵(바위), 찌(가위), 빠(보) 중 하나를 입력하세요: ")
        ai = random.choices(choice)

        u = choice.index(user)
        a = choice.index(ai)
        result = (u - a) % 3

        print(f"유저: {user}, AI : {ai} -> {result[result]}")

        if user == ai :
            print(f" {attacker} 승리! 게임 종료!")
            break

        attacker = ["AI", "유저"][result == 1]
        print(f"공격자가 {attacker}로 바뀝니다!")