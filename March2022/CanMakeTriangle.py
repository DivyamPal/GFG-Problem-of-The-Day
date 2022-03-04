#User function Template for python3
class Solution:
    def canMakeTriangle(self, a, n): 
        #code here
        def check(a,b,c):
            if a+b>c and a+c>b and c+b >a:
                return True
            return False
            
        result=[]   
        for i in range(0,len(a)-2):
            if check(a[i],a[i+1],a[i+2]):
                result.append(1)
            else:
                result.append(0)
        return result
