class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        num = 0
        n = len(word)
        i = 0
        for ch in abbr:
            if ch.isalpha():
                i += num
                num = 0
                if i == n or ch != word[i]:
                    return False
                i += 1
            else:
                if num == 0 and int(ch) == 0:
                    return False
                num = num * 10 + int(ch)
            # print(i, num)
        return i + num == n
