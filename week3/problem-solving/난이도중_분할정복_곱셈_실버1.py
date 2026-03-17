# 분할정복 - 곱셈 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1629

numList = list(map(int, input().split()))

def func(A, B, C):
    if B == 1:
        return A%C
    # B가 짝수일 때
    num = func(A, B//2, C)
    if B % 2 == 0:
        return (num * num) %C
    # B가 홀수일 때
    else:
        return ((num * num)*A )% C

print(func(numList[0], numList[1], numList[2]))
    

# 10, 11, 12
# 100000000000000 % 12 
# 10^11 % 12
# (10^(5 + 5)) % 12
# (10^5%12 * 10^5%12)

# 10^(5+5) = 10^5*10^5
# (10^5*10^5)%12
# (10^5%12)*(10^5%12)%12
# ((10^2%12)*(10^2%12)*10)%12 * ((10^2%12)*(10^2%12)*10)%12