#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int x ,int y){
    while(y!=0){
        int r=x%y;
        x=y;
        y=r;
    }
    return x;
}
int lcm(int x ,int y){
    return (x*y)/gcd(x,y);
}

int main(){
    int n,m;
    cin>>n>>m;

    cout<<gcd(n,m)<<endl;
    cout<<lcm(n,m)<<endl;
    
}