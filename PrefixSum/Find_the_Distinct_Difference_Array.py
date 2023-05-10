class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        s_pref = set()
        s_suf = set()
        pref = []
        suf = []
        n = len(nums)
        
        for i in range(n):
            s_pref.add(nums[i])
            pref.append(len(s_pref))
            
        for i in range(n):
            suf.append(len(s_suf))
            s_suf.add(nums[-i - 1])
        suf.reverse()

        
        res = [pref[i] - suf[i] for i in range(n)]
        return res
        