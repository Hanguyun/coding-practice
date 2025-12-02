import random

dice = [1, 2, 3, 4, 5, 6]  # 주사위 눈금을 랜덤으로 뽑기위한 리스트 = 주사위 인덱스

print("게임을 시작합니다!")
# = 룰 1.1~6의 눈이 있는 주사위 5개를 사용.
user = random.choices(dice, k=5)  # for문을 이용한 주사위 던지기 시작 1번 던지고 시작
# = 룰 2.사용자는 처음 포함 주사위를 3번 던짐
for j in range(2):  # 사용자가 총 3번을 던질 수 있게 만듦 첫 번재는 던졌기 때문에 for문으로 2번 더 던지게 만듦
    user.sort()  # user 카드를 보기 좋게 오름차순 정렬
    reroll_count = int(input(f"현재 패: {user} 몇 개를 다시 던지겠습니까? 0은 리롤 종료(0~5) :"))  # 룰 3.주사위를 다시 던지는 횟수를 입력받아 변수에 저장
    if reroll_count == 0:
        break
    for i in range(reroll_count):  # 주사위를 던지는 횟수를 입력 받아서 for문으로 반복해서 던지기
        user.sort()  # user 카드를 보기 좋게 오름차순 정렬
        reroll_position = int(
            input(f"현재 패: {user} 몇 번째를 다시 던지겠습니까? (1~5) :"))  # 룰 4.지금 가지고 있는 패를 확인하고 몇 번째를 다시 던질지를 입력받아 변수에 저장
        user_reroll = random.choice(dice)  # reroll_count 만큼 주사위 던지기
        reroll_position -= 1  # 인덱스는 0부터 시작이기 때문에 -1 적용
        del user[reroll_position]  # user에 있는 리스트 즉 현재 패에서 reroll_position -1을 적용한 인덱스를 제거
        user.append(user_reroll)  # 제거 후 user_reroll로 뽑은 주사위를 다시 현재 패에 삽입
print(f"현재 최종 패:{user}입니다.")
# ---------------------------------컴퓨터 동작---------------------------------------------------
ai = random.choices(dice, k=5)  # ai도 마찬가지로 1번 던지고 시작
ai.sort()  # ai패를 보기 좋게 정렬하고 시작
print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기

for y in range(2):  # 룰 = 컴퓨터도 사용자와 마찬가지로 주사위를 3번 던지기 가능 처음 주사위를 던지고 시작 그래서 2번 반복
    count_num = {}  # 각 원소의 등장 횟수를 카운팅할 딕셔너리
    for j in ai:  # https://jimmy-ai.tistory.com/217 참조
        try:
            count_num[j] += 1  # 딕셔너리에 이미 j 값이 있다면 기존 값에 +1
        except:
            count_num[j] = 1  # count[j]에 처음 들어오면 오류가 발생 except실행 하고 처음 값으로

    if len(ai) != len(set(ai)):  # ai(리스트) ai(세트)와 같지 않다면 즉 리스트는 중복 되면 사라지지 않지만 세트는 중복 불가라서 중복이 되면 숫자가 줄어든다 그렇다면 같지 않다가 성립 되면 중복되는 숫자가 있다는 뜻

        max_value = max(count_num.values())  # 룰 = 가장 많이 나오는 값을 고정 https://hgk5722.tistory.com/460 참조 max를 이용하여 가장 많이 나온 값을 변수에 저장
        max_ai = []  # 최대값만 저장하기 위한 리스트 생성
        values = list(count_num.values())  # 딕셔너리에 저장되어 있는 values만 추출하여 리스트에 저장
        max_key = max(count_num.keys())  # 딕셔너리에 저장되어 있는 key 중 높은 것만 저장하는 변수

 음
    if user[2] > ai[2]: # 카드 4개가 같으니깐 정렬 되어있는 숫자 중간을 비교하여 큰 수가 이기는 조건
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # 중간 숫자 user가 더 크면 user 승리
    elif user[2] < ai[2]: # 이것도 마찬가지 조건
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # 중간 숫자 ai가 더 크면 ai 승리
    else:
        print(f"USER 패:{user} AI 패:{ai} 무승부") # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif 4 in user_dack.values(): # user덱만 4카드면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif 4 in ai_dack.values(): # ai덱만 4카드면 ai 승리
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")

#------------------------------------3,2카드-----------------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 3,2 그리고 ai딕셔너리에 저장되어 있는 값이 3,2이라면
elif 3 in user_dack.values() and 2 in user_dack.values() and 3 in ai_dack.values() and 2 in ai_dack.values():
    if user[2] > ai[2]:  # 카드 3,2개가 같으니깐 정렬 되어있는 숫자 중간을 비교하여 큰 수가 이기는 조건 예) 2,2,2,3,3 이고 3,3,3,2,2면 중간에 무조건 3개짜리 숫자가 들어오기 때문에 그걸 이용하여 비교
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 중간 숫자 user가 더 크면 user 승리
    elif user[2] < ai[2]:  # 이것도 마찬가지 조건
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 중간 숫자 ai가 더 크면 ai 승리
    else:
        print(f"USER 패:{user} AI 패:{ai} 무승부")  # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif 3 in user_dack.values() and 2 in user_dack.values():  # user덱만 3,2카드면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif 3 in ai_dack.values() and 2 in ai_dack.values():  # ai덱만 3,2카드면 ai 승리
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")

