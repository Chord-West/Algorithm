#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	//cin.open("input2.txt");
	int n,m, num;
	vector<int> v;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		cin >> num;
		v.push_back(num);
	}
	sort(v.begin(), v.end());
	int lt = 0;
	int rt = n - 1;
	while (lt<=rt) {
		int mid = (lt + rt) / 2;
		if (v[mid] > m) {
			rt = mid - 1;
		}
		else if(v[mid] < m) {
			lt = mid + 1;
		}
		else {
			cout<<mid + 1;
		}
	}
}

