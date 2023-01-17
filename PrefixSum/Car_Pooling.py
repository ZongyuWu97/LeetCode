class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cache = {}
        for numPassengers, start, end in trips:
            cache[start] = cache.setdefault(start, 0) + numPassengers
            cache[end] = cache.setdefault(end, 0) - numPassengers

        for position in sorted(cache.keys()):
            capacity -= cache[position]

            if capacity < 0:
                return False

        return True
