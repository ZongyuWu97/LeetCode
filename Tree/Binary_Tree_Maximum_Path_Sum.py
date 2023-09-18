# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(root):
            # Max path sum of this subtree, max path sum of paths ending at the root
            if not root:
                return 0, 0
            maxSubtree, maxEndHere = root.val, root.val
            if root.left:
                left = helper(root.left)
                maxEndHere = max(maxEndHere, root.val + left[1])
                maxSubtree = max(left[0], maxSubtree, maxEndHere)
            if root.right:
                right = helper(root.right)
                maxEndHere = max(maxEndHere, root.val + right[1])
                maxSubtree = max(right[0], maxSubtree, maxEndHere)
            if root.left and root.right:
                maxSubtree = max(maxSubtree, left[1] + right[1] + root.val)
            return maxSubtree, maxEndHere
        return helper(root)[0]