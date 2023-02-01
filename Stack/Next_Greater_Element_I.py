class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}
        for i, num in enumerate(nums2):
            while stack and num > nums2[stack[-1]]:
                nextGreater[nums2[stack.pop()]] = num
            stack.append(i)

        res = []
        for num in nums1:
            res.append(nextGreater.get(num, -1))

        return res
