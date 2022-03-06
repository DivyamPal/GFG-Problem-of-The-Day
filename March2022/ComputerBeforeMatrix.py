class Solution:
    def computeBeforeMatrix(self, N, M, after):
        # Code here
        for j in range(M-1, -1, -1):
            for i in range(N-1, -1, -1):
                if i - 1 < 0:
                    val1 = 0
                else:
                    val1 = after[i-1][j]
                if j - 1 < 0:
                    val2 = 0
                else:
                    val2 = after[i][j-1]
                if i-1 < 0 or j-1 < 0:
                    val3 = 0
                else:
                    val3 = after[i-1][j-1]
                    
                after[i][j] = after[i][j] - (val1+val2) + val3
        return after 
