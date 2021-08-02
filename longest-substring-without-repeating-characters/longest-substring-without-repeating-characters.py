from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = Counter()
        
        l,r = 0,0
        unique = True
        res = 0
        
        while(r < len(s)):
            if(c[s[r]] + 1 > 1):
                c[s[l]] -= 1
                l += 1
            else:
                c[s[r]] += 1
                r += 1
                
            res = max(r-l, res)
            
        return res
            
                
        