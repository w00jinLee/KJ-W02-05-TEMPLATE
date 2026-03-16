# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stringNum1=""
        currentNode1 = l1
        while currentNode1:
            stringNum1 = str(currentNode1.val) + stringNum1
            currentNode1 = currentNode1.next

        stringNum2=""
        currentNode2 = l2
        while currentNode2:
            stringNum2 = str(currentNode2.val) + stringNum2
            currentNode2 = currentNode2.next
 
        sum = int(stringNum1) + int(stringNum2)
        
        strSum = str(sum)
        linkedList = ListNode(int(strSum[-1]))
        current = linkedList

        for i in range(len(strSum)-2,-1, -1):
            newNode = ListNode(int(strSum[i]))
            current.next = newNode
            current = current.next

        return linkedList