#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector <int> homecolors;
    vector <int> guestcolors;
    
    for (int i=0;i<n;++i){
        int h,g;
        cin >> h >> g;
        homecolors.push_back(h);
        guestcolors.push_back(g);
    }
    
    int clashes = 0;
    //we will use double for-loop
    for (int j=0; j<n; ++j){
        for (int k=0;k<n;++k){
            clashes+=(homecolors[j]==guestcolors[k]);
        }
    };
    
    cout << clashes << endl;
}

int main(){
    solve();
    return 0;
}
