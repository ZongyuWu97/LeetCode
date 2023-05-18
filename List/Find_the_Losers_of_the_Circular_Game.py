class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        people = [0] * n
        people[0] = 1
        curr = 0
        turn = 1
        while people[(curr + turn * k) % n] == 0:
            curr += turn * k
            curr %= n
            turn += 1
            people[curr] = 1
        return list(i + 1 for i in filter(lambda x: people[x] == 0, range(n)))