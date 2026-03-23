# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

computers = int(input())
edge = int(input())

visited = [False for _ in range(computers+1)]

graph = {}

for i in range(computers+1):
    graph[i] = []

for _ in range(edge):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

wormCnt =0

def dfs(start):
    global wormCnt
    visited[start] = True 
    wormCnt +=1

    for i in graph[start]:
        if visited[i] is False:
            dfs(i)
dfs(1)

print(wormCnt-1) # 1번 컴퓨터는 제외