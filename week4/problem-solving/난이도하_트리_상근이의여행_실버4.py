# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

T = int(input())
from collections import deque

for _ in range(T):
    N, M = map(int, input().split()) 
    queue = deque()
    graph = {}
    count = 0
    visited = [False for _ in range(N+1)]
    for i in range(N+1):
        graph[i] = []

    # N은 숫자 범위, M은 입력받을 횟수 
    for _ in range(M) : 
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)    

    queue.append(1)
    visited[1] = True
    while queue:
        v = queue.popleft()

        for u in graph[v]:
            if not visited[u] :
                visited[u] = True
                queue.append(u)
                count += 1

    print(count)