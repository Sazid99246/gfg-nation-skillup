class Solution:
    def sortInWave(self, arr):
        arr.sort()
        for i in range(0, len(arr)-1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
