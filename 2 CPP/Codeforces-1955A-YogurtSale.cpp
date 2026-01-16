#include <iostream>
using namespace std;

int main(){
    int nc;
    cin >> nc;
    
    for(int i=0;i<nc;i++){
        int n,a,b;
        cin >> n >> a >> b;
        if(b>2*a){
            cout << n*a << endl;
        }
        else if(n%2==1){
            cout << n/2*b+a << endl;
        }
        else{
            cout << n/2*b << endl;
        };
    };
    return 0;
}
