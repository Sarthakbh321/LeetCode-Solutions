class Solution {
public:
    void print(vector<int> vec) {
        for(int x: vec) {
            cout << x << " ";
        }

    }
    int calculateScore(vector<int>& vec) {
        int res = 0;
        for(int num: vec) {
            res ^= num;
        }
        
        return res;
    }
    
    void recurse(vector<int> curr, vector<int>& og, int idx, int& res) {
        if(idx > og.size()) return;
        
        res += calculateScore(curr);
        // print(curr);
        // cout << idx << endl;
        
        for(int i = idx; i < og.size(); i++) {
            vector<int> newVec = curr;
            newVec.push_back(og[i]);
            
            recurse(newVec, og, i+1, res);
        }
        
    }
    int subsetXORSum(vector<int>& nums) {
        int res = 0;
        vector<int> startVec = {};
        
        recurse(startVec, nums, 0, res);
        
        return res;
    }
};