//a tailwind code, runtime 31ms, memory 0
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    int size;
    cin >> size;
    vector <int> burles;
    for(int i=0; i<size;i++){
        int burle;
        cin >> burle;
        burles.push_back(burle);
    }
    int reqd=0;
    int maxelem = *max_element(burles.begin(),burles.end());
    for(int j=0; j<size;j++){
        int calc;
        calc = maxelem - burles[j];
        reqd = reqd+calc;
    }
    cout << reqd << endl;
}
