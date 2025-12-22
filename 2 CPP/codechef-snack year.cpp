//published by tailwind, runtime 0ms, memory 5.8mb//
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string h_or_not(int n){
    vector <int> masterlist = {2010,2015,2016,2017,2019};
    string ans = "NOT HOSTED";
    for(int i=0;i<5;i++){
        if(masterlist[i]==n){
           ans = "HOSTED"; 
        }
    }
    return ans;
}
int main() {
    int nc;
    cin >> nc;
    
    for(int j=0; j<nc;j++){
        int year;
        cin >> year;
        cout << h_or_not(year) << endl;
    }
    return 0;
}
