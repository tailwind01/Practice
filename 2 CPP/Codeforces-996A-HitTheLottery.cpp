#include <bits/stdc++.h>
using namespace std;

void solve(){
    long long int amount;
    cin >> amount ;
    
    vector <long long int> bills = {100,20,10,5,1}; //reversed to have the vector work right
    
    long long int ans = 0;
    
    for(int i=0;i<bills.size();++i){
        long long int den_bills = amount/bills[i];
        ans+=den_bills;
        long long int zero = 0;
        amount-=max(den_bills*bills[i],zero);
    };
    
    cout << ans << endl;
};

int main(){
    solve();
    return 0;
};
