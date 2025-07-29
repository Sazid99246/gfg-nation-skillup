class Solution:
    def asciirange(self, s):
        result = []
        n = len(s)

        # Initialize all indices to -1
        first = [-1] * 26
        last = [-1] * 26

        # Track first and last
        # occurrence of each character
        for i in range(n):
            idx = ord(s[i]) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            else:
                last[idx] = i

        # Compute ASCII sums
        # between first and last occurrence
        for i in range(26):
            if first[i] != -1 and last[i] != -1:
                sumval = 0
                for j in range(first[i] + 1, last[i]):
                    sumval += ord(s[j])
                if sumval != 0:
                    result.append(sumval)

        # Sort the results in increasing order

        return result
