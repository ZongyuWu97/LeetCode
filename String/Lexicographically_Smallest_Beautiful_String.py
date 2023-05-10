class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        A = [ord(ch) - ord('a') for ch in s]
        i = len(A) - 1

        while i >= 0:
            A[i] += 1
            if A[i] == k:
                i -= 1
            elif A[i] not in set(A[max(0, i - 2):i]):
                for j in range(i + 1, len(A)):
                    A[j] = min({0, 1, 2} - set(A[max(0, j - 2):j]))
                return ''.join([chr(ord('a') + i) for i in A])
        return ''