class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        store = []
        memo = set()
        num = 1
        while len(store) < n:
            if not k - num in memo:
                memo.add(num)
                store.append(num)
            num += 1
        return sum(store)