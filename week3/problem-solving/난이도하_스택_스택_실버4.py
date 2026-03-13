# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828
import sys

N = int(input())

stack=[]

def isPush(x):
#push X: 정수 X를 스택에 넣는 연산이다.
    stack.append(x)
def isPop():
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(stack) == 0:
        print("-1")
    else : 
        topNumber = stack[len(stack)-1]
        stack.pop()
        print(topNumber)

def isSize():
# size: 스택에 들어있는 정수의 개수를 출력한다.
    print(len(stack))
def isEmpty():
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
    if len(stack) == 0:
        print("1")
    else :
        print("0")

def isTop():
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
    if len(stack) == 0:
        print("-1")
    else : 
        print(stack[len(stack)-1])


inputList = []

for i in range(N):
    #일일이 input을 사용하면 최대 10,000 번까지 입력 받는 경우가 있어 시간 초과 발생

    string = sys.stdin.readline().strip()
    inputList.append(string)

    if "push" in inputList[i] :
        inputList[i] = inputList[i].split(" ")
        isPush(int(inputList[i][1]))
    elif inputList[i] == "pop" :
        isPop() 
    elif inputList[i] == "size" :
        isSize()
    elif inputList[i] == "empty" :
        isEmpty()
    elif inputList[i] == "top" :    
        isTop()
