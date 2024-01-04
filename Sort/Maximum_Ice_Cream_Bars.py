class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = [0] * (10 ** 5)
        for c in costs:
            count[c - 1] += 1
        
        cnt = 0
        for i, c in enumerate(count):
            num = i + 1
            if coins >= num * c:
                coins -= num * c
                cnt += c
            else:
                cnt += coins // num 
                return cnt
        return cnt
