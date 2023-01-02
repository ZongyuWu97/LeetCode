# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        def helper(root, nodes):
            if not root:
                return False

            # Number of nodes in root.left and root.right
            left = helper(root.left, nodes)
            right = helper(root.right, nodes)

            # If root is in nodes
            if root in nodes:
                curr = 1
                nodes.remove(root)
            else:
                curr = 0

            # Number of nodes in current subtree
            res = left + right + curr

            if res == n and not self.find:
                self.ans = root
                self.find = True
            return res

        self.ans = None
        self.find = False
        n = len(nodes)
        nodes = set(nodes)
        helper(root, nodes)
        return self.ans
