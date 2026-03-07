# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562


list = [int(input()) for i in range(9)]

max = 0
pos = 0
for i in range(9):
    if list[i] > max:
        max = list [i]
        pos = i+1

print(max, pos)