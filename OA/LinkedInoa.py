
numCalls = [2, 2, 2, 2, 5, 5, 5, 8]
alertThreshold = 4
precedingMinutes = 3


def linkedIn1(numCalls, alertThreshold, precedingMinutes):
    n = len(numCalls)
    if n <= precedingMinutes:
        return 0
    thres = alertThreshold * precedingMinutes
    curr = sum(numCalls[:precedingMinutes])
    res = int(curr > thres)
    l = 0
    for r in range(precedingMinutes, n):
        curr += numCalls[r] - numCalls[l]
        l += 1
        res += int(curr > thres)
    return res

print(linkedIn1(numCalls, alertThreshold, precedingMinutes))

from collections import Counter
def linkedIn2(a, b):
    def erase(a):
        for i, ch in enumerate(a):
            if ch != 0:
                return a[i:]
        return '0'
    
    def factorial(count):
        res = 1
        while count:
            res *= count
            count -= 1
        return res
    
    def similar(b):
        c = Counter(b)
        l = list(reversed(sorted(c.keys())))
        n = c[l[0]]
        res = 1
        for idx in range(1, len(l)):
            count = c[l[idx]]
            isZero = int(l[idx] == '0')
            res *= factorial(n + count - isZero) / (factorial(count) * factorial(n - isZero))
            n += count
        return res
            

    b = erase(b)
    if b == '0':
        return 1
    
    return similar(b)

a = '1234'
b = '2341'
print(linkedIn2(a, b))

a = '1100'
b = '1001'
print(linkedIn2(a, b))

a = '93700587'
b = '98757003'
print(linkedIn2(a, b))