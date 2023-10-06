class Solution:
    def decodeString(self, s: str) -> str:
        countStack = []
        stringStack = []
        currString = ''
        currCount = ''
        for ch in s:
            if ch.isdigit():
                currCount += ch
            elif ch == '[':
                countStack.append(currCount)
                currCount = ''
                stringStack.append(currString)
                currString = ''
            elif ch.isalpha():
                currString += ch
            elif ch == ']':
                currString *= int(countStack.pop())
                currString = stringStack.pop() + currString
        return currString
            