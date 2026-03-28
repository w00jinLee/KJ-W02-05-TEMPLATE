# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748

n = int(input())
memo=[None] * (n+1)
memo[0] = 0
memo[1] = 1

def fib(num):  
    if memo[num] is not None:
        return memo[num]
    memo[num] = fib(num-1) + fib(num-2)
    return memo[num]

print(fib(n))