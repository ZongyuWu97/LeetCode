from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        q = deque([("(", 1, 1)])
        while q:
            curr = q.popleft()
            # curr = (parenthesis, number of parenthesis, number of ( )
            if curr[1] == 2 * n:
                ans.append(curr[0])
                continue

            if curr[2] < n:
                q.append((curr[0] + "(", curr[1] + 1, curr[2] + 1))
            if curr[2] > curr[1] // 2:
                q.append((curr[0] + ")", curr[1] + 1, curr[2]))
        return ans
