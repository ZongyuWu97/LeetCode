#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.


def minimumSwaps(arr):
    n = len(arr)
    arr = [*enumerate(arr)]
    arr.sort(key=lambda x: x[1])

    visited = [False] * n
    ans = 0
    for i in range(n):
        if visited[i] or arr[i][0] == i:
            continue

        j = i
        cycle_size = 0
        while not visited[j]:
            visited[j] = True
            j = arr[j][0]
            cycle_size += 1

        ans += cycle_size - 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
