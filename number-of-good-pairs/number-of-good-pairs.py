class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        d = {}
        res = 0
        for i in nums:
            if(i in d):
                res += d[i]
            else:
                d[i] = 0
            
            d[i] += 1
        
        return res