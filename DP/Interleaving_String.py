class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @cache
        def helper(i1, i2, i3):
            if i1 == n1 and i2 == n2:
                return True
            elif i1 == n1:
                return s2[i2:] == s3[i3:]
            elif i2 == n2:
                return s1[i1:] == s3[i3:]

            if s1[i1] == s3[i3]:
                return helper(i1+1, i2, i3+1) or (s2[i2] == s3[i3] and helper(i1, i2+1, i3+1))
            else:
                return s2[i2] == s3[i3] and helper(i1, i2+1, i3+1)

        if not s1:
            return s2 == s3
        elif not s2:
            return s1 == s3

        n1, n2, n3 = len(s1), len(s2), len(s3)
        if not n1 + n2 == n3:
            return False

        return helper(0, 0, 0)
