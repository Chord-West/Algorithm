#include<iostream>
#include<vector>
#include<fstream>
#include <string>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	//fstream cin;
	//cin.open("input.txt");
	vector<int> num(10);
	int answer=0;
	int max = 0;
	string n;
	cin >> n;
	for (int i = 0; i < n.length(); i++) {
		num[n[i]-48]++;
	}
	for (int i = 0; i <= 9; i++) {
		if (max <= num[i]) {
			max = num[i];
			answer = i;
			if (answer < i) answer = i;
		}
	}
	cout << answer;
}