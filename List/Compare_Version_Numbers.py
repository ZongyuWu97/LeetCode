class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = list(map(int, version1.split(".")))
        l2 = list(map(int, version2.split(".")))
        n1, n2 = len(l1), len(l2)
        for i in range(min(n1, n2)):
            if l1[i] < l2[i]:
                return -1
            elif l1[i] > l2[i]:
                return 1
        if n1 < n2:
            if sum(l2[n1:]) > 0:
                return -1
        elif n1 > n2:
            if sum(l1[n2:]) > 0:
                return 1
        return 0
