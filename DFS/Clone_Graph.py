"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
            
        seen = {}
        def clone(node):
            if node in seen:
                return seen[node]
            res = Node(node.val)
            seen[node] = res
            if node.neighbors:
                res.neighbors = []
                for neighbor in node.neighbors:
                    res.neighbors.append(clone(neighbor))
            return res
        
        return clone(node)