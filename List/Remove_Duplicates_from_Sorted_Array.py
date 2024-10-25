class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                nums[count] = nums[i]
                seen.add(nums[i])
                count += 1
        return count
