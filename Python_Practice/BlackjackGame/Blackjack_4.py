import random # 난수 생성을 이용하기 위한 헤더
import copy # 깊은 복사 사용

choice = ['A',2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,'J','Q','K'] # 카드를 뽑기 위한 리스트
ai_A = [11, 1] # ai가 A를 뽑았을때 점수 랜덤 선택

ai = [random.choice(choice) for i in range(2)] # choice 리스트에서 초기 카드를 2개 뽑기
user = [random.choice(choice) for j in range(2)] # choice 리스트에서 초기 카드를 2개 뽑기


sum_user = copy.deepcopy(user)
sum_ai = copy.deepcopy(ai)

print("--------------------게임을 시작합니다--------------------")

#--------------------------------------------user 작동------------------------------------------------------------------
for c in range(len(sum_user)):
    if sum_user[c] in ['J', 'Q', 'K']:
        sum_user[c] = 10

if 'A' in sum_user:
    a = int(input(f"A가 뽑혔습니다. 1, 11 둘 중 하나를 고르시오:"))
    for i in range(len(sum_user)):
        if sum_user[i] == 'A':
            sum_user[i] = a

while True:
    user_score = sum(sum_user)
    print(f"USER 덱:{user} 현재 점수:{sum(user_score)}")
    drawing = int(input("카드를 더 뽑으시겠습니까? (0: 그만 뽑기, 1: 하나 더 뽑기): "))

    if user_score > 21:
        print("USER의 점수가 21을 초과했습니다. USER 패배")
        break

    if drawing == 0:
        print("카드 뽑기를 종료합니다.")

    elif drawing == 1:
        new_card = random.choice(choice)
        user.append(new_card)
        if new_card in ['J', 'Q', 'K']:
            sum_user.append(10)
        elif 'A' in sum_user:
            a = int(input(f"A가 뽑혔습니다. 1, 11 둘 중 하나를 고르시오:"))
            sum_user.append(a)
        else:
            sum_user.append(new_card)

#------------------------------------------------ai작동-----------------------------------------------------------------
while sum(sum_ai) >= 17:
    for k in range(len(sum_ai)):
        if sum_ai[k] in ['J', 'Q', 'K']:
            sum_ai[k] = 10

    while 'A' in sum_ai :
        sum_ai.remove('A')
        sum_ai.append(random.choice(ai_A))

#-----------------------------------------------------------------------------------------------------------------------
print(f"USER 덱:{user} 점수:{sum(sum_user)}")
print(f"AI 덱:{ai[0]} ??? 점수:???")
