from itertools import permutations
class Solution:
    def minimumString(self, a: str, b: str, c: str) -> str:
        def compare(s1, s2):
            m, n = len(s1), len(s2)
            for i in range(m):
                for j in range(min(n, m - i)):
                    if s1[i + j] != s2[j]:
                        break
                else:
                    return s1[:i] + s2 + s1[i + n:]
            return s1 + s2
                
                
        perms = permutations([a, b, c])
        possibleArr = []
        for perm in perms:
            possibleArr.append(compare(compare(perm[0], perm[1]), perm[2]))

        return min(possibleArr, key = lambda x:(len(x), x))