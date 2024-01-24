from collections import defaultdict

def primeQuery(n, first, second, values, queries):
    graph = construct_tree(n, first, second)
    prime_counts = [0] * (n + 1)
    visited = [False] * (n + 1)
    
    # Preprocess the tree with DFS
    preprocess(1, graph, values, prime_counts, visited)
    
    # Answer the queries
    return [prime_counts[query] for query in queries]

def construct_tree(n, first, second):
    tree = defaultdict(list)
    for f, s in zip(first, second):
        tree[f].append(s)
        tree[s].append(f)
    print(tree)
    return tree

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def preprocess(node, graph, values, prime_counts, visited):
    visited[node] = True
    prime_counts[node] = 1 if is_prime(values[node - 1]) else 0  # values are 1-indexed
    
    for child in graph[node]:
        if not visited[child]:
            preprocess(child, graph, values, prime_counts, visited)
            prime_counts[node] += prime_counts[child]

# Example usage
n = 5
first = [1, 2, 1, 3, 2]
second = [2, 3, 3, 4, 5]
values = [1, 2, 3, 5, 7]
queries = [1, 2, 3]

print(primeQuery(n, first, second, values, queries))

# New test case
n = 7
first = [1, 1, 2, 2, 3, 3]
second = [2, 3, 4, 5, 6, 7]
values = [11, 4, 6, 13, 9, 17, 10]
queries = [1, 2, 3, 4]

# Running the primeQuery function with the new test case
result = primeQuery(n, first, second, values, queries)
print(result)

