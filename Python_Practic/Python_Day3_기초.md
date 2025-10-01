## Python 가위바위보 프로그램(조건문)

- 조건문을 사용하여 랜덤 가위바위보 프로그램을 작성하시오.

```python
import random
player = input("가위, 바위, 보 중 하나를 입력하세요. :")

choices = ["가위", "바위", "보"]
computer = random.choice(choices)

if player == computer :
    print("비겼습니다.")
elif (player == "가위" and computer == "보") or \
     (player == "바위" and computer == "가위") or \
     (player == "보" and computer == "바위") :
    print("플레이어", player, "승!. 컴퓨터", computer, "패!")
else :
    print("플레이어", player, "패! 컴퓨터", computer, "승!")
```

---

### 1. 표준 라이블러리 모듈

```python
import random
```

- 표준 라이브러리 random 모듈을 불러온다.
- 이 모듈 random.choice() 같은 함수를 사용하기 위해 필요.

---

### 2. 입력 받기

```python
player = input("가위, 바위, 보 중 하나를 입력하세요. :")
```

- input() 문자열을 입력받아서 player 변수에 저장

---

### 3. 리스트

```python
choices = ["가위", "바위", "보"]
computer = random.choice(choices)
```

- 컴퓨터가 낼 수 있는 선택지를 만든다
- choices 리스트 중에서 하나를 무작위로 뽑아 computer 변수에 저장

---

### 4. 조건문 시작 → if

```python
if player == computer :
    print("비겼습니다.")
```

- player과 computer의 값이 같으면 이 조건이 참이 된다.
- 조건이 참일 때 실행. “비겼습니다.” 메세지 출력\

---

### 5. elif

```python
elif (player == "가위" and computer == "보") or \
     (player == "바위" and computer == "가위") or \
     (player == "보" and computer == "바위") :
    print("플레이어", player, "승!. 컴퓨터", computer, "패!")
```

- elif = “그렇지 않으면”
- 이 부분은 플레이어가 이기는 모든 경우를 나열한 조건문이다.
- and → 두 조건이 모두 참이어야 성립
- or → 여러 조건 중 하나만 참이어도 성립
- \ → 줄이 길어서 코드 줄을 다음 줄로 이어 쓸 때 사용
- elif 조건이 참일 때 "플레이어", player, "승!. 컴퓨터", computer, "패!" 이 부분을 출력

---

### 6. else

```python
else :
    print("플레이어", player, "패! 컴퓨터", computer, "승!")
```

- if, elif가 모두 거짓이면 실행되는 부분이다. 즉, 남은 경우는 컴퓨터가 이기는 경우이다.
- if, elif가 모두 거짓이면 실행 되기 때문에 "플레이어", player, "패! 컴퓨터", computer, "승!" 출력