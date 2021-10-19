class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return max(collections.Counter(nums).values()) > 1