#-----------------------------------연속되는 카드(1,2,3,4,5)or(2,3,4,5,6)-------------------------------------------------
 # 연속되는 카드는 경우의 수 2개 그 중 2,3,4,5,6이 더 크기 때문에 1,2,3,4,5 보다 앞
elif user == [2, 3, 4, 5, 6] and ai == [2, 3, 4, 5, 6]:
    print(f"USER 패:{user} AI 패:{ai} 무승부")  # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif user == [2, 3, 4, 5, 6]: # user덱만 2, 3, 4, 5, 6이면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif ai == [2, 3, 4, 5, 6]: # ai덱만 2, 3, 4, 5, 6이면 ai 승리
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")

elif user == [1, 2, 3, 4, 5] and ai == [1, 2, 3, 4, 5]: # 2,3,4,5,6 밑에 1,2,3,4,5가 있기 때문에 밑에 적용
    print(f"USER 패:{user} AI 패:{ai} 무승부")  # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif user == [1, 2, 3, 4, 5]: # user덱만 1, 2, 3, 4, 5이면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif ai == [1, 2, 3, 4, 5]: # ai덱만 1, 2, 3, 4, 5이면 ai 승리
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")

#------------------------------------3,1,1 카드--------------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 3,3,1 그리고 ai딕셔너리에 저장되어 있는 값이 3,3,1이라면
elif 3 in user_dack.values() and 1 in user_dack.values() and 1 in user_dack.values() \
        and 3 in ai_dack.values() and 1 in ai_dack.values() and 1 in ai_dack.values():
    # https://dojang.io/mod/page/view.php?id=2308 참조
    user_3 = [] # user_3 리스트 준비
    ai_3 = [] # ai_3 리스트 준비
    for key, value in user_dack.items(): # 딕셔너리 items는 키-값을 모두 가져올 수 있음 블로그에서는 프린트를 사용했지만 if문을 사용
        # 딕셔너리에 저장 되어있는 키와 값의 개수만큼 반복
        if value == 3: # 벨류 값이 3이랑 같다면
            user_3 = key # 키 값을 user_3_1_1에 저장 비교하기 3,1,1 중 3개가 같은거를 비교하기 위한 과정
    for key, value in ai_dack.items(): # ai도 마찬가지로 진행 된다
        if value == 3: # 벨류 = 값이 3이랑 같다면
            ai_3 = key # 키 값을 ai_3_1_1에 저장

    if user_3 > ai_3: # user키 값이 더 크다면 user가 승리
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
    elif user_3 < ai_3:  # ai키 값이 더 크다면 ai가 승리
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리")
    else: # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음
        user_3_1_1 = [] # 값이 지금 두 개라서 리스트에 한 번에 저장하기 위한 변수
        ai_3_1_1 = [] # ai도 마찬가지

        for key, value in user_dack.items(): # key, value 값을 items를 사용하여 키와 값을 불러온다
            if value == 1: # 값이 1과 같다면
                user_3_1_1.append(key) # 새로 만들어둔 리스트에 저장
        for key, value in ai_dack.items(): # key, value 값을 items를 사용하여 키와 값을 불러온다
            if value == 1: # 값이 1과 같다면
                ai_3_1_1.append(key) # 새로 만들어둔 리스트에 저장

        if max(user_3_1_1) > max(ai_3_1_1): # 키 값을 저장해 놓은 리스트를 max로 비교하고 승패 결정
            print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # 키 값이 user가 더 크면 유저 승리
        elif max(user_3_1_1) < max(ai_3_1_1):
            print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # 키 값이 ai가 더 크면 ai 승리
        else:
            print(f"USER 패:{user} AI 패:{ai} 무승부")

elif 3 in user_dack.values() and 1 in user_dack.values() and 1 in user_dack.values():
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # user 덱만 3,1,1이면 user 승리
elif 3 in ai_dack.values() and 1 in ai_dack.values() and 1 in ai_dack.values():
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # ai 덱만 3,1,1이면 ai 승리

