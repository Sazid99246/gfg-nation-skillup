class Solution:
    def longestSubarray(self, arr, k):
        prefix_sum = 0
        max_len = 0
        sum_indices = {}  # Stores first occurrence of prefix_sum

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_len = i + 1

            if (prefix_sum - k) in sum_indices:
                max_len = max(max_len, i - sum_indices[prefix_sum - k])

            # Store first occurrence only
            if prefix_sum not in sum_indices:
                sum_indices[prefix_sum] = i

        return max_len
