#include <iostream>
#include <vector>
#include <fstream>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	//cin.open("input2.txt");
	int n,n2,num, i, j;
	vector<int> v1, v2, ans;
	cin >> n;
	for (i = 0; i < n; i++) {
		cin >> num;
		v1.push_back(num);
	}
	cin >> n2;
	for (i = 0; i < n2; i++) {
		cin >> num;
		v2.push_back(num);
	}
	int m = 0;
	int k = 0;
	//1 3 5 , 2 3 6 7 8
	while (m<n&&k<n2) {
		if (v1[m] <= v2[k]) {
			ans.push_back(v1[m]);
			m++;
		}
		else {
			ans.push_back(v2[k]);
			k++;
		}
	}
	if (m == n) {
		for (i = k;  i < n2; i++) {
			ans.push_back(v2[i]);
		}
	}
	else {
		for (i = m; i < n; i++) {
			ans.push_back(v1[i]);
		}
	}
	for (i = 0; i < ans.size(); i++)
		cout << ans[i] << " ";
}