class Solution:
    def maxConsecBits(self, arr):
        count_1 = 0
        count_0 = 0
        max_1 = count_1
        max_0 = count_0
        for i in range(0, len(arr)):
            if arr[i] == 0:
                count_0 += 1
                count_1 = 0
                if count_0 > max_0:
                    max_0 = count_0
            elif arr[i] == 1:
                count_1 += 1
                count_0 = 0
                if count_1 > max_1:
                    max_1 = count_1
        return max(max_1, max_0)
