# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def helper(root, p, q):
            if not root:
                return False

            # If p or q exists in root.left or root.right
            left = helper(root.left, p, q)
            right = helper(root.right, p, q)

            # If p or q is current node
            curr = root == p or root == q

            if left + right + curr >= 2:
                self.ans = root
            return curr or left or right

        self.ans = None
        helper(root, p, q)
        return self.ans
