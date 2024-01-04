class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = defaultdict(set)
        n = len(words)
        indegree = Counter({c : 0 for word in words for c in word})
        # Get graph
        for i in range(n - 1):
            word1, word2 = words[i], words[i + 1]
            for a, b in zip(word1, word2):
                if a != b:
                    if not b in graph[a]:
                        graph[a].add(b)
                        indegree[b] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        # Topo sort
        output = []
        q = deque([c for c in indegree if indegree[c] == 0])
        while q:
            u = q.popleft()
            output.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        return "" if len(output) < len(indegree) else "".join(output)

        





