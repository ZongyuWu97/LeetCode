class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        subtracted = 0
        count = 0
        prev = 0
        for num in nums:
            if num == 0 or num == prev:
                continue
            subtracted += num - subtracted
            count += 1
            prev = num
            if subtracted == nums[-1]:
                return count
        return count
