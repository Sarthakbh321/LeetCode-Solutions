class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.num = n
    
    def find(self, a):
        temp = a
        
        while(a != self.parent[a]):
            a = self.parent[a]
        
        while(temp != a):
            temp, self.parent[temp] = self.parent[temp], a
        
        return a
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        
        if(pa != pb):
            if(self.size[pa] < self.size[pb]):
                pa,pb = pb,pa

            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
            self.num -= 1
        
        
        
        

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        dsu = DSU(n)
        extra = 0
        
        for u,v in connections:
            if(dsu.find(u) == dsu.find(v)):
                extra += 1
            
            dsu.union(u,v)
        
        comps = dsu.num
        required = comps-1
        
        if(extra >= required):
            return required
        else:
            return -1
            