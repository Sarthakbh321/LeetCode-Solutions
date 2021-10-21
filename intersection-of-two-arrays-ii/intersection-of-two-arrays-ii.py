from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        s = set(nums1) & set(nums2)
        
        res = []
        
        for i in s:
            res.extend([i for _ in range(min(c1[i], c2[i]))])
        
        return res