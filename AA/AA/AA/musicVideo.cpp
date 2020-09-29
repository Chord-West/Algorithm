#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int n;
vector<int>  v(1001);

int Count(int s) {
	int cnt = 1,sum=0;
	for (int i = 1; i <= n; i++) {
		if (sum+v[i]>s) {
			cnt++;
			sum = v[i];
		 }
		else {
			sum += v[i];
		}
	}
	return cnt;
}


int main() {
	//ifstream cin;
	//cin.open("input2.txt");
	int m,num;
	int lt = 1, rt = 0, res,mid; 
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		cin >> num;
		v[i]=num ;
		rt += v[i];
	}
	while (lt <= rt) {
		mid = (lt + rt) / 2;
		if (Count(mid)<=m) {
			res = mid;
			rt = mid - 1;
		}
		else {
			lt = mid + 1;
		}
	}
	cout << res;
}