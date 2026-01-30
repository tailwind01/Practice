//runs at 140ms and 0Kb which is optimal given the constraints of the problem
//
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int tc;
    cin >> tc;
    while(tc--){
        vector <int> nums;
        for(int i=0;i<3;++i){
            int n;
            cin >> n;
            nums.push_back(n);
        }
        
        sort(nums.begin(),nums.end());
        
        if(nums[1]!=nums[2]){
            cout << "NO" << endl;
        }
        else{
            cout << "YES" << "\n";
            cout << nums[0] << " "<<nums[0] << " " << nums[1]<< "\n";
        };
    }
    
}

int main(){
    solve();
    return 0;
}
