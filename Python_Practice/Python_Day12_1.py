# 주사위 합 맞추기
# 컴퓨터가 주사위 2개를 굴려서 (각 1~6) 비밀 합을 만든다.
# 사용자는 최대 5번까지 합을 맞혀본다.
# 매 시도마다 프로그램은 아래 중 하나를 출력한다.
# 입력이 2~12 범위를 벗어나면: 잘못된 입력입니다.
# 정답보다 크면: Down, 정답보다 작으면: Up, 정답이면: 정답! (시도 N회) 그리고 게임 종료
# 5번 안에 못 맞히면: 실패! 정답은 X였습니다. 출력하고 종료.
# random.randint(1, 6)로 주사위 두 개 합 구하기 (예: secret = a + b)
# while 반복문으로 최대 5회 입력 받기
# if / elif / else로 판정 (Up/Down/정답 + 예외 입력)
# 사용자가 입력한 값들을 리스트에 저장해 마지막에 보여주기

import random

secret = random.randint(1, 6) + random.randint(1, 6)
attempt = 0

while True:
    if attempt >= 5:
        print("실패! 정답은", secret, "였습니다.")
        break

    guess = int(input(f"주사위 합(2~12)을 맞추세요. (기회 {5 - attempt}번): "))
  
    if guess < 2 or guess > 12:
        print("잘못된 입력입니다.")
        continue

    attempt += 1

    if guess == secret:
        print(f"정답입니다! 시도: {attempt}회")
        break
    elif guess > secret:
        print("Down")
    else:
        print("Up")
