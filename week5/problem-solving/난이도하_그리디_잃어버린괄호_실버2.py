# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

numList = input().split("-")
result = 0

for i in range(len(numList)):
    listSum=0
    if "+" in numList[i]:
        numList[i] = numList[i].split("+")
        for j in range(len(numList[i])):
            listSum += int(numList[i][j])
        numList[i] = listSum
    else :
        numList[i] = int(numList[i])

result += numList[0]
for i in range(1, len(numList)):
    result -= numList[i]

print(result)