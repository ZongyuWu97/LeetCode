# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parent = {}
        parent[root] = None
        q = [root]

        # Find deepest leaves and get parents
        while q:
            tmp = []
            for node in q:
                if node.left:
                    parent[node.left] = node
                    tmp.append(node.left)
                if node.right:
                    parent[node.right] = node
                    tmp.append(node.right)
            if tmp:
                q = tmp
            else:
                break

        # Get LCA. Repeat getting parent layer by layer untill there's only one parent.
        while len(q) != 1:
            tmp = set()
            for node in q:
                tmp.add(parent[node])

            q = list(tmp)

        return q[0]
