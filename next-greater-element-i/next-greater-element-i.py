class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ind = {}
        for i in range(len(nums2)):
            ind[nums2[i]] = i
        
        stack = []
        nextGreats = [-1]*(len(nums2))
        
        for i in range(len(nums2)):
            if(len(stack) == 0):
                stack.append([nums2[i], i])
            else:
                while(stack and nums2[i] > stack[-1][0]):
                    popped = stack.pop()
                    nextGreats[popped[1]] = nums2[i]
                
                stack.append([nums2[i], i])
        
        res = []
        
        for i in nums1:
            res.append(nextGreats[ind[i]])
        
        return res
                    
        