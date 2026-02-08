#include <bits/stdc++.h>
using namespace std;

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        int num;
        cin >> num;
        string ans = (num%2!=0) ? "Yes":"No";
        cout << ans << "\n";
    }
}
