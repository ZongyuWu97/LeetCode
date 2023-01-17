class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
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
            UF[rootX] = rootY

        def BFS(node):
            q = deque()
            q.append((node, 1))
            seen = {node: 1}

            while q:
                node, level = q.popleft()

                for neighbor in graph[node]:
                    if not neighbor in seen:
                        seen[neighbor] = level + 1
                        q.append((neighbor, level + 1))
                    elif seen[neighbor] == level:
                        return -1
            return level

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            union(u, v)

        res = defaultdict(int)
        for vertex in range(1, n + 1):
            num_group = BFS(vertex)
            if num_group == -1:
                return -1

            root = find(vertex)
            res[root] = max(res[root], num_group)

        # print(res, graph)
        return sum(res.values())
