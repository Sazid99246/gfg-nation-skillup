from collections import defaultdict


class Solution:
    def majorityElement(self, arr):
        n = len(arr)

        countMap = defaultdict(int)

        for num in arr:
            countMap[num] += 1

            if countMap[num] > n // 2:
                return num

        return -1
