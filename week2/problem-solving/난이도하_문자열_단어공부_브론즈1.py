# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

str = input().upper()

#아스키 코드, A=65, Z= 90 a=97

check = [0 for i in range(91)]

for i in range(len(str)):
    check[ord(str[i])] +=1  #ord는 아스키 코드값에 해당하는 10진수로 반환해주는 함수

# for i in range(65, len(check)):
#     if check[i] > 0 :
#         print("check: ", check[i], ", 문지: ", chr(i))

max=0
multimax=False
idx = 0

for i in range(65, len(check)):
    if max < check[i] :
        multimax = False
        max = check[i]
        idx = i
    elif max == check[i] :
        multimax = True

if multimax :
    print("?")
else:
    print(chr(idx)) #chr은 10진수에 맞는 아스키 코드값으로 반환해주는 함수