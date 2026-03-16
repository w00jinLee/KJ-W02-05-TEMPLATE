# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920

N = int(input())
A_list = input().split()
A_list = list(map(int, A_list))

M = int(input())
num_list = input().split()
num_list = list(map(int, num_list))

A_list.sort()



for num in num_list:
    left=0
    right=N-1
    found = False

    while left <= right :
        mid = (left+right)//2
        if A_list[mid] == num:
            found = True
            break
        elif A_list[mid] > num:
            right = mid-1
        else:
            left = mid + 1
    if found :
        print(1)
    else : 
        print(0)

