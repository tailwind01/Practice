#include <iostream>
using namespace std;

int main(){
    int n;
    long long int x;
    cin >> n >> x;
    long long int  icecreams = x;
    int  distressed = 0;
    
    while(n--){
        char op;
        long long int magnitude;
        cin >> op >> magnitude;
        if(op=='+'){
            icecreams+=magnitude;
        }
        else{
            if(magnitude<=icecreams){
                icecreams-=magnitude;
            }
            else{
                distressed+=1;
            }
        }
    }
    cout << icecreams <<" "<<distressed << "\n";
}
