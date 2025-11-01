## Python 가위바위보 프로그램(조건문 없이)

- 조건문을 사용하지 않고 가위바위보 프로그램을 작성하시오.

```python
# 조건문을 사용하지 않고 가위바위보 프로그램을 작성하시오.
import random

choices = ["가위", "바위", "보"]
player = input("가위, 바위, 보 중 하나를 입력하세요. :")
computer = random.choice(choices)

p = choices.index(player)
c = choices.index(computer)

result = (p - c) % 3

outcomes = ["비겼습니다!", "플레이어 승!", "컴퓨터 승!"]
print(outcomes[result])
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

### 4. index() 메서드 사용

```python
p = choices.index(player)
c = choices.index(computer)
```

- index() 메서드로 선택지를 숫자로 변환
- ex) 플레이어 입력 “가위”  → p = 0
    - 컴퓨터는 c에 저장

---

### 5. 수학 공식 사용

```python
result = (p - c) % 3
```

- 승패 판정을 수학 공식으로 처리
    - 0 → 비김
    - 1 → 플레이어 승
    - 2 → 컴퓨터

---

### 6. 리스트 출력

```python
outcomes = ["비겼습니다!", "플레이어 승!", "컴퓨터 승!"]
print(outcomes[result])
```

- 결과 메세지를 outcomes에 담아둔 리스트
- result 값(0, 1, 2)에 해당하는 메세지를 출력

---

### 최종 요약

- 문자열(가위/바위/보)을 인덱스 번호로 현환
- (플레이어 - 컴퓨터) %3 공식을 이용하여 승패를 결정
- 결과를 리스트에서 바로 꺼내오기