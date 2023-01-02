import math


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def findPrimes(left, right):
            isPrime = [True] * (right + 1)
            for i in range(2, int(math.sqrt(right)) + 1):
                if isPrime[i]:
                    j = i
                    while i * j <= right:
                        isPrime[i * j] = False
                        j += 1
            res = []
            for num in range(max(left, 2), right + 1):
                if isPrime[num]:
                    res.append(num)
            return res

        primes = findPrimes(left, right)
        diff = []
        for i in range(1, len(primes)):
            diff.append((primes[i] - primes[i - 1], i - 1))
        diff.sort()
        return [primes[diff[0][1]], primes[diff[0][1] + 1]] if diff else [-1, -1]
