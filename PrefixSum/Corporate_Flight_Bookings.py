class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cache = [0] * n

        for first, last, seats in bookings:
            cache[first - 1] += seats
            if last < n:
                cache[last] -= seats

        prefix = 0
        for i in range(n):
            prefix += cache[i]
            cache[i] = prefix

        return cache
