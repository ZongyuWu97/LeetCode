class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getOnes(num):
            count = 0
            while num != 0:
                num, remainder = divmod(num, 2)
                count += remainder
            return count

        fre = {}
        for num in sorted(arr):
            count = getOnes(num)
            if count in fre:
                fre[count].append(num)
            else:
                fre[count] = [num]

        ans = []
        for num in sorted(fre.keys()):
            ans += fre[num]
        return ans

# one liner
# 	return sorted(arr, key=lambda x: (bin(x).count('1'), x));
