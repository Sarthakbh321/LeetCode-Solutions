class Solution {
public:
    int subsetXORSum(vector<int>& nums) {
        int res = 0;
        for(int i = 0; i < pow(2, nums.size()); i++) {
            int xors = 0;
            for(int j = 0; j < nums.size(); j++) {
                if(i & (1 << j)) {
                    xors ^= nums[j];
                }
            }
            res += xors;
        }
        
        return res;
    }
};