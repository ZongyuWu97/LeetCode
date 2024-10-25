import math


class BinomialHeapq:
    def __init__(self):
        pass

    @staticmethod
    def mergeTree(p, q):
        n = len(p)
        res = [0] * 2 * n
        if p[0] > q[0]:
            p, q = q, p

        h = int(math.log2(n * 2))
        i = 0
        level_start = 0
        for level in range(h):
            num_nodes = math.comb(h - 1, level)
            for j in range(level_start, level_start + num_nodes):
                res[i] = p[j]
                i += 1
            for j in range(level_start, level_start + num_nodes):
                res[i] = q[j]
                i += 1
            level_start += num_nodes
        return res

    @staticmethod
    def extractMin(p):
        n = len(p)
        k = n - 1
        res = p[0]
        while k > 0:
            if p[k] != float("inf"):
                break
            k -= 1

        p[0], p[k] = p[k], float("inf")
        h = int(math.log2(n))
        num_nodes = math.comb(h, 1)
        m = 0
        for i in range(1, num_nodes + 1):
            if p[i] < p[m]:
                m = i
        if m != 0:
            p[0], p[m] = p[m], p[0]
        return res

    @staticmethod
    def insert(p, num):
        if p[-1] != float("inf"):
            return p
        n = len(p)
        k = n - 1
        while k > 0:
            if p[k - 1] != float("inf"):
                break
            k -= 1
        h = math.log2(n)


# print(BinomialHeapq.mergeTree([1, 3], [0, 2]))
# assert BinomialHeapq.mergeTree([1, 3], [0, 2]) == [0, 1, 2, 3]
# print(BinomialHeapq.mergeTree([0, 2], [1, 3]))
# assert BinomialHeapq.mergeTree([0, 2], [1, 3]) == [0, 1, 2, 3]
# print(BinomialHeapq.mergeTree([0], [1]))
# assert BinomialHeapq.mergeTree([0], [1]) == [0, 1]
# print(BinomialHeapq.mergeTree([1], [0]))
# assert BinomialHeapq.mergeTree([1], [0]) == [0, 1]
# print(BinomialHeapq.mergeTree([7, 12, 8, 13], [3, 5, 4, 9]))
# assert BinomialHeapq.mergeTree([7, 12, 8, 13], [3, 5, 4, 9]) == [
#     3,
#     7,
#     5,
#     4,
#     12,
#     8,
#     9,
#     13,
# ]
# print(BinomialHeapq.mergeTree([3, 5, 4, 9], [7, 12, 8, 13]))
# assert BinomialHeapq.mergeTree([3, 5, 4, 9], [7, 12, 8, 13]) == [
#     3,
#     7,
#     5,
#     4,
#     12,
#     8,
#     9,
#     13,
# ]

### Test extractMin
arr = [3, 5, 4, 9]
assert BinomialHeapq.extractMin(arr) == 3
assert arr == [4, 5, 9, float("inf")]
assert BinomialHeapq.extractMin(arr) == 4
assert arr == [5, 9, float("inf"), float("inf")]
assert BinomialHeapq.extractMin(arr) == 5
assert arr == [9, float("inf"), float("inf"), float("inf")]
arr = [3, 7, 5, 4, 12, 8, 9, 13]
assert BinomialHeapq.extractMin(arr) == 3
assert arr == [4, 7, 5, 13, 12, 8, 9, float("inf")]
assert BinomialHeapq.extractMin(arr) == 4
assert arr == [5, 7, 9, 13, 12, 8, float("inf"), float("inf")]
assert BinomialHeapq.extractMin(arr) == 5
assert arr == [7, 8, 9, 13, 12, float("inf"), float("inf"), float("inf")]

arr = [3, 4, 5, 7, 12, 8, 9, 13]
assert BinomialHeapq.extractMin(arr) == 3
assert arr == [4, 8, 5, 7, 12, 13, 9, float("inf")]
assert BinomialHeapq.extractMin(arr) == 4
assert arr == [5, 8, 9, 7, 12, 13, float("inf"), float("inf")]
assert BinomialHeapq.extractMin(arr) == 5
assert arr == [7, 8, 9, 13, 12, float("inf"), float("inf"), float("inf")]


arr = BinomialHeapq.mergeTree([3, 4, 5, 7, 12, 8, 9, 13], [5, 6, 7, 9, 14, 10, 11, 15])
assert BinomialHeapq.extractMin(arr) == 3
assert arr == [4, 5, 8, 5, 7, 6, 7, 9, 12, 15, 9, 14, 10, 11, 13, float("inf")]
assert BinomialHeapq.extractMin(arr) == 4
assert arr == [
    5,
    6,
    8,
    5,
    7,
    10,
    7,
    9,
    12,
    15,
    9,
    14,
    13,
    11,
    float("inf"),
    float("inf"),
]
assert BinomialHeapq.extractMin(arr) == 5
assert arr == [
    5,
    6,
    8,
    9,
    7,
    10,
    7,
    9,
    12,
    15,
    11,
    14,
    13,
    float("inf"),
    float("inf"),
    float("inf"),
]

arr = BinomialHeapq.mergeTree([3, 4, 5, 7, 5, 8, 9, 6], [5, 6, 7, 9, 14, 10, 11, 15])
assert BinomialHeapq.extractMin(arr) == 3
assert arr == [4, 5, 5, 5, 7, 6, 7, 9, 6, 8, 9, 14, 10, 11, 15, float("inf")]
assert BinomialHeapq.extractMin(arr) == 4
assert arr == [5, 6, 5, 5, 7, 10, 7, 9, 6, 8, 9, 14, 15, 11, float("inf"), float("inf")]
assert BinomialHeapq.extractMin(arr) == 5
assert arr == [
    5,
    6,
    6,
    5,
    7,
    10,
    7,
    9,
    11,
    8,
    9,
    14,
    15,
    float("inf"),
    float("inf"),
    float("inf"),
]


# ### Test insert
# arr = BinomialHeapq.mergeTree([3, 4, 5, 7, 5, 8, 9, 6], [5, 6, 7, 9, 14, 10, 11, 15])
# BinomialHeapq.extractMin(arr)
# BinomialHeapq.extractMin(arr)
# BinomialHeapq.extractMin(arr)
# BinomialHeapq.insert(arr, 11)
# assert arr == [
#     5,
#     6,
#     6,
#     5,
#     7,
#     10,
#     7,
#     9,
#     11,
#     8,
#     9,
#     14,
#     15,
#     11,
#     float("inf"),
#     float("inf"),
# ]
# BinomialHeapq.insert(arr, 15)
# assert arr == [5, 6, 6, 5, 7, 10, 7, 9, 11, 8, 9, 14, 15, 11, 15, float("inf")]
# BinomialHeapq.insert(arr, 7)
# assert arr == [5, 6, 6, 5, 7, 7, 7, 9, 11, 8, 9, 10, 15, 11, 15, 14]
