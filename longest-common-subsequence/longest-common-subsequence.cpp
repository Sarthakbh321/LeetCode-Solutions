class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1));
                               
        for(int i = 0; i < dp.size(); i++) {
            for(int j = 0; j < dp[0].size(); j++) {
                dp[i][j] = 0;
            }
        }
        
        for(int i = 1; i < text1.size()+1; i++) {
            for(int j = 1; j < text2.size()+1; j++) {
                if(text1[i-1] == text2[j-1]) {
                    
                    // cout << "Hello" << text1[i] << " " << text2[j] << endl;
                    dp[i][j] = dp[i-1][j-1]+1;
                } else {
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        
        // for(int i = 0; i < dp.size(); i++) {
        //     for(int j = 0; j < dp[0].size(); j++) {
        //         cout << dp[i][j] << " ";
        //     }
        //     cout << "\n";
        // }
        
        
        return dp[text1.size()][text2.size()];
    }
};