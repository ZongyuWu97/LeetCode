class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(v):
            # print(v, curr, visited, self.is_circle)
            if v in visited:
                return
            if v in curr:
                self.is_circle = True
                return
            curr.add(v)

            if v in edges:
                for neighbor in edges[v]:
                    dfs(neighbor)
            res.append(v)
            curr.remove(v)
            visited.add(v)

        edges = {}
        for pair in prerequisites:
            if pair[1] in edges:
                edges[pair[1]].add(pair[0])
            else:
                edges[pair[1]] = {pair[0]}

        res = []
        visited = set()
        curr = set()
        self.is_circle = False
        for v in range(numCourses):
            dfs(v)

        return res[::-1] if not self.is_circle else []
