class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = []
        for word in arr:
            if word:
                if word == '.':
                    continue
                if word == '..':
                    if stack:
                        stack.pop()
                    continue
                stack.append(word)
        return '/' + '/'.join(stack)