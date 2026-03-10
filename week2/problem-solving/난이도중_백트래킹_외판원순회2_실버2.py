# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

# N = int(input())
# W=[]
# for i in range(N):
#     W.append(input().split()) #[ , , ,]형태로 저장 
    
#     for j in range(N):
#         W[i][j] = int(W[i][j])

# # [[0, 10, 15, 20], 
# #  [5, 0, 9, 10], 
# #  [6, 13, 0, 12],  
# #  [8, 8, 9, 0]]
#     List = []

# def backTracking(start, currentCost):
#     if start==N:
#         return List.append(currentCost)
    
#     for i in range(start, N):
#         currentCost += W[start][i]
#         backTracking(start+1, currentCost)
#         currentCost -= start

# print(backTracking(0, 0))

N = int(input())
visited=[False for i in range(N)]

W=[]
minCost=[]

for i in range(N):
    W.append(input().split())
    for j in range(N):
        W[i][j] = int(W[i][j])

def backTracking(start, cur, count, currentCost):
    if count == N:
        if W[cur][start]!=0:    # 자기 자신을 가리키는지
            minCost.append(currentCost + W[cur][start])
        return
        #종료 조건문
    for i in range(N):
        if visited[i] == True: # 이미 방문했으면 건너뛰기
            continue
        if W[cur][i] == 0: # 자기 자신을 가르키는지 
            continue
        visited[i]=True
        backTracking(start, i, count+1, currentCost + W[cur][i]) # 시작 도시, 현재위치, 방문한 도시횟수 증가,누적 비용에 현재 비용 추가
        visited[i]=False

visited[0]==True
backTracking(0, 0, 1, 0)        

minCost.sort()
print(minCost[0])
