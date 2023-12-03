import heapq
class Solution:
    def kBigIndices(self, nums: List[int], k: int) -> int:
        h_left = []
        h_right = []
        n = len(nums)
        left = []
        right = []

        for i in range(n):
            if len(h_left) < k:
                heapq.heappush(h_left, -nums[i])
                heapq.heappush(h_right, -nums[-i - 1])
            else:
                if nums[i] < -h_left[0]:
                    heapq.heapreplace(h_left, -nums[i])
                if nums[-i - 1] < -h_right[0]:
                    heapq.heapreplace(h_right, -nums[-i - 1])
            left.append(-h_left[0])
            right.append(-h_right[0])
        right.reverse()

        count = 0
        for i in range(k, n - k):
            if nums[i] > left[i - 1] and nums[i] > right[i + 1]:
                count += 1
        return count




