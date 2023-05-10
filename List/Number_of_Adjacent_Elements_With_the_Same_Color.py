class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        nums = [0] * n
        count = 0
        ans = []
        
        for idx, color in queries:
            if color == nums[idx]:
                ans.append(count)
                continue
            prev = nums[idx]
            nums[idx] = color
            
            if idx != 0:
                if nums[idx - 1] == 0:
                    pass
                elif nums[idx] == nums[idx - 1]:
                    count += 1
                elif prev == nums[idx - 1]:
                    count -= 1
                    
            if idx != n - 1:
                if nums[idx + 1] == 0:
                    pass
                elif nums[idx] == nums[idx + 1]:
                    count += 1
                elif prev == nums[idx + 1]:
                    count -= 1
            ans.append(count)
            
        return ans
            
        