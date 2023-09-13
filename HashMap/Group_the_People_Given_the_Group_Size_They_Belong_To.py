class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        count = defaultdict(list)
        for idx, size in enumerate(groupSizes):
            count[size].append(idx)
        
        ans = []
        for size in count:
            tmp = []
            for p in count[size]:
                tmp.append(p)
                if len(tmp) == size:
                    ans.append(tmp)
                    tmp = []
        return ans