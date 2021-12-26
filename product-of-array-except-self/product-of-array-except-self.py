class Solution:
    # Time -> O(n) | Extra Space -> O(n)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        prefixProduct = [1] # Space -> O(n)
        for i in range(n): # Time -> O(n)
            prefixProduct.append(prefixProduct[-1]*nums[i])
        
        suffixProduct = [1] # Space -> O(n)
        for i in range(n-1, -1, -1): # Time -> O(n)
            suffixProduct.append(suffixProduct[-1]*nums[i])
        
        suffixProduct = suffixProduct[::-1] # Time -> O(n)
        
        result = []
        
        for i in range(n): # Time -> O(n)
            prefix = prefixProduct[i] # Time -> O(1)
            suffix = suffixProduct[i+1] # Time -> O(1)
            
            result.append(prefix * suffix) # Time -> O(1)
            
        return result