from collections import Counter

class Solution:
    def cntSpecialNum(self, arr):
        max_val = max(arr)
        freq = Counter(arr)
        mark = [0] * (max_val + 1)

        # Step 1: Mark all multiples
        for num in freq:
            for mult in range(num * 2, max_val + 1, num):
                mark[mult] += freq[num]

        # Step 2: Count special numbers
        count = 0
        for num in arr:
            if freq[num] > 1 or mark[num] > 0:
                count += 1
        return count
