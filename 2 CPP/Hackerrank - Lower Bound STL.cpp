#/tailwind
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int numel;
    cin >> numel;
    
    vector <int> myvec;
    
    for (int i=0;i<numel;i++){
        int n;
        cin >> n;
        myvec.push_back(n);
    }   
    int q;
    cin >> q;
    for(int j=0; j<q;j++){
        int qn;
        cin >> qn;
        vector<int>::iterator low,up;
        low = lower_bound (myvec.begin(), myvec.end(), qn);
        up = upper_bound (myvec.begin(), myvec.end(), qn); 
        
        if(myvec[low-myvec.begin()]==qn){
            cout << "Yes " << (low-myvec.begin())+1 << endl;
        }
        else{
            cout << "No " << (low-myvec.begin())+1 << endl;
        }
    }
    return 0;
}
