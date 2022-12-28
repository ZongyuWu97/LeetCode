# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        nums = []
        inorder(root)

        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum < k:
                left += 1
            elif curr_sum > k:
                right -= 1
            else:
                return True
        return False
