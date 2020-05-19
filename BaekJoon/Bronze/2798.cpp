#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    vector<int> answer;
    int result=0;
    int n,g,num;
    int goal=0;
    cin>>n>>g;
    
    for(int i=0;i<n;i++)
    {
        cin>>num;
        answer.push_back(num);           
    }
   
    for(int i=0; i<n-2; i++){
        for(int j=i+1; j<n-1;j++){
            for(int k=j+1; k<n; k++){
                result=answer[i]+answer[j]+answer[k];
                if(result<=g&&goal<result){
                    goal=result;
                }
                
            }
        }

    }
  
    cout<<goal;
}