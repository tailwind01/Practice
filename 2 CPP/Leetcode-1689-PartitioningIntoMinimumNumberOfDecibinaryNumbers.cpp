//multiple versions of the code, both are 0ms runtime on leetcode
//
class Solution {
public:
    int minPartitions(string n) {
     string s = "987654321";
     int ans = 0;
     for(char &c:s){
        if (n.find(c) != string::npos){
            int ph = c-'0';
            ans = ph;
            break;
        };
        };
        return ans;
    };

};

class Solution {
public:
    int minPartitions(string n) {
     int maxNum=0;
     for(char &c:n){
        int ph = c-'0';
        if (ph>maxNum){
            maxNum = ph;
        };
     }
     return maxNum;   
    }
};
