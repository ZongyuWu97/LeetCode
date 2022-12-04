# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.getLeftBoundary(root) + self.getLeaves(root) + self.getRightBoundary(root)

    def getLeftBoundary(self, root):
        if not root.left:
            return []

        root = root.left
        ans = []
        while root:
            ans.append(root.val)
            root = root.left or root.right
        ans.pop()
        return ans

    def getLeaves(self, root):
        if not root.left and not root.right:
            return []

        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def getRightBoundary(self, root):
        if not root.right:
            return []

        root = root.right
        ans = []
        while root:
            ans.append(root.val)
            root = root.right or root.left
        ans.pop()
        return ans[::-1]
