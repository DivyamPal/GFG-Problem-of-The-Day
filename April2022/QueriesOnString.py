class Solution:
	def SolveQueris(self, s, query):
		# Code here
		result=[]
		for i,j in  query:
		  #  print(i,j)
		    result.append(len(set(s[i-1:j])))
		return result
