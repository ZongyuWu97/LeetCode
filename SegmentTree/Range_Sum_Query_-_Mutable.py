class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.segTree = [0] * 2 * self.n
        for i in range(self.n, 2 * self.n):
            self.segTree[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.segTree[i] = self.segTree[2 * i] + self.segTree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        idx = index + self.n
        self.segTree[idx] = val
        while idx > 0:
            left = right = idx
            if idx % 2 == 0:
                right = idx + 1
            else:
                left = idx - 1
            self.segTree[idx // 2] = self.segTree[left] + self.segTree[right]
            idx //= 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        res = 0
        while left <= right:
            if left % 2 == 1:
                res += self.segTree[left]
                left += 1
            if right % 2 == 0:
                res += self.segTree[right]
                right -= 1
            left //= 2
            right //= 2
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
