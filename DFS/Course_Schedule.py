class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(v):
            if v in visited:
                return True
            if v in curr:
                self.circle = True
                return False

            if v in edges:
                curr.add(v)
                for neighbor in edges[v]:
                    if not dfs(neighbor):
                        return False
                curr.remove(v)
            visited.add(v)
            return True

        edges = {}
        for pair in prerequisites:
            if pair[1] in edges:
                edges[pair[1]].add(pair[0])
            else:
                edges[pair[1]] = {pair[0]}

        visited = set()
        curr = set()
        self.circle = False
        for v in range(numCourses):
            if not dfs(v):
                return False
        return True
