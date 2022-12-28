class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use two pointers
        left, right = 0, len(numbers) - 1

        # Since numbers is already sorted, right-- makes current sum smaller
        # and left++ makes current sum larger
        while left < right:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum > target:
                right -= 1
            elif cur_sum < target:
                left += 1
            else:
                return [left + 1, right + 1]
