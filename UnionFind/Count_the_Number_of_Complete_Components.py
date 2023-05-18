class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        UF = {}
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                UF[rootX] = rootY
        
        def find(x):
            if not x in UF:
                UF[x] = x
            
            if UF[x] != x:
                UF[x] = find(UF[x])
            return UF[x]
        
        for u, v in edges:
            union(u, v)
        
        vertices = defaultdict(set)
        edges_sub = defaultdict(int)
        for u, v in edges:
            vertices[find(u)].add(u)
            vertices[find(u)].add(v)
            edges_sub[find(u)] += 1
        
        res = 0
        for vertex in vertices:
            m = len(vertices[vertex])
            if edges_sub[vertex] == (m * (m - 1)) / 2:
                res += 1
        
        res += n - sum(len(vertices[x]) for x in vertices)
        return res