class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        if not nums:
            if lower == upper:
                return [str(lower)]
            else:
                return [f'{lower}->{upper}']

        if nums[0] - lower == 1:
            ans.append(str(lower))
        elif nums[0] - lower > 1:
            ans.append(f'{lower}->{nums[0] - 1}')

        prev = nums[0]
        for num in nums[1:]:
            if num - prev == 2:
                ans.append(str(num - 1))
            elif num - prev > 2:
                ans.append(f'{prev + 1}->{num - 1}')
            prev = num

        if upper - prev == 1:
            ans.append(str(upper))
        elif upper - prev > 1:
            ans.append(f'{prev + 1}->{upper}')
        return ans
