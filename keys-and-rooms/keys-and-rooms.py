class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def BFS(graph):
            n = len(graph)
            
            visited = [False]*(n)
            
            q = [0]
            
            for i in q:
                visited[i] = True
                for j in graph[i]:
                    if(not visited[j]):
                        q.append(j)
            
            return visited.count(True) == n
        
        return BFS(rooms)