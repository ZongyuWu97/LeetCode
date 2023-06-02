class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return 0
        left, right = n // 2 - 1, (n + 1) // 2 
        
        count_l = count_r = 0
        while left >= 0:
            if s[left] != s[left + 1]:
                count_l += left + 1
            left -= 1
        while right <= n - 1:
            if s[right] != s[right - 1]:
                count_r += n - right
            right += 1

        return count_l + count_r - (s[n // 2 - 1] != s[n // 2] and n % 2 == 0) * (n // 2)