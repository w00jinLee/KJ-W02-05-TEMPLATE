# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946

# import sys

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     passCount = 0
#     peopleList = []
    
#     for i in range(N):
#         peopleList.append(tuple(map(int, sys.stdin.readline().split())))

#     peopleList.sort()
#     minMeeting = 100001

#     for i in range(len(peopleList)):
#         if peopleList[i][1] < minMeeting:
#             minMeeting = peopleList[i][1]
#             passCount+=1

#     print(passCount)


import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    passCount = 0
    peopleList = [0]*(N+1)
    
    for i in range(N):
        a, b = map(int, sys.stdin.readline().split())
        peopleList[a]=b

    minMeeting = 100001
    
    for i in range(1, len(peopleList)):
        if peopleList[i] < minMeeting:
            minMeeting = peopleList[i]
            passCount+=1

    print(passCount)