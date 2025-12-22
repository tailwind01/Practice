//published by tailwind, runtime 0.11s, memory 5.8mb//
#include <iostream>
using namespace std;

int winner(int n){
    if(n%2==0){
        return 1;
    }
    else{
        return 2;
    }
}
int main() {
    int nc;
    cin >> nc;
    for(int j=0; j<nc;j++){
        int size, recsum;
        cin >> size;
        recsum = 0;
        for(int j=0; j<size;j++){
            int num;
            cin >> num;
            recsum=recsum+num;
        }
        cout << winner(recsum) << endl;
    }
    return 0;
}
