class Solution:
    def searchInsertK(self, arr, n, k):
        # code here
        for i in range(n):
            if arr[i]==k:
                return i
                break
            if arr[i]>k:
                return i
            if k>arr[-1]:
                return n 
