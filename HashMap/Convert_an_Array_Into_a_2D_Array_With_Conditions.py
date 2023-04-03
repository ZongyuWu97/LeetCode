class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        res = [[] for _ in range(max(count.values()))]
        for num in count:
            for i in range(count[num]):
                res[i].append(num)
        return res