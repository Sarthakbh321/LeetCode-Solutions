from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Time -> O(n) | Space -> O(n)
        numsCounter = Counter(nums)
        
        result = []
        
        # Time -> O(n)
        for i in range(1, n+1):
            if(numsCounter[i] == 0): # Time -> O(1)
                result.append(i) # Time -> O(1)
                
        return result