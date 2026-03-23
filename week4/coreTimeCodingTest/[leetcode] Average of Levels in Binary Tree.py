
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        from collections import deque 
        
        queue = deque([root])
        result = []
    
        while queue :   
            nodeSum, nodeLevel = 0.0, len(queue)

            for _ in range(nodeLevel):
                node = queue.popleft()
                nodeSum += node.val
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
 
            result.append(nodeSum / nodeLevel)
        print(result)
        return result