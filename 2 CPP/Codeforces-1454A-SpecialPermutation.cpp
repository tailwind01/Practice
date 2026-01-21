// 2 versions of the solution - the code should be read in an isolated manner
// both solutions ran in 31ms, with almost no memory
// v2 - alternating swaps 

#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    // let's try to be greedy and make alternating swaps
    
    for(int i=1; i<n-1; ++i){
        if (i%2!=0){
            cout << i+1 << " ";
        }
        else{
            cout << i-1 << " ";
        };
    }
    
    if(n%2==0){
        cout << n <<" "<< n-1 << endl;
    }
    else{
        cout << n << " " << n-2 << endl; //making adjustment for odd n
    }
    
}

int main(){
    int nc;
    cin >> nc;
    for(int i=0;i<nc;i++){
        solve();
    };
    return 0;
}

//==================================================================////
//v1 - the first version which has the adjustment for one bottleneck

#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    
    int midpt = n/2; // we will push the midpoint (being the bottleneck to the end)
    if(n%2!=0){midpt+=1;} ; //for odd n, the bottleneck changes
    
    if (n%2==0){
        for(int i = 0; i<n;i++){
            if (i!= midpt){
                cout << n-i << " ";
                };
            };
        }
    else{
        for(int i = 1; i<n+1;i++){
            if (i!=midpt){
                cout << n+1-i << " ";
            };
        };
    }
    
    cout << midpt << endl;
}

int main(){
    int nc;
    cin >> nc;
    for(int i=0;i<nc;i++){
        solve();
    };
    return 0;
}
