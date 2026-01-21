#include <bits/stdc++.h>
using namespace std;

void solve(){
    string s;
    cin >> s;
    unordered_set<char> ss(s.begin(),s.end());
    if (ss.size()==1){
        cout << "No" << endl;
    }
    else{
        cout << "Yes" << endl;
        cout << s.substr(s.size()-1,1) << s.substr(0,s.size()-1)<<endl;
    }
    
}

int main(){
    int nc;
    cin >> nc;
    
    for(int i=0;i<nc;i++){
        solve();
    };
    
    return 0;
}
