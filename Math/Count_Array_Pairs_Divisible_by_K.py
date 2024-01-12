class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        n, res = len(nums), 0
        divisors = []
        counter = Counter()
        
        for i in range(1, k + 1):
            if k % i == 0:
                divisors.append(i)
        
        for i in range(n):
            remainder = k // math.gcd(k, nums[i])
            res += counter[remainder]
            for divisor in divisors:
                if nums[i] % divisor == 0:
                    counter[divisor] += 1
            
        return res