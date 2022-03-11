#User function Template for python3

class Solution:
    def findHeight(self, N, arr):
        # code here
        arr[0] = 1 
        for i in range(1,N):
            arr[i] = arr[arr[i]] + 1
        return arr[N-1]
