class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int currMin = prices[0];
        int res = 0;
        
        for(int i = 1; i < prices.size(); i++) {
            res = max(res, prices[i]-currMin);
            currMin = min(currMin, prices[i]);
        }
        
        return res;
    }
};