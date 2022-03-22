#User function Template for python3

import bisect
def Smallestonleft (arr,  n) : 
    #Complete the function
    #Using Bisect
    res=[]
    l=[]
    for i in arr:
        bisect.insort(l,i)
        temp=bisect.bisect_left(l,i)
        if temp:
            res.append(l[temp-1])
        else:
            res.append(-1)
    return res
    
    
    #TLE
    # res=[]
    # res.append(-1)
    # for i in range(1,n):
    #     l=arr[:i]
    #     while len(l)>0 and arr[i]<max(l):
    #         temp=max(l)
    #         l.remove(temp)
    #     if l:
    #         res.append(max(l))
    #     else:
    #         res.append(-1)
    # return res
        
