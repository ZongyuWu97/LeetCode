class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        neg = 0
        res = 0
        prev = -1
        while r < n:
            if nums[r] == 0:
                l = r = r + 1
                neg = 0
                prev = -1
                continue
            if nums[r] < 0:
                neg += 1
                if prev == -1:
                    prev = r
            if not neg % 2:
                res = max(res, r - l + 1)
            else:
                res = max(res, r - prev)
            r += 1
        return res