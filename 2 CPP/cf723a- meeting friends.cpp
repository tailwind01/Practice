//a tailwind publication, runtime 31ms, memory 0kbs, carpe diem//
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int mindist(int x, int y, int z){
    vector <int> arr {x,y,z};
    return *max_element(arr.begin(), arr.end())-*min_element(arr.begin(),arr.end());
}

int main(){
    int a,b,c;
    cin >> a >> b >> c;
    cout << mindist(a,b,c) << endl;
}
