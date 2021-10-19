class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0, n-1
        i = n-1
        
        res = [-1]*(n)
        
        while(l <= r):
            sq1 = nums[l]**2
            sq2 = nums[r]**2
            
            if(sq1 <= sq2):
                res[i] = sq2
                i -= 1
                r -= 1
            else:
                res[i] = sq1
                l += 1
                i -= 1
        
        return res