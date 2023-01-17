class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        res = 0
        currWindow = {}
        left = 0
        cnt = 0

        for i, num in enumerate(nums):
            currWindow[num] = currWindow.setdefault(num, 0) + 1
            cnt += currWindow[num] - 1

            while cnt >= k:
                currWindow[nums[left]] -= 1
                cnt -= currWindow[nums[left]]
                left += 1

            res += left

        return res
