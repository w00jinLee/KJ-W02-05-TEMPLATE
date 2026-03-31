# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

N, K = map(int, input().split())

items = []
dp = [0] * (K+1)

for _ in range(N):
    W, V = map(int, input().split())
    items.append((W,V))


for w, v in items:
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i] , dp[i-w] + v)
        

print(dp[-1])