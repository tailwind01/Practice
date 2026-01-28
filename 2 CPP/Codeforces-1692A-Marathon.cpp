#include <bits/stdc++.h>
using namespace std;

void solve() {
    int testcases;
    cin >> testcases;
    while(testcases--){
        int timur,o1,o2,o3;
        cin >> timur >> o1 >> o2 >> o3;
        int ahead = 0;
        //we have 3 separate if conditions which are independent of each other
        if (o1>timur){ahead+=1;};
        if (o2>timur){ahead+=1;};
        if (o3>timur){ahead+=1;};
        cout << ahead << "\n";  
    }
}

int main(){
    solve();
    return 0;
}
