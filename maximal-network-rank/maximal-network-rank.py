class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        
        graph = collections.defaultdict(set)
        
        deg = collections.Counter()
        
        for u,v in roads:
            graph[u].add(v)
            graph[v].add(u)
            
            deg[u] += 1
            deg[v] += 1
        
        res = -1
        for i in range(n):
            for j in range(i+1, n):
                degree = deg[i] + deg[j]
                
                if(j in graph[i]):
                    degree -= 1
                
                res = max(res, degree)
                
        return res
            