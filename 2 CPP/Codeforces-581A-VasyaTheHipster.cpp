#include <bits/stdc++.h>
using namespace std;

void solve() {
    int red, blue;
    cin >> red >> blue ;
    int diff = min(red, blue);
    int same = (red+blue-diff*2)/2 ; //as this has to be a pair of socks

    cout << diff << " "<< same << "\n";


}

int main(){
    solve();
    return 0;
}
