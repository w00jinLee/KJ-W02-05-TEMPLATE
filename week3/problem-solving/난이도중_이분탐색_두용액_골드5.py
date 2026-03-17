# 이분탐색 - 두 용액 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2470
import sys

N = int(input())

solList = list(map(int, sys.stdin.readline().split()))

#0에 가장 가까운 값, 더한 값에 abs 씌우고 그 중 최솟값 
solComb = [0, 0]
solList.sort()
    # -99 -2 -1 4 98

left = 0
right = N-1
minNum = 2000000000

while left < right : 
    if abs(solList[left] + solList[right]) < minNum :
        minNum = abs(solList[left] + solList[right])
        solComb[0] = solList[left]
        solComb[1] = solList[right]
    if solList[left] + solList[right] > 0 :
        right -= 1
    elif solList[left] + solList[right] == 0 :
        solComb[0] = solList[left]
        solComb[1] = solList[right]
        break
    else : 
        left +=1

print(solComb[0], solComb[1])