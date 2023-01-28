def getMex(a, i, j):
    mex = 0
    seen = set()
    for k in range(i, j + 1):
        el = a[k]
        seen.add(el)

        while mex in seen:
            mex += 1

    return mex


def mexReduction(a):
    n = len(a)
    # mex is the highest mex possible for any suffix of a
    # at any given time, initially the suffix is the whole array
    mex = getMex(a, 0, n - 1)
    # count of elements in the suffix we're dealing with
    ct = defaultdict(int)
    for el in a:
        ct[el] += 1

    ret = []

    i = 0
    while i < n:
        print(i)
        curMex = 0
        seen = set()
        # the only way to get the lexicographically maximum
        # array is to always take the highest mex possible,
        # so we will do that and stop as soon as we have it
        while curMex != mex:
            el = a[i]
            ct[el] -= 1
            seen.add(el)

            while curMex in seen:
                curMex += 1
            i += 1
        ret.append(curMex)

        # if curMex is 0, we need to take at least one element
        if curMex == 0:
            i += 1

        # next mex must be less than or equal to curMex,
        # and curMex <= the number of elements we just iterated
        # so this part of the code is O(N) worst case, BUT
        # it's also O(N) amortized over the whole call even
        # in the worst case, so overall TC is still O(N).
        nextMex = 0
        while ct[nextMex] > 0:
            nextMex += 1
        mex = nextMex

    return ret
