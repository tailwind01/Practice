//tailwind publication, runtime 15ms, memory 0kb, to find maximum GCD in a range of numbers//
//my hypothesis was that the max GCD will occur at the range bisection, i.e. num/2 //
//such an algo could handle the time-space constraints efficiently//

#include <iostream>
using namespace std;
int maxgcd(int n){
    return n/2;
}
int main(){
    int nc;
    cin >> nc;
    for(int j=0; j<nc;j++){
        int num;
        cin >> num;
        cout << maxgcd(num)<< endl;
    }
    return 0;
}




