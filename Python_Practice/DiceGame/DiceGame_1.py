import random

dice = [1, 2, 3, 4, 5, 6] # 주사위 눈금을 랜덤으로 뽑기위한 리스트

print("게임을 시작합니다!")

user = [random.choices(dice) for i in range(5)] # for문을 이용한 주사위 던지기 시작 5번

reroll_count = int(input(f"현재 패: {user} 몇 개를 다시 던지겠습니까? (1~2) :")) # 주사위를 다시 던지는 횟수를 입력받아 변수에 저장
reroll_position = int(input(f"현재 패: {user} 몇 번째를 다시 던지겠습니까? (1~5) :"))  # 지금 가지고 있는 패를 확인하고 몇 번째를 다시 던질지를 입력받아 변수에 저장

for i in range(reroll_count) :
    user_reroll = random.choice(dice) # reroll_count 만큼 주사위 던지기
    user_reroll -= 1
    del user[user_reroll]
    

print(user)
