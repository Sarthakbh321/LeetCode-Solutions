class Solution {
public:
    int rob(vector<int>& nums) {
        for(int i = 1; i < nums.size(); i++) {
            if(i == 1) {
                nums[i] = max(nums[i], nums[i-1]);
            } else {
                nums[i] = max(nums[i], max(nums[i-1], nums[i-2] + nums[i]));
            }
        }
    
        
        return nums[nums.size()-1];
    }
};