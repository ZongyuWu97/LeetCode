class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        ones = sum(data)
        res = ones - sum(data[:ones])
        curr = res

        for i in range(ones, n):
            curr += (data[i] == 0) - (data[i - ones] == 0)
            res = min(curr, res)
        return res