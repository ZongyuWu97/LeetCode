class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack = [[x] for x in range(1, n + 1)]
        nextStack = []
        # print(stack)

        step = 1
        while step < k:
            while stack:
                curr = stack.pop()
                for x in range(curr[-1] + 1, n + 1):
                    nextStack.append(curr + [x])
            stack, nextStack = nextStack, stack
            step += 1
        return stack