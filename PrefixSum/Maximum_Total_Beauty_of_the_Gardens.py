class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        A = [min(target, a) for a in flowers]
        A.sort()
		
		# Two edge cases
        if min(A) == target: return full * len(A)
        if newFlowers >= target * len(A) - sum(A):
            return max(full*len(A), full*(len(A)-1) + partial * (target-1))
        
		# Build the array `cost`.
        cost = [0]
        for i in range(1, len(A)):
            pre = cost[-1]
            cost.append(pre + i * (A[i] - A[i - 1]))

		# Since there might be some gardens having `target` flowers already, we will skip them.
        j = len(A) - 1
        while A[j] == target:
            j -= 1
        
		# Start the iteration
        ans = 0
        while newFlowers >= 0:
		
			# idx stands for the first `j` gardens, notice a edge case might happen.
            idx = min(j, bisect.bisect_right(cost, newFlowers) - 1)
			
			# bar is the current minimum flower in the incomplete garden
            bar = A[idx] + (newFlowers - cost[idx]) // (idx + 1)
			
            ans = max(ans, bar * partial + full *(len(A) - j - 1))
            
			# Now we would like to complete garden j, thus deduct the cost for garden j 
			# from new and move on to the previous(next) incomplete garden!
            newFlowers -= (target - A[j])
            j -= 1
            
        return ans