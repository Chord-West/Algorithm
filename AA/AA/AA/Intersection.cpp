#include <iostream>
#include <vector>
#include <fstream>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	//cin.open("input2.txt");
	int n, n2, num, i, j;
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
	sort(v1.begin(), v1.end());
	sort(v2.begin(), v2.end());
	int m = 0;
	int k = 0;
	while (m<n&&k<n2) {
		if (v1[m]<v2[k]) {
			m++;
		}
		else if (v1[m] > v2[k]) {
			k++;
		}
		else {
			ans.push_back(v1[m]);
			m++;
		}
	}
	for (i = 0; i < ans.size(); i++) 
		cout << ans[i] << " ";
	
}