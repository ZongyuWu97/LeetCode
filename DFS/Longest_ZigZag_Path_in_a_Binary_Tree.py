# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:  
        memo = collections.defaultdict(dict)
        self.res = 0
        def zigzag(root):
            if root in memo:
                return (memo[root]['left'], memo[root]['right'])
            if not root:
                return (-1, -1)
            
            memo[root]['left'] = 1 + zigzag(root.right)[1]
            memo[root]['right'] = 1 + zigzag(root.left)[0]
            self.res = max(self.res, memo[root]['left'], memo[root]['right'])
            
            return (memo[root]['left'], memo[root]['right'])
        
        zigzag(root)

        return self.res
