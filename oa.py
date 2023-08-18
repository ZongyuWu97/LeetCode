from collections import deque
import math
def solution(execution):
    n = len(execution)
    memo = {}
    for i, e in enumerate(execution):
        if not e in memo:
            memo[e] = deque([i])
        else:
            memo[e].append(i)

    time = 0
    store = [x for x in execution]
    for i, e in enumerate(execution):
        time += e
        cohesive = memo[store[i]]
        while cohesive and cohesive[0] <= i:
            cohesive.popleft()
        for idx in cohesive:
            execution[idx] = (execution[idx] + 1) // 2
        memo[store[i]] = cohesive
    print(memo, store, execution)
    return time

s = [5, 5, 3, 6, 5, 3]
print(solution(s))
