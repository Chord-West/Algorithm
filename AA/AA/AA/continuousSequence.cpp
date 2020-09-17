#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	//fstream cin;
	//cin.open("input.txt");
	int n;
	int cnt = 0;
	int before=0;
	int max = 0;
	cin >> n;
	int num;
	for (int i = 0; i < n; i++) {
		cin >> num;
		cnt++;
		if (before <= num) {
			if (max < cnt)
				max = cnt;
		}
		else {
			cnt = 1;
		}
		before = num;
	}
	cout << max;
}