#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int Count(int len, vector<int> x) {
	int cnt = 1, pos = x[1];
	for (int i = 2; i <= n; i++) {
		if (x[i] - pos >= len) {
			cnt++;
			pos = x[i];
		}
	}
	return cnt;
}

int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin;
	cin.open("input2.txt");
	int  c, x,mid,res;
	cin >> n >> c;
	vector<int> stable(n+1);
	vector<int> ans;
	for (int i = 1; i <= n; i++) {
		cin >> x;
		stable[i]=x;
	}
	sort(stable.begin(), stable.end());
	int lt = 1;
	int rt = stable[n];
	while (lt <= rt) {
		mid = (lt + rt) / 2;
		if (Count(mid, stable) >= c) {
			res = mid;
			lt = mid + 1;
		}
		else rt = mid - 1;
	}
	cout << res;
}