class Solution:
    def partitionString(self, s: str) -> int:
        currWindow = set()
        res = 0

        for ch in s:
            if ch in currWindow:
                res += 1
                currWindow = set()

            currWindow.add(ch)

        return res + 1
