# 정수론 - 소수 찾기 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/1978


N = int(input())
cnt = 0
numbers = input().split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    
print(numbers)

def  checkNumber(num):
    if num == 2:
        return True
    for i in range(2, num-1):
        if num % i == 0:
            return False
    return True

for i in range(len(numbers)):
    if numbers[i] != 1 and checkNumber(numbers[i]):
        cnt += 1

print(cnt)