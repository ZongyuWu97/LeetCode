class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:   
        def backtrack(count, curr_sum, idx):
            # 目前已有count个subset，当前记录的subset和，下一个可取的index
            if count == k - 1:
                return True
            if curr_sum == target_sum:
                return backtrack(count + 1, 0, 0)
            elif curr_sum > target_sum:
                return False
            
            for i in range(idx, n):
                if not taken[i]:
                    taken[i] = True
                    if backtrack(count, curr_sum + nums[i], i+1):
                        return True
                    taken[i] = False
            return False
        
        # 如果nums的和不能被整除直接False
        if sum(nums) % k != 0:
            return False
        
        n = len(nums)
        target_sum = sum(nums) // k
        taken = [False] * n
        nums.sort(key=lambda x:-x)

        return backtrack(0, 0, 0)