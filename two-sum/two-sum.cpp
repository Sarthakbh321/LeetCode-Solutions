class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> d;
        unordered_map<int, vector<int>> ind;
        
        vector<int> res;
        
        for(int i = 0; i < nums.size(); i++) {
            d[nums[i]]++;
            ind[nums[i]].push_back(i);
        }
        
        for(int x: nums) {
            int rem = target-x;
            d[x]--;
            
            if(d[rem] > 0) {
                if(x == rem) {
                    res.push_back(ind[x][0]);
                    res.push_back(ind[x][1]);
                } else {
                    res.push_back(ind[x][0]);
                    res.push_back(ind[rem][0]);
                }
                
                break;
            }
        }
        
        return res;
    }
};