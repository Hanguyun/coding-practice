import random

dice = [1, 2, 3, 4, 5, 6]  # 주사위 눈금을 랜덤으로 뽑기위한 리스트

print("게임을 시작합니다!")

user = random.choices(dice, k=5)  # for문을 이용한 주사위 던지기 시작 5번 1번 던짐

for i in range(2) : # 사용자가 총 3번을 던질 수 있게 만듦 첫 번재는 던졌기 때문에 for문으로 2번 더 던지게 만듦
    reroll_count = int(input(f"현재 패: {user} 몇 개를 다시 던지겠습니까? 0은 리롤 종료(0~5) :"))  # 주사위를 다시 던지는 횟수를 입력받아 변수에 저장
    if reroll_count == 0:
        break
    for i in range(reroll_count): # 주사위를 던지는 횟수를 입력 받아서 for문으로 반복해서 던지기
        reroll_position = int(input(f"현재 패: {user} 몇 번째를 다시 던지겠습니까? (1~5) :"))  # 지금 가지고 있는 패를 확인하고 몇 번째를 다시 던질지를 입력받아 변수에 저장
        user_reroll = random.choice(dice)  # reroll_count 만큼 주사위 던지기
        reroll_position -= 1 # 인덱스는 0부터 시작이기 때문에 -1 적용
        del user[reroll_position] # user에 있는 리스트 즉 현재 패에서 reroll_position -1을 적용한 인덱스를 제거
        user.append(user_reroll) # 제거 후 user_reroll로 뽑은 주사위를 다시 현재 패에 삽입

#---------------------------------컴퓨터---------------------------------------------------
ai = random.choices(dice, k=5) # ai도 마찬가지로 주사위 5개를 던지고 시작


print(f"현재 패 :{user}")
print(f"ai 패 :{ai}")
