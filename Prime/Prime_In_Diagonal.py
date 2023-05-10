class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        prune = lambda x: x in (2, 3) or (x % 6 in (1, 5) and x > 3)
        isPrime = lambda x: all(x % y for y in filter(prune, range(int(sqrt(x)) + 1)))

        n = len(nums)

        diagonals = sorted(
            filter(prune, {nums[i][i] for i in range(n)} | {nums[i][- i - 1] for i in range(n)}),
            reverse=True
        )

        for num in diagonals:
            if isPrime(num):
                return num
        return 0