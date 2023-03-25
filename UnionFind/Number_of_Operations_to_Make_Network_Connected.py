class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        def find(x):
            if not x in UF:
                UF[x] = x

            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                UF[rootX] = rootY

        if len(connections) < n - 1:
            return -1
        
        UF = {}
        for  x, y in connections:
            union(x, y)

        count = set()
        for x in range(n):
            count.add(find(x))
        
        return len(count) - 1