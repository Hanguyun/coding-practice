import random
import copy

choice = ['A',2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,'J','Q','K']
result = []
count = 0
while True:
    print(f"게임을 시작합니다.\n카드를 뽑겠습니다.")

    ai = [random.choice(choice) for i in range(2)] # ai 카드를 choice에서 랜덤으로 2개 뽑기
    user = [random.choice(choice) for i in range(2)] # user 카드를 choice에서 랜덤으로 2개 뽑기

    print(f"AI 공개 카드:{ai[0]} user 카드:{user}")  # ai 카드 한 장 보여주고 user 카드를 모두 보여주기
    if 'A' in user : # user 리스트 안에 A가 있는지 확인 후 실행
        a = input(f"A가 뽑혔습니다. 1 또는 10으로 사용가능 합니다. 어떤 숫자를 사용하시겠습니까? 1 또는 10 둘 중 하나를 고르시오:")
        if a == '10': # A를 리스트에서 삭제 후 10으로 변환
            user.remove('A')
            user.append('A: 10')
        elif a == '1' : # A를 리스트에서 삭제 후 1로 변환
            user.remove('A')
            user.append('A: 1')

    result_user = copy.deepcopy(user) # user리스트를 result에 깊은 복사를 이용하여 복사
    result_ai = copy.deepcopy(ai)

    if 'J' in result_user or 'J' in result_ai: # J,Q,K가 있다면 삭제하고 10 추가
        if 'J' in result_user:
            result_user.remove('J')
            result_user.append(10)
        if 'J' in result_ai:
            result_ai.remove('J')
            result_ai.append(10)
    if 'Q' in result_user or 'Q' in result_ai:
        if 'Q' in result_user:
            result_user.remove('Q')
            result_user.append(10)
        if 'Q' in result_ai:
            result_ai.remove('Q')
            result_ai.append(10)
    if 'K' in result_user or 'K' in result_ai:
        if 'K' in result_user:
            result_user.remove('K')
            result_user.append(10)
        if 'K' in result_ai:
            result_ai.remove('J')
            result_ai.append(10)

    if 'A: 1' in result : # user리스트에 'A: 1'이 있다면 삭제하고 1 추가
        result.remove('A: 1')
        result.append(1)
    elif 'A: 10' in result : # user리스트에 'A: 10'이 있다면 삭제하고 10 추가
        result.remove('A: 10')
        result.append(10)

    result = sum(result)
    print(f"AI 공개 카드:{ai[0]} user 카드:{user} 유저 합산:{result_user}") # ai 카드 한 장 보여주고 user 카드와 합산 보여주기
    break

while count == 5:
    while True:
        if result < 21 : # 21점 미만이면 게임을 더 할건지 안 할건지 묻기
            go = int(input(f"카드를 한 장 더 뽑겠습니까? 1 카드 뽑기 0 게임 종료:"))
            if go == 1 :
                count += 1
                ai_2 = [random.choice(choice)]  # ai 카드를 choice에서 랜덤으로 뽑기
                user_2 = [random.choice(choice)]  # user 카드를 choice에서 랜덤으로 뽑기
                ai = ai.append(ai_2) # ai가 추가로 뽑은 카드를 ai에 추가
                user = user_2.append(user_2) # user가 추가로 뽑은 카드를 user에 추가
#-----------------------------------------------------------------------------------------------            
            elif 'A' in user:  # user 리스트 안에 A가 있는지 확인 후 실행
                a = input(f"A가 뽑혔습니다. 1 또는 10으로 사용가능 합니다. 어떤 숫자를 사용하시겠습니까? 1 또는 10 둘 중 하나를 고르시오:")
                if a == '10':  # A를 리스트에서 삭제 후 10으로 변환
                    user.remove('A')
                    user.append('A: 10')
                elif a == '1':  # A를 리스트에서 삭제 후 1로 변환
                    user.remove('A')
                    user.append('A: 1')

                if 'J' in result_user or 'J' in result_ai:  # J,Q,K가 있다면 삭제하고 10 추가
                    if 'J' in result_user:
                        result_user.remove('J')
                        result_user.append(10)
                    if 'J' in result_ai:
                        result_ai.remove('J')
                        result_ai.append(10)
                if 'Q' in result_user or 'Q' in result_ai:
                    if 'Q' in result_user:
                        result_user.remove('Q')
                        result_user.append(10)
                    if 'Q' in result_ai:
                        result_ai.remove('Q')
                        result_ai.append(10)
                if 'K' in result_user or 'K' in result_ai:
                    if 'K' in result_user:
                        result_user.remove('K')
                        result_user.append(10)
                    if 'K' in result_ai:
                        result_ai.remove('J')
                        result_ai.append(10)
# -----------------------------------------------------------
            elif go == 0 : # 카드를 그만 받으면 출력
                print(f"AI 카드:{ai} AI 합산:{result_ai} user 카드:{user} 유저 합산:{result_user}")
            
            elif result_user >= 22 :
                    print(f"AI: {ai}로 AI 승리!")
                    break
            elif result_user == 21 :
                    print(f"AI 카드:{ai} AI 합산:{result_ai} user 카드:{user} USER가 21점으로 승리")
                    break
            elif result_user == result_ai :
                print(f"AI 카드:{ai} AI 합산:{result_ai} user 카드:{user} 비겼습니다.")
        elif result_user <= 17 :
            choice
            
