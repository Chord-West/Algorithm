#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;



void solution(int n,int k){
    // 1 2 3 4 5 6 7
    vector<bool> check(n+1);
    vector<int> tmp;
    int index=1;
    for(int i=0; i<n;i++)
    {
        int count=0;
        while(1)
        {
            if(check[index]==false){
                count++;
                 if(count==k)
                     break;
                 index++;
            }
            else{
                index++;
            }
            if(index>n){
                index=1;
            } 
           
        }
        check[index]=true;
        tmp.push_back(index);
        
    }
    cout<<"<";
    for(int i=0;i<tmp.size()-1;i++){
        cout<<tmp[i]<<", ";
    }
    cout<<tmp[tmp.size()-1]<<">";
}

int main(){
    int n,k;
    cin>>n>>k;
    solution(n,k);
}