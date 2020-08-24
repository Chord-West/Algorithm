#include <iostream>

using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	int sum = m;
	for (int i = n; i < m; i++) {
		cout << i << " + ";
		sum += i;
	}
	cout << m << " = " << sum;
	return 0;
}