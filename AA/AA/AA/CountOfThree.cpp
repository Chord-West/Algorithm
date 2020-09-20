#include <iostream>
#include <fstream>
#include <vector>

#include <string>

using namespace std;

int main() {
	//ifstream cin;
	//cin.open("input.txt");
	int n;
	cin >> n;
	int count = 0;
	for (int i = 0; i < n; i++) {
		int num = i;
		while (num > 0) {
			int res = num % 10;
			if (res == 3) {
				count++;
			}
			num /= 10;
		}
	}
	cout << count;
}