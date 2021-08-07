class Solution:
    def balancedStringSplit(self, s: str) -> int:
        d = {"L": 0, "R": 0}
        
        res = 0
        for i in range(len(s)):
            if(i == 0):
                d[s[i]] += 1
            else:            
                d[s[i]] += 1
                
                if(d["L"] == d["R"]):
                    d = {"L": 0, "R": 0}
                    res += 1
                    
        return res