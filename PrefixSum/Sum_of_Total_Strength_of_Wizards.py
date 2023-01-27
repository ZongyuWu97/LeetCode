from itertools import accumulate


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        n = len(strength)
        mod = 10 ** 9 + 7

        # Fitst min to the right.
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and strength[stack[-1]] > strength[i]:
                right[stack.pop()] = i
            stack.append(i)

         # Fitst min to the left.
        left = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and strength[stack[-1]] >= strength[i]:
                left[stack.pop()] = i
            stack.append(i)

        # Compute prefix sum.
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + strength[i - 1]

        acc_prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            acc_prefix[i] = acc_prefix[i - 1] + prefix[i]

        res = 0
        for i in range(n):
            l = left[i]
            r = right[i]

            curr_sum = -(acc_prefix[i] - acc_prefix[max(l, 0)]) * (r - i)\
                + (acc_prefix[r] - acc_prefix[i]) * (i - l)
            res = (res + curr_sum * strength[i]) % mod

        return res
