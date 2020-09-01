#include <iostream>
#include <fstream>
#include <vector>

using namespace std;


int digit_sum(int x) {
	int sum = 0;
	while (x > 0) {
		sum += x% 10;
		x = x / 10;
	}
	return sum;
}
int main() {
	ios_base::sync_with_stdio(false);
	ifstream cin;
	cin.open("input.txt");
	int t, num,sum;
	int max = 0;
	int max_num;
	cin >> t;
	vector<int> m(t);
	for (int i = 0; i < t; i++) {
		cin >> num;
		m[i] = num;
		sum=digit_sum(num);
		if (max < sum) {
			max = sum;
			max_num = num;
		}
		else if (max == sum) {
			if (num > max_num) 
				max_num = num;
		}
	}
	cout << max_num;
}

