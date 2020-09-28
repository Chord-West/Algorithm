#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//ifstream cin;
	//cin.open("input2.txt");
	int a, b = 1, cnt = 0, tmp, i;
	cin >> a;
	tmp = a;
	a--;
	while (a > 0) {
		b++;
		a = a - b;
		if (a % b == 0) {
			for (i = 1; i < b; i++) {
				cout << (a / b) + i << " + ";
			}
			cout << (a / b) + i << " = " << tmp << endl;
			cnt++;
		}
	}
	cout << cnt;
}