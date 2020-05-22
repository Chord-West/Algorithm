#include <iostream>
#include <vector>

using namespace std;

int main(){
    int n,k;
    cin>>n>>k;
    int a=1;
    int b=1;
    int c=1;
    for(int i=1;i<=n;i++){
        a*=i;
        if(i<=k)
            b*=i;
        if(i<=n-k)
            c*=i;
    }
    cout<<a/b/c;

}