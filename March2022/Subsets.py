#User function Template for python3
from itertools import combinations
class Solution:
    def subsets(self, a):
        #code here
        res=[()]
        for x in range(1,len(a)+1):
            l=list(combinations(a,x))
            for i in l:
               res.append(i)
        return sorted(res)
