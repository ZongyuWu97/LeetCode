class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters = []
        digits = []
        for log in logs:
            if log[-1].isalpha():
                i = 0
                while True:
                    if log[i] == ' ':
                        letters.append((log[:i], log[i + 1:]))
                        break
                    i += 1
            else:
                digits.append(log)

        letters.sort(key=lambda x: (x[1], x[0]))
        ans = []
        for log in letters:
            ans.append(log[0] + ' ' + log[1])
        ans.extend(digits)
        return ans
