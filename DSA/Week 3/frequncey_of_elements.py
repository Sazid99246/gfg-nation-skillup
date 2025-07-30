class Solution:
    def countFreq(self, arr):
        freq = {}
        result = []
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        for key, value in freq.items():
            result.append([key, value])
        return result
