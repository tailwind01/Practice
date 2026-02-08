#include <bits/stdc++.h>
using namespace std;

void solve(){
    int size;
    cin >> size;
    int numElems = 2*size;
    vector <int> merged;
    unordered_set <int> uniques;
    while(numElems--){
        int num;
        cin >> num;
        if (uniques.find(num)==uniques.end()){
            merged.push_back(num);
            uniques.insert(num);
        }
    }
    for (int i = 0;i<size-1;i++){
        cout << merged[i] << " ";
    }
    cout << merged[size-1] << "\n";
}

int main(){
    int tc;
    cin >> tc;
    while(tc--){
        solve();
    }
    return 0;
}
