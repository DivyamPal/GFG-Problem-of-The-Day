#User function Template for python3
class Solution:
    def countStrings(self, s): 
        #code here
        n = len(S)
        charSet = {}
        count = 0
        for i in S:
            if i in charSet:
                count = count + charSet[i] + 1
                charSet[i] += 1
            else:
                charSet[i] = 0
        ans = (n*(n-1)) // 2
        if(count >0):
            ans = ans - count + 1
        return ans
