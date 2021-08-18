class DSU:
    def __init__(self, l, n):
        self.n = n
        self.size = [0]*(n)
        
        for i in range(len(l)):
            for j in range(len(l[0])):
                if(l[i][j] == 1):
                    self.size[i*len(l[0]) + j] = 1
        
        self.parent = list(range(n))
    
    def union(self, a, b):
        pa = self.find(a)
        pb = self.find(b)
        
        if(pa != pb):
            if(self.size[pa] < self.size[pb]):
                pa,pb = pb,pa
            
            self.parent[pb] = pa
            self.size[pa] += self.size[pb]
        
    def find(self, a):
        temp = a
        
        while(self.parent[a] != a):
            a = self.parent[a]
        while(temp != a):
            self.parent[temp], temp = a, self.parent[temp]
        
        return a
    
    def getMax(self):
        return max(self.size)
    

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        d = DSU(grid, n*m)
        
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):
                    if(j > 0):
                        if(grid[i][j-1] == 1):
                            d.union(m*i + (j-1), m*i + j)
                    
                    if(j < m-1):
                        if(grid[i][j+1] == 1):
                            d.union(m*i + (j+1), m*i + j)
                    
                    if(i > 0):
                        if(grid[i-1][j] == 1):
                            d.union(m*(i-1) + j, m*i + j)
                    
                    if(i < n-1):
                        if(grid[i+1][j] == 1):
                            d.union(m*(i+1) + j, m*i + j)
        
        return d.getMax()
        
        