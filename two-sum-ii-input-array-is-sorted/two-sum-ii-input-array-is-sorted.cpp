class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0, j = numbers.size()-1;
        
        while(i < j) {
            int sum = numbers[i] + numbers[j];
            
            if(sum == target) {
                vector<int> res = {i+1, j+1};
                return res;
            }
            
            if(sum < target) {
                i++;
            } else {
                j--;
            }
        }
        
        vector<int> res = {-1};
        return res;
    }
};