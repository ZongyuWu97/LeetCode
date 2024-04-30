# Given an array of n integers, arr[n], determine all of its subsequences S of
# three elements and find the validity of arr. validity = min(3 * abs(mean(S) - median(S))
# for all 5 A subsequence is a sequence that can be derived from a sequence
# by deleting zero or more elements without changing the order of the remaining
# elements, for example [3, 4] is a subsequence of [5, 3, 2, 4].


def min_abs_diff_mean_median(arr):
    arr.sort()
    n = len(arr)
    min_diff = float("inf")

    for i in range(n - 2):
        # Considering all pairs of elements to the right of arr[i]
        j = i + 1
        k = n - 1

        while j < k:
            subseq = [arr[i], arr[j], arr[k]]
            subseq_mean = sum(subseq) / 3
            subseq_median = subseq[
                1
            ]  # Since the array is sorted, median is the middle element.
            diff = abs(subseq_mean - subseq_median)
            min_diff = min(min_diff, diff)

            # Move j or k depending on which side yields a smaller difference
            if subseq_mean < subseq_median:
                j += 1
            else:
                k -= 1

    return min_diff


# Example usage:
arr = [2, 3, 1, 4]
print(min_abs_diff_mean_median(arr))  # Output will be 0.6666666666666667
