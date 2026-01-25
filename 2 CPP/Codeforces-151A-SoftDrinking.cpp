#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n,k,l,c,d,p,nl,np;
    cin >> n >> k >> l >> c >> d >> p >> nl >> np;
    int drinkQty = k*l;
    int slices = c*d;
    int salt = p;
    int onetoastDrink = n*nl;
    int onetoastSalt = n*np;
    vector <int> bnecks = {drinkQty/onetoastDrink, slices/n, p/onetoastSalt};
    sort(bnecks.begin(),bnecks.end()); //so that the bottlneck is the first element of vector
    cout << bnecks[0] << endl;
}

int main(){
    solve();
    return 0;
}
