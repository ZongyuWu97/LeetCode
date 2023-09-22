class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        cups = [[0] * x for x in range(1, 102)]
        cups[0][0] = poured
        for row in range(query_row + 1):
            for cup in range(row + 1):
                champagne = cups[row][cup]
                if champagne > 1:
                    cups[row + 1][cup] += (champagne - 1) / 2
                    cups[row + 1][cup + 1] += (champagne - 1) / 2
        return min(1, cups[query_row][query_glass])