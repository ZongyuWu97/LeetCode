class Solution:
    from collections import Counter
    from itertools import permutations

    def largestVariance(self, s: str) -> int:
        counter = Counter(s)
        res = 0
        for a, b in permutations(counter, 2):
            # 分别检查所有两对字符的组合
            a_remain = counter[a]
            b_remain = counter[b]
            max_subarray = 0
            has_a = False
            has_b = False
            for ch in s:
                if ch != a and ch != b:
                    continue

                # 等于a或b
                if ch == a:
                    a_remain -= 1
                    max_subarray += 1
                    has_a = True
                else:
                    b_remain -= 1
                    max_subarray -= 1
                    has_b = True

                # 如果当前窗口a和b都有，则更新res为max_subarray
                if has_a and has_b:
                    res = max(res, max_subarray)

                # 如果当前窗口difference为负，如果后续两个字符都有，则重置窗口，如果都没有则结束当前循环，其他情况继续判断
                if max_subarray < 0:
                    if a_remain != 0 and b_remain != 0:
                        max_subarray = 0
                        has_a = False
                        has_b = False
                    elif a_remain == 0 and b_remain == 0:
                        break

        return res
