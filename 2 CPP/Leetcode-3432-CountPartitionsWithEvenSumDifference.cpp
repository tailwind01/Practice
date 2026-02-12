class Solution {
public:
    int countPartitions(vector<int>& nums) {
        int lsum = nums[0];
        int rsum = accumulate(nums.begin(),nums.end(),0)-lsum;
        int ans = 0;
        for(int i=1; i<nums.size();++i){
            int cn = nums[i];
            lsum+=cn;
            rsum-=cn;
            ans+=abs(lsum-rsum)%2==0;
        }
        return ans;
    }
};
