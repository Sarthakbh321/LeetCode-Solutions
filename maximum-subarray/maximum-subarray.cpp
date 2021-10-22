class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++) {
            int nx = nums[i] + nums[i-1];
            
            if(nx > 0) {
                nums[i] = max(nums[i], nx);
            }
        }
        
        int res = -1*INT_MAX;
        for(int i = 0; i < nums.size(); i++) {
            res = max(res, nums[i]);
        }
        
        return res;
        
    }
};