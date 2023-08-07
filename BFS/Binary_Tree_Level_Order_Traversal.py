# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        nextQ = deque()

        while q:
            tmp = []
            while q:
                curr = q.popleft()
                tmp.append(curr.val)
                if curr.left:
                    nextQ.append(curr.left)
                if curr.right:
                    nextQ.append(curr.right)
            res.append(tmp)
            q, nextQ = nextQ, q
        return res