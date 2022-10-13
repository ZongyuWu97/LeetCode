class Solution:
    def countArrangement(self, n: int) -> int:
        def backtrack(idx):
            # 在idx上放下一个元素。count是目前已有的beautiful arrangement
            if idx == n+1:
                self.count += 1
                return
            for num in range(1, n+1):
                if not taken[num]:
                    if idx % num == 0 or num % idx == 0:
                        taken[num] = True
                        backtrack(idx+1)
                        taken[num] = False

        taken = [False]*(n+1)
        self.count = 0
        backtrack(1)
        return self.count
