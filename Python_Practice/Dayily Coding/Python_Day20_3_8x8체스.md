## 8*8 체스판 프로그램 작성

> 8*8 체스판 위에 8개의 queen이 서로를 죽일 수 없는 자리에 위치히도록 하는 프로그램을 작성하여라.
2차원 리스트 사용하여 작성.
> 

```python
# 8*8 체스판 위에 8개의 queen이 서로를 죽일 수 없는 자리에 위치히도록 하는 프로그램을 작성하여라.
# 2차원 리스트 사용해야함

N = 8

board = [[0 for _ in range(N)] for _ in range(N)]

def is_safe(board, r, c):
    for i in range(r):
        if board[i][c] == 1:
            return False

    i, j = r - 1, c - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1; j -= 1

    i, j = r - 1, c + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1; j += 1

    return True

def place_queens(board, row=0):
    if row == N:
        print_board(board)
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            if place_queens(board, row + 1):
                return True
            board[row][col] = 0

    return False

def print_board(board):
    for r in range(N):
        line = []
        for c in range(N):
            line.append('Q' if board[r][c] == 1 else '.')
        print(' '.join(line))
    print()

if not place_queens(board):
    print("해를 찾을 수 없습니다.")

```

---

### 체스판 크기 지정

```python
N = 8
```

- 체스판 크기 (8x8)
- N이 바뀌면 4x4, 10x10도 가능

---

### 2차원 리스트

```python
board = [[0 for _ in range(N)] for _ in range(N)]
```

- 2차원 리스트로 체스판 생성.
- 0은 빈 칸, 1은 퀸이 놓인 칸.
- 결과 예시:
    
    ```python
    [
      [0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0],
      ...
    ]
    ```
    

---

### 함수

```python
def is_safe(board, r, c):
```

- (r, c) 위치에 퀸을 놓을 수 있는지 판단하는 함수
- r : 행(row), c : 열(column).

```python
for i in range(r):
	if borard[i][c] == 1:
		return False
```

- 같은 열(c) 위쪽 행들에 퀸이 있는지 확인.
- 위쪽만 보는 이유 → 아래쪽은 아직 퀸을 놓지 않았기 때문.
- 하나라도 있으면 공격받으니깐 False

```python
i, j = r - 1, c - 1
while i >= 0 and j >= 0 :
	if board[i][j] == 1 :
		return False
	i -= 1; j -= 1
```

- 좌상향 대각선 방향 검사.
- 현재 위치에서 위쪽 왼쪽 방향으로 퀸이 있는지 확인.
- board[i][j] == 1 이면 공격당하므로 False.

```python
i, j = r - 1, c +1
while i >= 0 and j < N :
	if board[i][j] == 1:
		return False
	i -= 1; j += 1
```

- 우상향 대각성 방향 검사.
- 위쪽 오른쪽에 퀸이 있는지 확인.
- 있으면 False.

```python
return True
```

- 위 세 방향 어디에도 퀸이 없으면 안전하다는 뜻 → True

---

### 실제로 퀸을 놓는 함수 (백트래킹)

```python
def place_queens(board, row=0):
```

- row번째 줄(행)에 퀸을 하나 놓고 다음 줄로 이동하는 함수.
- row는 현재 놓을 줄의 번호 (0~7).

```python
if row == N:
	print_board(board)
	return True
```

- row == 8 이면 (즉, 8개의 퀸을 다 놓았으면) 체스판을 출력하고 성공(True) 리턴.

```python
if col in range(N):
```

- 현재 row 행의 모든 열(col)을 하나씩 시도해봄.

```python
if is_safe(board, row, col) :
	board[row][col] = 1
```

- 해당 자리가 안전하면(is_safe == True) 퀸을 놓는다 (1 저장).

```python
if place_queens(board, row + 1):
	return True
```

- 바로 다음행(row+1)으로 넘어가서 같은 방식으로 퀸을 놓음.
- 그 아래에서 계속 성공하면 True로 전달되어 전체가 종료.

```python
board[row][col] = 0
```

- 만약 아래 행에서 더 이상 놓을 자리가 없으면 되돌아와서 퀸을 제거(백트래킹)
- 다른 열(col)로 다시 시도.

```python
return False
```

- 이 행(row)에서 어떤 열에도 퀸을 놓을 수 없으면 실패 → 이전 단계로 돌아감.

---

### 체스판 출력 함수

```python
def print_board(board)
```

- 현재 체스판 상대를 보기 좋게 출력하는 함수.

```python
for r in range(N):
	line = []
	for c in range(N):
		line.append('Q' if board[r][c] == 1 else '.')
	print(' '.join(line))
print()
```

- 각 행을 돌면서
    - 퀸이 있는 곳은 ‘Q’, 없는 곳은 ‘.’ 로 표시.
- ‘ ‘.join()은 띄어쓰기로 합쳐서 보기 쉽게 만듦.
- 출력 예:

```python
. Q . . . . . .
. . . Q . . . .
Q . . . . . . .
...
```

---

### 프로그램 시작 부분

```python
if not place_queens(board):
	print("해를 찾을 수 없습니다.")
```

- place_queens() 함수를 실행해서 해를 찾으면 자동으로 출력.
- 불가는할 경우 “해를 찾을 수 없습니다.” 표시