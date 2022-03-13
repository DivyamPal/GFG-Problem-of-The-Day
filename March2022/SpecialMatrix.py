
class Solution:
	def FindWays(self, R, C, blocked):
		# Code here
		maze = [[0 for j in range(C)] for i in range(R)]
		for b in blocked:
            maze[b[0] - 1][b[1] - 1] = -1
            
        if (maze[0][0] == -1) or (maze[R-1][C-1] == -1):
            return 0
            
        for i in range(R):
            if (maze[i][0] == 0):
                maze[i][0] = 1
            else:
                break
            
        for i in range(1, C, 1):
            if (maze[0][i] == 0):
                maze[0][i] = 1
            else:
                break
            
        for i in range(1, R, 1):
            for j in range(1, C, 1):
                
                if (maze[i][j] == -1):
                    continue
                
                if (maze[i - 1][j] > 0):
                    maze[i][j] = (maze[i][j] + maze[i - 1][j])
                    
                if (maze[i][j - 1] > 0):
                    maze[i][j] = (maze[i][j] + maze[i][j - 1])
 
        return maze[R-1][C-1] % (10**9 + 7)
