#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector <int> recipient;
    
    for(int i=0;i<n;i++){
        int g;
        cin >> g;
        recipient.push_back(g);
    };
    
    for(int j=0;j<n-1;++j){
        auto iter = find(recipient.begin(), recipient.end(),j+1);
        int giver = distance(recipient.begin(),iter);
        cout << giver+1 << " ";
    }
    auto iter2 = find(recipient.begin(), recipient.end(),n);
    int lastInd = distance(recipient.begin(),iter2);
    cout << lastInd+1 << endl;
};

int main(){
    solve();
    return 0;
};
