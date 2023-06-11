class Solution:
    def smallestString(self, s: str) -> str:
        base = ord('a')
        def encode(ch):
            return ord(ch) - base
        
        def decode(i):
            return chr(i + base)

        l = list(map(encode, s))
        n = len(l)
        
        left = n - 1
        for i in range(n):
            if l[i] != 0:
                left = i
                break
        
        right = n - 1
        for i in range(left + 1, n):
            if l[i] == 0:
                right = i - 1
                break
        
        for i in range(left, right + 1):
            l[i] -= 1
            l[i] %= 26
            
        return ''.join(map(decode, l))