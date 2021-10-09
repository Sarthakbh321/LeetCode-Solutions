from collections import deque
class Solution:
    res = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def BFS(graph):
            n = len(graph)
            
            visited = [False]*(n)
             
            q = deque([[0]])
            
            while(q):
                # print(q)
                currPath = q.popleft()
                currNode = currPath[-1]
                
                # visited[currNode] = True
                
                for i in graph[currNode]:
                    if(not visited[i]):
                        newPath = currPath + [i]
                        q.append(newPath)
                        
                        if(i == n-1):
                            self.res.append(newPath)
        self.res = []
        BFS(graph)
        return self.res
            