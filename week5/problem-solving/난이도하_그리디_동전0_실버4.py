# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
coins = []
for _ in range(int(N)):
    coins.append(int(input()))
count =0
# 큰 동전부터 나누기
coins.sort(reverse=True)

for coin in coins:
    if K >= coin:
        count += K // coin
        K = K % coin


print(count)
