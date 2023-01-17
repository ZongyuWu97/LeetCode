class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        UF = {}

        def find(x):
            if not x in UF:
                UF[x] = x

            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            if rootX != rootY:
                UF[rootX] = rootY

        edgeList.sort(key=lambda x: x[2])
        queries = sorted((limit, p, q, idx)
                         for idx, (p, q, limit) in enumerate(queries))
        res = [False] * len(queries)

        i, E = 0, len(edgeList)
        for limit, p, q, idx in queries:
            while i < E and edgeList[i][2] < limit:
                union(edgeList[i][0], edgeList[i][1])
                i += 1

            res[idx] = find(p) == find(q)
        return res
