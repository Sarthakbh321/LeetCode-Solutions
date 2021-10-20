class Solution {
public:
    int deleteAndEarn(vector<int>& nums) {
        int MAX = 10005;
        int dp[10005] = {0};
        
        for(int x: nums) dp[x]++;
        
        
        for(int i = 0; i < MAX; i++) {
            dp[i] = i*dp[i];
        }
        
        for(int i = 2; i < MAX; i++) {
            if(i == 2) {
                dp[i] = max(dp[i], dp[i-1]);
            } else {
                dp[i] = max(dp[i], max(dp[i-1], dp[i-2] + dp[i]));
            }
        }
        
        return dp[MAX-1];
    }
};