#include <bits/stdc++.h>
using namespace std;

void solve() {
    int r;
    cin >> r;
    string common="Division ";
    vector <string> classes = {"1","2","3","4"};
    
    while(r--){
        int rating;
        cin >> rating;
        int classIndex = 3; //default we keep in division 4
        if(rating>=1900){
            classIndex = 0;
        }
        else if(rating>=1600){
            classIndex = 1;
        }
        else if(rating>=1400){
            classIndex = 2;
        }
        cout << common+classes[classIndex] << endl; //output for each input
    }
}

int main(){
    solve();
    return 0;
}
