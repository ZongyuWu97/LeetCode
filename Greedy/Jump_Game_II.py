class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        visited = set([0])
        q = deque([(0, 0)])
        while q:
            curr, step = q.popleft()
            for position in range(curr + 1, min(curr + nums[curr] + 1, n)):
                if position == n - 1:
                    return step + 1
                if not position in visited:
                    visited.add(position)
                    q.append((position, step + 1))
            

