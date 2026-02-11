#include <bits/stdc++.h>
using namespace std;

void solve(){
    int size;
    cin >> size;
    vector <int> toColour(size);
    copy_n(istream_iterator <int> (cin), size, toColour.begin());
    sort(toColour.begin(),toColour.end());
    int ans = 0;
    if(toColour.size()>1){
        int mpt = (toColour.size()+1)/2;
        int firstHalf = accumulate(toColour.begin(),toColour.begin()+mpt,0);
        int secondHalf = accumulate(toColour.begin()+mpt,toColour.end(),0);
        ans = secondHalf-firstHalf;
        if(toColour.size()%2!=0){
            ans+=toColour[mpt-1];
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
