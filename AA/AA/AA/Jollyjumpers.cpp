#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	//ifstream cin;
	//cin.open("input.txt");
	vector<int> arr;
	vector<int> ans;
	string a = "YES";
	int n;
	int num;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		arr.push_back(num);
	}
	for (int i = 0; i < n-1; i++) {
		ans.push_back(abs(arr[i] - arr[i + 1]));
	}
	sort(ans.begin(), ans.end());
	for (int i = 0; i < ans.size()-1; i++) {
		if (ans[i + 1] - ans[i] > 1) {
			a = "NO";
			break;
		}
	}
	cout << a;
}