class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        window = collections.defaultdict(int)
        n = len(nums)
        for i in range(k):
            window[nums[i]] += 1
        ans = [len(window)]
        
        for i in range(k, n):
            window[nums[i]] += 1
            window[nums[i - k]] -= 1
            if window[nums[i - k]] == 0:
                del window[nums[i - k]]
            ans.append(len(window))
        return ans
