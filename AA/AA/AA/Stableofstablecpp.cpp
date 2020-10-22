#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int n, c;
vector<int> v;

int Count(int mid) {
	int count=1;
	int start = 0;
	for (int i = 1; i < v.size(); i++) {
		if (v[i] - v[start] >= mid) {
			count++;
			start = i;
		}
	}
	return count;
}

int main() {
	//ifstream cin;
	ios_base::sync_with_stdio(false);
	//cin.open("input2.txt");
	int x;
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		cin >> x;
		v.push_back(x);
	}
	sort(v.begin(), v.end()); //Á¤·Ä  1 2 4 8 9
	int max = INT_MIN;
	int start = v[0];
	int lt = v[0];
	int rt = v[n - 1];
	while (lt <= rt) {
		int mid = (lt + rt) / 2;
		if (Count(mid) < c) {
			rt = mid - 1;
		}
		else{
			lt = mid + 1;
			if (max < mid)max = mid;
		}
	}
	cout << max;
}