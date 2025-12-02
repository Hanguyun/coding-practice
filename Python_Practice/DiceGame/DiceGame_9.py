import random # 랜덤 라이브러리

dice = [1,2,3,4,5,6] # 주사위 눈금

print("게임을 시작합니다!") # 게임 시작을 알리는 프린트
print("---------------------------------------------------------------------------------------------------------------")

first_roll_dice = random.choices(dice, k=5) # dice 리스트에서 랜덤으로 숫자를 5개 가져와서 변수에 저장
first_roll_dice.sort()  # 첫 번째 굴린 주사위 정렬
user = [] # 주사위를 고정시키기 위하여 user리스트 생성

for i in range(2): # for문으로 2판 더 진행
    # 이미 한 번 던지고 시작했기 때문에 판수는 +1
    reroll_count = int(input(f"{i+1}판째 입니다. 현재 패:{first_roll_dice} 몇 개를 다시 던지겠습니까? 0~5 선택 :")) # 게임 판 수 입력받기
    if reroll_count == 0: # 입력 받은 리롤 횟수가 0이면
        break   # 종료

    for j in range(reroll_count): # reroll_count 변수에서 입력 받은 횟수를 가져옴
        user.sort() # 패를 보기 좋게 오름차순 정렬
        first_roll_dice.sort() # 패를 보기 좋게 오름차순 정렬
        reroll_position = int(input(f"현재 패: {first_roll_dice} 몇 번째를 다시 던지겠습니까? :")) # 주사위 횟수 입력받기
        reroll_position -= 1  # 인덱스는 0부터 시작이기 때문에 -1 적용
        del first_roll_dice[reroll_position] # reroll_position -1을 적용한 인덱스를 제거
        user.append(random.choice(dice)) # 다시 던진 주사위를 user 리스트에 넣어 고정
        print(f"현재 패:{first_roll_dice}   고정된 주사위:{user}")

user.extend(first_roll_dice) # user의 턴이 종료 되면 first_roll 주사위를 뽑아서 user로 삽입
user.sort() #패를 보기 좋게 오름차순 정렬
print(f"현재 USER 최종 패:{user}입니다.")

# ---------------------------------------------컴퓨터 동작---------------------------------------------------
ai = random.choices(dice, k=5)  # ai도 마찬가지로 1번 던지고 시작
ai.sort()  # ai패를 보기 좋게 정렬하고 시작

print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기

