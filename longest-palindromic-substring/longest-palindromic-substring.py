class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        dp = [[None for _ in range(n)] for __ in range(n)]
        
        r = -1
        m = (-1, -1)
        
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if(s[i] == s[i+1]):
                dp[i][i+1] = True
                r = 2
                m = (i, i+1)
                    
        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                if(s[i] == s[j] and dp[i+1][j-1]):
                    dp[i][j] = True
                    curr = j-i+1
                    if(curr > r):
                        
                        r = curr
                        m = (i, j)
                
        final = s[m[0]:m[1]+1]
        if(r == -1):
            final = s[0]
        
        return final