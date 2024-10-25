# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [str(node.val)]
            l, r = dfs(node.left), dfs(node.right)
            ans = []
            for child in l + r:
                ans.append(str(node.val) + "->" + child)
            return ans

        return dfs(root)
