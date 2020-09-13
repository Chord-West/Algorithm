#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	int t, n, res;
	cin >> t;
	for (int i = 0; i < t; i++) {
		cin >> n >> res;
		int sum = 0;
		for (int i = 1; i <= n; i++) {
			sum += i;
		}
		if (sum == res) cout << "YES";
		else cout << "NO";
	}
}