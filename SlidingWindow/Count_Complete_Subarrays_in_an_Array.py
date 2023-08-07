class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(Counter(nums))
        memo = defaultdict(int)
        n = len(nums)
        count = 0
        pivot = 0
        for i in range(n):
            while len(memo) < distinct and pivot < n:
                memo[nums[pivot]] += 1
                pivot += 1

            if len(memo) == distinct:
                count += n - pivot + 1
            else:
                break
            memo[nums[i]] -= 1
            if memo[nums[i]] == 0:
                del memo[nums[i]]
        return count