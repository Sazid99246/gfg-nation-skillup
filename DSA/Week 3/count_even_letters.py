class Solution:
    def count(self, s):
        result = 0
        freq = {}
        for l in s:
            freq[l] = freq.get(l, 0) + 1

        for value in freq.values():
            if value % 2 == 0:
                result += 1
        return result
