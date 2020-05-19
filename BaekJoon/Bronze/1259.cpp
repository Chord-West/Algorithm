#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int n;
    vector<string> answer;
    while(cin>>n){
        bool check=1;
        if(n==0){
            break;
        }
        string str = to_string(n);
        for(int i=0; i<str.length()/2;i++){
            if(str[i]!=str[str.length()-i-1]){
                check=0;
                break;
            }
        }
        if(check==1)
            answer.push_back("yes");
        else
            answer.push_back("no");
    }
    for(int i=0; i<answer.size();i++)
        cout<<answer[i]<<endl;
}