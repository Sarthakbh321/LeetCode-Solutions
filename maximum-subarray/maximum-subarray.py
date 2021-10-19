class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        for i in range(1, len(nums)):
            ne = nums[i] + nums[i-1]
            
            if(ne > nums[i]):
                nums[i] = ne
        
        return max(nums)