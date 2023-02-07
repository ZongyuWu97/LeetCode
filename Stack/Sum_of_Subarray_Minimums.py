class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)

        rightLess = [n] * n
        stack = []
        for i in range(n):
            while stack and arr[i] < arr[stack[-1]]:
                rightLess[stack.pop()] = i
            stack.append(i)

        leftLargeEqual = [-1] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                leftLargeEqual[stack.pop()] = i
            stack.append(i)

        ans = 0
        MOD = 10 ** 9 + 7
        for i in range(n):
            ans += arr[i] * (rightLess[i] - i) * (i - leftLargeEqual[i])
            ans %= MOD

        return ans
