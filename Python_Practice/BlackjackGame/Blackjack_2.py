import random # 난수 생성을 이용하기 위한 헤더
import copy # 깊은 복사를 이용하기 위한 헤더

choice = ['A',2 ,3 ,4 ,5 ,6 ,7 ,8 ,9 ,'J','Q','K'] # 카드를 뽑기 위한 리스트
ai_A = [10, 1] # ai가 A를 뽑았을때 점수 랜덤 선택
result_ai = [] # 총 합계를 구하기 위한 리스트
result_user = [] # 총 합계를 구하기 위한 리스트
count = 0

ai = [random.choice(choice) for i in range(2)] # choice 리스트에서 초기 카드를 2개 뽑기
user = [random.choice(choice) for i in range(2)] # choice 리스트에서 초기 카드를 2개 뽑기

result_user = copy.deepcopy(user) # user 리스트를 result_user에 깊은 복사를 이용하여 복사
result_ai = copy.deepcopy(ai) # com 리스트를 result_com에 깊은 복사를 이용하여 복사

print(f"AI 공개 카드:{ai[0]} user 카드:{user}")  # ai 카드 한 장 보여주고 user 카드를 모두 보여주기
if 'A' in user:  # user 리스트 안에 A가 있는지 확인 후 실행
    for i in range(2): # A가 두 번 뜰 수 있으므로 for문을 사용
        a = input(f"A가 뽑혔습니다. 1 또는 10으로 사용가능 합니다. 어떤 숫자를 사용하시겠습니까? 1, 10 둘 중 하나를 고르시오:")
        if a == '10':  # A를 리스트에서 삭제 후 10으로 변환
            user.remove('A')
            user.append('A: 10')
        elif a == '1':  # A를 리스트에서 삭제 후 1로 변환
            user.remove('A')
            user.append('A: 1')

if 'A' in ai :
    result_ai.remove('A')
    ai.append(random.choice(ai_A))

#---------------------------------------------------------------------------------
# J,Q,K가 있다면 삭제하고 10 추가 이 코드는 나중에 줄이기
# 지금은 일단 구동만
if 'J' in result_user or 'J' in result_ai:
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
#-------------------------------------------------------------------------------------
result_user = sum(result_user)
print(f"AI 공개 카드:{ai[0]} user 카드:{user} 유저 합산:{result_user}") # ai 카드 한 장 보여주고 user 카드와 합산 보여주기
