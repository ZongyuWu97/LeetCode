class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))

        maxSeen = 0
        cnt = 0
        for _, defence in properties[::-1]:
            if defence < maxSeen:
                cnt += 1
            maxSeen = max(maxSeen, defence)
        return cnt
