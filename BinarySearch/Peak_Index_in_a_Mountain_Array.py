class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n - 1
        while l < r:
            mid = (l + r) // 2

            if r - l == 1:
                return l if arr[l] > arr[r] else r
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            if arr[mid - 1] < arr[mid]:
                l = mid
            else:
                r = mid
        

