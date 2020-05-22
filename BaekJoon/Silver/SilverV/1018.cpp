#include <iostream>
#include <vector>
#include <string>

using namespace std;


vector<string> board;

int result=50000;

string WB[8]={
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB", 
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
};
string BW[8]={
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
};


void comparewb(int x, int y){
    int tmp=0;
    for(int i=0; i<8;i++){
        for(int j=0; j<8;j++){
            if(WB[i][j]==board[i+x][j+y]){
                tmp++;
            }
        }
    }
    if(tmp<result){
        result=tmp;
    }
}
void comparebw(int x, int y){
    int tmp=0;
    for(int i=0; i<8;i++){
        for(int j=0; j<8;j++){
            if(BW[i][j]==board[i+x][j+y]){
                tmp++;
            }
        }
    }
    if(tmp<result){
        result=tmp;
    }
}

int main(){
    
    int n,m;
    string str;
    cin>>n>>m;
    for(int i=0; i<n; i++){
        cin>>str;

        board.push_back(str);       
    }
    for(int i=0; i<=n-8;i++){
        for(int j=0; j<=m-8;j++){
            comparewb(i,j);
            comparebw(i,j);
        }
    }
    cout<<result;
   
}
