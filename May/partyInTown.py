class Solution:
    def partyHouse(self, N, adj):
        def dfs(n,d,vis,res):
            vis.add(n)
            res[0] = max(res[0],d)
            for ech in adj[n]:
                if ech not in vis:
                    dfs(ech,d+1,vis,res)
            
        ans = 10**10
        for i in range(1,N+1):
            res = [0]
            vis = set()
            dfs(i,0,vis,res)
            ans = min(ans,res[0])
        return ans
