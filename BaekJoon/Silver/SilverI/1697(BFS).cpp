#include <iostream>

#include <queue>



using namespace std;


bool check[100001]={0,};
int des[100001]={0,};


int main(){
    int max=100001;
    int n,m;
    cin>>n>>m;
    queue<int> q;
    int start=n;
    q.push(start);
    check[start]=true;
    while(q.front()!=m)
    {
        int pos=q.front();
        q.pop();
        if(pos-1>=0){
            if(check[pos-1]==0)//check 안되어있으면
            {
                q.push(pos-1);
                check[pos-1]=true;
                des[pos-1]=des[pos]+1;
            }
        }
        if(pos+1<=max){
            if(check[pos+1]==0){
                q.push(pos+1);
                check[pos+1]=true;
                des[pos+1]=des[pos]+1;
            }
        }
        if(2*pos<=max){
            if(check[2*pos]==0){
                q.push(2*pos);
                check[2*pos]=true;
                des[2*pos]=des[pos]+1;
            }
        }   
    }

    cout<<des[m];
}