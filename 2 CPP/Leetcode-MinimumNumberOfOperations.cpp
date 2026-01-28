//2 versions

//v2.2 -  using the addition by boolean
//
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int size = boxes.size();
        vector <int> ansArr (size,0);
        int ctL = 0, opL = 0;
        for(int i=0;i<size;++i){
            ansArr[i]+=opL;
            ctL+= (boxes[i]=='1');
            opL+=ctL;
        }
        int ctR = 0, opR = 0;
        for(int j=size-1;j>=0;--j){
            ansArr[j]+=opR;
            ctR+= (boxes[j]=='1');
            opR+=ctR;
        }
        return ansArr;
    }
};


//v2.1  -  left to right and right to left traversal
//

class Solution {
public:
    vector<int> minOperations(string boxes) {
        int size = boxes.size();
        vector <int> ansArr (size,0);
        int ctL = 0, opL = 0;
        for(int i=0;i<size;++i){
            ansArr[i]+=opL;
            if(boxes[i]=='1'){
                ctL+=1;
            }
            opL+=ctL;
        }
        int ctR = 0, opR = 0;
        for(int j=size-1;j>=0;--j){
            ansArr[j]+=opR;
            if(boxes[j]=='1'){
                ctR+=1;
            }
            opR+=ctR;
        }
        return ansArr;
    }
};


//v1 - comparing the index differences in a brute force manner..
class Solution {
public:
    vector<int> minOperations(string boxes) {
        vector <int> indsOf1;
        for(int i=0;i<boxes.size();++i){
            if(boxes[i]=='1'){
                indsOf1.push_back(i+1);
            }
        }

        vector <int> ansArr;

        for(int j =0;j<boxes.size();++j){
            int moves = 0;
            for(int k: indsOf1){
                moves+=abs(k-(j+1));
            }
            ansArr.push_back(moves);
        }
        return ansArr;
    }
};
