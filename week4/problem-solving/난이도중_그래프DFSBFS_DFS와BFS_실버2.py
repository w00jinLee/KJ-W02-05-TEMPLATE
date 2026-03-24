# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260

N, M, V = map(int, input().split())
# N은 정점의 개수, M은 간선의 개수, V는 시작 정점 번호

graph = {}

for i in range(N+1):
    graph[i] = []


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i].sort()

dfsOrder = []
dfsVisited = [False for _ in range(N+1)]

# graph
# {0: [],
#  1: [2, 3, 4], 
#  2: [1, 4],
#  3: [1, 4],
#  4: [1, 2, 3]}

def dfs(start):
    dfsOrder.append(start)
    dfsVisited[start] = True
    
    for i in graph[start]:
        if dfsVisited[i] is not True :
            dfs(i)
    return 

dfs(V)

from collections import deque
bfsOrder = []
bfsVisited = [False for _ in range(N+1)]
queue = deque()

def bfs(start):
    queue.append(start)
    bfsOrder.append(start)
    bfsVisited[start] = True
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if bfsVisited[i] is not True:
                queue.append(i)
                bfsOrder.append(i)
                bfsVisited[i] = True

bfs(V)

print(*dfsOrder)
print(*bfsOrder)