# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

T = int(input())



for i in range(T):
    str=""

    inputs = input().split() # ["반복횟수", "문자열" 로 저장]
    inputs[0] = int(inputs[0])

    for i in range(len(inputs[1])):
        for j in range(inputs[0]):
            str += inputs[1][i]

    print(str)       