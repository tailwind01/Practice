//tailwind, 389 ms, 0kb, ultimate testcase count = 50000, carpe fucking diem//
#include <iostream>
using namespace std;

long long int reqremain(long long int x, long long int y, long long int n){
  long long int lastperf = n/x;
  long long int ans = lastperf *x + y;
  if(ans<=n){
    return ans;
  }
  else{
    return ans-x;
  }
}

int main(){
  long long int nc;
  cin >> nc;
  for(long long int i=0; i<nc; i++){
    long long int a,b,c;
    cin >> a >> b >> c;
    cout << reqremain(a,b,c)<<endl;
  }
    
}
