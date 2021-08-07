class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        i,j = 0,len(s)
        
        res = []
        
        for k in range(len(s)):
            if(s[k] == "I"):
                res.append(i)
                i += 1
            else:
                res.append(j)
                j -= 1
        res.append(i)
        return res