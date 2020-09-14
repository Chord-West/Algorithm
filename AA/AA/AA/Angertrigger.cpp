#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	int n, num;
	int count = 0;
	
	cin >> n;
	vector<int> stu;
	for (int i = 0; i < n; i++) {
		cin >> num;
		stu.push_back(num);
	}
	int max = stu[n-1];
	for (int i = n - 1; i >= 0; i--) {
		if (stu[i] > max) {
			max = stu[i];
			count++;
		}
	}
	cout << count;
}