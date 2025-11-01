## 컴퓨터와 묵 찌 빠 하는 프로그램을 작성하시오.

```python
import random

choice = ["가위", "바위", "보"]
outcomes = ["비겼습니다.", "이겼습니다.", "졌습니다."]

while True:
    user = input("가위, 바위, 보 중에 선택하세요: ")
    ai = random.choice(choice)

    u = choice.index(user)
    a = choice.index(ai)
    res = (u - a) % 3

    print(f"user:{user}, ai:{ai} -> {outcomes[res]}")

    if res != 0:
        attacker = ["AI", "USER"][res == 1]
        print(f"공격자는 {attacker} 입니다.")
        break

while True:
    user = input("바위, 가위, 보 중 하나를 입력하세요: ")
    ai = random.choice(choice)

    u = choice.index(user)
    a = choice.index(ai)
    res = (u - a) % 3

    print(f"유저:{user}, AI:{ai} -> {outcomes[res]}")

    if user == ai:
        print(f"{attacker} 승리! 게임 종료!")
        break

    attacker = ["AI", "USER"][res == 1]
    print(f"공격자가 {attacker}로 바뀝니다!")

```

---

### 한 줄씩 /블록별 설명

```python
import random
	- 무작위 값을 뽑기 위한 표준 모듈을 불러온다.

choice = ["가위","바위","보"]
	- 가능한 손 모양을 담은 리스트. 인덱스는 각각 0, 1, 2
	
outcomes = ["비겼습니다.", "이겼습니다.", "졌습니다."]
	- 승패 계산 결과(0/1/2)를 사람이 읽을 문구로 변환하기 위해 준비한 리스트.
	- 규칙: 0 = 비김, 1 = 유저 승, 2 = 유저 패
```

---

### 공격자 결정

```python
while True :
	- 비기면 다시 해야 하므로 무한 반복 적용.
	
	user = input("가위, 바위, 보 중에 선택하세요: ")
		- 사용자 입력 받기(문자열)
		- 리스트에 문자열을 넣으면 나중에 index()에서 오류 실제 프로그램이라면 입력 검증이 필요.
	
	ai = random.choice(choice)
		- 위에서 지정한 리스트(choice)에서 하나를 무작위로 뽑아 AI의 선택으로 사용.
		
	u = choice.index(user)
		- 사용자가 낸 손의 인덱스(0,1,2)로 변환
	
	a = choice.index(ai)
		- AI가 낸 손의 인덱스(0,1,2)로 변환
		
	res = (u -a) % 3
		- 가위바위보 승패 계산 공식
		
	print(f"user:{user}, ai:{ai} -> {outcomes[res]}")
		- 이번 판의 양측 손과 결과 문구를 출력.
	
	if res != 0 :
		- 비김이 아니라면(=공격자를 정할 수 있으면) 아래 실행.
		
		attacker = ["AI", "USER"][res == 1]
			- 불리언 인덱싱 트릭: res == 1 이면 True(=1) -> "USER", 아니면 False(=0) -> "AI".
			- 즉 유저가 이겼으면 공격자 "USER", 유저가 졌으면 "AI".
			
		print(f"공격자는 {attacker} 입니다.")
			- 결정된 공격자를 출력.
			
		break
			- 공격자 정하기 루프 종료. 다음 라운드로 이동.
```

---

### 본 게임

```python
while True :
	- 같은 손이 나올 때까지 계속 진행하는 반복문.

	user = input("바위, 가위, 보 중 하나를 입력하세요: ")
		- 사용자 입력 받기(문자열)
	
	ai = random.choice(choice)
		- 위에서 지정한 리스트(choice)에서 하나를 무작위로 뽑아 AI의 선택으로 사용.
		
	u = choice.index(user)
		- 사용자가 낸 손의 인덱스(0,1,2)로 변환
	
	a = choice.index(ai)
		- AI가 낸 손의 인덱스(0,1,2)로 변환
		
	res = (u -a) % 3
		- 이번 턴 가위바위보 승패 계산
		
	print(f"유저:{user}, AI:{ai} -> {outcomes[res]}")
		- 이번 턴 결과를 출력.
	
		if user == ai:
			- 묵찌빠 규칙: 같은 손이면 현재 공격자 승리.
			- 같을 때만 게임을 종료
		
		print(f"{attacker} 승리! 게임 종료!")
			- 현재 공격자가 이겼음을 알리고 종료 메세지 출력.
		
		break
			- 게임 종료.
		
		attacker = ["AI", "USER"][res == 1]
			- 같은 손이 아니었다면(바로 위 if가 아니므로)
				이번 턴 가위바위보 승자에게 공격권을 넘긴다.
			- res == 1 -> 유저 승 -> 다음 공격자 "USER"
			- res == 2 -> AI 승 -> 다음 공격자 "AI"
		
		print(f"공격자가 {attacker}로 바뀝니다!")
			- 공격자 변경 안내 출력 후 다음 턴으로 반복.
```
