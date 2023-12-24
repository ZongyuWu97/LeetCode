"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pAnc, qAnc = [], []
        while p:
            pAnc.append(p)
            p = p.parent
        while q:
            qAnc.append(q)
            q = q.parent

        i = -1
        n = min(len(pAnc), len(qAnc))
        if n == 1:
            return pAnc[-1]
        for i in range(n - 1):
            if pAnc[-i - 1].val == qAnc[-i - 1].val and pAnc[-i - 2].val != qAnc[-i - 2].val:
                return pAnc[-i - 1]
        return pAnc[-n]

