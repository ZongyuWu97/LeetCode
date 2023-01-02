class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        cnt = defaultdict(int)
        pivot = nums.index(k)
        n = len(nums)

        # Compute balance for index right to pivot.
        bal = 0
        for i in range(pivot, n):
            if nums[i] > k:
                bal += 1
            elif nums[i] < k:
                bal -= 1
            cnt[bal] += 1

        # Compute balance for index left to pivot and count number of subarrays
        bal = 0
        res = 0
        for i in range(pivot, -1, -1):
            if nums[i] > k:
                bal += 1
            elif nums[i] < k:
                bal -= 1

            # Use -bal and -bal + 1 here due to odd and even of subarray.
            res += cnt[-bal] + cnt[-bal + 1]

        return res
