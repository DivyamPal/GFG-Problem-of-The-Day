#User function Template for python3

class Solution:
	def FindWays(self, matrix):
		# Code here
		dp=[[[0,0] for i in range(len(matrix))] for j in range(len(matrix))]
		dp[0][0]=[1,0]
		for i in range(len(matrix)):
		    for j in range(len(matrix)):
		        if i>0 and matrix[i-1][j] in (2,3):
		            dp[i][j][0]+=dp[i-1][j][0]
		            dp[i][j][1]= max(dp[i][j][1],dp[i-1][j][1])
		        if j>0 and matrix[i][j-1] in (1,3):
		           dp[i][j][0]+=dp[i][j-1][0]
		           dp[i][j][1]= max(dp[i][j][1],dp[i][j-1][1])
		        if dp[i][j][0]>0:
		            dp[i][j][0]%=1000000007
		            dp[i][j][1]+=matrix[i][j]
		return dp[-1][-1]
