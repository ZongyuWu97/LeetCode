class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if n < m:
            return -1

        longest_boarder = [0] * m
        curr_prefix = 0
        i = 1
        while i < m:
            if needle[i] == needle[curr_prefix]:
                curr_prefix += 1
                longest_boarder[i] = curr_prefix
                i += 1
            else:
                if curr_prefix == 0:
                    longest_boarder[i] = 0
                    i += 1
                else:
                    curr_prefix = longest_boarder[curr_prefix - 1]

        h_pointer, n_pointer = 0, 0
        while h_pointer < n:
            if needle[n_pointer] == haystack[h_pointer]:
                h_pointer += 1
                n_pointer += 1
                if n_pointer == m:
                    return h_pointer - m
            else:
                if n_pointer == 0:
                    h_pointer += 1
                else:
                    n_pointer = longest_boarder[n_pointer - 1]
        return -1
