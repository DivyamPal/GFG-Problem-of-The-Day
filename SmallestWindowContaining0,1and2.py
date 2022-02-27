#User function Template for python3
from collections import Counter
class Solution:
    def smallestSubstring(self, S):
        # Code here
        dic={'0':1,'1':1,'2':1}
        dic2={}
        have,need=0,3
        l,slen=0,float("infinity")
        for r in range(len(S)):
            c=S[r]
            dic2[c]=1+dic2.get(c,0)
            
            if dic2[c]==dic[c]:
                have+=1
            
            while have==need:
                if (r-l+1)<slen:
                    slen=(r-l+1)
                dic2[S[l]]-=1
                if S[l] in dic and dic2[S[l]]< dic[S[l]]:
                    have-=1
                l+=1
        return slen if slen!=float("infinity") else -1
        
