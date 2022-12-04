class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        fre = {}
        for i in range(len(nums)):
            if not nums[i] in fre:
                fre[nums[i]] = [1, i, i]
            else:
                fre[nums[i]][0] += 1
                fre[nums[i]][2] = i

        ans = nums[0]
        max_fre = 0
        min_len = float('inf')
        for key, val in fre.items():
            if val[0] > max_fre:
                min_len = val[2] - val[1] + 1
                max_fre = val[0]
            elif val[0] == max_fre:
                min_len = min(min_len, val[2] - val[1] + 1)

        return min_len
