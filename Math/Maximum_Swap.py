class Solution:
    def maximumSwap(self, num: int) -> int:
        l = list(map(int, list(str(num))))
        
        # If digits in num are decreasing then no need to swap.
        # So find the largest digit increasing.
        idx = 0
        M = None
        for i in range(1, len(l)):
            if not M and l[i] > l[i - 1]:
                idx = i
                M = l[i]
            if M and l[i] >= M:
                idx = i
                M = l[i]

        # No need to swap
        if not M:
            return num
        
        # Find the first element that's smaller than M and swap
        for i in range(idx):
            if l[i] < M:
                l[i], l[idx] = l[idx], l[i]
                break
        
        return int(''.join(map(str, l)))

