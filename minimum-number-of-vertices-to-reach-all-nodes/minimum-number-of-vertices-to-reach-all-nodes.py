from collections import defaultdict as dd
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = dd(list)
        
        indegree = Counter()
        
        for i in edges:
            graph[i[0]].append(i[1])
            indegree[i[1]] += 1
        
        res = []
        for i in range(n):
            if(indegree[i] == 0):
                res.append(i)
        
        return res
        
        