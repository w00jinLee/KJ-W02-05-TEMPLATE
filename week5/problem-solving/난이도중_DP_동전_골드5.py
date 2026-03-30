# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084

T = int(input())

for _ in range(T):
    N = int(input()) # N(1 ≤ N ≤ 20) 
    coins = list(map(int, input().split())) # 동전의 종류
    M = int(input()) # 만들어야 할 금액, M(1 ≤ M ≤ 10000)

    dp = [0]*(M+1)
    dp[0]=1

    # 모든 방법의 수
    for coin in coins:
        for i in range(coin, M+1):
            dp[i] += dp[i-coin]

    print(dp[M])