from collections import defaultdict, deque


# Complete the tasks function below.
def tasks(n, a, b):
    in_degree = {}
    graph = {}
    for u in range(1, n + 1):
        graph[u] = set()
        in_degree[u] = 0
    for u, v in zip(a, b):
        graph[u].add(v)
        in_degree[v] += 1

    zero_in = deque()
    for u in range(1, n + 1):
        if in_degree[u] == 0:
            zero_in.append(u)

    topo = []
    while zero_in:
        node = zero_in.popleft()
        topo.append(node)
        for neighbor in list(graph[node]):
            graph[node].remove(neighbor)
            # if len(graph[u]) == 0:
            #     del graph[u]
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in.append(neighbor)

    for u in list(graph):
        if len(graph[u]) == 0 and in_degree[u] == 0:
            del graph[u]
    print(graph)

    cycles = {}
    visited = set()
    for u in graph:
        if u in visited:
            continue
        curr_count = 1
        visited.add(u)
        q = deque([u])
        while q:
            node = q.popleft()
            for neighbor in graph[node]:
                if neighbor in visited:
                    continue
                else:
                    curr_count += 1
                    visited.add(neighbor)
                    q.append(neighbor)
                    # print(neighbor, curr_count)
        cycles[u] = curr_count
    # print(cycles)

    return len(topo) + sum([cycles[x] - 1 for x in cycles])
