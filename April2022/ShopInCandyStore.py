class Solution:

    def candyStore(self, candies,N,K):
        # code here
        candies.sort()
        minn,maxx=0,0
        n=N
        for i in range(n):
            minn+=candies[i]
            maxx+=candies[n-i-1]
            N-=(1+K)
            if N<=0:
                break
        return minn, maxx
        
