class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def maxDiff(left, right):
            # max difference this player can archieve
            if left == right:
                return nums[left]
            return max(nums[left] - maxDiff(left + 1, right),
                        nums[right] - maxDiff(left, right - 1))
            
        return maxDiff(0, len(nums) - 1) >= 0
                