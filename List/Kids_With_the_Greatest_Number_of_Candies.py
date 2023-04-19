class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        res = []
        for num in candies:
            res.append(num + extraCandies >= max_candy)
        return res