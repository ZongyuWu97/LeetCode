class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res = min(divisors)
        max_count = 0
        for divisor in divisors:
            count = 0
            for num in nums:
                count += num % divisor == 0
            if count > max_count:
                max_count = count
                res = divisor
            elif count == max_count:
                res = min(res, divisor)
        return res
        