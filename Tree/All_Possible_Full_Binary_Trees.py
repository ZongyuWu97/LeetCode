# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.memo = {}

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(0)]
        
        ans = []
        for i in range(n):
            leftTrees = self.allPossibleFBT(i)
            rightTrees = self.allPossibleFBT(n - i - 1)
            for l in leftTrees:
                for r in rightTrees:
                    ans.append(TreeNode(0, l, r))
        self.memo[n] = ans
        return ans
