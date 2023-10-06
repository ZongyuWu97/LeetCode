from sortedcontainers import SortedList
class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        # constructure the sweep line
        records = []
        max_pos = 0
        for i, [start, end] in enumerate(paint):
            records.append((start, i, 1)) # use 1 and -1 to records the type.
            records.append((end, i, -1))
            max_pos = max(max_pos, end)
        records.sort()

        # sweep across all position
        ans = [0 for _ in range(len(paint))]
        indexes = SortedList()
        i = 0
        for pos in range(max_pos + 1):
            while i < len(records) and records[i][0] == pos:
                pos, index, type = records[i]
                if type == 1:
                    indexes.add(index)
                else:
                    indexes.remove(index)
                i += 1
            if indexes:
                ans[indexes[0]] += 1
        return ans