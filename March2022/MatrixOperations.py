class Solution:
    def endPoints(self, matrix, m, n):
        ##code here
        dir = 0 #0 - right, 1 - down, 2 - left, 3 - up
        i = 0
        j = 0
        while 0<=i<m and 0<=j<n:
            v = matrix[i][j]
            if v==0:
                if dir==0:
                    j = j+1
                elif dir==1:
                    i = i+1
                elif dir==2:
                    j = j-1
                else:
                    i = i-1
            else:
                dir = (dir+1)%4
                matrix[i][j] = 0
               
        if i==-1:
            i = 0
        elif i==m:
            i = i-1
        elif j==-1:
            j = 0
        elif j==n:
            j = j-1
           
        return [i,j]
