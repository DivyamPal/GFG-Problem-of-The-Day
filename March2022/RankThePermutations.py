class Solution:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n-1)
	def findRank(self, S):
		#Code here
		n=len(S)
        res=0
        for i in range(n):
            count=0
            for j in range(i+1, n):
                if S[j] < S[i]:
                    count+=1
            res+=count*self.factorial(n-i-1)
        return res+1
