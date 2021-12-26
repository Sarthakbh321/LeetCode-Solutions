class Solution:
    
    # Time -> O(n) | Extra Space -> O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        result = []
        for i in nums: # Time -> O(n)
            currentNumber = abs(i)
            if(nums[currentNumber-1] < 0):
                result.append(currentNumber) # Time -> O(1)
            
            nums[currentNumber-1] *= -1
            
        
        return result