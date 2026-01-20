#include <iostream>
using namespace std;

void solve(){
    int x;
    cin >> x;
    cout << 1 << " "<< x-1 << endl;
}

int main() {
    int nc;
    cin >> nc;
    for(int i=0; i<nc;i++){
        solve();
    };
}
