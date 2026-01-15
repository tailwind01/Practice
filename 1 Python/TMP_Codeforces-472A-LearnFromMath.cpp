#include <iostream>
using namespace std;

int main(){
  long long int number;
  cin >> number;
  if(number%2==1){
      cout << 9 <<" "<<number-9;
  }
  else{
      cout << 8 << " " << number - 8;
  }
    return 0;
}
