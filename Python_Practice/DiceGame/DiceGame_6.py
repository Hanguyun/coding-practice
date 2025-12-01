import random

dice = [1, 2, 3, 4, 5, 6]  # 주사위 눈금을 랜덤으로 뽑기위한 리스트

print("게임을 시작합니다!")

user = random.choices(dice, k=5)  # for문을 이용한 주사위 던지기 시작 1번 던지고 시작

for i in range(2):  # 사용자가 총 3번을 던질 수 있게 만듦 첫 번재는 던졌기 때문에 for문으로 2번 더 던지게 만듦
    reroll_count = int(input(f"현재 패: {user} 몇 개를 다시 던지겠습니까? 0은 리롤 종료(0~5) :"))  # 주사위를 다시 던지는 횟수를 입력받아 변수에 저장
    if reroll_count == 0:
        break
    for i in range(reroll_count):  # 주사위를 던지는 횟수를 입력 받아서 for문으로 반복해서 던지기
        reroll_position = int(
            input(f"현재 패: {user} 몇 번째를 다시 던지겠습니까? (1~5) :"))  # 지금 가지고 있는 패를 확인하고 몇 번째를 다시 던질지를 입력받아 변수에 저장
        user_reroll = random.choice(dice)  # reroll_count 만큼 주사위 던지기
        reroll_position -= 1  # 인덱스는 0부터 시작이기 때문에 -1 적용
        del user[reroll_position]  # user에 있는 리스트 즉 현재 패에서 reroll_position -1을 적용한 인덱스를 제거
        user.append(user_reroll)  # 제거 후 user_reroll로 뽑은 주사위를 다시 현재 패에 삽입

# ---------------------------------컴퓨터 동작---------------------------------------------------
ai = random.choices(dice, k=5)  # ai도 마찬가지로 1번 던지고 시작

for y in range(2):  # 컴퓨터도 사용자와 마찬가지로 주사위를 3번 던지기 가능 처음 주사위를 던지고 시작 그래서 2번 반복
    if len(set(ai)) == 1:  # 중복이 되지 않는 세트의 특징을 이용하여 중복 제거가 되어 값이 1개만 남는다면 모든 값이 같다
        break  # 룰 = 5개의 주사위의 숫자가 모두 같다면 더 이상 던지지 않는다.
    elif len(set(ai)) == len(ai):  # 중복이 되지 않는 세트의 특징을 이용 중복 제거가 되지 않아 값이 5개일 경우 조건 성립
        sort_ai = ai.sort() # 모든 숫자가 연속되어 있다면 던지지 않게 하기 위한 오름차순 정렬
        if sort_ai == [1, 2, 3, 4, 5] or sort_ai == [2, 3, 4, 5, 6] : # 룰 = 모든 숫자가 연속되어 있다면 던지지 않음
            break
        ai.sort()  # 룰 = 높은 수 두 개를 고정하고 나머지 주사위 3개를 돌리기 위해 오름차순 정렬
        del ai[0:3]  # 룰 = 오름차순 정렬 후 높은 수 2개 고정 후 슬라이스를 이용해 0~2까지 삭제
        ai_reroll = random.choices(dice, k=3)  # 주사위 3개 다시 돌리기 ai_reroll 변수에 저장
        ai.extend(ai_reroll)  # ai_reroll 변수에 있던 정수를 ai 덱에 삽입
        continue    # 조건을 만족하면 밑에 조건을 건너뛰기 위해 continue
    elif len(ai) != len(set(ai)):  # ai(리스트) ai(세트)와 같지 않다면 즉 리스트는 중복 되면 사라지지 않지만 세트는 중복 불가라서 중복이 되면 숫자가 줄어든다 그렇다면 같지 않다가 성립 되면 중복되는 숫자가 있다는 뜻
        count_num = {}  # 각 원소의 등장 횟수를 카운팅할 딕셔너리
        for j in ai: # https://jimmy-ai.tistory.com/217 참조
            try:
                count_num[j] += 1 # 딕셔너리에 이미 j 값이 있다면 기존 값에 +1
            except :
                count_num[j] = 1 # count[j]에 처음 들어오면 오류가 발생 except실행 하고 처음 값으로

        max_value = max(count_num.values()) # 룰 = 가장 많이 나오는 값을 고정 https://hgk5722.tistory.com/460 참조 max를 이용하여 가장 많이 나온 값을 변수에 저장
        max_ai = [] # 최대값만 저장하기 위한 리스트 생성
        values = list(count_num.values()) # 딕셔너리에 저장되어 있는 values만 추출하여 리스트에 저장
        max_key = max(count_num.keys()) # 딕셔너리에 저장되어 있는 key 중 높은 것만 저장하는 변수

        for key, value in count_num.items(): # https://dojang.io/mod/page/view.php?id=2308 참조
            if value == max_value: # 딕셔너리 키와 값을 프린트하는 부분을 값이 제일 많은 것을 비교하기 위한 조건
                for x in range(value): # 값 만큼 max_ai에 키를 저장하는 반복문
                    max_ai.append(key)
                    del ai[0:5] # ai리스트에 가장 많은 숫자를 집어넣기 위하여 초기화
                    ai = max_ai[:]  # 얕은 복사를 이용하여 값을 이동 https://inkkim.github.io/python/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8-%EB%B3%B5%EC%82%AC/ 참조
                    reroll_num = 5-len(max_ai) # 5-최대값의 갯수를 빼면 몇 번의 주사위를 돌려야하는지 나옴 그걸 변수에 저장
                    ai.extend(random.choices(dice, k=reroll_num)) # 그리고 뺀 개수 만큼 dice리스트에서 주사위를 초이스하고 ai에 저장
    elif values == [2,2,1] or values == [2,1,2] or values == [1,2,2]: # 값만 저장되어있는 리스트를 불러와서 비교 경우의 수는 3가지
        ai.sort() # ai를 정렬
        del ai[0:3] # 높은 숫자 2개를 남겨놓고 나머지 3개 삭제
        ai.extend(random.choices(dice, k=3)) # 그리고 3개를 삭제 했으니 3개를 뽑아서 다시 추가
# 지금 간헐적으로 ai 패가 6개씩 나옴 나오는 경우가 주사위가 모두 같으면 나옴 예) 5,5,5,5,5,5 -> 이렇게 나옴.
#-------------------------------------------승패 결정--------------------------------------------------------------------
# 비교할때 가중치? 5개가 같으면 뭐 나왔는지 체킹 상대가 5개가 동일하지 않다면 바로 패배
# 같은게 4개 나왔는데 상대가 3개 나오면 이김
# 1,1,1,1,2가 나오고 1,1,1,1,3이 나오면?
if len(set(user)) <= len(set(ai)) :
    print(f"USER :{user} AI:{ai} USER 승리!")
elif len(set(user)) >= len(set(ai)) :
    print(f"USER :{user} AI:{ai} AI 승리!")



# --------------------------------------------------------------------------------------------------
print(f"현재 패 :{user}")
print(f"ai 패 :{ai}")
print(f"ai 딕셔너리 : {count_num.items()}")