#-------------------------------------2,2,1 카드-------------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 2,2,1 그리고 ai딕셔너리에 저장되어 있는 값이 2,2,1이라면
elif 2 in user_dack.values() and 2 in user_dack.values() and 1 in user_dack.values() \
        and 2 in ai_dack.values() and 2 in ai_dack.values() and 1 in ai_dack.values():
    user_2 = [] # 여기도 마찬가지로 key값을 담을 리스트를 준비한다
    ai_2 = [] # ai도 변수 준비
    for key, value in user_dack.items(): # key, value 값을 items를 사용하여 키와 값을 불러온다
        if value == 2: # 값이 2랑 같다면
            user_2.append(key) # 키를 user_2 리스트에 저장한다
    for key, value in ai_dack.items(): # ai도 마찬가지
        if value == 2: #  값이 2랑 같으면
            ai_2.append(key) # 키를 user_2 리스트에 저장 당현한거지만 리스트에 추가할땐 append

    if max(user_2) > max(ai_2): # 변수에 저장되어 있는 수가 user가 크면
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 키 값이 user가 더 크면 유저 승리
    elif max(user_2) < max(ai_2): # 변수에 저장되어 있는 수가 ai가 크면
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 키 값이 ai가 더 크면 ai 승리

    elif user_2 == ai_2: # user_2와 ai_2에 들어있는 값이 같다면
        user_2_1 = [] # user_2_1 변수 준비
        ai_2_1 = [] # ai_2_1 변수 준비

        for key, value in user_dack.items():  # key, value 값을 items를 사용하여 키와 값을 불러온다
            if value == 1:  # 값이 1과 같다면
                user_2_1 = key  # 키를 user_2_1에 저장
        for key, value in ai_dack.items():  # ai도 마찬가지
            if value == 1:  # 값이 1과 같으면
                ai_2_1 = key  # 키를 user_2_1에 저장한다

        if user_2_1 > ai_2_1:
            print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 키 값이 user가 더 크면 유저 승리
        elif user_2_1 < ai_2_1:
            print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 키 값이 ai가 더 크면 ai 승리
        else: # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음
            print(f"USER 패:{user} AI 패:{ai} 무승부")

elif 2 in user_dack.values() and 2 in user_dack.values() and 1 in user_dack.values():
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # user덱만 2,2,1이라면 user 승리
elif 2 in ai_dack.values() and 2 in ai_dack.values() and 1 in ai_dack.values():
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # ai덱만 2,2,1이라면 ai 승리

#------------------------------------------2,1,1,1카드-------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 2,1,1,1 그리고 ai딕셔너리에 저장되어 있는 값이 2,1,1,1이라면
elif 2 in user_dack.values() and 1 in user_dack.values() and 1 in user_dack.values() and 1 in user_dack.values() \
      and 2 in ai_dack.values() and 1 in ai_dack.values() and 1 in ai_dack.values() and 1 in ai_dack.values():
    user_2_1_1_1 = []  # user_2_1_1_1 리스트 준비
    ai_2_1_1_1 = []  # ai_2_1_1_1 리스트 준비

    for key, value in user_dack.items():  # items로 키와 값을 쌍으로 불러와 반복
        if value == 2:  # 벨류 값이 2이랑 같다면
            user_2_1_1_1 = key  # 키 값을 user_2_1_1_1에 저장 비교하기 2,1,1,1 중 2개가 같은거를 비교하기 위한 과정
    for key, value in ai_dack.items():  # ai도 마찬가지로 진행 된다
        if value == 2:  # 벨류 = 값이 2이랑 같다면
            ai_2_1_1_1 = key  # 키 값을 ai_2_1_1_1에 저장

    if user_2_1_1_1 > ai_2_1_1_1:
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 키 값이 user가 더 크면 유저 승리
    elif user_2_1_1_1 < ai_2_1_1_1:
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 키 값이 ai가 더 크면 ai 승리
    elif user_2_1_1_1 == ai_2_1_1_1:  # user_2_1_1_1와 ai_2_1_1_1에 들어있는 값이 같다면
        user_1_1_1 = []  # user_1_1_1 변수 준비
        ai_1_1_1 = []  # ai_1_1_1 변수 준비

        for key, value in user_dack.items():  # key, value 값을 items를 사용하여 키와 값을 불러온다
            if value == 1:  # 값이 1과 같다면
                user_1_1_1.append(key)  # 키를 user_1_1_1에 저장
        for key, value in ai_dack.items():  # ai도 마찬가지
            if value == 1:  # 값이 1과 같으면
                ai_1_1_1.append(key)  # 키를 ai_1_1_1에 저장한다

        if max(user_1_1_1) > max(ai_1_1_1):
            print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 키 값이 user가 더 크면 유저 승리
        elif max(user_1_1_1) < max(ai_1_1_1):
            print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 키 값이 ai가 더 크면 ai 승리
        else: # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음
            print(f"USER 패:{user} AI 패:{ai} 무승부")

elif 2 in user_dack.values() and 1 in user_dack.values() and 1 in user_dack.values() and 1 in user_dack.values():
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # user덱만 2,1,1,1이라면 user 승리
elif 2 in ai_dack.values() and 1 in ai_dack.values() and 1 in ai_dack.values() and 1 in ai_dack.values():
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # ai덱만 2,1,1,1이라면 ai 승리

#--------------------------------------------1,1,1,1,1 카드--------------------------------------------------------------
# 하이카드만 남았기 때문에 이제 else로 끝을 보면 된다
else:
    if user > ai:
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
    elif user < ai:
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리")
    else: # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음
        print(f"USER 패:{user} AI 패:{ai} 무승부")
