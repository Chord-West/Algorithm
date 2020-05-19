#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
    int t,a,b,n;
    cin>>t;
    int floor=0;
    int room=0;
    vector<int> answer;
    for(int i=0; i<t;i++){
        cin>>a>>b>>n;
      
            room=n/a+1;
            if(n%a==0){
                floor=a;
                room--;
                
            }else{
                floor=n%a;
            }
    
        answer.push_back(floor*100+room);
        
    }

    for(int i=0; i<answer.size();i++)
        cout<<answer[i]<<endl;
   
}