//v2 with ternary inside the for loop - same runtime..
//
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int tickets;
    cin >> tickets ;
    
    while(tickets--){
        string numStr;
        cin >> numStr;
        int checksum = 0;
        
        for(int i=0;i<6;i++){
            int asnum = numStr[i]-'0'; //converting the char into an integer number
            checksum+= (i<=2) ? asnum : -asnum; //ternary for the boolean
        }
        string ans = (checksum==0) ? "YES" : "NO";
        cout << ans << "\n" ;
    }
    
}

int main(){
    solve();
    return 0;
}


//v1 without the ternary..
#include <bits/stdc++.h>
using namespace std;

void solve() {
    int tickets;
    cin >> tickets ;
    
    while(tickets--){
        string numStr;
        cin >> numStr;
        int checksum = 0;
        
        for(int i=0;i<6;i++){
            int asnum = numStr[i]-'0'; //converting the char into an integer number
            if(i<=2){
                checksum+= asnum;
            }
            else{
                checksum-= asnum;
            };
        }
        string ans = (checksum==0) ? "YES" : "NO";
        cout << ans << "\n" ;
    }
    
}

int main(){
    solve();
    return 0;
}
