//this code does NOT pass all test cases, but it is still some work, so uploading for my records//

#include <iostream>
#include <set>
#include <iterator>
#include <algorithm>
using namespace std;

int primeTest(int N){
	if(N==1){return 0;}
	else if(N==2){return 1;}
	else{
	    for (int i = 2; i*i <= N; i++){
			if(N%i == 0 || N==1) { return 0;}
		}
    return 1;
	}
}
int main(){
	int n;
	cin >> n;
	set<int, greater<int>> primes;
	for(int j=0; j<n; j++){
		int num;
		cin >> num;
		if(primeTest(num)==1){
			primes.insert(num);
		}
	}
	if(primes.size()>=1){
		int calc;
		calc = *max_element(primes.begin(), primes.end())-*min_element(primes.begin(), primes.end());
		cout << calc << endl;
	}
	else{
		cout << -1 << endl;
	}
	return 0;

}
