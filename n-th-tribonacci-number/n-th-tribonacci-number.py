class Solution:
    def tribonacci(self, n: int) -> int:
        dp = [0,1,1]
        
        for i in range(3, n+1):
            dp.append(dp[-3] + dp[-2] + dp[-1])
        
        return dp[n]