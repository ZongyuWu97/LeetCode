class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i, c in enumerate(word):
            if c == ch:
                return "".join(reversed(word[: i + 1])) + word[i + 1 :]
        return word
