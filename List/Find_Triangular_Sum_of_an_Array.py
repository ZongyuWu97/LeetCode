class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        Cnk = 1
        ans = 0
        for i in range(n):
            ans = (ans + Cnk * nums[i]) % 10
            # ans %= 10
            # print(Cnk)
            Cnk = Cnk * (n - 1 - i) // (i + 1)
            # print(Cnk)
        return int(ans)
