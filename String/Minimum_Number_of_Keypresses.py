from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        frequency = Counter(s)
        button = [9, 9, 9]
        count = 0
        for ch, number in sorted(frequency.items(), key=lambda x: -x[1]):
            # print(ch, number)
            for i in range(3):
                if button[i] > 0:
                    button[i] -= 1
                    count += (i + 1) * number
                    break
        return count
