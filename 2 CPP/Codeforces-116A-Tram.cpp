#include <bits/stdc++.h>
using namespace std;

void solve(){
    int stops;
    cin >> stops ;
    int capacity = 0;
    int inTrain = 0; //initialized..
    //lets calculate the answer at the input stage itself
    for(int i=0;i<stops;++i){
        int a,b;
        cin >> a >> b;
        inTrain += b-a ; //in train variable changes with every stop
        capacity = (inTrain>capacity) ? inTrain : capacity; //whilst we could use max, trying the ternary operator for the fun of it
    }
    cout << capacity << endl; 
};

int main(){
    ios_base::sync_with_stdio (false);
    solve();
    return 0;
}
