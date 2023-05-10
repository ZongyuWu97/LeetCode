class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        rows = defaultdict(int)        
        cols = defaultdict(int)
        memo = {}
        
        for i in range(m):
            for j in range(n):
                memo[mat[i][j]] = (i, j)
        
        for idx, num in enumerate(arr):
            rows[memo[num][0]] += 1
            cols[memo[num][1]] += 1
            
            if rows[memo[num][0]] == n or cols[memo[num][1]] == m:
                return idx
        