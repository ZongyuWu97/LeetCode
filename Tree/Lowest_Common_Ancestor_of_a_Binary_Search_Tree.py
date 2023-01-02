# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, s, l):
            if not root:
                return
            if root.val > l:
                dfs(root.left, s, l)
            elif root.val < s:
                dfs(root.right, s, l)
            else:
                self.ans = root

        s, l = min(p.val, q.val), max(p.val, q.val)
        self.ans = None
        dfs(root, s, l)
        return self.ans
