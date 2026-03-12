# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

N = int(input())

inputNumber = input().split()
A = [int(i) for i in inputNumber]
visited = [False for i in range(len(A))]
# |20-1|+|1-15|+|15-8|+|8-4|+|4-10|
#  지금까지 만든 순열
#  사용한 숫자 체크
#  현재 합
#  마지막 숫자
maxSum=0
def backTracking(start, curSum, last):
    global maxSum
    if start == len(A):
        if curSum > maxSum:
            maxSum = curSum
        return 
    
    for i in range(len(A)):
        if not visited[i]:
            visited[i]=True
            if start==0:
                backTracking(start+1, curSum, i)
            else:
                curSum += abs(A[last] - A[i])
                backTracking(start+1, curSum, i)
                curSum -= abs(A[last] - A[i])
            visited[i]=False


backTracking(0, 0, 0)
print(maxSum)