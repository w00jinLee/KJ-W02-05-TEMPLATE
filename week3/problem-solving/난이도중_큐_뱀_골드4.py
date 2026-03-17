# 큐 - 뱀 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/3190

from collections import deque

# 보드의 크기 N
N = int(input())
# 사과의 개수 
K = int(input())
# 게임 시작 시간
X=0

board = [[0 for _ in range(N)] for _ in range(N)]
worm = deque()
worm.append((0,0))
board[0][0]=2

for _ in range(K):
   apple = list(map(int, input().split()))
   board[apple[0]-1][apple[1]-1] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
#     3 (↑)
# 2 (←)   0 (→)
#     1 (↓)
# (direction+1)%4하면 방향전환
# dir = 0이면 오른쪽, 1이면 아래, 2이면 왼쪽, 3이면 위
def move(y, x, dir):
    ny = y + dy[dir]
    nx = x + dx[dir]
    return (ny, nx)

# 뱀이 죽는 조건
def checkDie(ny, nx):
    if ny >= N or nx >= N or ny < 0 or nx < 0 or board[ny][nx] == 2 : 
        return True
    return False

command=[]
commandCnt = int(input())
for _ in range(commandCnt):
    command.append(input().split())
    
direction = 0
cmd_idx = 0
while True:
    X += 1
    head_y, head_x = worm[-1]
    ny, nx = move(head_y, head_x, direction)
    # 죽는 위치인지 검사
    if checkDie(ny, nx) :
        print(X)
        break
    
    worm.append((ny,nx))
    board[ny][nx] = 2

    # 사과 없으면 꼬리제거
    if board[ny][nx] != 1:
        tail_y, tail_x = worm.popleft()
        board[tail_y][tail_x] = 0

    if cmd_idx < commandCnt and X == int(command[cmd_idx][0]) :
        if  command[cmd_idx][1] == 'D':
            direction = (direction + 1) % 4
        else : # L
            direction = (direction - 1) % 4
            cmd_idx +=1
# 1. 시간 증가

# 2. 현재 머리 위치 가져오기
# 지금 뱀의 머리는 worm의 맨 뒤야.

# 3. 다음 위치 계산
# 4. 죽는지 검사
# 5.안 죽었으면 머리 이동
# 6.사과 있는지 확인

# 사과 있으면 꼬리 안 줄임




    # x초 뒤에 L(왼쪽), D(오른쪽) 방향으로 회전


    # 이동할 때마다 뱀의 위치를 큐에 저장, 
    # 이동 후 전의 위치와 현재 위치를 저장하고, 사과가 있다면 pop X, 없다면 전의 위치를 pop시킴




