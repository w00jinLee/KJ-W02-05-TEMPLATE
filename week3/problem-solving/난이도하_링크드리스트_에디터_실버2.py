# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406


# 한 줄로 된 간단한 에디터를 구현하려고 한다. 
# 이 편집기는 영어 소문자만을 기록할 수 있는 편집기로, 최대 600,000글자까지 입력할 수 있다.
# 이 편집기에는 '커서'라는 것이 있는데, 커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 
# 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치할 수 있다.
# 즉 길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있다.

# 이 편집기가 지원하는 명령어는 다음과 같다.
# L	커서를 왼쪽으로 한 칸 옮김 (커서가 문장의 맨 앞이면 무시됨)
# D	커서를 오른쪽으로 한 칸 옮김 (커서가 문장의 맨 뒤이면 무시됨)
# B	커서 왼쪽에 있는 문자를 삭제함 (커서가 문장의 맨 앞이면 무시됨)
# 삭제로 인해 커서는 한 칸 왼쪽으로 이동한 것처럼 나타나지만, 실제로 커서의 오른쪽에 있던 문자는 그대로임
# P $	$라는 문자를 커서 왼쪽에 추가함

# cursor = 커서의 왼쪽 노드

import sys 

class Node: 
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(None)
        self.cursor = self.head

    def push(self, data):
        new_node = Node(data)
        self.cursor.next = new_node
        
        new_node.prev = self.cursor
        self.cursor = new_node

        return

    def L(self):
        if self.cursor.prev:
            self.cursor = self.cursor.prev
        return
    def D(self):
        if self.cursor.next:
            self.cursor = self.cursor.next
        return
    
    def B(self):
        if self.cursor == self.head :
            return 
    
        delete_node = self.cursor
        prev_node = delete_node.prev
        next_node = delete_node.next

        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        
        self.cursor = prev_node

        return

    def P(self , data):
        #추가할 노드 
        new_node = Node(data)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next:
            self.cursor.next.prev = new_node

        self.cursor.next = new_node
        self.cursor = new_node

        return
    def printList(self):
        current = self.head.next
        result=""

        while current:
            result += current.data
            current = current.next
        print(result)
    

string = sys.stdin.readline().strip()
M = int(sys.stdin.readline())

li = LinkedList()

for i in range(len(string)) :
    li.push(string[i])
    
for i in range(M):
    command = sys.stdin.readline().strip()
        
    if "P" in command :
        command = command.split(" ") # [P , X] 로 저장
        li.P(command[1])
    elif command == "L" : 
        li.L()

    elif command == "D" :
        li.D()

    elif command == "B" :
        li.B()

li.printList()