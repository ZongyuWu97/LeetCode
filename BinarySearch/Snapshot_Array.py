class SnapshotArray:

    def __init__(self, length: int):
        self.length = length
        self.snaps = [[(-1, 0)] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        if self.snap_id == self.snaps[index][-1][0]:
            self.snaps[index].pop()
        self.snaps[index].append((self.snap_id, val))

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        curr = self.snaps[index]
        n = len(curr)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2
            if curr[mid][0] < snap_id:
                l = mid + 1
            else:
                r = mid

        if snap_id > curr[-1][0] and l == n - 1:
            return curr[l][1]
        return curr[l][1] if snap_id == curr[l][0] else curr[l - 1][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
