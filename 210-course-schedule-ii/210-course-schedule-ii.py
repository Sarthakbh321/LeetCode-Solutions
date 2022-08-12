from collections import defaultdict as dd, Counter

class Solution:
    def dfsUtil(self, graph, node, visited, stack, recStack):
        visited[node] = True
        recStack.add(node)
        
        
        for nextNode in graph[node]:
            if(not visited[nextNode]):
                self.dfsUtil(graph, nextNode, visited, stack, recStack)
            elif(nextNode in recStack):
                return False

        recStack.remove(node)
        stack.append(node)
        
    def topologicalSort(self, graph, numCourses):
        visited = [False]*(numCourses)
        stack = []
        recStack = set()
        
        for node in range(numCourses):
            if(not visited[node]):
                self.dfsUtil(graph, node, visited, stack, recStack)
        
        return stack
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = dd(list)
        
        for u,v in prerequisites:
            graph[u].append(v)
        
            
        res = self.topologicalSort(graph, numCourses)
        
        if(len(res) != numCourses):
            return []
        
        return res