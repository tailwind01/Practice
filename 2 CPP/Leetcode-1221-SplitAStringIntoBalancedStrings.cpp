class Solution {
public:
    int balancedStringSplit(string s) {
        int lseen=0,rseen=0,ans=0;
        for(char &c:s){
            if(c=='L'){
                lseen+=1;
            }
            else{
                rseen+=1;
            }
            ans+=(lseen==rseen);
        }
        return ans;
    }
};
