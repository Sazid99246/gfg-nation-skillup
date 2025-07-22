class Solution:
    def median(self, arr):
        arr = sorted(arr)
        if len(arr) % 2 != 0:
            return arr[len(arr) // 2]
        else:
            return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) // 2

    def mean(self, arr):
        return sum(arr) // len(arr)
