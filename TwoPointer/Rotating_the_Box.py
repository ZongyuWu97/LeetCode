class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for i in range(m):
            right = n - 1
            for j in range(n - 1, -1, -1):
                if box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][right] = '#'
                    right -= 1
                elif box[i][j] == '*':
                    right = j - 1 

        rotated = [['.'] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                rotated[j][m - 1 - i] = box[i][j]
        return rotated