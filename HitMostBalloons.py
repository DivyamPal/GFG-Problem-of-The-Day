class Solution: 
    def mostBalloons(self, n, points):
        # Code here
        if n<3:
           return n
        max_val=0
        for i in points:
           d = {}
           dups = 0
           cur_max = 0
           for j in points:
               if i!=j:
                   if j[0]==i[0]:
                       slope='inf'
                   else:
                       slope=float(j[1]-i[1])/float(j[0]-i[0])
                   d[slope] = d.get(slope,0)+1
                   cur_max=max(cur_max, d[slope])
               else:
                   dups+=1
           max_val=max(max_val, cur_max+dups)
        return max_val

      
