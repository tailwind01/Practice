    // solution to codeforces 1742A-Sum; 77ms, 0Kb efficiency
    #include <iostream>
    using namespace std;
     
    int main() {
        // Write C++ code here
        long long int nc;
        cin >> nc;
        for(long long int i=0; i<nc; i++) {
            int a,b,c;
            cin >> a >> b >> c;
            float one_half = (a+b+c)*0.5;
            int ctr = 0;
            if(one_half==a){ctr=1;}
            if(one_half==b){ctr=1;}
            if(one_half==c){ctr=1;}
            if(ctr==1) {cout << "YES" << endl;
                ctr=0;
            }
            else {cout << "NO" << endl;
                ctr=0;
            }
        }
     
        return 0;
    }
