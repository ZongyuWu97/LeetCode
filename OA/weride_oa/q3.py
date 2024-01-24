from collections import defaultdict, deque
# def getMinRepairCost_corrected(g_nodes, g_from, g_to, g_weight, k):
#     """
#     Corrected function to find the minimum cost to repair roads such that one can reach the city g_nodes from city 1 by traveling at most k roads.
#     """
#     # Combine the edges with their weights and sort them
#     edges = sorted(zip(g_weight, g_from, g_to))

#     # Iterate over the sorted edges
#     for cost, _, _ in edges:
#         graph = defaultdict(list)
        
#         # Create graph with edges having cost less or equal to the current cost
#         for w, u, v in edges:
#             if w <= cost:
#                 graph[u].append(v)
#                 graph[v].append(u)

#         # Check if a path exists from city 1 to g_nodes using at most k roads
#         if bfs_path_exists(graph, 1, g_nodes, k):
#             return cost

#     # If no path exists for any cost
#     return -1

def bfs_path_exists(graph, start, end, k):
    """
    Perform BFS to find if there is a path from start to end with at most k edges.
    """
    visited = set([start])
    queue = deque([(start, 0)])  # (node, number of edges)

    while queue:
        node, edges = queue.popleft()

        if node == end:
            return True

        if edges < k:
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, edges + 1))

    return False
def binary_search_min_cost(edges, g_nodes, k):
    """
    Perform a binary search over the sorted edge costs to find the minimum cost
    to travel from city 1 to city g_nodes using at most k roads.
    """
    # Extract unique costs and sort them
    unique_costs = sorted(set(w for w, _, _ in edges))

    left, right = 0, len(unique_costs) - 1
    min_cost = -1

    while left <= right:
        mid = (left + right) // 2
        cost = unique_costs[mid]

        # Construct a graph with edges having cost less or equal to the current cost
        graph = defaultdict(list)
        for w, u, v in edges:
            if w <= cost:
                graph[u].append(v)
                graph[v].append(u)

        # Check if a path exists
        if bfs_path_exists(graph, 1, g_nodes, k):
            min_cost = cost
            right = mid - 1  # Search for a lower cost
        else:
            left = mid + 1  # Search for a higher cost

    return min_cost

def getMinRepairCost(g_nodes, g_from, g_to, g_weight, k):
    """
    Optimized function to find the minimum cost to repair roads such that one can reach the city g_nodes from city 1 by traveling at most k roads.
    """
    # Combine the edges with their weights
    edges = list(zip(g_weight, g_from, g_to))

    # Use binary search to find the minimum cost
    return binary_search_min_cost(edges, g_nodes, k)
# Testing the corrected function with both examples
g_nodes = 5
g_edges = 6
g_from = [1, 3, 4, 3, 1, 2]
g_to = [3, 4, 5, 5, 2, 5]
g_weight = [2, 4, 6, 9, 7, 8]
k= 2
print(getMinRepairCost(g_nodes,g_from,g_to,g_weight,k))

g_nodes = 4
g_edges = 4
g_from = [2,3,2,1]
g_to = [3,1,4,2]
g_weight = [6,4,5,2]
k= 3
print( getMinRepairCost(g_nodes,g_from,g_to,g_weight,k))


g_nodes = 5
g_edges = 3
g_from = [1,2,4]
g_to = [4,5,3]
g_weight = [10,25,15]
k= 5
print( getMinRepairCost(g_nodes,g_from,g_to,g_weight,k))