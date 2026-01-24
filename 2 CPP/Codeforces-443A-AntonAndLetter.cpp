//v2 of the code - filtering the input at the cin stage itself
//
#include <bits/stdc++.h>
using namespace std;

void solve(){
    vector <char> elements;
    char buffer;
    while(cin>> buffer){
        if(buffer!='{'&& buffer!='}'&& buffer!=','){
            elements.push_back(buffer);
        };
    };
    
    set <char> as_set (elements.begin(),elements.end());
    
    cout << as_set.size() << endl;
}

int main(){
    solve();
    return 0;
}

//v1 of the code - 2 traversals through the characters

#include <bits/stdc++.h>
using namespace std;

void solve(){
    vector <char> elements;
    char buffer;
    while(cin>> buffer){
        elements.push_back(buffer);
    };
    
    vector <char> inclElements;
    
    for (int i=0; i<elements.size();++i){
        if(elements[i]!='{'&& elements[i]!='}'&& elements[i]!=','){
            inclElements.push_back(elements[i]);
        };
    };

    set <char> as_set (inclElements.begin(),inclElements.end());
    
    cout << as_set.size() << endl;
}

int main(){
    solve();
    return 0;
}
