class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def ok(x):
            # Check if there exists k distinct candies with minimum difference larger or equal to x.
            prev, i, count = price[0], 1, 1
            while count < k and i < n:
                if price[i] - prev >= x:
                    count += 1
                    prev = price[i]
                i += 1
            return count == k

        n = len(price)
        price.sort()
        low, high = 0, price[-1] - price[0]

        while low < high:
            mid = (low + high) // 2 + 1
            if ok(mid):
                low = mid
            else:
                high = mid - 1

        return low
