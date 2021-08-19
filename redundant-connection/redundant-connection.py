class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*(n)
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        
        if(pa != pb):
            if(self.size[pa] < self.size[pb]):
                pa,pb=pb,pa
            
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
            
    def find(self,a):
        temp = a
        while(self.parent[a] != a):
            a = self.parent[a]
        
        while(temp != a):
            self.parent[temp], temp = a, self.parent[temp]
            
        return a
        
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d = DSU(len(edges))
        
        for u,v in edges:
            pu = d.find(u-1)
            pv = d.find(v-1)
            
            if(pu == pv):
                return [u,v]
            else:
                d.union(u-1, v-1)
            
            