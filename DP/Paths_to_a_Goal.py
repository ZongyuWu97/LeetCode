def paths_to_a_goal(s, n, x, y):
    # https://leetcode.com/discuss/interview-question/800573/path-to-a-goal-coding-question-asked-at-gameskraft
    # s - string of instructions
    # n - longest number line
    # x - starting point
    # y - ending point
    # return - number of distinct path that starting at x and ending at y
    # dp
    # 1. previous sum
    MODULO = 10 ** 9 + 7
    pre_sum = [0] * len(s)
    idx_l = idx_r = -1
    for i in range(len(pre_sum)):
        if s[i] == 'l':
            pre_sum[i] = idx_l
            idx_l = i
        else:
            pre_sum[i] = idx_r
            idx_r = i

    # 2. dp
    # dp[i][j] be the number of ways to use the first i letters of s to end up at position j
    # Base case: dp[0][x] = 1. All else is 0.
    # Recurrence: Set dp[i][j] = dp[i-1][j] (corresponds to don't use current character).
    # Then, if s[i] (1-indexed) is l, add dp[i-1][j+1] (j+1 <= n). Otherwise, add dp[i-1][j-1] (j-1 >= 0).
    dp = [[0] * (n + 1) for _ in range(len(s) + 1)]
    dp[0][x] = 1
    for i in range(1, len(s) + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
            if s[i - 1] == 'l':
                if j + 1 <= n:
                    dp[i][j] += dp[i - 1][j + 1]
                    if pre_sum[i - 1] >= 0:
                        dp[i][j] -= dp[pre_sum[i - 1]][j + 1]
            else:
                if j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]
                    if pre_sum[i - 1] >= 0:
                        dp[i][j] -= dp[pre_sum[i - 1]][j - 1]
            dp[i][j] = (dp[i][j] + MODULO) % MODULO
    return dp[len(s)][y]
