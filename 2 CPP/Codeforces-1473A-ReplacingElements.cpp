#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n, d;
    cin >> n >> d;
    vector <int> nums(n);
    copy_n(istream_iterator <int> (cin), n, nums.begin());
    sort(nums.begin(),nums.end());
    int initSum = nums[0]+nums[1];
    string ans = "Yes";
    for(int i=0;i<n;++i){
        if(min(nums[i],initSum)>d){
            ans = "No";
            break;
        }
    }
    cout << ans << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