for k in range(2): # for문으로 2판 더 진행
    count_num = {}  # 각 원소의 등장 횟수를 카운팅할 딕셔너리
    for j in ai:  # https://jimmy-ai.tistory.com/217 참조
        try:
            count_num[j] += 1  # 딕셔너리에 이미 j 값이 있다면 기존 값에 +1
        except:
            count_num[j] = 1  # count[j]에 처음 들어오면 오류가 발생 except실행 하고 처음 값으로

    # sort가 안돼서 찾아봄 https://dev-records.tistory.com/entry/Python-sort-sorted-%EC%B0%A8%EC%9D%B4 참조
    # sort는 기존의 리스트를 수정해서 정렬된 결과를 반환하고 list만 가능 sorted는 정렬된 새로운 리스트를 반환
    sort_value = sorted(count_num.values())

    if 5 in count_num.values(): # 값이 5면 = 같은게 5개라면
        break # 룰 주사위의 숫자가 모두 같다면 던지지 않는다

    elif ai == [1, 2, 3, 4, 5] or ai == [2, 3, 4, 5, 6]:  # 룰 = 스트레이트는 경우의 수가 2가지
        print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기
        break  # 룰 = 모든 숫자가 연속되어 있다면 던지지 않음

    elif len(set(ai)) == 5: # 모두 다른 숫자라면
        ai.sort() # 패를 오름차순으로 정렬
        del ai[0:3] # 높은 숫자 2개 고정 후 나머지 3개 삭제
        ai.extend(random.choices(dice, k=3))  # 주사위 3개 다시 뽑기 extend로 하나씩 뽑아 넣기
        continue  # 위에 조건 만족 했으니 continue로 밑에 조건 건너뛰기

    # ai 패가 1,1,1,2 이면 실행
    elif sort_value == [1, 1, 1, 2]:
        del ai[0:5] # ai에 있는 패를 다 삭제 후
        # 리스트와 딕셔너리 컴프리헨션을 사용
        # https://wikidocs.net/92540 https://wikidocs.net/22805 참조 https://wikidocs.net/22797 참조
        # count_num딕셔너리에서 .items()를 사용하여 키,값을 뽑아 반복문을 돌리는데 값이 2라면 pair2 리스트에 저장
        pair2_list = [key for key, value in count_num.items() if value == 2]
        pair2 = pair2_list[0] # pair2 리스트에서 숫자를 꺼내와서 pair2에 저장
        ai.append(pair2) # []에 * 2를 하면 될줄 알았는데 sort에서 막혀서 append를 쓰기로 함...
        ai.append(pair2)
        ai.extend(random.choices(dice, k=3)) # 주사위 3개 다시 뽑기 extend로 하나씩 뽑아 넣기
        ai.sort()  # ai패를 보기 좋게 정렬하고 진행
        print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기
        continue  # 위에 조건 만족 했으니 continue로 밑에 조건 건너뛰기
    # ai 패가 1,1,3 이면 실행
    elif sort_value == [1, 1, 3]:
        del ai[0:5] # ai에 있는 패를 다 삭제 후
        pair3_list = [key for key, value in count_num.items() if value == 3] # 값이 3인 키를 pair3에 저장
        pair3 = pair3_list[0]  # pair3 리스트에서 숫자를 꺼내와서 pair3에 저장
        ai.append(pair3)  # 변수 pair3에 저장한 중복 되는 수 3개를 ai에 삽입 후
        ai.append(pair3)
        ai.append(pair3)
        ai.extend(random.choices(dice, k=2))  # 주사위 2개 다시 뽑기 extend로 하나씩 뽑아 넣기
        ai.sort()  # ai패를 보기 좋게 정렬하고 진행
        print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기
        continue  # 위에 조건 만족 했으니 continue로 밑에 조건 건너뛰기
    # ai 패가 1,4이면 실행
    elif sort_value == [1, 4]:
        del ai[0:5]  # ai에 있는 패를 다 삭제 후
        pair4_list = [key for key, value in count_num.items() if value == 4] # 값이 4인 키를 pair4에 저장
        pair4 = pair4_list[0]  # pair4 리스트에서 숫자를 꺼내와서 pair4에 저장
        ai.append(pair4)  # 변수 pair4에 저장한 중복 되는 수 4개를 ai에 삽입 후
        ai.append(pair4)
        ai.append(pair4)
        ai.append(pair4)
        ai.append(random.choice(dice))  # 주사위 1개 다시 뽑기 1개라서 append
        ai.sort()  # ai패를 보기 좋게 정렬하고 진행
        print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기
        continue  # 위에 조건 만족 했으니 continue로 밑에 조건 건너뛰기
    # ai 패가 2,3이면 실행
    elif sort_value == [2, 3]:
        del ai[0:5]  # ai에 있는 패를 다 삭제 후
        pair3_2_list = [key for key, value in count_num.items() if value == 3]  # 값이 3인 키를 pair3_2에 저장
        pair3_2 = pair3_2_list[0]  # pair3_2 리스트에서 숫자를 꺼내와서 pair3_2에 저장
        ai.append(pair3_2)   # 변수 pair3_2에 저장한 중복 되는 수 3개를 ai에 삽입 후
        ai.append(pair3_2)
        ai.append(pair3_2)
        ai.extend(random.choices(dice, k=2))  # 주사위 2개 다시 뽑기 extend로 하나씩 뽑아 넣기
        ai.sort()  # ai패를 보기 좋게 정렬하고 진행
        print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기
        continue  # 위에 조건 만족 했으니 continue로 밑에 조건 건너뛰기

    else: # 패가 2,2,1이면 실행
        del ai[0:5]  # ai에 있는 패를 다 삭제 후
        pair2_2_list = [key for key, value in count_num.items() if value == 2]  # 값이 2인 키를 pair2_2에 저장
        pair2_2 = max(pair2_2_list) # pair2_2 리스트에서 max숫자를 꺼내와서 pair2_2에 저장
        ai.append(pair2_2)  # 변수 pair2_2에 저장한 중복 되는 수 2개를 삽입 후
        ai.append(pair2_2)
        ai.extend(random.choices(dice, k=3))  # 주사위 3개 다시 뽑기 extend로 하나씩 뽑아 넣기
        ai.sort()  # ai패를 보기 좋게 정렬하고 진행
        print(f"현재 ai패: {ai}")  # 룰 = 컴퓨터와 사람이 주사위를 던진 후, 던질때 마다 패를 표기

