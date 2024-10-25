class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        ans = [[1], [1, 1]]
        for _ in range(numRows - 2):
            curr = [1]
            for i in range(len(ans[-1]) - 1):
                curr.append(ans[-1][i] + ans[-1][i + 1])
            curr.append(1)
            ans.append(curr)
        return ans
