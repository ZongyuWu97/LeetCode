# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        count = 0
        q = deque([root])
        tmp_q = deque()
        while q:
            tmp = []
            while q:
                node = q.popleft()
                if node.left:
                    tmp_q.append(node.left)
                if node.right:
                    tmp_q.append(node.right)
                tmp.append(node.val)

            count += self.minimumSwaps(tmp, len(tmp))
            q, tmp_q = tmp_q, q
        return count

    def dfs(self, vec, vis, node, compSize):
        vis[node] = True
        compSize[0] += 1
        for x in vec[node]:
            if not vis[x]:
                self.dfs(vec, vis, x, compSize)

    def minimumSwaps(self, a, n):
        aux = [*enumerate(a)]
        aux.sort(key=lambda it: it[1])
        vis = [False] * (n + 1)
        vec = [[] for i in range(n + 1)]
        for i in range(n):
            vec[aux[i][0] + 1].append(i + 1)
        ans = 0
        for i in range(1, n + 1):
            compSize = [0]
            if not vis[i]:
                self.dfs(vec, vis, i, compSize)
                ans += compSize[0] - 1
        return ans
