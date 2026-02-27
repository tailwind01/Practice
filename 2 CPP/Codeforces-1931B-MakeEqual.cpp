// forward pass version

#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector <int> warr (n);
    copy_n(istream_iterator <int> (cin), n, warr.begin());
    int target = accumulate(warr.begin(),warr.end(),0)/n;
    int collectedfromleft = 0;
    int ansbool = 1;
    for(int i=0;i<n;i++){
        collectedfromleft += warr[i]-target;
        if (collectedfromleft<0){
            ansbool = 0;
            break;
        }
    }
    string ans = (ansbool==1) ? "Yes":"No";
    cout << ans << "\n";
}

int main(){
    int numcases;
    cin >> numcases;
    while(numcases--){
        solve();
    }
    return 0;
}


// backward pass version
#include <bits/stdc++.h>
using namespace std;

void solve(){
    int n;
    cin >> n;
    vector <int> warr (n);
    copy_n(istream_iterator <int> (cin), n, warr.begin());
    int target = accumulate(warr.begin(),warr.end(),0)/n;
    int reqdfromleft = 0;
    int ansbool = 1;
    for(int i=n-1;i>=0;i--){
        reqdfromleft += target-warr[i];
        if (reqdfromleft<0){
            ansbool = 0;
            break;
        }
    }
    string ans = (ansbool==1) ? "Yes":"No";
    cout << ans << "\n";
}

int main(){
    int numcases;
    cin >> numcases;
    while(numcases--){
        solve();
    }
    return 0;
}
