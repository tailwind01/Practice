class Solution {
public:
    string removeOuterParentheses(string s) {
        string result = "";
        int opened = 0;
        for(int i=0;i<s.size();++i){
            char c = s[i];
            if(c=='('){
                if (opened>0) result+=c;
                opened+=1;
            }
            else{
                opened-=1;
                if (opened>0) result+=c;
            }
        }
        return result;
    }
};
