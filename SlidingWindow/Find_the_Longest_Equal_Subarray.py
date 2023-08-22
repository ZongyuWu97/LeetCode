from collections import defaultdict, deque
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        def LES(arrays, k):
            window = deque()
            res = 0
            count = 0
            for array in arrays:
                count += array[1] - array[0] + 1
                window.append(array)
                if len(window) != 1:
                    k -= array[0] - window[-2][-1] - 1
                    while k < 0:
                        remove = window.popleft()
                        k += window[0][0] - remove[1] - 1
                        count -= remove[1] - remove[0] + 1
                res = max(res, count)
            return res
                
        n = len(nums)
        prev = nums[0]
        count = 0
        memo = defaultdict(list)
        for idx, num in enumerate(nums):
            if num == prev:
                count += 1
            else:
                memo[prev].append((idx - count, idx - 1))
                count = 1
                prev = num
        memo[prev].append((idx - count + 1, idx))

        res = 0
        for num in memo:
            res = max(res, LES(memo[num], k))
        return res
        