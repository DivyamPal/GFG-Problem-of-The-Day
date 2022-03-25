#User function Template for python3
import bisect
import copy
def greaterElement (arr,  n) : 
    #Complete the function
    temp = copy.deepcopy(arr)
    arr.sort()
    ans = [0 for i in range(n)]
    for i in range(n):
        idx = bisect.bisect(arr,temp[i])
        #print(arr[i],idx)
        if idx <= n-1:
            ans[i] = arr[idx]
        else:
            ans[i] = -10000000
    return ans
