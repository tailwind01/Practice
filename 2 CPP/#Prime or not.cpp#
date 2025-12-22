//code to check if given number is prime or not//
#include <iostream>
using namespace std;
int primeTest(unsigned long long int N){
  for (unsigned long long int i = 2; i*i <= N; ++i){
    if(N%i == 0) { return 0;}
  }
  return 1;
}
int main(){
  int nc;
  cin >> nc;
  for(int j=0; j<nc; j++){
    unsigned long long int num;
    cin >> num;
    if(primeTest(num)==1){
      cout << "prime" << endl;
    }
    else{
      cout << "composite" << endl;
    }
  }
}
