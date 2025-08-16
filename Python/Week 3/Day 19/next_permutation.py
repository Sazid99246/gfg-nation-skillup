class Solution:
    def nextPermutation(self, arr):
        # code here
        n = len(arr)
        flag = True
        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                flag = False
                break
        # print(flag)
        if flag:
            arr[:] = arr[::-1]
            return
        for j in range(n-1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                break
        arr[:] = arr[:i+1]+arr[n-1:i:-1]
