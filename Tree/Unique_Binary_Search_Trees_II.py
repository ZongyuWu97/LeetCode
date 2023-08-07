# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(x, y):
            if x == y:
                return [TreeNode(x)]
            if x > y:
                return [None]
            res = []
            for i in range(x, y + 1):
                leftTrees = generate(x, i - 1)
                rightTrees = generate(i + 1, y)
                for l in leftTrees:
                    for r in rightTrees:
                        res.append(TreeNode(i, l, r))
            return res
        return generate(1, n)
            