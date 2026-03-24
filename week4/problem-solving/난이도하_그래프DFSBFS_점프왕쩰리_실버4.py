# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

N = int(input())

gameArea = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    gameArea[i] = list(map(int, input().split()))

visited = [[False for _ in range(N)] for _ in range(N)]

def dfs(y, x):
    if y >=N or x >= N or y<0 or x<0 :
        return False
    if visited[y][x] :
        return False
    if y == N-1 and x == N-1:
        return True

    visited[y][x] = True
    jump = gameArea[y][x]
    return dfs(y + jump, x) or dfs(y, x+jump)


if dfs(0,0):
    print("HaruHaru")
else:
    print("Hing")

