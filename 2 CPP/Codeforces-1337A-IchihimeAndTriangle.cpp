#include <bits/stdc++.h>
using namespace std;

void solve(){
    int nc;
    cin >> nc;
    while(nc--){
        //given the nature of inputs, we set x=b,y=c,z=c and output it
        //no need to do ANY fancy processing since a triangle can always be formed with given constraints
        long long int a,b,c,d;
        cin >> a >> b >> c >> d;
        cout << b << " "<< c << " "<<  c << "\n";
    }
}

int main(){
    solve();
    return 0;
}
