#include <bits/stdc++.h>
using namespace std;

void solve(){
    unsigned long long int n;
    cin >> n;
    int  l2_int = log2(n);
    long ans = pow(2,l2_int)-1; 
    cout << ans << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}

//code on which I encountered TLE
//
#include <bits/stdc++.h>
using namespace std;

void solve(){
    unsigned long long int n;
    cin >> n;
    unsigned long long int ans = n & n-1;
    n = n-1; //if we have found ans at the first instance itself..
    while(ans!=0){
        n = n-1;
        ans = ans & n;
    }
    cout << n << "\n";
}

int main(){
    int t;
    cin >> t;
    while(t--){
        solve();
    }
    return 0;
}
