import math

class Solution:
    def distance(self, x, y):
        return math.sqrt((x[0]-y[0])**2 + (x[1]-y[1])**2)
        
        
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        res = []
    
        for i in queries:
            c = [i[0], i[1]]
            inside = 0
            for j in points:
                if(self.distance(c, j) <= i[2]):
                    inside += 1
                    
            res.append(inside)
            
        return res
            
        
        