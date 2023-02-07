class Solution:
    def nextGreaterElement(self, n: int) -> int:
        l = list(map(int, list(str(n))))

        N = len(l)
        i = N - 2
        while i >= 0:
            if l[i] < l[i + 1]:
                break
            i -= 1

        if i == -1:
            return -1

        j = i + 1
        while j <= N - 1:
            if l[j] <= l[i]:
                break
            j += 1

        l[i], l[j - 1] = l[j - 1], l[i]
        l[i + 1:] = reversed(l[i + 1:])

        res = int(''.join(list(map(str, l))))
        return res if res <= 2 ** 31 - 1 else -1
