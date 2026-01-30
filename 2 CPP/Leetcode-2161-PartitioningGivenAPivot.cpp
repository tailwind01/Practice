class Solution {
public:
    vector<int> pivotArray(vector<int>& nums, int pivot) {
        vector <int> l,m,r,ans;
        for(int i=0;i<nums.size();++i){
            if(nums[i]<pivot){
                l.push_back(nums[i]);
            }
            else if(nums[i]>pivot){
                r.push_back(nums[i]);
            }
            else{
                m.push_back(nums[i]);
            }
        }
        
        ans.insert(end(ans),begin(l),end(l));
        ans.insert(end(ans),begin(m),end(m));
        ans.insert(end(ans),begin(r),end(r));

        return ans;
    }
};
