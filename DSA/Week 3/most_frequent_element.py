class Solution:
    def mostFreqEle(self, arr):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(list(freq.values()))

        for key, value in list(freq.items()):
            if value != max_freq:
                del freq[key]

        return max(list(freq.keys()))
