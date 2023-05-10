class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        n = len(player1)
        sum1 = 0
        sum2 = 0
        
        for i in range(n):
            prev1 = prev2 = False
            if i - 1 >= 0:
                prev1 = prev1 or player1[i - 1] == 10
                prev2 = prev2 or player2[i - 1] == 10
            if i - 2 >= 0:
                prev1 = prev1 or player1[i - 2] == 10
                prev2 = prev2 or player2[i - 2] == 10
            
            sum1 += (prev1 + 1) * player1[i]            
            sum2 += (prev2 + 1) * player2[i]
            # print(sum1, sum2)
            
        if sum1 > sum2:
            return 1
        elif sum1 < sum2:
            return 2
        else:
            return 0