class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        gates = []
        visited = set()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    gates.append((i, j, 0))
                    visited.add((i, j))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque(gates)
        while q:
            row, col, dis = q.popleft()
            for x, y in directions:
                newRow, newCol = row + x, col + y
                if 0 <= newRow < m and 0 <= newCol < n and not (newRow, newCol) in visited and not rooms[newRow][newCol] == -1:
                    visited.add((newRow, newCol))
                    rooms[newRow][newCol] = dis + 1
                    q.append((newRow, newCol, dis + 1))
