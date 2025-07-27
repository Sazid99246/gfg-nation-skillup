class Solution:
    def extractPoints(self, arr):
        if not arr:
            return []
        if len(arr) == 1:
            return [arr[0]]

        n = len(arr)
        result = [arr[0]]

        i = 1

        while i < n and arr[i] == arr[i - 1]:
            i += 1

            if i == n:
                return result

        prev_dir = 1 if arr[i] > arr[i - 1] else -1

        for j in range(i + 1, n):
            if arr[j] == arr[j - 1]:
                continue

            curr_dir = 1 if arr[j] > arr[j - 1] else -1
            if curr_dir != prev_dir:
                result.append(arr[j - 1])
                prev_dir = curr_dir

        if result[-1] != arr[-1]:
            result.append(arr[-1])

        return result
