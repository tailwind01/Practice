//tailwind 30ms, 0kb, carpe diem
#include <iostream>
#define ll long long
using namespace std;

int main(){
    int n1,n2;
    cin >> n1 >> n2;
    ll prod;
    prod = 1;
    if(n1>n2){
        for(int i=1;i<=n2;i++){
            prod = prod*i;
        }
        cout << prod << endl;
    }
    else {
        for(int i=1;i<=n1;i++){
            prod = prod*i;
        }
        cout << prod << endl;
    }
    return 0;
}
