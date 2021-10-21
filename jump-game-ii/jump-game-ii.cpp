class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int l = 0, r = min(nums[0], n-1);
        
        if(n == 1) return 0;
        
        int jumps = 1;
        
        while(r < n-1) {
            int temp = r;
            int next = r;
            for(int i = l; i <= r; i++) {
                next = max(next, i+nums[i]);
            }
            
            l = temp;
            r = next;
            jumps++;
        }
        
        return jumps;
    }
};