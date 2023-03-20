import heapq


class Solution:
    def kSum(self, nums: List[int], k: int) -> int:
        maxSum = sum([x for x in nums if x > 0])
        absNum = sorted(map(abs, nums))
        ans = maxSum
        n = len(nums)

        count = k
        h = [(-(maxSum - absNum[0]), 0)]
        while count > 1:
            nextSum, idx = heapq.heappop(h)
            nextSum = -nextSum
            if idx < n - 1:
                heapq.heappush(h, (-(nextSum - absNum[idx + 1]), idx + 1))
                heapq.heappush(
                    h, (-(nextSum + absNum[idx] - absNum[idx + 1]), idx + 1))
            ans = nextSum
            count -= 1
        return ans
