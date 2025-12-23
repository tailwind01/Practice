// link - https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
// O(1) Time and Space solution

class Solution {
public:
    int differenceOfSums(int n, int m) {
        int allSum, mMultiple,num1,num2;
        allSum = n*(n+1)/2;
        if (m!=1){
            mMultiple = n/m;
            num2 = mMultiple*(m+mMultiple*m)*0.5;
            num1 = allSum - num2;
            return num1-num2;
            }
        else {
            return -allSum;
        }
        return 0;      
    }
};
