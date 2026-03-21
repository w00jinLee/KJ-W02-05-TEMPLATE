# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        maxDepth=0

        def func(node, depth):
            nonlocal maxDepth
            
            if node.left == None and node.right == None:
                maxDepth = max(maxDepth, depth)
                return 
    
            if node.left is not None:
                func(node.left, depth+1)
            if node.right is not None:
                func(node.right, depth+1)


        func(root,1)
        return maxDepth