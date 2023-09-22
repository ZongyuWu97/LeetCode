import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        h = [(0, 0, 0)]
        visited = set([(0, 0, 0)])
        effort = 0
        while h:
            curr, row, col = heapq.heappop(h)
            effort = max(effort, curr)
            # print(curr, row, col)
            # print()
            if row == m - 1 and col == n - 1:
                return effort

            for x, y in directions:
                newRow, newCol = row + x, col + y
                if 0 <= newRow < m and 0 <= newCol < n:
                    nextNode = (abs(heights[row][col] - heights[newRow][newCol]), newRow, newCol)
                    if not nextNode in visited:
                        visited.add(nextNode)
                        heapq.heappush(h, nextNode)
            
