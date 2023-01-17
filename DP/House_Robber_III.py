# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}
        return self.robHelper(root, memo)

    def robHelper(self, root, memo):
        if root in memo:
            return memo[root]
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val

        take = root.val
        if root.left:
            take += self.robHelper(root.left.left, memo) + \
                self.robHelper(root.left.right, memo)
        if root.right:
            take += self.robHelper(root.right.left, memo) + \
                self.robHelper(root.right.right, memo)

        memo[root] = max(self.robHelper(root.left, memo) +
                         self.robHelper(root.right, memo), take)

        return memo[root]
