# 함수를 이용한 묵찌빠 5판 3선승제

import random
aw = 0
uw = 0
choice = ['가위', '바위', '보']
outcomes = ["비겼습니다", "이겼습니다", "졌습니다"]

def RCP(user, ai) :
    u = choice.index(user)
    a = choice.index(ai)
    result = (u - a) % 3
    print(f"user : {user}, Ai: {ai} -> {outcomes[result]}")

    return result

while aw < 3 or uw < 3 :
    while True :
        user = input("가위,바위,보 중에 선택하세요:")
        ai = random.choice(choice)

        result = RCP(user, ai)


        if result != 0 :
            attacker = ["AI", "USER"][result == 1]
            print(f"공격자는 {attacker} 입니다.")
            break

        while True :
            user = input("묵(바위), 찌(가위), 빠(보) 중 하나를 입력하세요: ")
            ai = random.choice(choice)

            result = RCP(user, ai)

            if user == ai :
                print(f" {attacker} 승리!")
                if attacker == "USER" :
                    uw = uw + 1
                elif attacker == "AI" :
                    aw = aw + 1
                break

            attacker = ["AI", "유저"][result == 1]
            print(f"공격자가 {attacker}로 바뀝니다!")
