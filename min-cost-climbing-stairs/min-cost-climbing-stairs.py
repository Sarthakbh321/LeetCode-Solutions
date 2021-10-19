class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0,0]
        
        for i in range(len(cost)):
            dp.append(min(dp[-1], dp[-2]) + cost[i])
        
        return min(dp[-1], dp[-2])
            