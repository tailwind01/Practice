#include <bits/stdc++.h>
using namespace std;

void solve(){
    int size;
    cin >> size;
    vector <int> nums(size);
    copy_n(istream_iterator <int> (cin), size, nums.begin());
    int total = accumulate(nums.begin(),nums.end(),0);
    int ctof1ms = 0;
    for(int i=0;i<size;++i){
        ctof1ms+=nums[i]%3==1;
    }
    int ans = (total%3)==0 ? 0:1;
    if(total%3==1 && ctof1ms==0){
        ans+=1;
    }
    cout << ans << "\n";
}

int main(){
    int numcases;
    cin >> numcases;
    while(numcases--){
        solve();
    }
    return 0;
}
