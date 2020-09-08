#include <iostream>


using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	int n;
	int sum = 0;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		int index = 0;
		int num = i;
		while (num> 0) {
			index++;
			num/= 10;
		}
		sum += index;
	}
	cout << sum;
}