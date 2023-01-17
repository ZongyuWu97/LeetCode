class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        UF = list(range(n + 1))

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)

            UF[rootX] = rootY

        eg1 = [e for e in edges if e[0] == 1]
        eg2 = [e for e in edges if e[0] == 2]
        eg3 = [e for e in edges if e[0] == 3]

        e1 = e2 = res = 0
        for _, u, v in eg3:
            rootU, rootV = find(u), find(v)

            if rootU != rootV:
                union(u, v)
                e1 += 1
                e2 += 1
            else:
                res += 1

        UF0 = UF[:]
        for _, u, v in eg1:
            rootU, rootV = find(u), find(v)

            if rootU != rootV:
                union(u, v)
                e1 += 1
            else:
                res += 1

        UF = UF0
        for _, u, v in eg2:
            rootU, rootV = find(u), find(v)

            if rootU != rootV:
                union(u, v)
                e2 += 1
            else:
                res += 1

        if e1 != n - 1 or e2 != n - 1:
            return -1

        return res
