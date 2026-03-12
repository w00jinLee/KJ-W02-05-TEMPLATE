# 백트래킹 - N-Queen (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/9663

# 퀸을 체스판에 놓을 때 
# N=1일 때는 1, N=2일때는 불가능한디
# N=3, 

# N = int(input())

# isQueen = [[False for i in range(N)] for i in range(N)]
# cnt=0

# def checkQueen(y,x) :   
#     for i in range(N):
#         for j in range(N): 
#             # 위, 아래
#             if isQueen[N-j-1][x] == False:
#                 isQueen[N-j-1][x] == True
#             # 오른쪽, 왼쪽
#             if isQueen[y][N-i-1] == False:
#                 isQueen[y][N-i-1] == True
#             # 대각선 /
#             if isQueen[N-1-i][i] == False:
#                 isQueen[N-1-i][i] == True
#             # 대각선 \
#             if isQueen[i][N-1-i] == False:
#                 isQueen[i][N-1-i] == True
    
# def backTracking(y, x):
#     global cnt
#     if N==1:
#         return 1
#     if N==2:
#         return 0
#     if  x == N or y == N : 
#         return

#     for i in range(N):
#         if isQueen[y][x] == False:
#             cnt+=1
#             checkQueen(y,x)
#             backTracking(y+1,x)
#         else:
#             backTracking(y+1, x+1)
#         return

# backTracking(0, 0) 

# print(cnt)


N = int(input())

# 열 검사  
flag_a = [False]*N
#\ 대각선 검사
flag_b = [False for i in range(2*N-1)]
# / 대각선 검사
flag_c = [False for i in range(2*N-1)]


def backTracking(num):
    global cnt
    if num == N:
        cnt+=1
        return
    for i in range(N):
        if not flag_a[i] and not flag_b[num+i] and not flag_c[N-1+num-i]:                     
            flag_a[i] = True
            flag_b[num+i] = True
            flag_c[N-1+num-i] = True
            
            backTracking(num+1)
            flag_a[i] = False
            flag_b[num+i] = False
            flag_c[N-1+num-i] = False        
    
cnt=0

backTracking(0)

print(cnt)