#include <bits/stdc++.h>
using namespace std;

void solve(){
    int k,l,m,n,d;
    cin >> k >> l >> m >> n >> d;
    
    int damaged = d; //initialized with the assumption that every dragon got damaged, we change this only if we see evidence contrary to this
    
    for(int i=1;i<d+1;++i){
        if (i%k!=0 && i%l!=0 && i%m!=0 && i%n!=0){
            damaged-=1;
        };
    }; // thereafter, we dont need to take a set, we can just reduce the answer
    
    cout << damaged << endl;
};

int main(){
    solve();
    return 0;
};
