#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	vector<int> a, b;
	int n, num;
	cin >> n;
	for (int i = 0; i < n; i++) {
		cin >> num;
		a.push_back(num);
	}
	for (int i = 0; i < n; i++) {
		cin >> num;
		b.push_back(num);
	}
	for (int i = 0; i < a.size(); i++) {
		int win = a[i] - b[i];
		if (win == -1 || win == 2) cout << "B" << endl;
		else if (win == 1 || win == -2) cout << "A" << endl;
		else cout << "D" << endl;


	}
}