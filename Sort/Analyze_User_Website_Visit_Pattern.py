from collections import defaultdict, Counter
from itertools import combinations


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        people = defaultdict(list)
        n = len(username)
        for user, time, web in sorted(zip(username, timestamp, website), key=lambda x: x[1]):
            people[user].append(web)

        pattern = Counter()
        for user in people:
            pattern.update(set(combinations(people[user], 3)))

        return max(sorted(pattern), key=lambda x: pattern[x])
