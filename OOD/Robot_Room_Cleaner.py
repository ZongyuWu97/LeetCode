# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        def goBack():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(row, col, direction):
            visited.add((row, col))
            robot.clean()

            for i in range(4):
                new_direction = (direction + i) % 4
                new_row, new_col = row + \
                    directions[new_direction][0], col + \
                    directions[new_direction][1]

                if not (new_row, new_col) in visited and robot.move():
                    dfs(new_row, new_col, new_direction)
                    goBack()

                robot.turnRight()

        visited = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dfs(0, 0, 0)
        # print(visited)
