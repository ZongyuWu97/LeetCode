class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(v):
            if v in visited:
                return
            visited.add(v)
            for idx in range(n):
                if isConnected[v][idx]:
                    dfs(idx)

        n = len(isConnected)
        res = 0
        visited = set()
        for v in range(n):
            if not v in visited:
                res += 1
                dfs(v)
        return res
