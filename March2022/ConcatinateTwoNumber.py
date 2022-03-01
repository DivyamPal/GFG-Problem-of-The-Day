class Solution:
    def countPairs(self, n, x, numbers): 
        #code here
        st={}
        for i in numbers:
            st[str(i)]=st.get(str(i),0)+1
        x=str(x)
        left=x[0]
        right=x[1::]
        count=0
        while(len(right)>0):
            if left in st and right in st:
                if left==right:
                    count+=((st[left]*st[right])-st[left])
                else:
                    count+=(st[left]*st[right])
            left+=right[0]
            right=right[1::]
        return count
