# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([(root, 0)]) # node, index
        new_q = deque()
        left, right = 0, 0
        res = 0
        while q:
            left = q[0][1]
            while q:
                node, right = q.popleft()
                if node.left:
                    new_q.append((node.left, right * 2))
                if node.right:
                    new_q.append((node.right, right * 2 + 1))
            res = max(res, right - left + 1)
            q, new_q = new_q, q
            
        return res