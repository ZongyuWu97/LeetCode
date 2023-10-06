# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def find(root, val, path):
            if root.val == val:
                return True
            if root.left and find(root.left, val, path):
                path += 'L'
            elif root.right and find(root.right, val, path):
                path += 'R'
            return path
        
        s, d = [], []
        find(root, startValue, s)
        find(root, destValue, d)

        while s and d and s[-1] == d[-1]:
            s.pop()
            d.pop()
        return 'U' * len(s) + ''.join(reversed(d))
 
            
            