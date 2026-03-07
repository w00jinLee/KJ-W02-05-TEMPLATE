# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

list = [i for i in range(C)]

for i in range(C):
    arr = input().split()

    for i in range(len(arr)):
        arr[i] = int(arr[i])

    sum = 0
    avg = 0

    for j in range(1, len(arr)):
        sum += arr[j] 
    avg = sum / arr[0]
    cnt = 0

    for j in range(1, len(arr)):
        if arr[j] > avg: 
            cnt +=1

    num = cnt / arr[0]*100
    print('%.3f%%' %num)