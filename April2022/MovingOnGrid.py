class Solution:
	def movOnGrid(self, r, c):
		# code here
		r=(r-1)%7
		c=(c-1)%4
		if r!=c:
		    return 'JON'
		return 'ARYA'
