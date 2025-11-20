import random

dice = [1, 2, 3, 4, 5, 6]  # 주사위 눈금을 랜덤으로 뽑기위한 리스트

print("게임을 시작합니다!")

user = random.choices(dice, k=5)  # for문을 이용한 주사위 던지기 시작 1번 던지고 시작

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
ai = random.choices(dice, k=5) # ai도 마찬가지로 1번 던지고 시작

for i in range(2) : # 컴퓨터도 사용자와 마찬가지로 주사위를 3번 던지기 가능 처음 주사위를 던지고 시작 그래서 2번 반복
    if len(set(ai)) == 1 : # 중복이 되지 않는 세트의 특징을 이용하여 중복 제거가 되어 값이 1개만 남는다면 모든 값이 같다
        break # 룰 = 5개의 주사위의 숫자가 모두 같다면 더 이상 던지지 않는다.
    elif len(set(ai)) == len(ai) : # 중복이 되지 않는 세트의 특징을 이용 중복 제거가 되지 않아 값이 5개일 경우 조건 성립
        ai.sort() # 룰 = 높은 수 두 개를 고정하고 나머지 주사위 3개를 돌리기 위해 오름차순 정렬
        del ai[0,1,2] # 룰 = 오름차순 정렬 후 높은 수 2개 고정 후 0, 1, 2 제거
        ai_reroll = random.choices(dice, k=3) # 주사위 3개 다시 돌리기 ai_reroll 변수에 저장
        ai.append(ai_reroll) # ai_reroll 변수에 있던 정수를 ai 덱에 삽입
    elif len(ai) != len(set(ai)) : # ai(리스트) ai(세트)와 같지 않다면 즉 리스트는 중복 되면 사라지지 않지만 세트는 중복 불가라서 중복이 되면 숫자가 줄어든다 그렇다면 같지 않다가 성립 되면 중복되는 숫자가 있다는 뜻
        
                

print(f"현재 패 :{user}")
print(f"ai 패 :{ai}")

# 비교할때 가중치? 5개가 같으면 뭐 나왔는지 체킹 상대가 5개가 동일하지 않다면 바로 패배
# 같은게 4개 나왔는데 상대가 3개 나오면 이김
