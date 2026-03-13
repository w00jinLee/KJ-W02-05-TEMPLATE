# 스택 - 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2493

import sys

# 탑의 수 N(1 <= N <= 500,000)가 주어지고, 탑의 높이가 N개 주어짐
# 가장 오른쪽에 있는 탑부터 왼쪽 방향으로 신호를 보내고, 자신보다 높은 탑을 만나면 그 탑이 신호를 수신함
# 자신보다 높은 탑을 못 만나면 0출력 

N = int(input())

string = sys.stdin.readline()
topList = string.split(" ")
topList = [int(i) for i in topList]
result = [0 for i in range(N)] 
stack = []

for i in range(N) :
    # 현재 탑의 높이는 topList[i]
    # 만약 stack의 맨위에 탑이 topList[i]보다 작거나 같으면 그 탑은 더 이상 의미가 없음 -> 제거

    while len(stack) > 0 and stack[len(stack)-1][1] <= topList[i] :
        stack.pop()

    if len(stack) > 0 : 
        result[i] = result[i] = stack[len(stack)-1][0] + 1
    stack.append((i, topList[i]))

for i in range(len(result)):
    sys.stdout.write(f"{result[i]} ")