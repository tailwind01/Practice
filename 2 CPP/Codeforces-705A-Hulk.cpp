#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n ;
    string ans ="";
    
    for(int i=0;i<n-1;++i){
        string currPhrase;
        currPhrase = (i%2==0) ? "I hate that ":"I love that "; // using the ternary operator idiom
        ans+=currPhrase;
    }
    
    string finalPhrase;
    finalPhrase = ((n-1)%2==0) ? "I hate it":"I love it";
    ans+=finalPhrase ;
    
    cout << ans << endl;
   
};

int main(){
    solve();
    return 0;
};
