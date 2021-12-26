class Solution:
    
    # Time -> O(n) | Space -> O(1)
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        
        # Time -> O(n)
        for number in nums:
            result ^= number # Time -> O(1)
            
        return result