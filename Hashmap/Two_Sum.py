class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        needs = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in needs:
                return [needs[need], i]
            else:
                needs[num] = i
