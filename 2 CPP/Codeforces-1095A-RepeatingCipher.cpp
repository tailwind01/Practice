#include <bits/stdc++.h>
using namespace std;

int main(){
    int size;
    string input;
    cin >> size;
    cin >> input;
    int pointer = 0, stepSize = 1;
    string ans = "";
    while(pointer<size){
        ans+=input[pointer];
        pointer+=stepSize;
        stepSize+=1;
    }
    cout << ans << "\n";
    return 0;
}
