class Solution:
    def findDuplicates(self, arr):
        arr.sort()
        result = []
        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                result.append(arr[i])
        return result


s = Solution()
print(s.findDuplicates([2, 3, 1, 2, 3]))
