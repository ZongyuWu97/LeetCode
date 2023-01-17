class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        cache = [0] * length

        for start, end, val in updates:
            cache[start] += val
            if end + 1 < length:
                cache[end + 1] -= val

        currSum = 0
        for i in range(length):
            currSum += cache[i]
            cache[i] = currSum

        return cache
