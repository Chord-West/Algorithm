#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin;
	cin.open("input2.txt");
	int n,c,x;
	cin >> n >> c;
	vector<int> stable;
	for (int i = 0; i < n; i++) {
		cin >> x;
		stable.push_back(x);
	}
}