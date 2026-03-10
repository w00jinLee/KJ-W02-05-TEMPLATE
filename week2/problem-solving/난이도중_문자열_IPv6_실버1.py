# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107

IPV6 = input()

count=0
list = IPV6.split(":")
string=""
if "::" in IPV6:

    string = IPV6.split("::") 
    left = string[0].split(":") if string[0] else []
    right = string[1].split(":") if string[1] else []
    size = len(left) + len(right)
    for i in range(len(right)):
        for j in range(len(right[i]),4):
            right[i] = "0" + right[i]
    for i in range(len(left)):
        for j in range(len(left[i]),4):
            left[i] = "0" + left[i]
    string = left 
    for i in range(8-size):
            string.append("0000")

    string = string + right  

else:
    string = IPV6.split(":") 

    for i in range(len(string)):
        for j in range(len(string[i]),4):
            string[i] = "0" + string[i]

result=""
for i in range(len(string)):
    result += string[i]+":"
result = result.rstrip(":")
print(result)