#-------------------------------------------승패 결정--------------------------------------------------------------------
user.sort()
ai.sort()

user_dack = {} # 딕셔너리를 이용하여 숫자 키를 알 수 있고 값이 이제 키가 몇개 들어있는지 확인 가능
ai_dack = {} # ai도 마찬가지 예를 들어 5,6,6,6,6가 나오면 딕셔너리 키와 값은 5:1, 6:4 이렇게 나옴 이걸 변수에 저장하고 max로 판별

for j in user: # https://jimmy-ai.tistory.com/217 참조
    try:
        user_dack[j] += 1 # # 딕셔너리에 이미 j 값이 있다면 기존(키) 값에 +1
    except :
        user_dack[j] = 1 # count[j]에 처음 들어오면 오류가 발생 except실행 하고 처음 값(키)으로 저장하고 값을 1로 지정

for x in ai: # https://jimmy-ai.tistory.com/217 참조
    try:
        ai_dack[x] += 1 # 딕셔너리에 이미 j 값이 있다면 기존(키) 값에 +1
    except :
        ai_dack[x] = 1 # count[j]에 처음 들어오면 오류가 발생 except실행 하고 처음 값(키)으로 저장하고 값을 1로 지정

user_v = sorted(user_dack.values()) # 패에 있는 값을 sorted로 정렬하고 user_v, ai_v에 새로운 리스트에 저장
ai_v = sorted(ai_dack.values()) # 판정 부분에서 부족했던 정확성을 올리기 위한 작업

#---------------------------------5 카드------------------------------------------------------------------------------
if user_v == [5] and ai_v == [5]: # user덱의 값이 5고 ai 값이 5일 때 key값이 높은걸로 승패 결정
    if max(user_dack.keys()) > max(ai_dack.keys()) : # 5개가 모두 같으니 숫자 아무거나 비교해도 상관 없음
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # max함수 사용으로 user 수가 크면 유저 승리
    elif max(user_dack.keys()) < max(ai_dack.keys()): # 이것도 마찬가지로 아무거나 비교해도 상관 없음
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # max 함수 사용으로 ai 수가 크면 ai 승리
    else :
        print(f"USER 패:{user} AI 패:{ai} 무승부") # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif 5 in user_dack.values(): # user덱만 5카드면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif 5 in ai_dack.values(): # ai덱만 5카드면 ai 승리
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")

