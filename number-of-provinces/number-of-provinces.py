class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*(n)
        self.sets = n
        
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        
        if(pa != pb):
            if(self.size[pa] < self.size[pb]):
                pa,pb = pb,pa
                
            self.parent[pb] = pa
            self.sets -= 1
            self.size[pa] += self.size[pb]
                
    def find(self, a):
        temp = a
        
        while(self.parent[a] != a):
            a = self.parent[a]
        
        while(temp != a):
            self.parent[temp],temp = a,self.parent[temp]
        
        return a

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        d = DSU(len(isConnected))
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if(isConnected[i][j] == 1):
                    d.union(i, j)
        
        return d.sets
        