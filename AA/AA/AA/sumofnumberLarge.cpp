#include <iostream>
#include <cmath>

using namespace std;

// 1 - 9 : 9�� * 1
// 10-99 : 90�� * 2
// 100 - 999 : 900�� *3
int main() {
	ios_base::sync_with_stdio(false);
	int n;
	int sum = 0;
	cin >> n;
	int num = n;
	int index = -1;
	while (n > 0) {
		index++;
		n /= 10;
	}
	for (int i = 0; i <index; i++) {
		sum += 9 * pow(10, i) * (i+1);
	}
	sum += (num - pow(10, index) +1) * (index + 1);
	cout << sum;
}