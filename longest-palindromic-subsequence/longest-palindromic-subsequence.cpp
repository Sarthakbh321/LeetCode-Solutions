class Solution {
public:
    int longestPalindromeSubseq(string s) {
        int dp[s.size()][s.size()];
        
        for(int i = 0; i < s.size(); i++) {
            for(int j = 0; j < s.size(); j++) {
                dp[i][j] = 1;
            }
        }
        
        for(int i = 0; i < s.size(); i++) {
            for(int j = i; j < s.size(); j++) {
                if(i == j) dp[i][j] = 1;
                else if(s[i] == s[j]) dp[i][j] = 2;
            }
        }
        
        
        for(int k = 2; k < s.size(); k++) {
             for(int i = 0; i < s.size()-k; i++) {
                 int j = i+k;
                 if(s[i] == s[j]) {
                     // cout << i << " " << j << " " << dp[i+1][j-1] << endl;
                    dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2);
                } else {
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j]);
                }
             }
        }
       
        int res = 0;
        for(int i = 0; i < s.size(); i++) {
            res = max(res, dp[i][s.size()-1]);
        }
        

        return res;
    }
};