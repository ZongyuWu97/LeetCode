class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        position = collections.defaultdict(set)
        for idx, num in enumerate(arr):
            position[num].add(idx)
        
        visited = set([0])
        q = collections.deque([(0, 0)])
        position[arr[0]].remove(0)
        while q:
            curr, step = q.popleft()
            if curr == n - 1:
                return step
            elif n - 1 in position[arr[curr]]:
                return step + 1

            if curr - 1 >= 0 and not (curr - 1) in visited:
                visited.add(curr - 1)
                q.append((curr - 1, step + 1))
            if curr + 1 < n and not (curr + 1) in visited:
                visited.add(curr + 1)
                q.append((curr + 1, step + 1))
            
            for idx in list(position[arr[curr]]):
                if not idx in visited:
                    visited.add(idx)
                    q.append((idx, step + 1))
            position[arr[curr]] = []
        