# ---------------------------------4 카드-------------------------------------------------------------------------------
# 유저덱에 같은 값이 4개, 1개 ai 덱에 같은 값이 4개, 1개 있다면을 만족하는 조건문 값이 4면 나머지 키는 1
elif user_v == [1, 4] and ai_v == [1, 4]:
    user_1 = []
    ai_1 = []
    for key, value in user_dack.items(): # 딕셔너리 items는 키-값을 모두 가져올 수 있음 블로그에서는 프린트를 사용했지만 if문을 사용
        # 딕셔너리에 저장 되어있는 키와 값의 개수만큼 반복
        if value == 1: # 벨류 값이 1이랑 같다면
            user_1 = key # 키 값을 user_1에 저장 비교하기 위한 과정
    for key, value in ai_dack.items(): # ai도 마찬가지로 진행 된다
        if value == 1: # 벨류 = 값이 1이랑 같다면
            ai_1 = key # 키 값을 ai_3_1_1에 저장
    if user[2] > ai[2]: # 카드 4개가 같으니깐 정렬 되어있는 숫자 중간을 비교하여 큰 수가 이기는 조건
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # 중간 숫자 user가 더 크면 user 승리
    elif user[2] < ai[2]: # 이것도 마찬가지 조건
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # 중간 숫자 ai가 더 크면 ai 승리
    elif user[2] == ai[2]:
        if user_1 > ai_1:
            print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 중간 숫자 user가 더 크면 user 승리
        elif user_1 < ai_1:
            print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 중간 숫자 ai가 더 크면 ai 승리
        else:
            print(f"USER 패:{user} AI 패:{ai} 무승부")  # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif user_v == [1, 4]: # user덱만 4카드면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif ai_v == [1, 4]: # ai덱만 4카드면 ai 승리
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리")

#------------------------------------3,2카드-----------------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 3,2 그리고 ai딕셔너리에 저장되어 있는 값이 3,2이라면
elif user_v == [2, 3] and ai_v == [2, 3]:
    if user[2] > ai[2]:  # 카드 3,2개가 같으니깐 정렬 되어있는 숫자 중간을 비교하여 큰 수가 이기는 조건 예) 2,2,2,3,3 이고 3,3,3,2,2면 중간에 무조건 3개짜리 숫자가 들어오기 때문에 그걸 이용하여 비교
        print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # 중간 숫자 user가 더 크면 user 승리
    elif user[2] < ai[2]:  # 이것도 마찬가지 조건
        print(f"USER 패:{user} 패배 AI 패:{ai} 승리")  # 중간 숫자 ai가 더 크면 ai 승리
    else:
        print(f"USER 패:{user} AI 패:{ai} 무승부")  # 주사위를 각자 돌리기 때문에 무승부가 나올 수 있음

elif user_v == [2, 3]:  # user덱만 3,2카드면 user 승리
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")
elif ai_v == [2, 3]:  # ai덱만 3,2카드면 ai 승리
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
elif user_v == [1, 1, 3] and ai_v == [1, 1, 3]:
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

elif user_v == [1, 1, 3]:
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # user 덱만 3,1,1이면 user 승리
elif ai_v == [1, 1, 3]:
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # ai 덱만 3,1,1이면 ai 승리

#-------------------------------------2,2,1 카드-------------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 2,2,1 그리고 ai딕셔너리에 저장되어 있는 값이 2,2,1이라면
elif user_v == [1, 2, 2] and ai_v == [1, 2, 2]:
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

elif user_v == [1, 2, 2]:
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배") # user덱만 2,2,1이라면 user 승리
elif ai_v == [1, 2, 2]:
    print(f"USER 패:{user} 패배 AI 패:{ai} 승리") # ai덱만 2,2,1이라면 ai 승리

#------------------------------------------2,1,1,1카드-------------------------------------------------------------------
# user딕셔너리에 저장되어 있는 값이 2,1,1,1 그리고 ai딕셔너리에 저장되어 있는 값이 2,1,1,1이라면
elif user_v == [1, 1, 1, 2] and ai_v == [1, 1, 1, 2]:
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

elif user_v == [1, 1, 1, 2]:
    print(f"USER 패:{user} 승리 AI 패:{ai} 패배")  # user덱만 2,1,1,1이라면 user 승리
elif ai_v == [1, 1, 1, 2]:
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
