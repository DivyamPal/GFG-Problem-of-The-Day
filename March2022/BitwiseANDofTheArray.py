import sys
class Solution:
    def count(self, N, A, X): 
        # code here
        ans=sys.maxsize
        m=0
        for i in range(31,-1,-1):
            if((X>>i)&1):
                m|=(1<<i)
                continue
            count=0
            temp=m|(1<<i)
            for i in range(N):
                if((A[i]&temp)==temp):
                    count+=1
            ans=min(ans,N-count)
        return ans
